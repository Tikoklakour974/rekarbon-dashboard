import streamlit as st
import pandas as pd
import time
import secrets
import random

# ===================================================================
# PARTIE 1 : DÉFINITION DE TOUTES LES FONCTIONS DE SIMULATION "JURY"
# ===================================================================

# --- THÉMATIQUES ORIGINALES AMÉLIORÉES ---

def simuler_maintenance_predictive_v2(scenario='Normal'):
    st.subheader("⚙️ Simulation : Maintenance Prédictive")
    # ... (code de la fonction v2) ...
    st.success("Simulation terminée.")

def simuler_optimisation_logistique_v2():
    st.subheader("🚚 Simulation : Optimisation Logistique")
    # ... (code de la fonction v2) ...
    st.success("Simulation terminée.")

def simuler_reforestation_et_carbone_v2():
    st.subheader("🌳 Simulation : Reforestation & Crédits Carbone")
    # ... (code de la fonction v2) ...
    st.success("Simulation terminée.")

def simuler_livraison_temps_pluie_v2():
    st.subheader("⛈️ Simulation : Itinéraire de Livraison Météo-dépendant")
    with st.spinner("ANALYSE (IA Rekarbon): Analyse des données météo en temps réel et de l'état des routes..."):
        time.sleep(2)
    st.info("MÉTÉO: Pluies fortes détectées sur l'itinéraire de livraison principal (Route du Littoral).")
    st.subheader("⚖️ Matrice de Décision de l'IA")
    decision_data = {
        'Option': ['Plan A: Maintenir', 'Plan B: Détourner'],
        'Risque de retard important': ['Élevé (85%)', 'Faible (10%)'],
        'Coût Carburant Estimé': ['135 €', '165 € (+22%)'],
        'Satisfaction Client Estimée': ['-40 pts', '+5 pts']
    }
    st.table(pd.DataFrame(decision_data))
    with st.spinner("DÉCISION (IA Rekarbon): Sélection du plan B pour garantir la livraison..."):
        time.sleep(2)
    st.success("✅ NOUVEL ITINÉRAIRE DÉFINI: Le camion a été redirigé via la Plaine des Palmistes. Retard estimé: 25 minutes.")

def simuler_vente_et_tokenisation_v2():
    st.subheader("🔥 Simulation : Vente de Biochar & Tokenisation")
    quantite_vendue = 25
    prix_tonne = 600
    valeur_transaction = quantite_vendue * prix_tonne
    tokens_generes = int(valeur_transaction / 10)
    st.info(f"TRANSACTION: Vente de **{quantite_vendue} tonnes** de biochar à 'Client Industriel SAS'.")
    col1, col2 = st.columns(2)
    col1.metric("Montant de la Vente", f"€ {valeur_transaction:,.0f}")
    col2.metric("Tokens REKAR Générés", f"{tokens_generes} REKAR", "Récompense")
    with st.spinner("DÉCISION (IA Rekarbon): Enregistrement de la transaction et des tokens sur la blockchain..."):
        time.sleep(2)
    st.success(f"TOKENISATION RÉUSSIE: {tokens_generes} tokens 'REKAR' ont été générés et assignés au client.")
    st.code(f"ID de Transaction Blockchain: 0x{secrets.token_hex(30)}")
    st.subheader("🧠 Indicateur IA : Potentiel Marché du Token")
    st.metric("Prévision de valeur du token REKAR à 6 mois", "13.80 €", "+15%", help="Basé sur l'anticipation des marchés carbone volontaires.")

# --- NOUVELLES THÉMATIQUES ---

def simuler_cession_token():
    st.subheader("🔁 Simulation : Cession de Tokens B2B")
    valeur_token = 12
    tokens_cedes = 500
    montant_total = valeur_token * tokens_cedes
    st.info("Contexte : **Client A** cède une partie de ses tokens REKAR à **Client B** pour sa compensation carbone.")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Cédant : Client A")
        st.metric("Tokens Cédés", f"- {tokens_cedes} REKAR")
    with col2:
        st.subheader("Acquéreur : Client B")
        st.metric("Tokens Reçus", f"+ {tokens_cedes} REKAR")
    st.metric("Montant Total de la Transaction", f"€ {montant_total:,.0f}", f"Basé sur 1 token = {valeur_token}€")
    with st.spinner("TRANSACTION: Enregistrement de la cession sur la blockchain..."):
        time.sleep(2)
    st.success("CESSION VALIDÉE ET ENREGISTRÉE.")
    st.code(f"ID de Transaction Cession: 0x{secrets.token_hex(30)}")

def simuler_rapport_fmi():
    st.subheader("🌍 Rapport Synthétique : Demande de Financement FMI (Île Maurice)")
    st.info("Objectif : Obtenir un financement vert de 8,5M € pour le déploiement national de Rekarbon.")
    with st.expander(" 🌱 Secteur Agricole & Énergie"):
        [cite_start]st.markdown("- Valorisation des déchets agricoles (canne à sucre) via pyrolyse. [cite: 33]")
        [cite_start]st.markdown("- Vente de biochar à prix subventionné aux exploitants locaux pour améliorer les sols. [cite: 34]")
    with st.expander("💻 Secteur Numérique & Emploi"):
        [cite_start]st.markdown("- Création d’un réseau autonome IA-native sur panneaux solaires pour les zones rurales. [cite: 35]")
        [cite_start]st.markdown("- Objectif : +1000 emplois verts et formation aux nouvelles technologies. [cite: 36]")
    st.subheader("📈 Objectifs Clés pour 2030")
    col1, col2, col3 = st.columns(3)
    col1.metric("Réduction Émissions", "-25%", "vs 2020")
    col2.metric("Emplois Créés", "+1000", "verts")
    col3.metric("Autosuffisance Énergétique", "+15%", "Partielle")
    st.success("✅ DEMANDE DE FINANCEMENT VALIDÉE PAR L'IA: Le projet respecte tous les critères de financement vert du FMI.")

