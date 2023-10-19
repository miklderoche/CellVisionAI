import streamlit as st

# %% (_.~" PAGES "~._) 

# Fonctions pour chaque page
def page_accueil():
# contenu de la page d'accueil...

    left_co, cent_co,last_co = st.columns(3)
    with cent_co:
        st.image('images/logo_VisionCellAI.png')

# Titre principal
    st.title('Cell Vision AI')

# Introduction
    st.write(
    '''
    Dans le domaine de la médecine et de la recherche biomédicale, l'analyse des cellules dans les frottis sanguins 
    est d'une importance cruciale pour le diagnostic et la compréhension de nombreuses pathologies. Cependant, leur 
    analyse manuelle est fastidieuse, sujette à des erreurs humaines, et peut être chronophage. De plus, cela 
    nécessite de nombreux appareils relativement onéreux et l’utilisation de consommables potentiellement dangereux.
    '''
)

# Objectif du projet
    st.header('Objectif du Projet')
    st.write(
    '''
    L’objectif principal du projet **CellVisionAI** est la création d’algorithmes d’apprentissage machine et d’apprentissage profond 
    dédiés à la reconnaissance et la classification de cellules du sang. Cet outil pourrait être utilisé pour 
    faciliter le diagnostic de la leucémie en détectant des leucocytes anormaux.
    '''
    )

# Equipe du projet
    st.write(
    '''
    **Projet réalisé par Wilfried Condemine, Michael Deroche, Claudia Mattei et Charles Sallard**.
    (Promotion sept23_DS Datascientest)
    '''
    )

def page_projet():
    # contenu de la page démonstration...
    st.title("Projet")
    st.write(
    '''
    Voici la page du projet.
    '''
    )

def page_demo():
    # contenu de la page démonstration...
    st.title("Démonstration")
    st.write("Voici la page de démonstration.")

def page_resultats():
    # contenu de la page résultats...
    st.title("Résultats")
    st.write("Voici la page des résultats.")

def page_docs():
    # contenu de la page Documentation...
    st.title("Documentation")
    st.write("Voici la page de documentation.")
   

# %% (_.~" MENU LATERAL "~._) 

# Initialisation de l'état de la session
if 'page' not in st.session_state:
    st.session_state['page'] = 'Accueil'

# Image en haut du menu latéral
st.sidebar.image('images/logo_VisionCellAI_2.png', width=100)

# Menu latéral avec des boutons
if st.sidebar.button('Accueil'):
    st.session_state['page'] = 'Accueil'
if st.sidebar.button('Projet'):
    st.session_state['page'] = 'Projet'
if st.sidebar.button('Démonstration'):
    st.session_state['page'] = 'Démonstration'
if st.sidebar.button('Résultats'):
    st.session_state['page'] = 'Résultats'
if st.sidebar.button('Documentation'):
    st.session_state['page'] = 'Documentation'

# Affichage de la page en fonction de l'état de la session
if st.session_state['page'] == 'Accueil':
    page_accueil()
elif st.session_state['page'] == 'Projet':
    page_projet()

