from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class SessionYearModel(TimeStampedModel):
    session_start_year = models.DateField()
    session_end_year = models.DateField()

    def __str__(self):
        return f"{self.session_start_year} to {self.session_end_year}"


class CustomUser(AbstractUser):
    HOD = "1"
    STAFF = "2"
    STUDENT = "3"

    USER_TYPE_CHOICES = (
        (HOD, "HOD"),
        (STAFF, "Staff"),
        (STUDENT, "Student"),
    )

    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default=HOD)

    def __str__(self):
        return self.get_full_name() or self.username


class AdminHOD(TimeStampedModel):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.admin.email


class Staffs(TimeStampedModel):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    profile_pic = models.FileField(upload_to="staff_profile_pics/", blank=True, null=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.admin.get_full_name() or self.admin.username


class Courses(TimeStampedModel):
    course_name = models.CharField(max_length=255)

    def __str__(self):
        return self.course_name


class Subjects(TimeStampedModel):
    subject_name = models.CharField(max_length=255)
    course_id = models.ForeignKey(Courses, on_delete=models.CASCADE, default=1)
    staff_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject_name


class Students(TimeStampedModel):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    gender = models.CharField(max_length=50, blank=True)
    profile_pic = models.FileField(upload_to="student_profile_pics/", blank=True, null=True)
    address = models.TextField(blank=True)
    course_id = models.ForeignKey(Courses, on_delete=models.DO_NOTHING, default=1)
    session_year_id = models.ForeignKey(SessionYearModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.admin.get_full_name() or self.admin.username


class Attendance(TimeStampedModel):
    subject_id = models.ForeignKey(Subjects, on_delete=models.DO_NOTHING)
    attendance_date = models.DateField()
    session_year_id = models.ForeignKey(SessionYearModel, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.subject_id.subject_name} - {self.attendance_date}"


class AttendanceReport(TimeStampedModel):
    student_id = models.ForeignKey(Students, on_delete=models.DO_NOTHING)
    attendance_id = models.ForeignKey(Attendance, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)


class LeaveReportStudent(TimeStampedModel):
    student_id = models.ForeignKey(Students, on_delete=models.CASCADE)
    leave_date = models.CharField(max_length=255)
    leave_message = models.TextField()
    leave_status = models.IntegerField(default=0)


class LeaveReportStaff(TimeStampedModel):
    staff_id = models.ForeignKey(Staffs, on_delete=models.CASCADE)
    leave_date = models.CharField(max_length=255)
    leave_message = models.TextField()
    leave_status = models.IntegerField(default=0)


class FeedBackStudent(TimeStampedModel):
    student_id = models.ForeignKey(Students, on_delete=models.CASCADE)
    feedback = models.TextField()
    feedback_reply = models.TextField(blank=True)


class FeedBackStaffs(TimeStampedModel):
    staff_id = models.ForeignKey(Staffs, on_delete=models.CASCADE)
    feedback = models.TextField()
    feedback_reply = models.TextField(blank=True)


class NotificationStudent(TimeStampedModel):
    student_id = models.ForeignKey(Students, on_delete=models.CASCADE)
    message = models.TextField()


class NotificationStaffs(TimeStampedModel):
    stafff_id = models.ForeignKey(Staffs, on_delete=models.CASCADE)
    message = models.TextField()


class StudentResult(TimeStampedModel):
    student_id = models.ForeignKey(Students, on_delete=models.CASCADE)
    subject_id = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    subject_exam_marks = models.FloatField(default=0)
    subject_assignment_marks = models.FloatField(default=0)

    class Meta:
        unique_together = ("student_id", "subject_id")


@receiver(post_save, sender=CustomUser)
def build_user_role_profile(sender, instance, created, **kwargs):
    if not created:
        return

    user_type = str(instance.user_type)

    if user_type == CustomUser.HOD:
        AdminHOD.objects.create(admin=instance)
    elif user_type == CustomUser.STAFF:
        Staffs.objects.create(admin=instance, address="")
    elif user_type == CustomUser.STUDENT:
        default_course = Courses.objects.first()
        default_session = SessionYearModel.objects.first()
        if default_course and default_session:
            Students.objects.create(
                admin=instance,
                course_id=default_course,
                session_year_id=default_session,
                address="",
                gender="",
            )


@receiver(post_save, sender=CustomUser)
def sync_user_role_profile(sender, instance, **kwargs):
    user_type = str(instance.user_type)
    try:
        if user_type == CustomUser.HOD and hasattr(instance, "adminhod"):
            instance.adminhod.save()
        elif user_type == CustomUser.STAFF and hasattr(instance, "staffs"):
            instance.staffs.save()
        elif user_type == CustomUser.STUDENT and hasattr(instance, "students"):
            instance.students.save()
    except Exception:
        pass

