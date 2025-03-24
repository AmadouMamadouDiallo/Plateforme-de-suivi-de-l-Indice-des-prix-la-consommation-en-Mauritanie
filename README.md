# 📊 Suivi de l'Indice des Prix à la Consommation en Mauritanie

> **Une plateforme web interactive pour analyser l'évolution de l'IPC en Mauritanie.**  
> 🔍 Suivi des prix | 📈 Visualisation des tendances | 💰 Indicateurs économiques  

---

## 🌍 Table des Matières  
1. [📖 Description du Projet](#-description-du-projet)  
2. [🎯 Objectif](#-objectif)  
3. [⚙️ Technologies Utilisées](#%EF%B8%8F-technologies-utilisées)  
4. [🚀 Fonctionnalités Clés](#-fonctionnalités-clés)  
5. [📸 Aperçu Visuel](#-aperçu-visuel)  
6. [📦 Installation & Utilisation](#-installation--utilisation)  
7. [🛠️ Améliorations Possibles](#%EF%B8%8F-améliorations-possibles)  
8. [📬 Contact](#-contact)  

---

## 📖 Description du Projet  
Ce projet est une **plateforme web** permettant de **suivre et analyser** l'évolution de l'Indice des Prix à la Consommation (**IPC**) en Mauritanie.  

🔹 Interface interactive pour explorer les données 📊  
🔹 Outils d'analyse avancés pour les économistes et décideurs 🏦  

---

## 🎯 Objectif  
**💡 Offrir une visualisation claire et dynamique des tendances économiques.**  
✔️ Faciliter l'accès aux données d'inflation  
✔️ Aider à la prise de décision économique et financière  

**🛠️ Public cible :**  
📊 **Économistes & chercheurs**  
📈 **Gouvernements & institutions**  
💰 **Entrepreneurs & investisseurs**  
🏠 **Citoyens curieux de l’inflation**  

---

## ⚙️ Technologies Utilisées  

| Technologie | Rôle |
|------------|------|
| 🐍 **Python** | Backend et traitement des données |
| 🌍 **Django** | Développement du serveur web |
| 🗄️ **PostgreSQL** | Base de données |
| 🎨 **HTML / CSS / JS** | Interface utilisateur |
| 📊 **Chart.js / D3.js** | Visualisation des tendances |
| 🐳 **Docker** | Conteneurisation et déploiement |

---

## 🚀 Fonctionnalités Clés  
✅ **Tableau de bord interactif** – Visualisation des prix par produit et région  
✅ **Filtres avancés** – Recherche par catégorie, date, région  
✅ **Graphiques dynamiques** – Courbes, histogrammes, heatmaps  
✅ **API RESTful** – Accès aux données JSON  
✅ **Mode Admin** – Gestion des données via Django Admin  
✅ **Déploiement Dockerisé** – Facile à exécuter sans config complexe  

---

## 📸 Aperçu Visuel  

| Tableau de bord 📊 | Analyse des prix 🏷️ |
|--------------------|--------------------|
| ![Dashboard](https://via.placeholder.com/600x300) | ![Graphiques](https://via.placeholder.com/600x300) |

> 🖼️ **Ajoute des captures d'écran ici !**  

---

## 📦 Installation & Utilisation  

```bash
# 1️⃣ Cloner le projet
git clone https://github.com/AmadouMamadouDiallo/Suivi-de-I-indice-des-prix-a-la-consommation-en-Mauritanie.git
cd Suivi-de-I-indice-des-prix-a-la-consommation-en-Mauritanie

# 2️⃣ Créer un environnement virtuel et installer les dépendances
python -m venv venv
source venv/bin/activate  # (Sous Windows: venv\Scripts\activate)
pip install -r requirements.txt

# 3️⃣ Lancer le serveur Django
python manage.py migrate
python manage.py runserver

# 4️⃣ Accéder à l'application
http://127.0.0.1:8000/
