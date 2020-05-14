from django.shortcuts import render,get_object_or_404, redirect
from .models import Projects
from django.core.paginator import Paginator
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail



# Create your views here.
from storage.models import Extra
def index(request):
    resume = get_object_or_404(Extra, id=1)
    context = {
        'resume': resume
    }
    return render(request,'pages/index.html',context)

def about(request):
    return render(request,'pages/about.html')

def projects(request):
    projects = Projects.objects.all()
    paginator = Paginator(projects,6)
    page = request.GET.get('page')
    page_posts = paginator.get_page(page)
    return render(request,'pages/projects.html',{'projects':page_posts})

def user_login(request):
    user = User
    if request.user.is_authenticated:
        return redirect('private')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('private')
            else:
                return redirect('login')
        else:
            return render(request, 'pages/login.html')
@login_required
def user_logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('index')
def contact_me(request):
    if request.method == 'POST':
        print(request.POST)
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        send_mail(
            name + ' has sent you  a message :',
            message +', his email id is:' +email,
            'cristomathew7@gmail.com',
            ['cristomathew7@gmail.com'],
            fail_silently = False
        )
    return redirect ('about')