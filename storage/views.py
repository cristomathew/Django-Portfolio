from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Entertainment, Extra, Study, Category
# Create your views here.
@login_required
def private(request):
    return render(request, 'pages/private.html')

@login_required
def entertainment(request):
    enter = Category.objects.all().filter(typ="Entertainment")
    return render(request,'pages/entertainment.html', {'posts':enter})

@login_required
def study(request):
    enter = Category.objects.all().filter(typ="Study")
    return render(request,'pages/study.html', {'posts':enter})

@login_required
def extra(request):
    enter = Category.objects.all().filter(typ="Extra")
    return render(request,'pages/extra.html', {'posts':enter})

@login_required
def e_detail(request):
    query_set = Extra.objects.all()
    if 'category' in request.GET:
        category = request.GET['category']
        if category:
            query_set = query_set.filter(category=category)
    context = {
        'posts': query_set,
        'category':category,
        'type': 'extra'
    }
    return render(request, 'pages/detail.html', context)

@login_required
def s_detail(request):
    query_set = Study.objects.all()
    if 'category' in request.GET:
        category = request.GET['category']
        if category:
            query_set = query_set.filter(category=category)
    context = {
        'posts': query_set,
        'category':category,
        'type': 'study'
    }
    return render(request, 'pages/detail.html', context)

@login_required
def ent_detail(request):
    query_set = Entertainment.objects.all()
    if 'category' in request.GET:
        category = request.GET['category']
        if category:
            query_set = query_set.filter(category=category)
    context = {
        'posts': query_set,
        'category':category,
        'type': 'entertainment'
    }
    return render(request, 'pages/detail.html', context)