def simuler_rapport_commune():
    st.subheader("🇷🇪 Rapport de Commune : Financement Européen (Saint-Paul, La Réunion)")
    st.info("Objectif : Obtenir un soutien de 460 000 € du programme FEDER pour une implantation locale.")
    st.subheader("Actions Déjà Réalisées")
    [cite_start]st.markdown("- ✅ Étude des gisements de déchets bois flottés post-cycloniques. [cite: 40]")
    [cite_start]st.markdown("- ✅ Mise en place d’un comité local Rekarbon avec élus et agriculteurs. [cite: 40]")
    [cite_start]st.markdown("- ✅ Implantation d'un site test dans la zone agricole de Savannah. [cite: 40]")
    st.subheader("Résultats Attendus sur 2 Ans")
    col1, col2, col3 = st.columns(3)
    col1.metric("CO₂ Réduit", "300 tonnes/an", "localement")
    col2.metric("Emplois Créés", "10", "directs")
    col3.metric("Tokens Générés", "12 000 REKAR", "pour la communauté")
    st.success("✅ PROJET ÉLIGIBLE: L'IA confirme que le projet pilote a un fort impact local et correspond aux objectifs européens.")

def simuler_vente_bio_huile():
    st.subheader("🧴 Simulation : Vente de Bio-Huile en Boutique")
    st.info("Vente d'un produit fini Rekarbon avec traçabilité carbone.")
    st.markdown("---")
    col1, col2 = st.columns([3, 1])
    with col1:
        st.write("**Produit :** Bio-huile 'Source des Hauts' 5L")
        st.write("**Client :** Boutique 'Cosmétiques des Cimes' (Cilaos)")
        st.write("**Usage :** Base pour des produits cosmétiques naturels")
    with col2:
        st.metric("Prix de Vente", "42 €")
    with st.spinner("Génération du token de traçabilité carbone..."):
        time.sleep(2)
    st.success("✅ TOKEN DE VALEUR CARBONE ASSOCIÉ : 1,2 REKAR")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/QR_code_for_mobile_English_Wikipedia.svg/1200px-QR_code_for_mobile_English_Wikipedia.svg.png", width=100, caption="QR Code de Traçabilité (simulé)")

def simuler_reforestation_ciblee():
    st.subheader("🌲 Simulation : Reforestation Ciblée (Grand-Coude)")
    location_data = pd.DataFrame({'lat': [-21.1745], 'lon': [55.3410]})
    st.info("Objectif : Planter 1000 arbres endémiques et tokeniser la séquestration carbone.")
    st.map(location_data, zoom=10)
    col1, col2, col3 = st.columns(3)
    col1.metric("Surface", "4 ha")
    col2.metric("Essences Plantées", "2", "Tamarins, Bois de senteur")
    col3.metric("CO₂ Séquestré (10 ans)", "75 tonnes")
    with st.spinner("Génération des tokens de séquestration..."):
        time.sleep(2)
    st.success("✅ PROJET ENREGISTRÉ : 75 tokens REKAR ont été pré-alloués. Leur libération sera conditionnée à la croissance des arbres, suivie par l'IA.")


# ===================================================================
# PARTIE 2 : LE DICTIONNAIRE "RACCOURCIS"
# ===================================================================
simulations = {
    # Thématiques originales améliorées
    "Maintenance Prédictive": simuler_maintenance_predictive_v2,
    "Optimisation Logistique": simuler_optimisation_logistique_v2,
    "Livraison (Météo)": simuler_livraison_temps_pluie_v2,
    "Vente & Tokenisation": simuler_vente_et_tokenisation_v2,
    
    # Nouvelles thématiques du document
    "Cession de Tokens (B2B)": simuler_cession_token,
    "Rapport FMI (Maurice)": simuler_rapport_fmi,
    "Rapport Local (St-Paul)": simuler_rapport_commune,
    "Vente Produit (Bio-Huile)": simuler_vente_bio_huile,
    "Reforestation (Grand-Coude)": simuler_reforestation_ciblee,
    
    # La v2 de reforestation est maintenant intégrée dans la nouvelle simulation plus spécifique
    # On peut la retirer pour éviter les doublons
}
# Nettoyage des doublons potentiels (si l'ancienne fonction est encore là)
# del simulations["Reforestation & Carbone"] # décommentez si besoin


# ===================================================================
# PARTIE 3 : L'INTERFACE UTILISATEUR
# ===================================================================
st.title("Tableau de Bord de Contrôle Global - Rekarbon")

st.sidebar.title("MENU SIMULATIONS")
choix = st.sidebar.selectbox(
    "Choisissez une simulation à lancer :",
    list(simulations.keys())
)

if choix == "Maintenance Prédictive":
    scenario_choisi = st.sidebar.radio(
        "Choisissez un état pour le système :",
        ('Normal', 'Alerte'),
        key='maintenance_scenario'
    )
    if st.button(f"▶️ Lancer la simulation : {choix} ({scenario_choisi})"):
        simuler_maintenance_predictive_v2(scenario=scenario_choisi)
else:
    if st.button(f"▶️ Lancer la simulation : {choix}"):
        fonction_a_lancer = simulations[choix]
        fonction_a_lancer()