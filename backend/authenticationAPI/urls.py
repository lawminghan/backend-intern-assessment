from django.urls import path
from .views import Registration, SingleUser, ListUsers, ManageUsers
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('account/registration', Registration.as_view(), name="registrationView"),
    path('account/user', SingleUser.as_view(), name='singleUserView'),
    path('account/admin/users', ListUsers.as_view(), name='listUsersView'),
    path('account/admin/users/<int:id>', ManageUsers.as_view(), name='manageUsersView'),
    
]