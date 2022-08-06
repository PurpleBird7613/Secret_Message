from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.views import View
from .models import Message
from .forms import MessageForm
import re

url = "https://secretmessage.pythonanywhere.com"

# Logging In
def user_name(request):
	context = {}	
	user = request.user

	if user.is_authenticated:
		return redirect("home")
	
	if request.method == "POST":
		username = request.POST.get('username','')
		login_user = authenticate(username=username, password="Password@")
		
		if login_user is not None:
			login(request,login_user)
			return redirect("home")
		else:
			user = User.objects.create_user(username, password="Password@")
			user.save()
			login(request,user)
			return redirect("home")
	
	return render(request,"signup.html",context)

# Sign Out
def signout(request):
	logout(request)
	return redirect("/")

# Home
def home(request):
	context = {}
	user = request.user
	context["user"] = user

	if not user.is_authenticated:
		return redirect("/")
		
	message = Message.objects.filter(author=user).order_by('-date')
	m = Message.objects.all().order_by("-date").first()
	print(m)
	
	context["message"] = message
	
	form = MessageForm(data=request.POST ,files=request.FILES)
	new_message = None
	password = None

	if request.method == "POST":
		password = request.POST.get("password","")
		
		# creating link for the message
		msg_link = Message.objects.all().order_by('-date')[0:1]
		mess = str(msg_link)
		msg = re.findall(r'\d+', mess) 
		n = list(map(int, msg))
		num = n[0]+1
		number = str(num)	
		link = f"{url}/message/{number}"
				
		if password == "":
			msg = "please enter password"
			context["no_password"] = msg
			
		if form.is_valid():
			new_message = form.save(commit=False)
			new_message.password = password
			new_message.message_link = link
			new_message.author = request.user
			new_message.save()
			return redirect("give_link")
		
	form = MessageForm()
	context["form"] = form
		
	return render(request,"home.html", context)

# Displaying Message
class message_display(View):
	def get(self, request,pk,*args,**kwargs):
		import re
		context = {}
		user = request.user
		context["user"] = user

		message = Message.objects.get(pk=pk)
		
		mess = str(message)
		msg = re.findall(r'\d+', mess) 
		n = list(map(int, msg))
		num = n[0]
		number = str(num)		
		link = f"{url}/message/{number}"
		context["link"] = link	
		context["message"] = message
		
		return render(request,"message_display.html",context)

# Giving yhe Message Link
def give_link(request):
	import re
	context = {}
	user = request.user
	context["user"] = user
	
	if not user.is_authenticated:
		return redirect("/")
	
	message = Message.objects.filter(author=user).order_by('-date')[0:1]
	
	mess = str(message)
	msg = re.findall(r'\d+', mess) 
	n = list(map(int, msg))
	num = n[0]
	number = str(num)	
	link = f"{url}/message/{number}"
	
	context["link"] = link
	context["message"] = message
	
	return render(request,"give_link.html",context)

# History
def history(request):
	context = {}
	user = request.user
	context["user"] = user
	
	if not user.is_authenticated:
		return redirect("/")
	
	message = Message.objects.filter(author=user).order_by('-date')
	context["message"] = message
	return render(request,"history.html", context)
	


