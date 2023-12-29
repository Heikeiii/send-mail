
1. Installer Docker
2. Créer un dossier `app` 
3. Aller dans le dossier
4. Cloner le repo git (celui-ci est sur mon github personnel, voir à le mettre dans gitlab)

```
git clone git@github.com:Heikeiii/send-mail.git
```

5. Créer un fichier `.env` contenant 2 variables

```
MAIL="Adresse mail d'envoi"
MDP="Mot de passe de l'adresse d'envoi"
```
6. Créer un fichier `Dockerfile` et le mettre dans le dossier `app`

```
# app/Dockerfile

FROM python:3.9-slim

WORKDIR /app

# Installer les outils nécessaires, y compris OpenSSH
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copier le contenu du dossier send-mail dans le dossier /app du conteneur
COPY send-mail /app

# Copier le fichier .env crée au préalable
COPY .env /app

# Installer les dépendances Python
RUN pip3 install -r /app/requirements.txt

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# Lancer le fichier Accueil.py depuis le dossier /app/send-mail
ENTRYPOINT ["streamlit", "run", "/app/Accueil.py", "--server.port=8501", "--server.address=0.0.0.0"]

```

7. Créer l'image docker

```
 docker build -t streamlit .
```

8. Lancer l'image docker

```
docker run -d -p 8501:8501 streamlit
```

9. Se rendre au lien suivant : 

```
http://{IP de la machine}:8501/
```
