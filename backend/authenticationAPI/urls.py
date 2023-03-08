from django.urls import path
from .views import Registration, SingleUser, ListUsers, ManageUsers


urlpatterns = [
    path('registration', Registration.as_view(), name="registrationView"),
    path('user', SingleUser.as_view(), name='singleUserView'),
    path('admin/users', ListUsers.as_view(), name='listUsersView'),
    path('admin/users/<int:id>', ManageUsers.as_view(), name='manageUsersView'),
    
]