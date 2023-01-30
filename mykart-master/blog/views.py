from django.http import HttpResponse
from django.shortcuts import render

from blog.models import Blogpost


# Create your views here.
def index(request):
    allblog = Blogpost.objects.all()
    return render(request, 'blog/index.html',{ 'allblog':allblog})


def blogpost(request,id):
    blog = Blogpost.objects.filter(post_id=id)

    return render(request, 'blog/blogpost.html',{'blog':blog[0]})
