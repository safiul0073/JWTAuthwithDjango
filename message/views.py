from django.http.response import JsonResponse
from rest_framework import status
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MessageSerializer
from .models import Message
# Create your views here.
@api_view(['GET'])
def ApiOverView(request):
    hello = {
        'name': "anis",
        'email': "anis@mail.com",
        'pass': "padsfsdkfj",
    }
    return Response(hello)

@api_view(['GET', 'PUT', 'DELETE'])
def MessageListView(request, pk):

    if pk :
        try:
            message = Message.objects.get(pk=pk)
        except Message.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        messages = Message.objects.get(pk=pk)
        serialize = MessageSerializer(messages, many=False)
        return Response(serialize.data)

    elif request.method == 'PUT':
        serializer = MessageSerializer(message, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        message.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def getAllMessages(request):

    if request.method == 'GET':
        messages = Message.objects.all()
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serialize = MessageSerializer(data = request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status = status.HTTP_201_CREATED)
        
        return Response(serialize.errors, status = status.HTTP_400_BAD_REQUEST)        

    

