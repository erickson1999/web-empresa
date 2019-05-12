from django.shortcuts import render
from .models import Project
# Create your views here.

def about(request):
    projects=Project.objects.all()
    return render(request,"core/about.html",{'projects':projects})
