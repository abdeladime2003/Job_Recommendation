from rest_framework import serializers

class FlexibleJobOfferSerializer(serializers.Serializer):
    titre = serializers.CharField(max_length=255, required=False, allow_blank=True)
    entreprise = serializers.CharField(max_length=255, required=False, allow_blank=True)
    description = serializers.CharField( required=False, allow_blank=True)
    localisation = serializers.CharField(max_length=255, required=False, allow_blank=True)
    competences_cles = serializers.ListField(
        child=serializers.CharField(max_length=255, required=False), required=False
    )
    niveau_etudes_requis = serializers.CharField(max_length=255, required=False, allow_blank=True)
    niveau_experience = serializers.CharField(max_length=255, required=False, allow_blank=True)
    contrat_propose = serializers.CharField(max_length=50, required=False, allow_blank=True)
    teletravail = serializers.CharField(max_length=3, required=False, allow_blank=True)
    ## accepter les dates et string 
    date_publication = serializers.DateField(
        format="%d.%m.%Y",
        input_formats=["%d.%m.%Y"],
        required=False,
        allow_null=True,
    )
    date_limite = serializers.DateField(
        format="%d.%m.%Y",
        input_formats=["%d.%m.%Y"],
        required=False,
        allow_null=True,
    )

    nombre_postes = serializers.CharField(max_length=255, required=False, allow_blank=True)
    lien = serializers.URLField(required=False, allow_blank=True)
    def validate_competences_cles(self, value):
        """
        Validation personnalisée pour les compétences.
        Si la liste est vide ou non fournie, elle peut être ignorée.
        """
        return value or []
