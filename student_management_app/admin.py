from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import (
    AdminHOD,
    Attendance,
    AttendanceReport,
    Courses,
    CustomUser,
    FeedBackStaffs,
    FeedBackStudent,
    LeaveReportStaff,
    LeaveReportStudent,
    NotificationStaffs,
    NotificationStudent,
    SessionYearModel,
    Staffs,
    StudentResult,
    Students,
    Subjects,
)


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (("Role", {"fields": ("user_type",)}),)
    list_display = ("username", "email", "first_name", "last_name", "user_type", "is_staff")


admin.site.register(AdminHOD)
admin.site.register(Staffs)
admin.site.register(Courses)
admin.site.register(Subjects)
admin.site.register(Students)
admin.site.register(SessionYearModel)
admin.site.register(Attendance)
admin.site.register(AttendanceReport)
admin.site.register(LeaveReportStudent)
admin.site.register(LeaveReportStaff)
admin.site.register(FeedBackStudent)
admin.site.register(FeedBackStaffs)
admin.site.register(NotificationStudent)
admin.site.register(NotificationStaffs)
admin.site.register(StudentResult)
