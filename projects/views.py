from django.shortcuts import render, redirect, get_list_or_404
from projects.models import Project
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from projects.forms import ProjectForm

# Create your views here.


@login_required
def list_projects(request):
    projects = Project.objects.filter(owner=request.user)
    context = {
        "projects": projects,
    }
    return render(request, "projects/list.html", context)
