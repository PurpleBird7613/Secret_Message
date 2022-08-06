from rest_framework import serializers
from message.models import Message, Show_Message_Password
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
        
class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ["id","body","file","password","message_link"]
        
class Show_Message_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ["body","file"]
        
class Show_Message_Password_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Show_Message_Password
        fields = ["password"]