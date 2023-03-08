from django.shortcuts import get_object_or_404
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import WaveScanUser
from .serializers import WaveScanUserSerializer


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
        message = {"message" : f"User {user.email} deleted successfully"}
        user.delete()
        return Response(message, status=status.HTTP_200_OK)
