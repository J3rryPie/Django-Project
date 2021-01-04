from django.shortcuts import render, get_object_or_404, redirect
from .models import Question
from .models import Stud_Ans
from .form import Answer, NewUserForm
from .form import New_Question_Form
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
# from Scripts.src import csi_student
from csi_student.models import Student

from django import forms
# from .form import Upvote
from django.db.models import F


# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})


def about_view(request, *args, **kwags):
    return render(request, "about.html", {})


def forum_view(request):
    queryset = Question.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "forum.html", context)


def ans_view(request, id):
    try:
        queryset = Stud_Ans.objects.filter(q_id=id)
    except Stud_Ans.DoesNotExist:
        queryset = None
    obj = Question.objects.get(id=id)
    form = Answer(request.POST or None)
    if form.is_valid():
        # a=Stud_Ans(q_id=id).save()
        # print(a.id
        #  )
        Stud_Ans.objects.create(answer=form.cleaned_data["answer"], q_id=id)
        form.save()
        form = Answer()
    '''upvote_form = Upvote(request.POST or None)
    if upvote_form.is_valid():
        ans_id=upvote_form.cleaned_data["pk"]
        a=Stud_Ans.objects.get(id=ans_id)
        a.total_upvotes = F('total_upvotes') + 1
        a.save()
        upvote_form.save()
    a = Stud_Ans.objects.get(id=id)'''
    context = {
        # "a":a,
        "q_id": queryset,
        "con": obj,
        'ans_form': form,
        # 'upvote_form':upvote_form,
        # 'testing':a,
    }
    return render(request, "dynamic_questions.html", context)


def form_create_view(request, *args, **kwargs):
    form = New_Question_Form(request.POST or None)
    if form.is_valid():
        form.save()
    form = New_Question_Form()
    context = {
        'question_form': form
    }
    return render(request, "question_create.html", context)


def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New Account Created: {username}")
            Student.objects.create(name=username)
            login(request, user)
            messages.info(request, f"You are now logged in as {username}")
            print("yaaa!")
            return redirect("../forum/")
        else:
            print("FFFFFF")
            # for msg in form.error_messages:
            #   messages.error(request, f"{msg}: {form.error_messages[msg]}")
            #   print(msg)
            password1 = form.data['password1']
            password2 = form.data['password2']
            # email = form.data['email']
            for msg in form.errors.as_data():
                if msg == 'email':
                    messages.error(request, f"Declared {email} is not valid")
                if msg == 'password2' and password1 == password2:
                    messages.error(request, f"Selected password: {password1} is not strong enough")
                elif msg == 'password2' and password1 != password2:
                    messages.error(request,
                                   f"Password: '{password1}' and Confirmation Password: '{password2}' do not match")
                else:
                    messages.error(request,
                                   f"Tu Chutiya He!")
    form = UserCreationForm
    return render(request=request,
                  template_name="register.html",
                  context={"form": form})


'''



WHY DOES THIS NOT WORK???



        form=NewUserForm(request.POST or None)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            uid=form.cleaned_data.get('uid')
            interests=form.cleaned_data.get('interests')
            profile_photo=form.cleaned_data.get('profile_photo')
            Student.objects.create(password1=password1,name=username,uid=uid,interests=interests,profile_photo=profile_photo,password2=password2)
            messages.success(request, f"New account created: {username}")
            login(request,user)
            return redirect("forum/")
        else:
            print("Tu Chutiya He!")
            for msg in form.error_messages:
                print(form.cleaned_data.get('password1'))
                print(form.cleaned_data.get('password2'))
                messages.error(request, f"{msg}: {form.error_messages[msg]}")
            return render(request = request,
                          template_name = "register.html",
                          context={"form":form})
    form = NewUserForm
    return render(request = request,
                  template_name = "register.html",
                  context={"form":form})'''


def logout_view(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("../")


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('../forum')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request,
                  "login.html",
                  {"form": form})
