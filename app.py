import streamlit as st

# %% (_.~" PAGES "~._) 

# Fonctions pour chaque page
def page_projet():
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
    L’objectif principal du projet est la création d’algorithmes d’apprentissage machine et d’apprentissage profond 
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

def page_demo():
    st.title("Démonstration")
    st.write("Voici la page de démonstration.")
    # contenu de la page démonstration...

def page_resultats():
    st.title("Résultats")
    # contenu de la page résultats...

def page_docs():
    st.title("Documentation")
    # contenu de la page Documentation...

# %% (_.~" MENU BARRE LATERALE "~._) 

# Menu latéral
st.sidebar.title("")
pages = {
    "Projet": page_projet,
    "Démonstration": page_demo,
    "Résultats": page_resultats,
    "Documentation": page_docs,
}

selection = st.sidebar.selectbox(list(pages.keys()))

# Affichage de la page en fonction de la sélection
pages[selection]()

