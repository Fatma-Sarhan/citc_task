from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from .models import Bloodtest,Livertest,UserProfile
from django.core.context_processors import csrf
from django.shortcuts import get_object_or_404, render

# Create your views here.


def index(request) :
	if request.COOKIES.get("sessionid", None):
		print "already"
		# return HttpResponseRedirect('loggedin')
		return HttpResponseRedirect('home')
	else:
		c = {}
		c.update(csrf(request))
		return render(request, 'labs/index.html', c)


def signin(request):
	username = request.POST.get('username','')
	password = request.POST.get('password','')
	user = authenticate(username=username, password=password)
	if not request.POST.get('remember_me'):
		request.session.set_expiry(0)
		# print "fatma"
		# return HttpResponseRedirect('loggedin')

	if user is not None:
		auth_login(request, user)
		# return HttpResponse('User is valid, active and authenticated')

		return HttpResponseRedirect('home')
	else:
		message = "Invalid username or password please try again !"
		return render(request,'labs/index.html',{'message':message})

	return render(request,'labs/index.html')


def logout_view(request):
	logout(request)
	return render(request,'labs/index.html')
	


def home(request):
	pat_id = request.user.id
	try:
   		b_test=Bloodtest.objects.get(patient_id = pat_id)
	except Bloodtest.DoesNotExist:
		b_test= None
	
	try:
   		l_test=Livertest.objects.get(patient_id = pat_id)
	except Livertest.DoesNotExist:
		l_test= None

	try:
   		profile=UserProfile.objects.get(user_id= pat_id)
	except UserProfile.DoesNotExist:
		profile= None
	
	return render(request,'labs/home.html',{'l_test':l_test , 'b_test':b_test , 'profile':profile})