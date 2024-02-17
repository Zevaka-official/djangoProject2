import os

from django.core.management.base import BaseCommand

from users_app.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email=os.getenv('ADMIN_EMAIL'),
            first_name='Admin',
            last_name='Admin',
            is_superuser=True,
            is_staff=True,
            is_active=True
        )
        user.set_password(os.getenv('ADMIN_PW'))
        user.save()
