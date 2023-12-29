
>Cher utilisateur bonjour, cette plateforme sert à envoyer des mails préenregistrés afin de simuler la réception de messages malveillants. 

#### Les différentes pages :

1. Accueil

La page d'accueil est là pour présenter les différentes fonctionnalités disponibles. (c'est un tuto quoi)

2. Ajouter un mail 

Cette page permet d'ajouter un mail d'exemple à envoyer (ex: un joli spam remonté par un client) au format .eml 
Il suffit de déposer votre fichier eml, un id lui sera donné et le système récupère l'objet du message afin de pouvoir le sélectionner à l'envoi.
Le système récupère le contenu html du message et le sauvegarde dans un fichier du type {nom}.html
Les informations sont également stockées dans un fichier json dont on reparlera plus tard. 

Attention certains mails ne contenant pas de html ou encodé ne sont pas forcément pris en compte. 

3. Envoyer un mail 

Cette page permet d'envoyer des exemples de messages disponibles à un destinataire. 
Il faut entrer l'adresse du destinataire. 
Vous pouvez modifier le header FROM, par défaut les messages sont envoyés authentifiés depuis la boîte "support@secuserve.com" (voir à modifier si nécessaire)
Puis appuyer sur "Soumettre" pour envoyer

4. Supprimer un mail

Cette page permet de supprimer un exemple de mail s'il vous plait pas, il suffit de sélectionner son nom et de cliquer sur le bouton "Soumettre", cela supprimera le message au format html et également son enregistrement dans le fichier "messages.json"

#### Le stockage des messages

Les informations de chaque message sont stockés dans un fichier "messages.json" à la racine du projet contenant 3 valeurs : 

1. ID

Correspond à un identifiant unique du message

2. objet 

L'objet récupéré dans le fichier eml du message qui sera affiché dans les selectbox et envoyé aux destinataires

3. path

Le chemin du fichier html avec le contenu du message. 
Ce fichier est stocké dans un dossier "stockage_fichiers" avec un nom de type {id}.html

#### Améliorations 

1. Meilleurs prise en compte des messages ou prise en compte de plus de message, non sensible à la casse. 

2. Pouvoir envoyer des messages avec plusieurs configuration 
    - Serveurs SMTP différents
    - Authentifiés/Non authentifiés
    - Avec/Sans SPF/DKIM/DMARC/BIMI
    - Office 365 etc....

3. Affichage des messages dans ajouter/supprimer un mail dans des petites cartes (comme dans la capture mais en beau)


