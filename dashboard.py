import streamlit as st
import pandas as pd
import time
import secrets
import random

# ===================================================================
# PARTIE 1 : DÉFINITION DE TOUTES LES FONCTIONS DE SIMULATION
# ===================================================================

def simuler_maintenance_predictive_v2(scenario='Normal'):
    st.subheader("⚙️ Simulation : Maintenance Prédictive")
    if scenario == 'Alerte':
        data = {
            'timestamp': pd.to_datetime(['18:20:01', '18:20:02', '18:20:03', '18:20:04', '18:20:05'], format='%H:%M:%S').time,
            'vibration_level': [0.21, 0.23, 0.22, 0.85, 0.87],
            'temperature_celsius': [45, 46, 45, 68, 70],
            'power_consumption_kw': [150.5, 151.0, 150.2, 185.7, 188.1]
        }
    else: # Scénario 'Normal'
        data = {
            'timestamp': pd.to_datetime(['18:20:01', '18:20:02', '18:20:03', '18:20:04', '18:20:05'], format='%H:%M:%S').time,
            'vibration_level': [0.21, 0.23, 0.22, 0.24, 0.21],
            'temperature_celsius': [45, 46, 45, 47, 46],
            'power_consumption_kw': [150.5, 151.0, 150.2, 152.0, 151.5]
        }
    df = pd.DataFrame(data).set_index('timestamp')
    
    st.subheader("📈 Données des Capteurs en Temps Réel")
    st.line_chart(df)

    with st.spinner("ANALYSE (IA Rekarbon): Corrélation des données en cours..."):
        time.sleep(1.5)

    latest_data = df.iloc[-1]
    if latest_data['vibration_level'] > 0.8:
        st.error("⚠️ ALERTE SYSTÈME : Risque de défaillance critique détecté !", icon="🚨")
        col1, col2, col3 = st.columns(3)
        col1.metric("Niveau de Vibration", f"{latest_data['vibration_level']} g", "Élevé")
        col2.metric("Température", f"{latest_data['temperature_celsius']} °C", "Critique")
        col3.metric("Consommation", f"{latest_data['power_consumption_kw']} kW", "+25%")
        st.warning("**Synthèse de l'IA :** Corrélation anormale détectée, probabilité de défaillance imminente de 98%.")
        st.success("✅ ACTIONS INITIÉES : Ticket de maintenance créé, pièce commandée, ligne de production mise en sécurité.")
    else:
        st.success("✅ STATUT : Tous les systèmes du broyeur sont opérationnels.", icon="👍")

def simuler_optimisation_logistique_v2():
    st.subheader("🚚 Simulation : Optimisation Logistique")
    with st.spinner("ANALYSE (IA Rekarbon): Analyse des inventaires, des carnets de commandes et de la capacité de production..."):
        time.sleep(2.5)
    data_inventaire = {
        'Produit': ['Bio-huile', 'Biochar Granulé', 'Engrais Liquide'],
        'Stock Actuel (tonnes)': [15, 80, 45],
        'Stock de Sécurité': [30, 50, 50],
        'Commandes à Honorer (tonnes)': [40, 65, 20]
    }
    df_inventaire = pd.DataFrame(data_inventaire)
    produit_critique = df_inventaire.loc[0]
    deficit = produit_critique['Commandes à Honorer (tonnes)'] - produit_critique['Stock Actuel (tonnes)']
    st.subheader("📦 État des Stocks Actuels")
    st.dataframe(df_inventaire)
    st.subheader(f"📊 Analyse du Produit Critique : {produit_critique['Produit']}")
    col1, col2, col3 = st.columns(3)
    col1.metric("Stock Actuel", f"{produit_critique['Stock Actuel (tonnes)']} t")
    col2.metric("Commandes à Honorer", f"{produit_critique['Commandes à Honorer (tonnes)']} t")
    col3.metric("Déficit", f"{deficit} t", delta_color="inverse")
    st.error("⚠️ ALERTE LOGISTIQUE : Rupture de stock imminente sur la ligne 'Bio-huile'.", icon="📦")
    st.warning(f"**Synthèse de l'IA :** Le stock de bio-huile ({produit_critique['Stock Actuel (tonnes)']} t) est inférieur de {deficit} tonnes à la demande client ({produit_critique['Commandes à Honorer (tonnes)']} t).")
    with st.spinner("DÉCISION (IA Rekarbon): Formulation d'un plan d'action correctif..."):
        time.sleep(2)
    st.success("✅ PLAN D'ACTION PROPOSÉ:")
    st.info("""
    1.  **Production :** Augmenter la cadence de production de bio-huile de 15% pour les 7 prochains jours.
    2.  **Commercial :** Contacter le client 'Client-ABC' pour proposer une livraison partielle de sa commande.
    3.  **Achats :** Lancer une commande d'urgence pour 10 tonnes de matière première brute.
    """)

