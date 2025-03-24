import time
from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    """Commande personnalisée Django pour attendre que la base de données soit disponible"""

    def handle(self, *args, **options):
        self.stdout.write("🕒 Attente de la base de données...")
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections['default']
                self.stdout.write(self.style.SUCCESS("✅ Base de données disponible !"))
            except OperationalError:
                self.stdout.write("⏳ Base de données indisponible, nouvelle tentative dans 1 seconde...")
                time.sleep(1)
