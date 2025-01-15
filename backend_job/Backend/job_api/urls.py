from django.urls import path
from .views import AddJobOfferView

urlpatterns = [
    path('add-job-offer/', AddJobOfferView.as_view(), name='add-job-offer'),
]
