from django.shortcuts import render
from rest_framework.views import APIView
from api.serializer import Signup,productserializer
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from store.models import Product
from rest_framework import status
# Create your views here.
class SignupView(APIView):
    def post(self,request,*args,**kwargs):
        serializer=Signup(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        
class TaskviewSet(ViewSet):
    def list(self,request,*args,**kwargs):
        qs=Product.objects.all()
        serializer=productserializer(qs,many=True)
        return Response(data=serializer.data,status=status.HTTP_202_ACCEPTED)
    def create(self,request,*args,**kwargs):
        serializer=productserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_202_ACCEPTED)
        else:
            return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Product.objects.get(id=id)
        serializer=productserializer(qs)
        return Response(data=serializer.data,status=status.HTTP_201_CREATED)
    
    def destroy(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Product.objects.get(id=id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def update(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Product.objects.get(id=id)
        serializer=productserializer(instance=qs,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_202_ACCEPTED)
        else:
            return Response(data=serializer.errors,status=status.HTTP_204_NO_CONTENT)
        
        

