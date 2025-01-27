from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from pymongo import MongoClient, errors
from bson import ObjectId
from datetime import datetime, date
from .serializers import FlexibleJobOfferSerializer
from .utils.mongo import get_mongo_connection
class AddJobOfferView(APIView):
    def convert_dates(self, data):
        """
        Convertit les objets datetime.date en datetime.datetime pour MongoDB.
        """
        for key, value in data.items():
            if isinstance(value, date) and not isinstance(value, datetime):
                data[key] = datetime(value.year, value.month, value.day)
        return data

    def post(self, request):
        serializer = FlexibleJobOfferSerializer(data=request.data)
        print(request.data)  # Vérifie les données reçues
        if serializer.is_valid():
            validated_data = serializer.validated_data
            print(validated_data)  # Vérifie les données avant l'insertion

            # Connexion à MongoDB
            try:
                job_offers_collection = get_mongo_connection()

                # Convertir les dates avant insertion
                validated_data = self.convert_dates(validated_data)

                # Insertion dans MongoDB
                try:
                    result = job_offers_collection.insert_one(validated_data)
                    
                    # Convertir l'ObjectId en chaîne pour la réponse
                    validated_data["_id"] = str(result.inserted_id)
                    return Response({
                        "message": "Données enregistrées avec succès dans MongoDB.",
                        "data": validated_data
                    }, status=status.HTTP_201_CREATED)
                except errors.PyMongoError as e:
                    return Response({
                        "message": "Erreur lors de l'insertion dans MongoDB.",
                        "error": str(e)
                    }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            except errors.ConnectionFailure as e:
                return Response({
                    "message": "Erreur de connexion à MongoDB.",
                    "error": str(e)
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # En cas de validation échouée
        return Response({
            "message": "Erreur de validation des données.",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
class GetJobOffersView(APIView):
    def format_job_offer(self, job_offer):
        """
        Formater un document MongoDB en un dictionnaire lisible par JSON.
        """
        job_offer["_id"] = str(job_offer["_id"])  # Convertir ObjectId en chaîne
        return job_offer

    def get(self, request):
        try:
            job_offers_collection = get_mongo_connection()

            # Obtenir le nombre d'offres depuis les paramètres de requête
            limit = request.query_params.get('limit', 5)  # Par défaut, limite à 5
            try:
                limit = int(limit)  # Convertir en entier
            except ValueError:
                return Response({
                    "message": "Le paramètre 'limit' doit être un entier."
                }, status=status.HTTP_400_BAD_REQUEST)

            # Récupérer les offres d'emploi triées par date de publication
            job_offers = job_offers_collection.find().sort([("date_publication", -1)]).limit(limit)

            # Formater les données pour JSON
            formatted_job_offers = [self.format_job_offer(offer) for offer in job_offers]

            return Response({
                "message": "Données récupérées avec succès.",
                "data": formatted_job_offers
            }, status=status.HTTP_200_OK)

        except errors.ConnectionFailure as e:
            return Response({
                "message": "Erreur de connexion à MongoDB.",
                "error": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
