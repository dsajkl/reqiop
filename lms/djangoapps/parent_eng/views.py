# Create your views here.
# Create your views here.
#from django.http import httpResponse
	
	#def home(request):
	#	return HttpResponse("Hello World!!!!!!!")

'''
from courseware import grades
from xmodule.modulestore.django import modulestore
from courseware.courses import get_courses, get_course, get_studio_url, get_course_with_access, sort_by_announcement

import survey.utils
import survey.views

from courseware.access import has_access
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
'''



from django.contrib.auth.decorators import login_required
from django_future.csrf import ensure_csrf_cookie



from django.http import Http404
from edxmako.shortcuts import  render_to_response
from edxmako.shortcuts import render_to_string
#from django.db import connection
#from django.shortcuts import render
#from student.models import CourseEnrollment
#from django.contrib.auth.models import User

#from django.template import Context

#from django.shortcuts import * # render_to_response
from .forms import *
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from .models import P_Data
from django.http import HttpResponse

from django.core.mail import send_mail, BadHeaderError


from django.contrib.auth.models import User, AnonymousUser
from django.core.exceptions import ObjectDoesNotExist

#from screamshot.utils import render_template

#def home(request):return render_to_response("parent/home.html", {'hello':"hi this is block test"})
@login_required
@ensure_csrf_cookie
#def home(request):return render_to_response('p_form1.html')
def home(request):#render_template('dashboard.html', {'context': 'variables'}, output='/media/sf_Production_sF/rendering.png', format='png')


	k = request.user.id
	try:
		st_id = P_Data.objects.get(studentid=k) 
	except ObjectDoesNotExist:
		return render_to_response('p_form1.html')        
       
	return render_to_response('p_alreadyRegistered.html',{"name":st_id.parentname, "email":st_id.parentemail, "phone":st_id.parentphone})



#templates/parent/form1.html
@login_required
@ensure_csrf_cookie
def create(request):
	#if request.POST: 
	#	form = Forms(request.POST)
	#	if form.is_valid():
	#		form.save()

 	k = request.user.id
	try:
                st_id = P_Data.objects.get(studentid=k)
		return render_to_response('p_alreadyRegistered.html',{"name":st_id.parentname, "email":st_id.parentemail, "phone":st_id.parentphone})

	except ObjectDoesNotExist:
		if 'name' in request.GET:
			if 'email' in request.GET and 'phone' in request.GET:
				p_name = request.GET['name']
				p_email = request.GET['email']
				p_phone = request.GET['phone']
				p_studentid = request.user.id
				p_studentemail =request.user.email

			
				new_p = P_Data(studentid = p_studentid,studentemail = p_studentemail, parentname = p_name, parentemail = p_email, parentphone = p_phone)
				new_p.save()
				return HttpResponse('Data saved sucessfully, thankyou')
		return  HttpResponse('Some input data are missing or invalid') #render_to_response('home', args)


	#else:
	#	form = Forms()
	
	#args = {}
	#args.update(csrf(request))
	#args['form'] = form





@login_required
@ensure_csrf_cookie
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

'''
@login_required
@cache_control(no_cache=True, no_store=True, must_revalidate=True)
@transaction.commit_manually
@ensure_valid_course_key
def progress(request, course_id, student_id=None):
    """
    Wraps "_progress" with the manual_transaction context manager just in case
    there are unanticipated errors.
    """

    course_key = SlashSeparatedCourseKey.from_deprecated_string(course_id)

    with modulestore().bulk_operations(course_key):
        with grades.manual_transaction():
            return _progress(request, course_key, student_id)


def _progress(request, course_key, student_id):
    """
    Unwrapped version of "progress".
    User progress. We show the grade bar and every problem score.
    Course staff are allowed to see the progress of students in their class.
    """
    course = get_course_with_access(request.user, 'load', course_key, depth=None, check_if_enrolled=True)

    # check to see if there is a required survey that must be taken before
    # the user can access the course.
    if survey.utils.must_answer_survey(course, request.user):
        return redirect(reverse('course_survey', args=[unicode(course.id)]))

    staff_access = has_access(request.user, 'staff', course)

    if student_id is None or student_id == request.user.id:
        # always allowed to see your own profile
        student = request.user
    else:
        # Requesting access to a different student's profile
        if not staff_access:
            raise Http404
        student = User.objects.get(id=int(student_id))

    # NOTE: To make sure impersonation by instructor works, use
    # student instead of request.user in the rest of the function.

    # The pre-fetching of groups is done to make auth checks not require an
    # additional DB lookup (this kills the Progress page in particular).
    student = User.objects.prefetch_related("groups").get(id=student.id)

    courseware_summary = grades.progress_summary(student, request, course)
    studio_url = get_studio_url(course, 'settings/grading')
    grade_summary = grades.grade(student, request, course)

    if courseware_summary is None:
        #This means the student didn't have access to the course (which the instructor requested)
        raise Http404

    context = {
        'course': course,
        'courseware_summary': courseware_summary,
        'studio_url': studio_url,
        'grade_summary': grade_summary,
        'staff_access': staff_access,
        'student': student,
        'reverifications': fetch_reverify_banner_info(request, course_key)
    }

    with grades.manual_transaction():
        response = render_to_response('courseware/progress.html', context)

    return response
'''
