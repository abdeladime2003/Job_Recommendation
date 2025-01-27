from django.urls import path
from .views import AddJobOfferView , GetJobOffersView
urlpatterns = [
    path('add-job-offer/', AddJobOfferView.as_view(), name='add-job-offer'),
    path('get-job-offers/', GetJobOffersView.as_view(), name='get-job-offers')
]
