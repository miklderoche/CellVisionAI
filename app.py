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

# Contenu de la page "Projet"
def page_projet():
    st.title("Projet", size=30)
    st.header('Le Projet')

    # Onglet "Objectif du Projet"
    with st.tabs(["Objectif du Projet", "Fonctionnalités"]):
        if st.tab_selection == "Objectif du Projet":
            st.write(
                '''
                Voici l'objectif du projet.
                ''',
                size=16,
            )
            st.write(
                '''
                Le projet **CellVisionAI** vise à créer un outil d'aide au diagnostic de la leucémie. Cet outil sera basé sur des algorithmes d'apprentissage machine et d'apprentissage profond capables de reconnaître et de classifier les cellules du sang.
                ''',
                size=14,
            )
        elif st.tab_selection == "Fonctionnalités":
            st.write(
                '''
                Voici les fonctionnalités du projet.
                ''',
                size=16,
            )
            st.write(
                '''
                Le projet **CellVisionAI** aura les fonctionnalités suivantes :
                * Reconnaissance des cellules du sang
                * Classification des cellules du sang
                * Diagnostic de la leucémie
                ''',
                size=14,
            )

# Contenu de la page "Démonstration"
def page_demo():
    st.title("Démonstration", size=30)
    st.header('Objectif de la démonstration')

    st.write(
        '''
        La démonstration du projet **CellVisionAI** consiste en une interface utilisateur permettant à l'utilisateur de charger une image de frottis sanguin. L'outil est ensuite capable de reconnaître et de classifier les cellules du sang présentes dans l'image.
        ''',
        size=16,
    )

# Contenu de la page "Résultats"
def page_resultats():
    st.title("Résultats", size=30)
    st.header('Objectif des résultats')

    st.write(
        '''
        Les résultats du projet **CellVisionAI** sont encore en cours d'évaluation. Cependant, les premiers résultats sont prometteurs. L'outil est capable de reconnaître et de classifier avec précision les cellules du sang présentes dans les frottis


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

# %% (_.~" DÉMONSTRATION "~._) 

# Chargement de l'image
if st.session_state['page'] == 'Démonstration':
    image = st.file_uploader(label='Charger une image')

    if image is not None:
        # Détection et classification des cellules du sang
        cells = detect_and_classify_cells(image)

        # Affichage des résultats
        st.write('Les cellules du sang détectées sont les suivantes :')
        for cell in cells:
            st.write(cell)

# %% (_.~" RÉSULTATS "~._) 

# Affichage des résultats
if st.session_state['page'] == 'Résultats':
    st.write(
        '''
        Les résultats du projet **CellVisionAI** sont encore en cours d'évaluation. Cependant, les premiers résultats sont prometteurs. L'outil est capable de reconnaître et de classifier avec précision les cellules du sang présentes dans les frottis sanguins.

        Les résultats sont présentés sous forme de tableaux et de graphiques. Ils montrent que l'outil est capable de reconnaître et de classifier avec précision les différents types de cellules du sang, y compris les leucocytes anormaux.

        Le projet **CellVisionAI** a le potentiel de révolutionner le diagnostic de la leucémie. Il pourrait permettre aux médecins de diagnostiquer la leucémie plus rapidement et plus précisément, ce qui pourrait améliorer les chances de survie des patients.
        ''',
        size=14,
    )

# %% (_.~" DOCUMENTATION "~._) 

# Affichage de la documentation
if st.session_state['page'] == 'Documentation':
    st.write(
        '''
        La documentation du projet **CellVisionAI** est disponible sur le site web du projet. Elle comprend une description détaillée de l'outil, ainsi que des instructions d'utilisation.

        La documentation est disponible en anglais et en français.
        ''',
        size=14,
    )
