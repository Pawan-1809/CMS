from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render


def render_public_home(request):
    return render(request, "index.html")


def render_login_page(request):
    return render(request, "login.html")


def process_login_request(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")

    user = authenticate(
        request,
        username=request.POST.get("email"),
        password=request.POST.get("password"),
    )

    if user is None:
        messages.error(request, "Invalid Login Credentials!")
        return redirect("login")

    login(request, user)

    user_type = getattr(user, "user_type", None)
    if user_type == "1":
        return redirect("admin_home")
    if user_type == "2":
        return redirect("staff_home")
    if user_type == "3":
        return redirect("student_home")

    messages.error(request, "Invalid Login!")
    return redirect("login")


def fetch_user_details(request):
    if request.user.is_authenticated:
        return HttpResponse(
            f"User: {request.user.email} User Type: {request.user.user_type}"
        )
    return HttpResponse("Please Login First")


def process_logout_request(request):
    logout(request)
    return HttpResponseRedirect("/")