def simuler_reforestation_et_carbone_v2():
    st.subheader("🌳 Simulation : Reforestation & Crédits Carbone")
    with st.spinner("ANALYSE (IA Rekarbon): Traitement des dernières images satellites..."):
        time.sleep(2.5)
    total_hectares_reboises = 120
    hectares_valides_maturite = 87
    taux_maturite = int((hectares_valides_maturite / total_hectares_reboises) * 100)
    carbone_par_hectare = 15.5
    total_carbone_sequestre = hectares_valides_maturite * carbone_par_hectare
    prix_credit_carbone = 35
    st.info(f"**Analyse de la parcelle 'REK-AF-01' ({total_hectares_reboises} ha)**")
    st.write(f"**Taux de maturité des arbres :** {taux_maturite}%")
    st.progress(taux_maturite)
    st.subheader("📊 Bilan de Séquestration Carbone")
    col1, col2, col3 = st.columns(3)
    col1.metric("Hectares Matures", f"{hectares_valides_maturite} ha", "Certifiés")
    col2.metric("CO2 Séquestré", f"{total_carbone_sequestre:,.0f} tonnes", "Annuel")
    col3.metric("Valorisation Potentielle", f"€ {total_carbone_sequestre * prix_credit_carbone:,.0f}", f"à {prix_credit_carbone}€/t")
    st.warning("**Synthèse de l'IA :** L'analyse de la canopée et de la densité de biomasse confirme que 87 hectares ont atteint le seuil de maturité requis pour la certification.")
    with st.spinner("DÉCISION (IA Rekarbon): Préparation du dossier de certification..."):
        time.sleep(2)
    st.success("✅ DOSSIER PRÊT: Le rapport de certification a été généré et est prêt à être soumis.")

def simuler_livraison_temps_pluie():
    st.subheader("⛈️ Simulation : Livraison en Temps de Pluie")
    with st.spinner("ANALYSE (IA Rekarbon): Analyse des données météo en temps réel et de l'état des routes..."):
        time.sleep(2)
    st.info("MÉTÉO: Pluies fortes détectées sur l'itinéraire de livraison principal.")
    with st.spinner("DÉCISION (IA Rekarbon): Calcul d'un itinéraire alternatif..."):
        time.sleep(2)
    st.success("✅ NOUVEL ITINÉRAIRE DÉFINI: Le camion a été redirigé via la route secondaire. Retard estimé: 25 minutes.")

def simuler_vente_biochar_et_token():
    st.subheader("🔥 Simulation : Vente de Biochar & Tokenisation")
    quantite_vendue = 25
    prix_tonne = 600
    valeur_transaction = quantite_vendue * prix_tonne
    tokens_generes = int(valeur_transaction / 10)
    st.info(f"TRANSACTION: Vente de {quantite_vendue} tonnes de biochar à un client industriel.")
    with st.spinner("DÉCISION (IA Rekarbon): Génération de tokens de récompense pour le client..."):
        time.sleep(2)
    st.success(f"TOKENISATION: {tokens_generes} tokens 'REKAR' ont été générés et assignés au client.")
    st.code(f"ID de Transaction Blockchain: {secrets.token_hex(16)}")

# ===================================================================
# PARTIE 2 : LE DICTIONNAIRE "RACCOURCIS"
# ===================================================================
simulations = {
    "Maintenance Prédictive": simuler_maintenance_predictive_v2,
    "Optimisation Logistique": simuler_optimisation_logistique_v2,
    "Reforestation & Carbone": simuler_reforestation_et_carbone_v2,
    "Livraison (Météo)": simuler_livraison_temps_pluie,
    "Vente & Tokenisation": simuler_vente_biochar_et_token
}

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