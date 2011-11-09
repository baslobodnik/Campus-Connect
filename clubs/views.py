# Create your views here.

from campusconnect.clubs.models import Organization, Major, College
from django.shortcuts import render_to_response

def homepage(request):
    organization = Organization.objects.order_by('club_title')
    return render_to_response('homepage.html',{
        'organization':organization,
    })
def major(request):
    major = Major.objects.order_by('name')
    return render_to_response('major.html',{
        'major':major,
    })
def college(request):
    college = College.objects.order_by('name')
    return render_to_response('college.html',{
        'college':college,
    })
