from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer, LoginSerializer, EmailVerificationSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.urls import reverse
from django.contrib.sites.shortcuts import get_current_site
from django.conf import settings
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
import jwt
from .utils import Util
from . import models
from rest_framework.permissions import AllowAny
class RegisterView(APIView):
    permission_classes = [AllowAny]  # ✅ Ajouté

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user_data = serializer.data
            user_email = models.User.objects.get(email=user_data['email']) 
            tokens = RefreshToken.for_user(user_email).access_token 

            current_site = get_current_site(request).domain
            relative_link = reverse('email-verify') 
            absurl = f'http://{current_site}{relative_link}?token={str(tokens)}'

            email_body = f'Bonjour {user_data["first_name"]},\n\nUtilisez le lien ci-dessous pour vérifier votre email :\n{absurl}'
            data = {
                'email_body': email_body,
                'to_email': user_data['email'],
                'email_subject': 'Vérifiez votre email'
            }
            Util.send_email(data)  
            return Response({'user': user_data, 'token': str(tokens)}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = [AllowAny]  # ✅ Ajouté

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(request, username=email, password=password)
        if user is not None: 
            if not user.is_verified:
                return Response({'error': 'Veuillez vérifier votre email.'}, status=status.HTTP_403_FORBIDDEN)
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh_token': str(refresh),
                'access_token': str(refresh.access_token),
                'user': user.first_name + ' ' + user.last_name
            }, status=status.HTTP_200_OK)


class VerifyEmail(APIView):
    permission_classes = [AllowAny]  # ✅ Ajouté

    serializer_class = EmailVerificationSerializer
    token_param_config = openapi.Parameter(
        'token', in_=openapi.IN_QUERY, description='Token de vérification', type=openapi.TYPE_STRING
    )

    @swagger_auto_schema(manual_parameters=[token_param_config])
    def get(self, request):
        token = request.GET.get('token')
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms='HS256')
            user = models.User.objects.get(id=payload['user_id'])
            if not user.is_verified:
                user.is_verified = True
                user.save()
            return Response({'email': 'Email vérifié.'}, status=status.HTTP_200_OK)
        except jwt.ExpiredSignatureError:
            return Response({'error': 'Lien expiré.'}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError:
            return Response({'error': 'Lien invalide.'}, status=status.HTTP_400_BAD_REQUEST)
