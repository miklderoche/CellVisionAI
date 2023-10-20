import streamlit as st

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
    left_co, cent_co, last_co = st.columns(3)
    with cent_co:
        st.image('images/logo_VisionCellAI.png', width=200)

    st.title('Cell Vision AI')

    st.write(
    '''
    Dans le domaine de la médecine et de la recherche biomédicale, l'analyse des cellules dans les frottis sanguins 
    est d'une importance cruciale pour le diagnostic et la compréhension de nombreuses pathologies. Cependant, leur 
    analyse manuelle est fastidieuse, sujette à des erreurs humaines, et peut être chronophage. De plus, cela 
    nécessite de nombreux appareils relativement onéreux et l’utilisation de consommables potentiellement dangereux.
    '''
    )

    st.header('Objectif du Projet')
    st.write(
    '''
    L’objectif principal du projet **CellVisionAI** est la création d’algorithmes d’apprentissage machine et d’apprentissage profond 
    dédiés à la reconnaissance et la classification de cellules du sang. Cet outil pourrait être utilisé pour 
    faciliter le diagnostic de la leucémie en détectant des leucocytes anormaux.
    '''
    )

    st.write(
    '''
    **Projet réalisé par Wilfried Condemine, Michael Deroche, Claudia Mattei et Charles Sallard**.
    (Promotion sept23_DS Datascientest)
    '''
    )

elif st.session_state['page'] == 'Projet':
    st.title("Projet")
    st.header('Le Projet')

    tab1, tab2 = st.tabs(["Objectif du Projet", "Fonctionnalités"])

    with tab1:
        st.write(
            '''
            Voici l'objectif du projet.
            Le projet **CellVisionAI** vise à créer un outil d'aide au diagnostic de la leucémie. Cet outil sera basé sur des algorithmes d'apprentissage machine et d'apprentissage profond capables de reconnaître et de classifier les cellules du sang.
            '''
        )
        
    with tab2:
        st.write(
            '''
            Voici les fonctionnalités du projet.
            Le projet **CellVisionAI** aura les fonctionnalités suivantes :
            - Reconnaissance des cellules du sang
            - Classification des cellules du sang
            - Diagnostic de la leucémie
            '''
        )

elif st.session_state['page'] == 'Démonstration':
    st.title("Démonstration")
    st.header('Objectif de la démonstration')

    tab3, tab4 = st.tabs(["Machine Learning", "Deep Learning"])

    with tab3:
        st.write(
        '''
        La démonstration du projet **CellVisionAI** consiste en une interface utilisateur permettant à l'utilisateur de charger une image de frottis sanguin. L'outil est ensuite capable de reconnaître et de classifier les cellules du sang présentes dans l'image.
        '''
    )
    
    with tab4:
        st.write(
        '''
        La démonstration du projet **CellVisionAI** consiste en une interface utilisateur permettant à l'utilisateur de charger une image de frottis sanguin. L'outil est ensuite capable de reconnaître et de classifier les cellules du sang présentes dans l'image.
        '''
    )
    
elif st.session_state['page'] == 'Résultats':
    st.title("Résultats")
    st.header('Objectif des résultats')

    st.write(
        '''
        Les résultats du projet **CellVisionAI** sont encore en cours d'évaluation. Cependant, les premiers résultats sont prometteurs. L'outil est capable de reconnaître et de classifier avec précision les cellules du sang présentes dans les frottis sanguins.
        '''
    )

elif st.session_state['page'] == 'Documentation':
    st.title("Documentation")
    st.header('header')
    
    tab5, tab6 = st.tabs(["Datasets", "Littératures"])

    with tab5:
    st.write(
        '''
        La documentation du projet **CellVisionAI** est en cours de préparation.
        '''
    )
    
    with tab6:
    st.write(
        '''
        La documentation du projet **CellVisionAI** est en cours de préparation.
        '''
    )
