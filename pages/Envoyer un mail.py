import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import json
import ssl
from dotenv import load_dotenv
import os

load_dotenv()

def afficher_formulaire():
    st.title('Envoyer un mail')
    receiver = st.text_input('Destinataire', '')
    sender = st.text_input('Header From', '')  # Nouvel input pour le champ "Header From"

    # Charger les données JSON depuis le fichier
    messages_disponibles = charger_donnees()

    # Utiliser selectbox pour choisir le fichier HTML
    choix = st.selectbox('Choisir un fichier HTML', [message['objet'] for message in messages_disponibles])

    # Prévisualiser les fichiers HTML
    for message in messages_disponibles:
        if message['objet'] == choix:
            chemin = message.get('path', '')

    if st.button('Soumettre'):
        st.success(f'Données soumises : Destinataire: {receiver}, Header From: {sender}')

        # Paramètres du serveur SMTP
        smtp_address = 'next.optimails.com'
        smtp_port = 465  # Port standard pour le serveur SMTP avec SSL

        # Informations sur l'adresse e-mail
        email_address = os.getenv("EMAIL")

        # Sélection du fichier HTML en fonction de la selectbox
        chemin = [message.get('path', '') for message in messages_disponibles if message['objet'] == choix][0]
        sujet = [message.get('objet', '') for message in messages_disponibles if message['objet'] == choix][0]

        # Vérifier si le chemin du contenu HTML est disponible
        if chemin:
            # Lire le contenu du fichier HTML
            with open(chemin, "r", encoding="utf-8") as file:
                html_content = file.read()

            # Création de l'e-mail
            message = MIMEMultipart("alternative")
            message["Subject"] = sujet
            message["From"] = sender if sender else email_address  # Utilisation de l'expéditeur personnalisé ou de l'enveloppe "From"
            message["To"] = receiver

            # Ajout du contenu HTML
            html_mime = MIMEText(html_content, 'html')
            message.attach(html_mime)

            # Connexion au serveur avec SSL
            context = ssl.create_default_context()
            server = smtplib.SMTP_SSL(smtp_address, smtp_port, context=context)

            # Connexion au serveur avec le nom d'utilisateur et le mot de passe
            server.login(email_address, os.getenv("MDP"))

            # Envoi de l'e-mail
            server.sendmail(email_address, receiver, message.as_string())

            # Fermeture de la connexion
            server.quit()
        else:
            st.error('Le contenu du message sélectionné n\'est pas disponible.')

# Charger les données JSON depuis le fichier
def charger_donnees():
    try:
        with open('messages.json', 'r') as file:
            data = json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        data = []
    return data


afficher_formulaire()
