import streamlit as st
import json
import os
from email import policy
from email.parser import BytesParser
from bs4 import BeautifulSoup

# Charger les données JSON depuis le fichier
def charger_donnees():
    try:
        with open('messages.json', 'r') as file:
            data = json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        data = []
    return data

# Sauvegarder les données JSON dans le fichier
def sauvegarder_donnees(data):
    with open('messages.json', 'w') as file:
        json.dump(data, file, indent=4, separators=(',', ':'))

# Fonction pour lire le contenu HTML à partir d'un fichier EML
def lire_contenu_eml(uploaded_file):
    # Utiliser BytesParser pour parser le contenu du fichier EML
    message = BytesParser(policy=policy.default).parse(uploaded_file)

    # Extraire le sujet du message
    sujet_message = message.get('subject', 'Sujet inconnu')

    # Récupérer le corps du message
    contenu_message = extraire_contenu_html(message)

    return sujet_message, contenu_message

def afficher_formulaire():
    st.title('Ajouter un exemple d\'email')
    
    # Utiliser st.file_uploader pour permettre le téléchargement du fichier EML
    content_upload = st.file_uploader('Télécharger le fichier EML', type=['eml'])
    
    if st.button('Soumettre'):
        # Charger les données existantes depuis le fichier
        data = charger_donnees()

        id = len(data) + 1
        # Dossier de stockage des fichiers
        dossier_stockage = 'stockage_fichiers'
        # Créer le dossier de stockage s'il n'existe pas
        os.makedirs(dossier_stockage, exist_ok=True)
        # Si un fichier a été téléchargé
        if content_upload:
            # Lire le contenu HTML et le sujet à partir du fichier EML
            sujet, contenu_message = lire_contenu_eml(content_upload)
            # Enregistrer le fichier HTML dans le dossier de stockage
            chemin_fichier_html = os.path.join(dossier_stockage, f"{id}.html")
            with open(chemin_fichier_html, 'w', encoding='utf-8') as fichier_html:
                fichier_html.write(contenu_message)
            # Ajouter le nouvel e-mail à la liste avec le chemin du fichier HTML
            nouvel_email = {
                'id': id,
                'objet': sujet,
                'path': chemin_fichier_html
            }
            data.append(nouvel_email)
            # Sauvegarder les données mises à jour dans le fichier
            sauvegarder_donnees(data)
            st.success(f'E-mail ajouté : Sujet: {sujet}')
        else:
            st.warning('Veuillez télécharger un fichier EML.')

# Fonction pour extraire le contenu HTML du message
def extraire_contenu_html(message):
    # Itérer sur chaque partie du message
    for partie in message.iter_parts():
        # Vérifier si la partie est de type texte et HTML
        if partie.get_content_type() == 'text/html':
            # Récupérer et retourner le corps de la partie
            return partie.get_payload()

    # Si aucune partie HTML n'est trouvée, retourner une chaîne vide
    return ''

afficher_formulaire()
