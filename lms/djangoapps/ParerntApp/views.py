# Create your views here.
#from django.http import httpResponse
	
	#def home(request):
	#	return HttpResponse("Hello World!!!!!!!")

from django.shortcuts import * # render_to_response
from ParerntApp.forms import *
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from .models import ParentData
from django.http import HttpResponse

from django.core.mail import send_mail, BadHeaderError

#def home(request):return render_to_response("parent/home.html", {'hello':"hi this is block test"})

def home(request):return render_to_response("parent/form1.html", {'form':Forms()},context_instance=RequestContext(request))


def create(request):
	if request.POST: 
		form = Forms(request.POST)
		if form.is_valid():
			form.save()
			
			return HttpResponse('Data saved sucessfully')
	else:
		form = Forms()
	
	args = {}
	args.update(csrf(request))
	args['form'] = form

	return  HttpResponse('Some input data are missing or invalid') #render_to_response('home', args)


def sendmail(request):
    subject = 'Hello from my app'	# request.POST.get('subject', '')
    message = 'This is the message'   #request.POST.get('message', '')
    from_email = 'aiemailelslam@example.com'   # request.POST.get('from_email', '')
    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, ['khaled.fahmy.ee@gmail.com'], fail_silently=False)
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponse('Emailsent...thanks')
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponse('Make sure all fields are entered and valid.')
