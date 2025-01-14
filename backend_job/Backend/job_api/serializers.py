from rest_framework import serializers
from datetime import datetime

class JobOfferSerializer(serializers.Serializer):
    titre = serializers.CharField(max_length=255, required=False)
    entreprise = serializers.CharField(max_length=255, required=False)
    localisation = serializers.CharField(max_length=255, required=False)
    competences_cles = serializers.ListField(
        child=serializers.CharField(), required=False
    )
    date_publication = serializers.DateField(required=False)
    lien = serializers.URLField(required=False)

    def validate_date_publication(self, value):
        """ Validation flexible pour les dates de publication au format dd.mm.yyyy """
        if isinstance(value, str):
            try:
                # Convertir la date de 'dd.mm.yyyy' vers 'yyyy-mm-dd'
                return datetime.strptime(value, '%d.%m.%Y').date()
            except ValueError:
                raise serializers.ValidationError("Format de date invalide. Utilisez le format dd.mm.yyyy.")
        return value

    def to_internal_value(self, data):
        """
        Logique conditionnelle pour adapter le parsing des données en fonction du format
        de la source, comme pour les compétences clés qui sont une chaîne.
        """
        # Convertir 'Compétences clés' de chaîne à liste
        if 'Compétences clés' in data and isinstance(data['Compétences clés'], str):
            data['competences_cles'] = [skill.strip() for skill in data['Compétences clés'].split('-')]
        
        # Convertir la date de publication si elle est en format string
        if 'Date de publication' in data and isinstance(data['Date de publication'], str):
            data['date_publication'] = self.validate_date_publication(data['Date de publication'])
        
        return super().to_internal_value(data)

    def to_representation(self, instance):
        """ Transformation des données avant de les renvoyer """
        data = super().to_representation(instance)
        
        # Ajouter des valeurs par défaut si certains champs sont absents
        if 'competences_cles' not in data:
            data['competences_cles'] = []
        
        if 'titre' not in data:
            data['titre'] = "Titre non spécifié"
        
        return data
