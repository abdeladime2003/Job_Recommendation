from django.urls import path
from .views import CVUploadView

urlpatterns = [
    path('upload/', CVUploadView.as_view(), name='cv-upload'),
]
