# Create your views here.

from campusconnect.clubs.models import Organization, Major, College
from django.shortcuts import render_to_response

def homepage(request):
    return render_to_response('homepage.html',{})

def major(request):
    major = Major.objects.order_by('name')
    return render_to_response('major.html',{
        'major':major,
    })
def major_detail(request, major):
    clubs = Organization.objects.filter(pertaining_major__name_slug=major)
    return render_to_response('major_detail.html',{
        'clubs':clubs,
    })
def college(request):
    college = College.objects.order_by('name')
    return render_to_response('college.html',{
        'college':college,
    })
def college_detail(request, college):
    clubs = Organization.objects.filter(pertaining_college__name_slug=college)
    return render_to_response('college_detail.html',{
        'clubs':clubs,
    })
def club(request):
    organization = Organization.objects.order_by('club_title')
    return render_to_response('club.html',{
        'organization':organization,
    })
def club_detail(request, detail):
    clubs = Organization.objects.filter(pertaining_club__name_slug=club)
    return render_to_response('club_detail.html',{
        'clubs':clubs,
    })
def question(request):
    organization = Organization.objects.order_by('question')
    return render_to_response('question.html',{
        'question':question,
    })
def question_detail(request, detail):
    question = Question.objects.order_by('name')
    return render_to_response('question.html',{
    })
