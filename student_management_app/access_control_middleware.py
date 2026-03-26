from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render, redirect
from django.urls import reverse


class LoginCheckMiddleWare(MiddlewareMixin):

    def process_view(self, request, view_func, view_args, view_kwargs):
        modulename = view_func.__module__
        user = request.user

        if modulename == "django.views.static" or modulename == "django.contrib.staticfiles.views":
            return None

        if modulename.startswith("django.contrib.admin"):
            return None

        if modulename == "student_management_app.debug_views":
            return None

        if modulename == "whitenoise.middleware":
            return None

        if user.is_authenticated:
            if user.user_type == "1":
                if modulename == "student_management_app.admin_portal_views":
                    pass
                elif modulename == "student_management_app.views":
                    pass
                else:
                    return redirect("admin_home")

            elif user.user_type == "2":
                if modulename == "student_management_app.faculty_portal_views":
                    pass
                elif modulename == "student_management_app.views":
                    pass
                else:
                    return redirect("staff_home")

            elif user.user_type == "3":
                if modulename == "student_management_app.learner_portal_views":
                    pass
                elif modulename == "student_management_app.views":
                    pass
                else:
                    return redirect("student_home")

            else:
                return redirect("login")

        else:
            if request.path == reverse("login") or request.path == reverse("doLogin"):
                pass
            elif request.path.startswith("/static/") or request.path.startswith("/media/") or request.path.startswith("/admin/"):
                pass
            elif request.path.startswith("/debug/"):
                pass
            else:
                return redirect("login")
