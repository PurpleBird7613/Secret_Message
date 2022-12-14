"""secret_message URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static

from message.views import *


app_name = "message"

urlpatterns = [
    path('admin/', admin.site.urls),

    path("home/",home,name="home"),
    
    # Message views
    path("",user_name,name = "user_name"),
    path("signout/",signout,name = "signout"),
    path("message/<int:pk>",message_display.as_view(),name = "message_display"),
    path("give_link/",give_link,name = "give_link"),
    path("history/",history, name = "history"),
    
    # API
    path("api/",include("api.urls"),name = "api"),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
