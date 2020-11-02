from django.shortcuts import render
from .models import offerpost
from django.http import HttpResponse


# Create your views here.
def index(request):
    myposts = offerpost.objects.all()
    print(myposts)
    return render(request, 'offer/index.html', {'myposts': myposts})


def Offerpost(request, id):
    post = offerpost.objects.filter(post_id = id)[0]
    print(post)
    return render(request, 'offer/blogpost.html', {'post':post})