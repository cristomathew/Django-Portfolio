from django.shortcuts import render
from .models import Blog
from django.core.paginator import Paginator
# Create your views here.
def list(request):
    blog = Blog.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(blog,6)
    page = request.GET.get('page')
    page_posts = paginator.get_page(page)
    context = {
        'posts': page_posts
    }
    return render(request, 'blog/blog.html', context)