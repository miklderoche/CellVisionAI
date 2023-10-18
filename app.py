import streamlit as st

col1, col2, col3 = st.beta_columns([1,6,1])

with col1:
st.write("dqfqefqdf")

with col2:
st.image('images/logo_VisionCellAI.png', width=250)

with col3:
st.write("qsdqsdqsd")

# Titre principal
st.title('Cell Vision AI')

# Introduction
st.header('Introduction')
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

# Tu peux ajouter d'autres sections si nécessaire, par exemple:
# st.header('Méthodologie')
# st.write('...')
