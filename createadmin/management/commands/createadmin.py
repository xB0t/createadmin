from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.conf import settings

DEFAULT_ADMIN_USERNAME = "admin"
DEFAULT_ADMIN_PASSWORD = "admin"
DEFAULT_ADMIN_EMAIL = "admin@example.com"


class Command(BaseCommand):
    help = 'Create an Admin for initial setup for Production.'

    def create_superuser(self, username=DEFAULT_ADMIN_USERNAME, password=DEFAULT_ADMIN_PASSWORD, email=DEFAULT_ADMIN_EMAIL):
        User = get_user_model()
        return User.objects.create_superuser(username, email, password)

    def handle(self, *args, **options):
        try:
            users = get_user_model().objects.all()

            if users.count() == 0:
                username = getattr(settings, 'CREATE_ADMIN', {}).get(
                    'username', DEFAULT_ADMIN_USERNAME)
                password = getattr(settings, 'CREATE_ADMIN', {}).get(
                    'password', DEFAULT_ADMIN_PASSWORD)
                email = getattr(settings, 'CREATE_ADMIN', {}).get(
                    'email', DEFAULT_ADMIN_EMAIL)

                if username == DEFAULT_ADMIN_USERNAME:
                    print(
                        f'Created superuser account for username: {username}, password: {password} , and email: {email}')
                else:
                    print(
                        f'Created superuser account for username: {username} & email: {email}')

                self.create_superuser(username, password, email)
            else:
                print("One admin account already exists")
        except Exception as e:
            print(f"An error occurred: {e}")
