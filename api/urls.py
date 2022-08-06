from django.urls import path,include
from . views import *

urlpatterns = [       
    path("",Api,name = "api"),
    path("api-urls/",Api_Urls.as_view()),
    path("message-history/",message_history.as_view()),
    path("message/<int:pk>",show_message.as_view()),
    path("message-create/",message_create.as_view()),
    
]