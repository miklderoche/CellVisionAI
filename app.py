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

# %% (_.~" MENU LATERAL "~._) 

# Menu latéral
# Initialisation de l'état de la session
if 'page' not in st.session_state:
    st.session_state['page'] = 'Projet'

# Menu latéral avec des boutons
st.sidebar.markdown("## Menu")

menu_items = {
    "Projet": "🏠",
    "Démonstration": "🎥",
    "Résultats": "📊",
    "Documentation": "📄"
}

for item, icon in menu_items.items():
    button_code = f'<a style="text-decoration:none;color:white;" href="javascript:void(0);" onclick="document.getElementById(\'{item}\').click();">{icon} {item}</a>'
    st.sidebar.markdown(button_code, unsafe_allow_html=True)
    if st.sidebar.button(item, key=item, on_click=lambda x=item: st.session_state.update({"page": x}), help=f"Cliquez pour aller à {item}"):
        pass

# CSS pour l'effet de survol
hover_css = """
<style>
a:hover {{
    color: red;
}}
</style>
"""
st.sidebar.markdown(hover_css, unsafe_allow_html=True)

# Affichage de la page en fonction de l'état de la session
if st.session_state['page'] == 'Projet':
    page_projet()
elif st.session_state['page'] == 'Démonstration':
    page_demo()

