from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.db import IntegrityError


class Command(BaseCommand):
    help = 'Fix admin user password for production deployment'

    def add_arguments(self, parser):
        parser.add_argument(
            '--email',
            type=str,
            default='admin@college.edu',
            help='Email of the admin user to fix'
        )
        parser.add_argument(
            '--password',
            type=str,
            default='admin123',
            help='New password for the admin user'
        )

    def handle(self, *args, **options):
        User = get_user_model()
        email = options['email']
        password = options['password']

        try:
            try:
                user = User.objects.get(email=email)
                self.stdout.write(
                    self.style.SUCCESS(f'✅ Found existing user with email: {email}')
                )
            except User.DoesNotExist:
                try:
                    user = User.objects.get(username=email)
                    self.stdout.write(
                        self.style.SUCCESS(f'✅ Found existing user with username: {email}')
                    )
                except User.DoesNotExist:
                    self.stdout.write(
                        self.style.WARNING(f'⚠️  User {email} not found. Creating new admin user...')
                    )
                    user = User.objects.create_superuser(
                        username=email,
                        email=email,
                        password=password,
                        first_name='Admin',
                        last_name='User',
                        user_type=1
                    )
                    self.stdout.write(
                        self.style.SUCCESS(f'✅ New admin user created!')
                    )
                    self._display_login_info(email, password)
                    return

            user.set_password(password)
            user.is_active = True
            user.is_superuser = True
            user.is_staff = True
            user.user_type = 1

            if not user.username:
                user.username = email
            if not user.email:
                user.email = email

            user.save()

            self.stdout.write(
                self.style.SUCCESS('✅ Admin user password and settings updated successfully!')
            )
            self._display_login_info(email, password)

            self.stdout.write('')
            self.stdout.write('📋 User Details:')
            self.stdout.write(f'Username: {user.username}')
            self.stdout.write(f'Email: {user.email}')
            self.stdout.write(f'Name: {user.first_name} {user.last_name}')
            self.stdout.write(f'Is Active: {user.is_active}')
            self.stdout.write(f'Is Superuser: {user.is_superuser}')
            self.stdout.write(f'Is Staff: {user.is_staff}')
            self.stdout.write(f'User Type: {user.user_type} (1=HOD, 2=Staff, 3=Student)')

        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'❌ Error fixing admin user: {e}')
            )
            raise

    def _display_login_info(self, email, password):
        self.stdout.write('')
        self.stdout.write(
            self.style.SUCCESS('🔐 Login Credentials:')
        )
        self.stdout.write(f'Email/Username: {email}')
        self.stdout.write(f'Password: {password}')
        self.stdout.write('')
        self.stdout.write(
            self.style.WARNING('⚠️  Please change this password after first login!')
        )
        self.stdout.write('')
        self.stdout.write('🌐 Try logging in at: https://college-management-portal.onrender.com')
