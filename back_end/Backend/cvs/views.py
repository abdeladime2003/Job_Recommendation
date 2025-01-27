import os
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class CVUploadView(APIView):
    def post(self, request, *args, **kwargs):
        file = request.FILES.get('file')
        if file:
            # Définir le chemin de sauvegarde du fichier
            file_path = os.path.join(settings.MEDIA_ROOT, 'cvs', file.name)

            # Créer le répertoire 'cvs' si il n'existe pas déjà
            os.makedirs(os.path.dirname(file_path), exist_ok=True)

            # Sauvegarder le fichier
            with open(file_path, 'wb') as f:
                for chunk in file.chunks():
                    f.write(chunk)

            return Response({"message": "Fichier téléchargé avec succès!"}, status=status.HTTP_200_OK)
        return Response({"error": "Aucun fichier fourni."}, status=status.HTTP_400_BAD_REQUEST)
