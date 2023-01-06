from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.contrib.auth import login,authenticate
# from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserForm
from django.contrib.auth.decorators import login_required
from .models import Executives,Resources


class HomePage(TemplateView):
    template_name='home.html'

# Login is required to access the resources page
#
@login_required
def resourcesPage(request):
        data=[
        {
            "id":"1",
            "title":"FrontEnd Roadmap",
            "description":"This is demo data for resources page",
            "resourcesURL":"https://youtube.com",
            "imageURL":"static/images/meta11.jpg"
        },
        {
            "id":"2",
            "title":"FrontEnd Roadmap",
            "description":"This is demo data for resources page",
            "resourcesURL":"https://youtube.com",
            "imageURL":"static/images/meta11.jpg"
        },
        {
            "id":"3",
            "title":"FrontEnd Roadmap",
            "description":"This is demo data for resources page",
            "resourcesURL":"https://youtube.com",
            "imageURL":"static/images/meta11.jpg"
        },
        {
            "id":"4",
            "title":"FrontEnd Roadmap",
            "description":"This is demo data for resources page",
            "resourcesURL":"https://youtube.com",
            "imageURL":"static/images/meta11.jpg"
        },
        {
            "id":"3",
            "title":"FrontEnd Roadmap",
            "description":"This is demo data for resources page",
            "resourcesURL":"https://youtube.com",
            "imageURL":"static/images/meta11.jpg"
        },
        {
            "id":"3",
            "title":"FrontEnd Roadmap",
            "description":"This is demo data for resources page",
            "resourcesURL":"https://youtube.com",
            "imageURL":"static/images/meta11.jpg"
        }
            ]
        context={
            "data":data
        }

        return render(request,'resources.html',context)



def detialPage(request,id):
    return render(request,'resource-detail.html')  


def aboutPage(request):
    executives=Executives.objects.all()
    context={
        "executives":executives
    }
    return render(request,'about.html',context)


def aboutDetailPage(request,id):
    executive=Executives.objects.get(id=id)
    context={
        "executive":executive
    }
    return render(request,"about-detail.html",context)


def signUpPage(request):
    form=CustomUserForm()
    if request.method=="POST":
        form=CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('email')
            password=form.cleaned_data.get('password1')
            user=authenticate(username=username,password=password)
            login(request,user)
            return redirect('home')
    
    return render(request,'registration/register.html',{'form':form})
