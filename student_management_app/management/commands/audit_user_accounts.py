from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'List all users in the system for debugging'

    def handle(self, *args, **options):
        User = get_user_model()

        users = User.objects.all()

        if not users:
            self.stdout.write(
                self.style.WARNING('❌ No users found in the system')
            )
            return

        self.stdout.write(
            self.style.SUCCESS(f'📋 Found {users.count()} users:')
        )

        for user in users:
            status = "✅ Active" if user.is_active else "❌ Inactive"
            superuser = "👑 Superuser" if user.is_superuser else "👤 Regular"
            user_type = dict(User.USER_TYPE_CHOICES).get(str(user.user_type), "Unknown")

            self.stdout.write(f"")
            self.stdout.write(f"Username: {user.username}")
            self.stdout.write(f"Email: {user.email}")
            self.stdout.write(f"Name: {user.first_name} {user.last_name}")
            self.stdout.write(f"Status: {status}")
            self.stdout.write(f"Type: {superuser} - {user_type}")
            self.stdout.write(f"User Type Code: {user.user_type}")
            self.stdout.write("-" * 40)

        self.stdout.write("")
        self.stdout.write(
            self.style.SUCCESS('🔐 Login Instructions:')
        )
        self.stdout.write("This system uses EMAIL for authentication")
        self.stdout.write("Login with: admin@college.edu / admin123")
        self.stdout.write("")
