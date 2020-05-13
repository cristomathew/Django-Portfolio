from django.shortcuts import render,get_object_or_404
from .models import Projects
from django.core.paginator import Paginator

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