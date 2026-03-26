from datetime import date

from django.core.management.base import BaseCommand

from student_management_app.models import (
    Attendance,
    AttendanceReport,
    Courses,
    CustomUser,
    FeedBackStaffs,
    FeedBackStudent,
    LeaveReportStaff,
    LeaveReportStudent,
    SessionYearModel,
    Staffs,
    StudentResult,
    Students,
    Subjects,
)


class Command(BaseCommand):
    help = "Create demo records and login credentials for the CMS project."

    def handle(self, *args, **options):
        course, _ = Courses.objects.get_or_create(course_name="CSE (AIML)")
        session, _ = SessionYearModel.objects.get_or_create(
            session_start_year=date(2025, 1, 1),
            session_end_year=date(2026, 1, 1),
        )

        admin_user, _ = CustomUser.objects.get_or_create(
            email="admin@college.edu",
            defaults={
                "username": "admin",
                "first_name": "Admin",
                "last_name": "User",
                "user_type": CustomUser.HOD,
                "is_staff": True,
                "is_superuser": True,
            },
        )
        admin_user.username = "admin"
        admin_user.first_name = "Admin"
        admin_user.last_name = "User"
        admin_user.user_type = CustomUser.HOD
        admin_user.is_staff = True
        admin_user.is_superuser = True
        admin_user.set_password("admin123")
        admin_user.save()

        staff_user, _ = CustomUser.objects.get_or_create(
            email="staff@college.edu",
            defaults={
                "username": "staff",
                "first_name": "Staff",
                "last_name": "User",
                "user_type": CustomUser.STAFF,
            },
        )
        staff_user.username = "staff"
        staff_user.first_name = "Staff"
        staff_user.last_name = "User"
        staff_user.user_type = CustomUser.STAFF
        staff_user.set_password("staff123")
        staff_user.save()

        student_user, _ = CustomUser.objects.get_or_create(
            email="student@college.edu",
            defaults={
                "username": "student",
                "first_name": "Student",
                "last_name": "User",
                "user_type": CustomUser.STUDENT,
            },
        )
        student_user.username = "student"
        student_user.first_name = "Student"
        student_user.last_name = "User"
        student_user.user_type = CustomUser.STUDENT
        student_user.set_password("student123")
        student_user.save()

        staff_profile, _ = Staffs.objects.get_or_create(admin=staff_user)
        staff_profile.address = "Heritage Campus, Kolkata"
        staff_profile.save()

        student_profile, _ = Students.objects.get_or_create(
            admin=student_user,
            defaults={
                "course_id": course,
                "session_year_id": session,
            },
        )
        student_profile.course_id = course
        student_profile.session_year_id = session
        student_profile.gender = "Male"
        student_profile.address = "Kolkata"
        student_profile.save()

        subject, _ = Subjects.objects.get_or_create(
            subject_name="Machine Learning",
            course_id=course,
            staff_id=staff_user,
        )

        attendance, _ = Attendance.objects.get_or_create(
            subject_id=subject,
            attendance_date=date(2026, 3, 20),
            session_year_id=session,
        )
        AttendanceReport.objects.get_or_create(
            student_id=student_profile,
            attendance_id=attendance,
            defaults={"status": True},
        )

        StudentResult.objects.update_or_create(
            student_id=student_profile,
            subject_id=subject,
            defaults={
                "subject_exam_marks": 82,
                "subject_assignment_marks": 17,
            },
        )

        LeaveReportStaff.objects.get_or_create(
            staff_id=staff_profile,
            leave_date="2026-03-18",
            defaults={
                "leave_message": "Medical leave request",
                "leave_status": 1,
            },
        )
        LeaveReportStudent.objects.get_or_create(
            student_id=student_profile,
            leave_date="2026-03-19",
            defaults={
                "leave_message": "Family function",
                "leave_status": 1,
            },
        )

        FeedBackStaffs.objects.get_or_create(
            staff_id=staff_profile,
            feedback="Need projector support in Lab 2.",
            defaults={"feedback_reply": "Noted by HOD."},
        )
        FeedBackStudent.objects.get_or_create(
            student_id=student_profile,
            feedback="Course portal is working well.",
            defaults={"feedback_reply": "Thank you for the feedback."},
        )

        self.stdout.write(self.style.SUCCESS("Demo data created successfully."))
        self.stdout.write("Admin: admin@college.edu / admin123")
        self.stdout.write("Staff: staff@college.edu / staff123")
        self.stdout.write("Student: student@college.edu / student123")
