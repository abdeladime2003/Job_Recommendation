from rest_framework import serializers
from .models import Feedback
from user.models import User

class FeedbackSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    stars = serializers.ChoiceField(choices=[(1, '1 Star'), (2, '2 Stars'), (3, '3 Stars'), (4, '4 Stars'), (5, '5 Stars')])
    comment = serializers.CharField(max_length=1000)
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Feedback
        fields = ['user', 'stars', 'comment', 'created_at']

       