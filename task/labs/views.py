from django.shortcuts import render
from django.http import HttpResponse
import json
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from .models import Bloodtest,Livertest,UserProfile
from django.core.context_processors import csrf
from django.core import serializers
from django.contrib.auth.models import User,Group
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
	pat_group = Group.objects.get(pk=3)
	if not request.POST.get('remember_me',''):
		request.session.set_expiry(0)
		# print "fatma"
		# return HttpResponseRedirect('loggedin')

	if user is not None:
		pat = user.groups.filter(name='Patients').exists()
		if pat:
			auth_login(request, user)
			return HttpResponseRedirect('home')
		else:
			return HttpResponseRedirect('admin')
		
	else:
		message = "Invalid username or password please try again !"
		return render(request,'labs/index.html',{'message':message})

	return render(request,'labs/index.html')


def mob_login(request):
	username = request.GET.get('username','')
	password = request.GET.get('password','')
	user = authenticate(username=username, password=password)
	pat_group = Group.objects.get(pk=3)
	data ={}

	if user is not None:
		auth_login(request, user)
		pat_id = request.user.id
		fname = str(request.user.first_name)
		lname = str(request.user.last_name)
		# b_test = Bloodtest.objects.filter(patient_id = pat_id).values_list('wbc','rbc','platelets')
		b_test = Bloodtest.objects.get(patient_id = pat_id)
		wbc = str(b_test.wbc)
		rbc = str(b_test.rbc)
		plat = str(b_test.platelets)
		l_test = Livertest.objects.get(patient_id = pat_id)
		sgot = str(l_test.sgot)
		sgpt= str(l_test.sgpt)
		alb = str(l_test.albumin)

		context={'fname':fname,'lname':lname,'wbc':wbc,'rbc':rbc,'plat':plat,'sgot':sgot,'sgpt':sgpt,'alb':alb}
		return JsonResponse(context, content_type='application/json')

		
	else:
		msg = "Invalid username or password please try again !"
		json_data = {msg:'msg'}
		return JsonResponse(json_data,content_type='application/json')
		




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