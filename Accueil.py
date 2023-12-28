import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.title('Accueil')

accueil_md = "Accueil.md"


# Charger le contenu du fichier Markdown (.md)
with open(accueil_md, 'r', encoding='utf-8') as file:
    contenu_md = file.read()

# Afficher le contenu du fichier Markdown
st.markdown(contenu_md)
st.image("send_mail.png")
