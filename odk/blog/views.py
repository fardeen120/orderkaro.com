from django.shortcuts import render
from django.http import HttpResponse
from .models import Blogpost
from django.contrib.auth.models import User
from django.contrib import messages

def index(request):
    mypost=Blogpost.objects.all()
    return render(request,'blog\index.html',{'mypost':mypost})

def blogpost(request,id):
    post=Blogpost.objects.filter(post_id=id)[0]
    return render(request,'blog/blogpost.html',{'post':post})


def handlesignup(request):
    if request.method == "POST":
        # Get the post parameters
        username = request.POST['username']
        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # check for errorneous input

        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, " Your iCoder has been successfully created")


    else:
        return HttpResponse("404 - Not found")

# Create your views here.