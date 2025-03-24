<p align="center">
  
</p>

<h1 align="center">📊 Suivi de l'Indice des Prix à la Consommation en Mauritanie</h1>

<p align="center">
  <b>Une plateforme interactive pour analyser l'évolution de l'INPC en Mauritanie.</b>  
</p>

<p align="center">
  🔍 <i>Suivi des prix</i> | 📈 <i>Visualisation des tendances</i> | 💰 <i>Indicateurs économiques</i>  
</p>

---

## 🌍 Table des Matières  
🔹 [📖 Description du Projet](#-description-du-projet)  
🔹 [🎯 Objectif](#-objectif)  
🔹 [⚙️ Technologies Utilisées](#%EF%B8%8F-technologies-utilisées)  
🔹 [🚀 Fonctionnalités Clés](#-fonctionnalités-clés)  
🔹 [📸 Aperçu Visuel](#-aperçu-visuel)  
🔹 [📦 Installation & Utilisation](#-installation--utilisation)  
🔹 [💡 Améliorations Futures](#-améliorations-futures)  
🔹 [📬 Contact](#-contact)  

---

## 📖 Description du Projet  
> **Un outil moderne pour comprendre l'évolution des prix en Mauritanie.**  
📊 Interface intuitive pour explorer les variations de prix  
📉 Analyse détaillée des tendances économiques  
🛒 Comparaison des catégories de produits  

---

## 🎯 Objectif  
💡 **Offrir une visualisation dynamique et précise des tendances économiques.**  

🎯 **Pour qui ?**  
✔️ **Économistes & chercheurs** 📊  
✔️ **Gouvernements & institutions** 📈  
✔️ **Entrepreneurs & investisseurs** 💰  
✔️ **Citoyens curieux des tendances économiques** 🏠  

---

## ⚙️ Technologies Utilisées  

| 🛠️ Technologie | 🚀 Rôle |
|------------|------|
| 🐍 **Python** | Backend et traitement des données |
| 🌍 **Django** | Développement du serveur web |
| 🗄️ **PostgreSQL** | Base de données |
| 🎨 **HTML / CSS / JS** | Interface utilisateur |
| 📊 **Chart.js / D3.js** | Visualisation des tendances |
| 🐳 **Docker** | Conteneurisation et déploiement |

---

## 🚀 Fonctionnalités Clés  
✅ **📊 Tableau de bord interactif** – Suivi des prix par produit et région  
✅ **🔍 Filtres avancés** – Catégories, périodes spécifiques  
✅ **📈 Visualisation dynamique** – Graphiques (courbes, heatmaps, histogrammes...)  
✅ **📡 API RESTful** – Récupération des données JSON  
✅ **🔐 Mode Admin** – Gestion des données via Django Admin  
✅ **🐳 Déploiement Dockerisé** – Exécution rapide sans dépendances locales  

---

## 📸 Aperçu Visuel  

<img src="images/dashboard.png" alt="Tableau de bord" width="600" height="300">
<img src="images/graphique.png" alt="Graphiques dynamiques" width="600" height="300">


---
## Contact et Liens
- **LinkedIn** : www.linkedin.com/in/amadou-diallo-ing04
- **Email** : 23217@esp.mr


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
