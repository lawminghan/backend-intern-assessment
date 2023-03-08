from django.shortcuts import get_object_or_404
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import WaveScanUser
from .serializers import WaveScanUserSerializer, UserRoleSerializer


# Create your views here.
class Registration(APIView):
    def post(self, request):
        serialized_user = WaveScanUserSerializer(data=request.data)
        serialized_user.is_valid(raise_exception=True)
        serialized_user.save()
        return Response(serialized_user.data, status=status.HTTP_200_OK)



class SingleUser(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        user = get_object_or_404(WaveScanUser,id=request.user.id)
        serialized_user = WaveScanUserSerializer(user)
        return Response(serialized_user.data, status=status.HTTP_200_OK)
    
    # allowed to update first name, last  name, password, company and designation.
    def patch(self,request):
        user = get_object_or_404(WaveScanUser, id=request.user.id)
        serialized_user = WaveScanUserSerializer(instance=user, data=request.data, partial=True)
        serialized_user.is_valid(raise_exception=True)
        serialized_user.save()
        return Response(serialized_user.data, status=status.HTTP_200_OK)


    def delete(self, request):
        user = get_object_or_404(WaveScanUser, id=request.user.id)
        message = {"message" : f"{user.role} {user.email} deleted successfully"}
        user.delete()
        return Response(message, status=status.HTTP_200_OK)



class ListUsers(generics.ListAPIView):
    queryset = WaveScanUser.objects.all()
    serializer_class = WaveScanUserSerializer
    permission_classes = [IsAdminUser]

class ManageUsers(APIView):
    permission_classes = [IsAdminUser]
    
    def get(self, request, id):
        user = get_object_or_404(WaveScanUser, id=id)
        serialized_user = WaveScanUserSerializer(user)
        return Response(serialized_user.data, status=status.HTTP_200_OK)
    
    # ADMIN allowed to change user roles for other users or downgrade their own roles to “MEMBER” or “TECHNICIAN”
    def patch(self, request, id):
        user = get_object_or_404(WaveScanUser, id=id)
        
        # only allowed to update role
        data = {
            'role' : request.data.get('role', request.user.role)
        }
        
        serialized_user = UserRoleSerializer(instance=user, data=data, partial=True)
        serialized_user.is_valid(raise_exception=True)
        serialized_user.save()
        return self.get(request,id)
    
    # ADMIN allowed to delete their own account and any other user’s account.
    def delete(self, request, id):
        user = get_object_or_404(WaveScanUser, id=id)
        message = {"message" : f"{user.role} {user.email} deleted successfully"}
        user.delete()
        return Response(message, status=status.HTTP_200_OK)