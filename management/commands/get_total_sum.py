from django.core.management.base import BaseCommand
from shopapp.models import Order


class Command(BaseCommand):
    help = 'Obtaining a total amount greater than the specified one'

    def add_arguments(self,parser):
        parser.add_argument('total_sum', type=int)

    def handle(self, *args, **kwargs):
        total_sum = kwargs['total_sum']
        order = Order.objects.filter(total_sum__gt=total_sum)
        self.stdout.write(f'{order}')