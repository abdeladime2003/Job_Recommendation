from django.urls import path
from .views import RegisterView, LoginView , VerifyEmail

urlpatterns = [
    path('signup/', RegisterView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('email-verify/', VerifyEmail.as_view(), name="email-verify"),
]