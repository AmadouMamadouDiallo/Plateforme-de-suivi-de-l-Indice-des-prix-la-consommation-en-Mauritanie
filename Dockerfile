 # Utilisation de Python 3.10
FROM python:3.8

# Définition du répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers de l'hôte vers le conteneur
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le code source
COPY . .

# Commande par défaut pour exécuter le serveur Django
CMD ["sh", "-c", "cd prj && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]

