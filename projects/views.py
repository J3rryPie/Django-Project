from django.shortcuts import render, get_object_or_404, redirect
from .models import Project
from .form import ProjectForm
from .form import comment_form
from .models import Comments
from csi_student.models import Student
# from .functions import handle_uploaded_file
from django.core.files.storage import FileSystemStorage


# Create your views here.
def all_projects(request):
    queryset = Project.objects.all()
    # print(queryset)
    context = {
        "object_list": queryset
    }
    return render(request, "projects/all_projects.html", context)


def create_project_view(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            name = request.user
            stud_name = Student.objects.get(name=name)
            instance.author = stud_name
            #instance.author = request.user  # Do this once login is done!
            # instance.author='Anonymous'
            instance.save()
            return redirect('../')
    else:
        form = ProjectForm()
    return render(request, "projects/create_project.html", {'form': form})


def one_project_view(request, id):
    obj = Project.objects.get(id=id)
    print(obj.author)
    all = Comments.objects.filter(Project_title_id=obj.id)
    form = comment_form(request.POST or None)
    if form.is_valid():
        c = form.cleaned_data["comment"]
        instance = form.save(commit=False)
        instance.comments = c
        instance.Project_title = obj
        instance.save()
        form = comment_form()
    context = {
        "all": all,
        "con": obj,
        "form": form,
    }
    return render(request, "projects/one_project.html", context)
