from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import JobOfferSerializer
from .mongo import job_offers_collection  # 🟢 Import MongoDB collection

class JobOfferCreateView(APIView):
    def post(self, request):
        serializer = JobOfferSerializer(data=request.data)
        if serializer.is_valid():
            # Insert data into MongoDB
            job_offers_collection.insert_one(serializer.data)
            return Response({"message": "Job offer added successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
