from django.shortcuts import render, get_object_or_404, redirect
from .models import Student
from projects.models import Project
from .forms import UpdateForm
from django.db.models import F


# Create your views here.
# from django.venv.Scripts.src.csi_student.models import Student


def all_students_details(request):
    queryset = Student.objects.all()
    context = {
        "object_list": queryset
    }
    print(queryset)
    return render(request, "csi_student/all_students.html", context)


def chat_window_view(request):
    obj = get_object_or_404(Student, id=id)
    context = {
        "con": obj,
    }
    return render(request, "students/chat_window.html", context)


def about_me(request, id):
    obj = Student.objects.get(id=id)
    # print(request.user)
    # pro=Project.objects.filter(author=request.user)
    pro = Project.objects.filter(author=obj.id)
    # print(pro)
    context = {
        "con": obj,
        "pro": pro,
    }
    return render(request, "csi_student/profile.html", context)


def edit_profile(request, id):
    context = {}
    print("yy")
    if request.method == 'POST':
        print("we")
        form = UpdateForm(request.POST or None)
        if form.is_valid():
            print("UFFF")
            obj = Student.objects.get(id=id)
            if obj.id == request.user:
                email_id = form.cleaned_data['email_id']
                Student.objects.get(id=id).update(email_id=email_id)
                form.save()
                context = {'form': form}
                form = UpdateForm()
        return render(request, "csi_student/edit_profile.html", context)
    else:
        return render(request, "csi_student/edit_profile.html", context)
