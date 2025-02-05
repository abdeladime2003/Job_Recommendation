from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from Feedbacks.models import Feedback
from Feedbacks.serializers import FeedbackSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
class FeedbackCreateView(APIView):
    authentication_classes = [JWTAuthentication]  # ✅ Ensure JWT authentication is used
    permission_classes = [IsAuthenticated]  # ✅ Require authentication

    def post(self, request):
        print("🔹 User:", request.user)  # Debug: Check user authentication
        print("🔹 Auth:", request.auth)  # Debug: Check token authentication

        if not request.user or request.user.is_anonymous:
            return Response({"error": "User not authenticated"}, status=status.HTTP_401_UNAUTHORIZED)

        serializer = FeedbackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
