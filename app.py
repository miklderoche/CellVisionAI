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
if st.sidebar.button('Analyse'):
    st.session_state['page'] = 'Analyse'
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

elif st.session_state['page'] == 'Analyse':
    st.title("Analyse")
    st.header('Analyse des jeux de données')

    tab1, tab2, tab3, tab4 = st.tabs(["PBC Dataset Normal DIB", "Leukemia Dataset", "Acute Promyelocytic Leukemia (APL)", "Recommandations"])

    with tab1:
        st.header("PBC Dataset Normal DIB")
    
        st.write(
            '''
            Le dataset contient des images de cellules sanguines normales d'individus sains, servant de base de référence 
            pour l'entraînement des modèles pour reconnaître différents types de cellules sanguines normales.
            
            **Description**

            - Type : Images JPEG
            - Volume : 268 Mo
            - Nombre d'Images : 17 092
            - Classes : 8
            
            Ce jeu de données contient des images de cellules normales individuelles, classées en huit catégories. Les images ont été acquises à l'Hôpital de Barcelone.
            
            **Analyse**
            
            - Diversité des formes et des tailles de cellules
            - Distribution équilibrée des images entre les classes
            - Nécessité de normaliser la luminosité et la taille des images
            '''
            )
        
    with tab2:
        st.header("Leukemia Dataset")
        
        st.write(
            '''
             Le dataset contient des images de cellules sanguines de patients sains et de patients atteints de Leucémie Lymphoblastique Aiguë (ALL), avec des informations sur les centroïdes. 
             Il est utile pour tester la segmentation, la classification, et les méthodes de prétraitement des images.
             
            **Description**
            
            - Type : Images JPEG et TIFF
            - Sous-ensembles : ALL_IDB1 (143 Mo, 108 images), ALL_IDB2 (49 Mo, 260 images)
            - Classes : Patients sains et patients atteints de Leucémie Lymphoblastique Aiguë (ALL)
            
            Ce jeu de données contient des images de cellules sanguines provenant de patients sains et atteints de leucémie.
            
            **Analyse**
            
            - Une limitation est l'absence de classification des cellules, rendant difficile la vérification de la performance des modèles.
            - Les coordonnées des centroïdes des cellules sont fournies pour les images ALL_IDB1
            - Diversité des données pour construire un modèle robuste
            - Nécessité de prétraitement spécifique pour les images TIFF
            '''
            )

    with tab3:
        st.header("Acute Promyelocytic Leukemia (APL)")
        
        st.write(
            '''
            Le dataset est composé d'images de cellules sanguines classées de patients atteints de différentes formes de leucémie. 
            Certaines cellules n'ont pas été classées, introduisant de l'incertitude dans la variable cible.
            
            **Description**
            
            - Type : Images JPEG
            - Volume : 515 Mo
            - Nombre d'Images : 25 721
            - Origine : Cellules de 106 patients de l’Hôpital Johns Hopkins, atteints de Leucémie Myéloïde Aiguë (AML) ou de Leucémie Aiguë Promyélocytaire (APL)
            
            Ce jeu de données contient des images de cellules de patients atteints de deux types de leucémie. Les cellules sont classées dans des dossiers par catégorie, et il existe également un dossier pour les cellules non classées.
            
            **Analyse**
            
            - Conditions d'Acquisition :
            \nLes conditions d'acquisition des images semblent similaires à celles du Dataset 1.
            
            - Classification des Cellules :
            Plus de 15 000 images sont classées selon le type de cellules, mais environ 10 000 images ne sont pas classées.
            
            - Artifacts :
            Certains types de cellules, tels que les "smudge cells", contiennent de nombreux outliers et pourraient ne pas être utiles pour l'analyse.
            
            - Variations de Taille :
            Des variations de taille plus importantes sont observées par rapport au Dataset 1, sans dépendance apparente avec les classes de cellules.
            
            - Informations des Patients :
            Un fichier master.csv contient les diagnostics et quelques informations sur les patients. Il y a une répartition équilibrée des données entre les sexes et les tranches d'âge, 
            avec une prédominance masculine conforme à la prévalence de la maladie.
            '''
            )
        
    with tab4:
        st.header("Recommandations pour le Traitement des Données")

        st.write(
            '''
            **Analyse Exploratoire des Données :**
            Effectuer une analyse approfondie pour comprendre les limites potentielles et les caractéristiques spécifiques de chaque jeu de données.
            
            **Nettoyage des Données :**
            Pour le Dataset 3, bien que la majorité des données soient propres, une analyse détaillée des images peut révéler des problèmes, 
            tels que la difficulté de reconnaissance des noyaux par les algorithmes, nécessitant l'élimination de certaines données.
            
            **Prétraitement :**
            Des fichiers de données au format CSV ont été créés pour simplifier l’analyse statistique des données, y compris le nombre de classes, 
            le nombre d’images par classe, et les formats et dimensions des images.
            
            **Gestion des Limitations :**
            Les différences en termes de qualité, de format, et de représentativité des catégories de cellules entre les jeux de données peuvent poser des défis.
            Une stratégie d'intégration et de normalisation doit être développée pour gérer ces différences.
            Le manque de classification des cellules dans le Dataset 2 et les incertitudes dans le Dataset 3 nécessitent des stratégies spécifiques pour gérer et, si possible, minimiser ces limitations.
            '''
            )
## %%% PAGE DEMONSTRATION %%% ##

elif st.session_state['page'] == 'Démonstration':
    st.title("Démonstration")
    st.header('Objectif de la démonstration')

    tab5, tab6 = st.tabs(["Machine Learning", "Deep Learning"])

    with tab5:
        st.write(
        '''
        La démonstration du projet **CellVisionAI** consiste en une interface utilisateur permettant à l'utilisateur de charger une image de frottis sanguin. L'outil est ensuite capable de reconnaître et de classifier les cellules du sang présentes dans l'image.
        '''
    )
    
    with tab6:
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
    
    tab7, tab8 = st.tabs(["Datasets", "Bibliographie"])

    with tab7:
        st.write(
            '''
            - [PBC Dataset Normal DIB - National Library of Medicine](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7182702/)
            - [Acute Promyelocytic Leukemia (APL) - Kaggle](https://www.kaggle.com/eugeneshenderov/acute-promyelocytic-leukemia-apl)
            - [Leukemia Dataset - Kaggle](https://www.kaggle.com/nikhilsharma00/leukemia-dataset)
        '''
        )
    
    with tab8:
        st.write(
        '''
        - [Recognition of peripheral blood cell images using convolutional neural networks](https://www.sciencedirect.com/science/article/abs/pii/S0169260719303578?via%3Dihub)
        - [A deep learning model (ALNet) for the diagnosis of acute leukaemia lineage using peripheral blood cell images](https://www.sciencedirect.com/science/article/abs/pii/S0169260721000742?via%3Dihub)
        '''
        )
