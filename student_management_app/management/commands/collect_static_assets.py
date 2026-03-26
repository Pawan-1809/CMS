from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.conf import settings
import os
import sys


class Command(BaseCommand):
    help = 'Collect static files safely, handling missing file errors'

    def add_arguments(self, parser):
        parser.add_argument(
            '--no-input',
            action='store_true',
            help='Do not prompt for user input'
        )
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Clear existing static files first'
        )

    def handle(self, *args, **options):
        self.stdout.write("🔧 Starting safe static file collection...")

        original_storage = settings.STATICFILES_STORAGE

        try:
            self.stdout.write("📦 Attempting collectstatic with manifest storage...")
            call_command('collectstatic',
                        interactive=not options['no_input'],
                        clear=options.get('clear', False),
                        verbosity=1)

            self.stdout.write(
                self.style.SUCCESS('✅ Static files collected successfully!')
            )

        except Exception as e:
            self.stdout.write(
                self.style.WARNING(f'⚠️  Manifest storage failed: {e}')
            )

            self.stdout.write("🔄 Falling back to basic static files storage...")

            settings.STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

            try:
                call_command('collectstatic',
                           interactive=not options['no_input'],
                           clear=options.get('clear', False),
                           verbosity=1)

                self.stdout.write(
                    self.style.SUCCESS('✅ Static files collected with basic storage!')
                )

            except Exception as fallback_error:
                self.stdout.write(
                    self.style.ERROR(f'❌ Both methods failed: {fallback_error}')
                )
                sys.exit(1)
            finally:
                settings.STATICFILES_STORAGE = original_storage
