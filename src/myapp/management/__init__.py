 
import time
from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    """Commande pour attendre que la base de données soit disponible"""

    def handle(self, *args, **kwargs):
        self.stdout.write("⏳ Attente de la base de données...")
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections['default']
            except OperationalError:
                self.stdout.write("🔄 Base de données indisponible, nouvel essai dans 2 secondes...")
                time.sleep(2)

        self.stdout.write(self.style.SUCCESS("✅ Base de données disponible !"))
