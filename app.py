import streamlit as st

# Initialisation de l'état de la session
if 'page' not in st.session_state:
    st.session_state['page'] = 'Accueil'

## %%% BARE LATERALE %%% ##

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

## %%% PAGE ACCUEIL %%% ##

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

## %%% PAGE PROJET %%% ##

elif st.session_state['page'] == 'Projet':
    st.title("Projet")
    st.header('Le Projet')

    tab1, tab2 = st.tabs(["Objectif du Projet", "Fonctionnalités"])

    with tab1:
        st.write(
            '''
            Sur le plan **technique**, le projet repose sur des avancées récentes dans le domaine de la vision par ordinateur et de l'apprentissage automatique. 
            Des algorithmes de deep learning seront utilisés pour extraire des informations pertinentes à partir d'images de frottis sanguins. 
            Les données d'entraînement seront essentielles pour former le modèle et permettre une classification des cellules sanguines.
            \n
            Du point de vue **économique**, le développement d'un tel outil réduirait possiblement les coûts de main-d'œuvre associés à l'analyse manuelle des échantillons de sang. 
            Il pourrait également contribuer à des diagnostics plus rapides, améliorer les chances de traitement précoce des patients atteints de maladies du sang et réduire 
            les coûts de soins de santé à long terme.
            \n
            Sur le plan **scientifique**, ce projet permettrait d'explorer des approches pour l'analyse des cellules sanguines et d'approfondir la compréhension des mécanismes sous-jacents aux maladies du sang. En développant des modèles de classification précis, il peut ouvrir la voie à des recherches plus avancées sur la leucémie et autres pathologies.
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

## %%% PAGE DEMONSTRATION %%% ##

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

## %%% PAGE RESULTATS %%% ##

elif st.session_state['page'] == 'Résultats':
    st.title("Résultats")
    st.header('Objectif des résultats')

    st.write(
        '''
        Les résultats du projet **CellVisionAI** sont encore en cours d'évaluation. Cependant, les premiers résultats sont prometteurs. L'outil est capable de reconnaître et de classifier avec précision les cellules du sang présentes dans les frottis sanguins.
        '''
    )

## %%% PAGE DOCUMENTATION %%% ##

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
