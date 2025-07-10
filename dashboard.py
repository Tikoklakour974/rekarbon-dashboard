import streamlit as st
import pandas as pd
import time
import secrets
import random
from datetime import datetime

# ===================================================================
# PARTIE 1 : DÉFINITION DE TOUTES LES FONCTIONS DE SIMULATION "JURY"
# ===================================================================

def simuler_maintenance_predictive_v2(scenario='Normal'):
    st.subheader("⚙️ Simulation : Maintenance Prédictive")
    # --- Données de Simulation ---
    if scenario == 'Alerte':
        data = {'timestamp': pd.to_datetime(['18:20:01', '18:20:02', '18:20:03', '18:20:04', '18:20:05'], format='%H:%M:%S').time, 'vibration_level': [0.21, 0.23, 0.22, 0.85, 0.87], 'temperature_celsius': [45, 46, 45, 68, 70], 'power_consumption_kw': [150.5, 151.0, 150.2, 185.7, 188.1]}
    else: # Scénario 'Normal'
        data = {'timestamp': pd.to_datetime(['18:20:01', '18:20:02', '18:20:03', '18:20:04', '18:20:05'], format='%H:%M:%S').time, 'vibration_level': [0.21, 0.23, 0.22, 0.24, 0.21], 'temperature_celsius': [45, 46, 45, 47, 46], 'power_consumption_kw': [150.5, 151.0, 150.2, 152.0, 151.5]}
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
        
        # --- SECTION : GÉNÉRATION DE DOCUMENT ---
        with st.expander("📄 Afficher le Rapport d'Intervention Confidentiel"):
            st.markdown("---")
            # En-tête
            col1, col2 = st.columns(2)
            with col1:
                st.write("**Rekarbon S.A.S**")
                st.write("1 Rue de l'Avenir, Savannah")
                st.write("97460 Saint-Paul, La Réunion")
                st.write("**SIRET :** 843 456 789 00015")
                st.write("**TVA Intra. :** FR 12 843456789")
            with col2:
                st.write(f"**Rapport N° :** MNT-{datetime.now().year}-{random.randint(100, 999)}")
                st.write(f"**Date d'émission :** {datetime.now().strftime('%d/%m/%Y %H:%M')}")
                st.write("**Niveau :** Confidentiel Interne")
            st.markdown("---")
            # Corps
            st.subheader("Objet : Rapport d'Intervention Prédictive - Broyeur à bois")
            st.markdown("Ce rapport est généré par l'IA d'orchestration **IA Rekarbon** suite à la détection d'une anomalie critique.")
            st.write("**Diagnostic IA :**")
            st.warning("**Cause Racine :** La corrélation d'une vibration élevée, d'une surchauffe et d'une surconsommation électrique indique une probabilité de 98% de défaillance imminente du roulement principal (pièce SKF-6203).")
            st.write("**Actions Correctives Automatisées :**")
            st.info("""1.  **Mise en Sécurité :** Ligne de production 'Broyage' mise en pause.
            2.  **Maintenance :** Ticket de maintenance prioritaire assigné à l'équipe technique.
            3.  **Logistique :** Commande de la pièce 'Roulement à billes SKF-6203' passée automatiquement.""")
            st.markdown("---")
            # Pied de page
            st.caption("Ce document est la propriété de Rekarbon S.A.S. Diffusion non autorisée interdite.")
    else:
        st.success("✅ STATUT : Tous les systèmes du broyeur sont opérationnels.", icon="👍")

def simuler_optimisation_logistique_v2():
    st.subheader("🚚 Simulation : Optimisation Logistique")
    with st.spinner("ANALYSE (IA Rekarbon): Analyse des inventaires, commandes et capacité de production..."):
        time.sleep(2.5)
    data_inventaire = {'Produit': ['Bio-huile', 'Biochar Granulé', 'Engrais Liquide'], 'Stock Actuel (tonnes)': [15, 80, 45], 'Stock de Sécurité': [30, 50, 50], 'Commandes à Honorer (tonnes)': [40, 65, 20]}
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
    st.info("""1.  **Production :** Augmenter la cadence de production de bio-huile de 15%.
    2.  **Commercial :** Contacter le client 'Client-ABC' pour proposer une livraison partielle.
    3.  **Achats :** Lancer une commande d'urgence de matière première.""")

def simuler_livraison_temps_pluie_v2():
    st.subheader("⛈️ Simulation : Itinéraire de Livraison Météo-dépendant")
    with st.spinner("ANALYSE (IA Rekarbon): Analyse des données météo en temps réel et de l'état des routes..."):
        time.sleep(2)
    st.info("MÉTÉO: Pluies fortes détectées sur l'itinéraire de livraison principal (Route du Littoral).")
    st.subheader("⚖️ Matrice de Décision de l'IA")
    decision_data = {'Option': ['Plan A: Maintenir', 'Plan B: Détourner'], 'Risque de retard important': ['Élevé (85%)', 'Faible (10%)'], 'Coût Carburant Estimé': ['135 €', '165 € (+22%)'], 'Satisfaction Client Estimée': ['-40 pts', '+5 pts']}
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
    st.warning("**Synthèse de l'IA :** L'analyse de la canopée confirme que 87 hectares ont atteint le seuil de maturité requis pour la certification.")
    with st.spinner("DÉCISION (IA Rekarbon): Préparation du dossier de certification..."):
        time.sleep(2)
    st.success("✅ DOSSIER PRÊT: Le rapport de certification est généré.")

