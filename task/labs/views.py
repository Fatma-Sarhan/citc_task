from django.shortcuts import render

# Create your views here.


def index(request) :
	# output ="<b> Welcome to index page </b>"
	# return HttpResponse(output)
	return render(request,'labs/index.html')
