# Open-Meteo Forecast Viewer

Open-Meteo Forecast Viewer est une application Python qui récupère et affiche la météo prévue pour le lendemain à partir des coordonnées géographiques (latitude et longitude) que vous fournissez.

## Fonctionnalités
- Récupère les prévisions de temperatures pour le jour suivant.
- Affiche les informations de manière simple et lisible via un graphique.
- Entrée facile via latitude et longitude.

## Installation en mode standalone
1. Clonez le dépôt :
```bash
git clone https://github.com/votre-utilisateur/open-meteo-forecast-viewer.git
cd open-meteo-forecast-viewer
```

2. Installer les librairies:
```bash
pip install -r requirements.txt python weather.py
```

3. Lancer le programme:
```bash
python weather.py
```

## Installation via docker
1. Construire l’image Docker :
```bash
docker build -t weather-forecast .
```

2. Lancer le conteneur:
```bash
docker run -it --rm weather-forecast
```

