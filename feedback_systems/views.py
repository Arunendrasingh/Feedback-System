from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.utils.datastructures import MultiValueDictKeyError
from .models import feedback
from django.utils import timezone


# Create your views here.
def home(request):
    return render(request, "home.html")


def log_in(request):
    if request.method == "POST":
        Username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=Username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid Username or Password")
            return redirect("login")
    else:
        return render(request, "login.html")


def dashboard(request):
    if request.user.is_authenticated:
        all_feedback_data = feedback.objects.all()
        try:
            maxid = all_feedback_data.order_by("-id")[0]
        except IndexError:
            maxid = 0
        print(maxid)
        return render(request, "admin.html", {
            "feedback_value": all_feedback_data,
             "total_data":all_feedback_data.count(),
              "max_id": maxid
              })
    else:
        messages.error(request, "Please Login to view this section!")
        return redirect("login")


def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
    return redirect("login")

def comming_soon(request):
    return render(request, 'comming_soon.html')


def save_feedback(request): 

    if request.method == "POST":
        try:
            user_name = request.POST["your_name"].capitalize()
            # user_name = captli(user_name)
        except MultiValueDictKeyError:
            user_name = False

        try:
            user_email = request.POST["your_email"]
        except MultiValueDictKeyError:
            user_email = False

        try:
            about_college = request.POST["abaout_your_college"].capitalize()
        except MultiValueDictKeyError:
            about_college = False

        try:
            your_branch = request.POST["branch_name"]
        except MultiValueDictKeyError:
            your_branch = False

        try:
            faculty_name = request.POST["faculty_name"].capitalize()
        except MultiValueDictKeyError:
            faculty_name = False

        try:
            subj_teacher = request.POST["subj_teacher"].upper()
        except MultiValueDictKeyError:
            subj_teacher = False

        try:
            teaching_skill = request.POST["teaching_skill"]
        except MultiValueDictKeyError:
            teaching_skill = False

        try:
            class_intraction = request.POST["class_intraction"]
        except MultiValueDictKeyError:
            class_intraction = False

        try:
            after_class_intraction = request.POST["after_class_intraction"]
        except MultiValueDictKeyError:
            after_class_intraction = False

        try:
            faculty_behaviour = request.POST["behaviour"]
        except MultiValueDictKeyError:
            faculty_behaviour = False

        try:
            knowledge_about_subj = request.POST["knowledge_about_subj"]
        except MultiValueDictKeyError:
            knowledge_about_subj = False

        try:
            Doubt_clearing = request.POST["Doubt_clearing"]
        except MultiValueDictKeyError:
            Doubt_clearing = False

        try:
            your_suggestion = request.POST["suggestion"].capitalize()
        except MultiValueDictKeyError:
            your_suggestion = False

        feed_back = feedback(
            your_name=user_name,
            your_email=user_email,
            about_college=about_college,
            your_branch=your_branch,
            faculty_name=faculty_name,
            subj_teacher=subj_teacher,
            teaching_skill=teaching_skill,
            class_feedback=class_intraction,
            after_class_feedback=after_class_intraction,
            faculty_behaviour=faculty_behaviour,
            knowledge_about_subj=knowledge_about_subj,
            Doubt_clearing=Doubt_clearing,
            your_suggestion=your_suggestion,
            feedback_date=timezone.now(),
        )
        feed_back.save()
    return render(request, "home.html")


def showfeedback(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            id_value = request.GET["id"]
            user = feedback.objects.filter(id=id_value)
            return render(request, "showfeedback.html", {"user_feedback": user})
    else:
        return redirect("login")
