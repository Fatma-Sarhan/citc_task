from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.core.context_processors import csrf

# Create your views here.


def index(request) :
	if request.COOKIES.get("sessionid", None):
		print "already"
		# return HttpResponseRedirect('loggedin')
		return HttpResponse('You are logged in')
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
		return HttpResponse('User is valid, active and authenticated')

		# return HttpResponseRedirect('loggedin')
	else:
		message = "Invalid username or password please try again !"
		return render(request,'labs/index.html',{'message':message})

		# return HttpResponse("Invalid Pass or username")
		# print ("fatma")

	return render(request,'labs/index.html')