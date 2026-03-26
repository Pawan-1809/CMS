import json

from django.test import Client, TestCase
from django.urls import reverse

from .models import Courses, CustomUser, SessionYearModel, Staffs, Students, Subjects


class PortalSmokeTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.course = Courses.objects.create(course_name="CSE (AIML)")
        self.session = SessionYearModel.objects.create(
            session_start_year="2025-01-01",
            session_end_year="2026-01-01",
        )

        self.admin_user = CustomUser.objects.create_user(
            username="admin",
            email="admin@college.edu",
            password="admin123",
            first_name="Admin",
            last_name="User",
            user_type=CustomUser.HOD,
        )
        self.staff_user = CustomUser.objects.create_user(
            username="staff",
            email="staff@college.edu",
            password="staff123",
            first_name="Staff",
            last_name="User",
            user_type=CustomUser.STAFF,
        )
        self.student_user = CustomUser.objects.create_user(
            username="student",
            email="student@college.edu",
            password="student123",
            first_name="Student",
            last_name="User",
            user_type=CustomUser.STUDENT,
        )

        self.student_profile = Students.objects.get(admin=self.student_user)
        self.student_profile.course_id = self.course
        self.student_profile.session_year_id = self.session
        self.student_profile.save()

        self.staff_profile = Staffs.objects.get(admin=self.staff_user)
        self.staff_profile.address = "Faculty Block"
        self.staff_profile.save()

        self.subject = Subjects.objects.create(
            subject_name="Data Structures",
            course_id=self.course,
            staff_id=self.staff_user,
        )

    def test_login_page_loads(self):
        response = self.client.get(reverse("login"))
        self.assertEqual(response.status_code, 200)

    def test_admin_login_redirects_to_dashboard(self):
        response = self.client.post(
            reverse("doLogin"),
            {"email": "admin@college.edu", "password": "admin123"},
        )
        self.assertRedirects(response, reverse("admin_home"))

    def test_staff_get_students_endpoint_returns_students(self):
        self.client.force_login(self.staff_user)
        response = self.client.post(
            reverse("get_students"),
            {"subject": self.subject.id, "session_year": self.session.id},
        )
        payload = json.loads(json.loads(response.content.decode()))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(payload[0]["id"], self.student_user.id)

    def test_student_dashboard_loads(self):
        self.client.force_login(self.student_user)
        response = self.client.get(reverse("student_home"))
        self.assertEqual(response.status_code, 200)

# Create your tests here.
