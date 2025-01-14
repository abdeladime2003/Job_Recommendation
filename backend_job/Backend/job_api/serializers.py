from rest_framework import serializers

class JobOfferSerializer(serializers.Serializer):
    Description = serializers.CharField(allow_blank=True, required=False)
    Lien = serializers.URLField(allow_blank=True, required=False)
    Contrat = serializers.CharField(allow_blank=True, required=False)
    Lieu = serializers.CharField(allow_blank=True, required=False)
    comptence = serializers.ListField(
        child=serializers.CharField(), required=False, allow_empty=True)
    Date = serializers.CharField(allow_blank=True, required=False)

    def validate_comptence(self, value):
        """
        Si le champ 'comptence' est une liste, la transformer en chaîne.
        """
        if isinstance(value, list):
            return ', '.join(value)  # Convertit la liste en une chaîne
        return value

    def validate(self, data):
        """
        Valider le dictionnaire complet avant d'envoyer.
        """
        # Exemple de validation: vérifier si un champ nécessaire est vide
        if not data.get('Description'):
            raise serializers.ValidationError("Le champ Description est requis.")
        
        return data
