from django.shortcuts import render
#from django.views.generic import ListView
from .models import Project
from .forms import ProjectForm


# Create your views here.
def project_list_view(request):
    my_projects = Project.objects.all()

    return render(request, 'content/project_list.html', {"projects": my_projects})

def project_new_view(request):
    form = ProjectForm()
    return render(request, 'content/project_new.html', {'form': form})

# class ProjectListView(ListView):
#     model = Project
#     template_name = "content/project_list.html"
#     context_object_name = "projects"