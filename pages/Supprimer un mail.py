import streamlit as st
import json
import os

# Charger les données JSON depuis le fichier
def charger_donnees():
    try:
        with open('messages.json', 'r') as file:
            data = json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        data = []
    return data

# Fonction pour supprimer un message par son ID
def supprimer_message(identifiant, messages):
    messages = [message for message in messages if message['id'] != identifiant]
    return messages

# Fonction pour mettre à jour les ID après suppression d'un message
def update_id(messages):
    for i, message in enumerate(messages, start=1):
        message['id'] = i 
        nouveau_chemin = os.path.join('stockage_fichiers', f"{i}.html")
        ancien_chemin = message['path']

        # Mettre à jour le chemin dans les données
        message['path'] = nouveau_chemin

        # Renommer le fichier
        if os.path.exists(ancien_chemin):
            os.rename(ancien_chemin, nouveau_chemin)

    return messages

# Supprimer le fichier HTML associé
def supprimer_fichier_html(identifiant):
    chemin_fichier_html = os.path.join('stockage_fichiers', f'{identifiant}.html')
    if os.path.exists(chemin_fichier_html):
        os.remove(chemin_fichier_html)

# Sauvegarder les données JSON dans le fichier
def sauvegarder_donnees(data):
    with open('messages.json', 'w') as file:
        json.dump(data, file, indent=4, separators=(',', ':'))

def afficher_delete():
    st.title('Supprimer un mail d\'exemple')

    # Charger les données JSON depuis le fichier
    messages_disponibles = charger_donnees()

    # Utiliser selectbox pour choisir le fichier HTML
    choix = st.selectbox('Choisir un mail à supprimer', [message['objet'] for message in messages_disponibles])

    # Trouver l'ID correspondant à l'objet sélectionné
    choix_id = next((message['id'] for message in messages_disponibles if message['objet'] == choix), None)

    if choix_id is not None and st.button('Supprimer'):
        # Supprimer l'élément sélectionné
        messages_disponibles = supprimer_message(choix_id, messages_disponibles)

        # Supprimer le fichier HTML associé
        supprimer_fichier_html(choix_id)

        # Mettre à jour les ID et les chemins (paths)
        update_id(messages_disponibles)

        # Sauvegarder les données mises à jour dans le fichier JSON
        sauvegarder_donnees(messages_disponibles)

        st.success(f'Mail d\'exemple avec l\'objet "{choix}" supprimé avec succès.')

        # Redémarrer l'application Streamlit pour recharger la page
        st.experimental_rerun()

afficher_delete()
