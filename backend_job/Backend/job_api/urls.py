from django.urls import path
from .views import JobOfferCreateView

urlpatterns = [
    path('add-job-offer/', JobOfferCreateView.as_view(), name='add-job-offer'),
]
