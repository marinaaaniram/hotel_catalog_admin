from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        if not User.objects.filter(is_superuser=True).count():
            User.objects.create_superuser(
                email='admin@admin.com',
                password='admin'
            )
