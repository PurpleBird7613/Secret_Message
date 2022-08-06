from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout

from message.models import Message,Show_Message_Password
from django.contrib.auth.models import User
import re

#from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework import permissions, status
from rest_framework import serializers
from .serializers import  MessageSerializer,Show_Message_Password_Serializer,Show_Message_Serializer

from rest_framework.authtoken.models import Token

url = "https://secretmessage.pythonanywhere.com"

# API
def Api(request):
    context = {}
    user = request.user
    context["user"] = user

    if not user.is_authenticated:
        return redirect("/")

    context["create_message"] = f'{url}/api/message-create/'
    context["show_message"] = f'{url}/api/message/<int:pk>'
    context["message_history"] = f'{url}/api/message-history/'
    
    try:
        token = Token.objects.create(user = request.user)
    except:
        token = Token.objects.get(user = user)
        context["Api_Token"] = token.key	     
    
    return render(request,"api.html",context)

# API URLS
class Api_Urls(APIView):
    def get(self, request, formate=None):
        api_urls = {
            'Message History' : f'{url}/api/message-history/',
            'Show Message' : f'{url}/api/message/<int:pk>',
            'Create Message' : f'{url}/api/message-create/',
        }
        return Response(api_urls)


# HISTORY OF MESSAGE
class message_history(APIView):    
    def get(self, request,formate=None):
        messages = Message.objects.filter(author = request.user)
        serializer = MessageSerializer(messages, many = True)
        return Response({"Messages" : serializer.data})
        
        
# SHOWING THE MESSAGE
class show_message(APIView):    
    def post(self, request,pk):
        # Author's Messages
        user_messages = Message.objects.filter(author = request.user)
        # Showing Message
        messages = Message.objects.get(id = pk)
        
        # Getting the Password of The Message in string
        mesg_serializer = MessageSerializer(messages, many = False)
        mesg_password = mesg_serializer.data["password"]
        
        if messages in user_messages:
             serializer = MessageSerializer(messages, many = False)
             return Response({"Message" : serializer.data})
        else:
            # Saving the password
            Author = Show_Message_Password(author = request.user)  
            serializer = Show_Message_Password_Serializer(Author,data = request.data)
            if serializer.is_valid():
                serializer.save()
            
            # Comparing The Message Password
            pswrd = Show_Message_Password.objects.filter(author = request.user).order_by("-date")[0:1]
            # Getting the password in string format
            pswrd_serializer = Show_Message_Password_Serializer(pswrd,many = True)
            password = pswrd_serializer.data[0]["password"]
            
            if password == mesg_password:
                serializer = Show_Message_Serializer(messages, many = False)
                return Response({"Message" : serializer.data})
            else:
                return Response({"Message" : "Wrong Password!!!"})


# CREATING MESSAGE
class message_create(APIView):
    def post(self, request, formate=None):
        user = request.user
        
        # creating link for the message
        msg_link = Message.objects.all().order_by('-date')[0:1]
        mess = str(msg_link)
        msg = re.findall(r'\d+', mess) 
        n = list(map(int, msg))
        num = n[0]+1
        number = str(num)	
        link = f"{url}/message/{number}"
        
        Author_MsgLink = Message(message_link = link,author = user)
        serializer = MessageSerializer(Author_MsgLink,data = request.data)
        
        if serializer.is_valid():
            serializer.save()
    
        return Response(serializer.data,status = status.HTTP_201_CREATED)

    