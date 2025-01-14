from rest_framework import serializers

class JobOfferSerializer(serializers.Serializer):
    entreprise = serializers.CharField(max_length=255 , required=False)
    lieu = serializers.CharField(max_length=255)
    description = serializers.CharField()
    date_publication = serializers.DateField()
    type = serializers.CharField(max_length=50)
    competences_requises = serializers.ListField(
        child=serializers.CharField()
    )
    lien_postulation = serializers.URLField()
