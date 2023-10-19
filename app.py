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

    # Onglet "Introduction"
    with st.tabs(["Introduction", "Objectif du Projet", "Equipe du projet"]):
        if st.tab_selection == "Introduction":
            st.write(
                '''
                Dans le domaine de la médecine et de la recherche biomédicale, l'analyse des cellules dans les frottis sanguins 
                est d'une importance cruciale pour le diagnostic et la compréhension de nombreuses pathologies. Cependant, leur 
                analyse manuelle est fastidieuse, sujette à des erreurs humaines, et peut être chronophage. De plus, cela 
                nécessite de nombreux appareils relativement onéreux et l’utilisation de consommables potentiellement dangereux.
                '''
            )
        elif st.tab_selection == "Objectif du Projet":
            st.write(
                '''
                L’objectif principal du projet **CellVisionAI** est la création d’algorithmes d’apprentissage machine et d’apprentissage profond 
                dédiés à la reconnaissance et la classification de cellules du sang. Cet outil pourrait être utilisé pour 
                faciliter le diagnostic de la leucémie en détectant des leucocytes anormaux.
                '''
            )
        else:
            st.write(
                '''
                **Projet réalisé par Wilfried Condemine, Michael Deroche, Claudia Mattei et Charles Sallard**.
                (Promotion sept23_DS Datascientest)
                '''
            )

def page_projet():
    # contenu de la page démonstration...
    st.title("Projet")
    st.header('Le Projet')
    st.write(
    '''
    Voici la page du projet.
    '''
    )

def page_demo():
    # contenu de la page démonstration...
    st.title("Démonstration")
    st.header('Objectif de la démonstration')
    st.write(
    '''
    Voici la page de la démonstration.
    '''
    )

def page_resultats():
    # contenu de la page résultats...
    st.title("Résultats")
    st.header('Objectif des résultats')
    st.write(
    '''
    Voici la page des résultats.
    '''
    )

def page_docs():
    # contenu de la page Documentation...
    st.title("Documentation")
    st.header('Objectif de la documentation')
    st.write(
    '''
    Voici la page de la documentation.
    '''
    )
   

# %% (_.~" MENU LATERAL "~._) 

# Initialisation de l'état de la session
if 'page' not in st.session_state:
    st.session_state['page'] = 'Accueil'

# Image en haut du menu latéral
st.sidebar.image('images/logo_VisionCellAI.png', width=100)

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
if st.session_state['page'] == 'Projet':
    page_projet()
if st.session_state['page'] == 'Démonstration':
    page_demo()
if st.session_state['page'] == 'Résultats':
    page_resultats()
if st.session_state['page'] == 'Documentation':
    page_docs()
