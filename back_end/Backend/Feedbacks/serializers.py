from rest_framework import serializers
from Feedbacks.models import Feedback

class FeedbackSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')  # ✅ Rendre `user` non modifiable

    class Meta:
        model = Feedback
        fields = ['id', 'user', 'comment', 'rating', 'created_at']
