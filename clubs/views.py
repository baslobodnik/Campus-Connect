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

def major_detail(request, major_slug):
    major = Major.objects.get(name_slug=major_slug)
    clubs = Organization.objects.filter(pertaining_major__name_slug=major_slug)
    return render_to_response('major_detail.html',{
        'clubs':clubs,
        'major':major,
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
    organizations = Organization.objects.order_by('name')
    return render_to_response('club.html',{
        'organizations':organizations,
    })
def club_detail(request, club):
    club = Organization.objects.get(name_slug=club)
    return render_to_response('club_detail.html',{
        'club':club,
    })
def question(request):
    organization = Organization.objects.order_by('question')
    return render_to_response('question.html',{
        'question':question,
    })
def question_detail(request, question):
    question = Question.objects.order_by('name')
    return render_to_response('question.html',{
    })
