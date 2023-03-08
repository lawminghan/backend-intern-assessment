from django.urls import path
from .views import Registration, SingleUser


urlpatterns = [
    path('registration', Registration.as_view(), name="registrationView"),
    path('user', SingleUser.as_view(), name='singleUserView'),
]