def simuler_cession_token():
    st.subheader("🔁 Simulation : Cession de Tokens B2B")
    valeur_token = 12
    tokens_cedes = 500
    montant_total = valeur_token * tokens_cedes
    st.info("Contexte : **Client A** cède des tokens REKAR à **Client B** pour sa compensation carbone.")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Cédant : Client A")
        st.metric("Tokens Cédés", f"- {tokens_cedes} REKAR")
    with col2:
        st.subheader("Acquéreur : Client B")
        st.metric("Tokens Reçus", f"+ {tokens_cedes} REKAR")
    st.metric("Montant Total de la Transaction", f"€ {montant_total:,.0f}", f"Basé sur 1 token = {valeur_token}€")
    with st.spinner("TRANSACTION: Enregistrement sur la blockchain..."):
        time.sleep(2)
    st.success("CESSION VALIDÉE ET ENREGISTRÉE.")
    st.code(f"ID de Transaction: 0x{secrets.token_hex(30)}")

def simuler_rapport_fmi():
    st.subheader("🌍 Rapport Synthétique : Demande de Financement FMI (Île Maurice)")
    st.info("Objectif : Obtenir un financement vert de 8,5M € pour un déploiement national.")
    with st.expander(" 🌱 Secteur Agricole & Énergie"):
        st.markdown("- Valorisation des déchets agricoles (canne à sucre) via pyrolyse.")
        st.markdown("- Vente de biochar subventionné aux exploitants locaux.")
    with st.expander("💻 Secteur Numérique & Emploi"):
        st.markdown("- Création d’un réseau autonome IA-native sur panneaux solaires.")
        st.markdown("- Objectif : +1000 emplois verts et formation.")
    st.subheader("📈 Objectifs Clés pour 2030")
    col1, col2, col3 = st.columns(3)
    col1.metric("Réduction Émissions", "-25%", "vs 2020")
    col2.metric("Emplois Créés", "+1000", "verts")
    col3.metric("Autosuffisance Énergétique", "+15%", "Partielle")
    st.success("✅ DEMANDE DE FINANCEMENT VALIDÉE PAR L'IA: Le projet respecte les critères de financement vert du FMI.")

def simuler_rapport_commune():
    st.subheader("🇷🇪 Rapport de Commune : Financement Européen (Saint-Paul)")
    st.info("Objectif : Obtenir un soutien de 460 000 € du programme FEDER.")
    st.subheader("Actions Déjà Réalisées")
    st.markdown("- ✅ Étude des gisements de déchets bois flottés.")
    st.markdown("- ✅ Mise en place d’un comité local Rekarbon.")
    st.markdown("- ✅ Implantation d'un site test à Savannah.")
    st.subheader("Résultats Attendus sur 2 Ans")
    col1, col2, col3 = st.columns(3)
    col1.metric("CO₂ Réduit", "300 tonnes/an", "localement")
    col2.metric("Emplois Créés", "10", "directs")
    col3.metric("Tokens Générés", "12 000 REKAR", "pour la communauté")
    st.success("✅ PROJET ÉLIGIBLE: L'IA confirme que le projet pilote correspond aux objectifs européens.")

def simuler_vente_bio_huile():
    st.subheader("🧴 Simulation : Vente de Bio-Huile en Boutique")
    st.info("Vente d'un produit fini Rekarbon avec traçabilité carbone.")
    st.markdown("---")
    col1, col2 = st.columns([3, 1])
    with col1:
        st.write("**Produit :** Bio-huile 'Source des Hauts' 5L")
        st.write("**Client :** Boutique 'Cosmétiques des Cimes' (Cilaos)")
    with col2:
        st.metric("Prix de Vente", "42 €")
    with st.spinner("Génération du token de traçabilité carbone..."):
        time.sleep(2)
    st.success("✅ TOKEN DE VALEUR CARBONE ASSOCIÉ : 1,2 REKAR")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/QR_code_for_mobile_English_Wikipedia.svg/1200px-QR_code_for_mobile_English_Wikipedia.svg.png", width=100, caption="QR Code de Traçabilité (simulé)")

def simuler_reforestation_ciblee():
    st.subheader("🌲 Simulation : Reforestation Ciblée (Grand-Coude)")
    location_data = pd.DataFrame({'lat': [-21.2958], 'lon': [55.5694]})
    st.info("Objectif : Planter 1000 arbres endémiques et tokeniser la séquestration carbone.")
    st.map(location_data, zoom=11)
    col1, col2, col3 = st.columns(3)
    col1.metric("Surface", "4 ha")
    col2.metric("Essences Plantées", "2", "Tamarins, Bois de senteur")
    col3.metric("CO₂ Séquestré (10 ans)", "75 tonnes")
    with st.spinner("Génération des tokens de séquestration..."):
        time.sleep(2)
    st.success("✅ PROJET ENREGISTRÉ : 75 tokens REKAR ont été pré-alloués.")

# ===================================================================
# PARTIE 2 : LE DICTIONNAIRE "RACCOURCIS"
# ===================================================================
simulations = {
    "Maintenance Prédictive": simuler_maintenance_predictive_v2,
    "Optimisation Logistique": simuler_optimisation_logistique_v2,
    "Livraison (Météo)": simuler_livraison_temps_pluie_v2,
    "Vente & Tokenisation": simuler_vente_et_tokenisation_v2,
    "Cession de Tokens (B2B)": simuler_cession_token,
    "Rapport FMI (Maurice)": simuler_rapport_fmi,
    "Rapport Local (St-Paul)": simuler_rapport_commune,
    "Vente Produit (Bio-Huile)": simuler_vente_bio_huile,
    "Reforestation (Grand-Coude)": simuler_reforestation_ciblee,
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