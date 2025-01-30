import os
import logging
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Ocr_Model.main import main
from .utils.logger import logger
logger.info("Logger initialisé pour le traitement des CVs.")
class CVUploadView(APIView):
    def post(self, request, *args, **kwargs):
        try : 
            file = request.FILES.get('file')
            logger.info(f"Requête POST reçue pour le fichier {file.name}")
        except Exception as e:
            logger.error(f"Erreur lors de la récupération du fichier : {e}")
            return Response({"error": "Une erreur est survenue lors de la récupération du fichier."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        if not file:
            print("Aucun fichier fourni.")
            return Response({"error": "Aucun fichier fourni."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Validation : Vérifier le type de fichier (seulement PDF)
        if not file.name.endswith('.pdf'):
            logger.error("Seuls les fichiers PDF sont autorisés.")
            return Response({"error": "Seuls les fichiers PDF sont autorisés."}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            # Définir le chemin de sauvegarde du fichier
            file_path = os.path.join(settings.MEDIA_ROOT, 'cvs', file.name)
            # Créer le répertoire 'cvs' s'il n'existe pas déjà
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            # Sauvegarder le fichier
            with open(file_path, 'wb') as f:
                for chunk in file.chunks():
                    f.write(chunk)
            logger.info(f"Fichier {file.name} sauvegardé avec succès.")
            try : 
                main(file_path) 
                logger.info(f"Fichier {file.name} traité avec succès.")
                return Response({"message": "Fichier traité avec succès."}, status=status.HTTP_200_OK)
            except Exception as e:
                logger.error(f"Erreur lors du traitement du fichier : {e}")
                return Response({"error": "Une erreur est survenue lors du traitement du fichier."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            logger.error(f"Erreur lors du traitement du fichier : {e}")
            return Response({"error": "Une erreur essst survenue lors du traitement du fichier."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)