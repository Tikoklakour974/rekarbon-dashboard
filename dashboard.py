import streamlit as st
import pandas as pd
import time
import secrets
import random
from datetime import datetime
from fpdf import FPDF
from io import BytesIO

# ===================================================================
# FONCTION UTILITAIRE POUR LA GÉNÉRATION DE PDF
# ===================================================================
def generate_pdf(simulation_title, report_data):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, 'Rekarbon - Rapport de Simulation Confidentiel', 0, 1, 'C')
    pdf.set_font("Arial", '', 8)
    pdf.cell(0, 10, f"Généré le : {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}", 0, 1, 'C')
    pdf.ln(10)
    
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, simulation_title, 0, 1, 'L')
    pdf.set_font("Arial", '', 11)
    
    for key, value in report_data.items():
        pdf.set_font("Arial", 'B', 10)
        pdf.multi_cell(0, 8, f"- {key}:")
        pdf.set_font("Arial", '', 10)
        # Gère les listes pour un affichage propre
        if isinstance(value, list):
            for item in value:
                pdf.multi_cell(0, 6, f"  • {item}")
        else:
            pdf.multi_cell(0, 8, f"  {str(value)}")
            
    # Sauvegarde du PDF en mémoire pour le téléchargement
    pdf_output = pdf.output(dest='S').encode('latin-1')
    return BytesIO(pdf_output)

# ===================================================================
# DÉFINITION DES 10 FONCTIONS DE SIMULATION "JURY"
# ===================================================================

def simuler_maintenance_predictive_v2(scenario='Normal'):
    st.subheader("⚙️ Simulation : Maintenance Prédictive")
    report_content = {}
    if scenario == 'Alerte':
        data = {'timestamp': pd.to_datetime(['18:20:01', '18:20:02', '18:20:03', '18:20:04', '18:20:05'], format='%H:%M:%S').time, 'vibration_level': [0.21, 0.23, 0.22, 0.85, 0.87], 'temperature_celsius': [45, 46, 45, 68, 70], 'power_consumption_kw': [150.5, 151.0, 150.2, 185.7, 188.1]}
        df = pd.DataFrame(data).set_index('timestamp')
        st.subheader("📈 Données des Capteurs en Temps Réel")
        st.line_chart(df)
        with st.spinner("ANALYSE (IA Rekarbon)..."): time.sleep(1.5)
        latest_data = df.iloc[-1]
        st.error("⚠️ ALERTE SYSTÈME : Risque de défaillance critique détecté !", icon="🚨")
        col1, col2, col3 = st.columns(3)
        col1.metric("Vibration", f"{latest_data['vibration_level']} g", "Élevé")
        col2.metric("Température", f"{latest_data['temperature_celsius']} °C", "Critique")
        col3.metric("Consommation", f"{latest_data['power_consumption_kw']} kW", "+25%")
        st.warning("**Synthèse IA :** Corrélation anormale détectée, probabilité de défaillance imminente de 98%.")
        st.success("✅ ACTIONS INITIÉES : Ticket créé, pièce commandée, ligne de production mise en sécurité.")
        report_content = {"Statut": "ALERTE", "Diagnostic": "Probabilité de défaillance de 98% (roulement SKF-6203)", "Actions": ["Arrêt de la ligne 'Broyage'", "Commande automatique de la pièce", "Assignation d'un ticket de maintenance prioritaire"]}
    else: 
        data = {'timestamp': pd.to_datetime(['18:20:01', '18:20:02', '18:20:03', '18:20:04', '18:20:05'], format='%H:%M:%S').time, 'vibration_level': [0.21, 0.23, 0.22, 0.24, 0.21], 'temperature_celsius': [45, 46, 45, 47, 46], 'power_consumption_kw': [150.5, 151.0, 150.2, 152.0, 151.5]}
        df = pd.DataFrame(data).set_index('timestamp')
        st.subheader("📈 Données des Capteurs en Temps Réel")
        st.line_chart(df)
        with st.spinner("ANALYSE (IA Rekarbon)..."): time.sleep(1.5)
        st.success("✅ STATUT : Tous les systèmes du broyeur sont opérationnels.", icon="👍")
        report_content = {"Statut": "NORMAL", "Diagnostic": "Aucune anomalie détectée", "Actions": "Aucune action requise"}
    
    if st.button("📄 Générer le Rapport d'Intervention", key="pdf_maintenance"):
        pdf_file = generate_pdf("Rapport de Maintenance Prédictive", report_content)
        st.download_button("📥 Télécharger le PDF", data=pdf_file, file_name="rapport_maintenance.pdf", mime="application/octet-stream")

def simuler_optimisation_logistique_v2():
    st.subheader("🚚 Simulation : Optimisation Logistique")
    with st.spinner("ANALYSE (IA Rekarbon): Analyse des inventaires, commandes et capacité de production..."):
        time.sleep(2.5)
    data_inventaire = {'Produit': ['Bio-huile', 'Biochar Granulé', 'Engrais Liquide'], 'Stock Actuel (tonnes)': [15, 80, 45], 'Commandes à Honorer (tonnes)': [40, 65, 20]}
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
    with st.spinner("DÉCISION (IA Rekarbon): Formulation d'un plan d'action correctif..."):
        time.sleep(2)
    st.success("✅ PLAN D'ACTION PROPOSÉ:")
    action_plan = ["**Production :** Augmenter la cadence de 15%.", "**Commercial :** Contacter 'Client-ABC' pour livraison partielle.", "**Achats :** Commande d'urgence de matière première."]
    st.info("\n".join(f"{i+1}. {item}" for i, item in enumerate(action_plan)))
    report_content = {"Statut": "ALERTE STOCK", "Produit Critique": "Bio-huile", "Déficit": f"{deficit} tonnes", "Plan d'action": action_plan}
    if st.button("📄 Générer le Rapport Logistique", key="pdf_logistique"):
        pdf_file = generate_pdf("Rapport d'Optimisation Logistique", report_content)
        st.download_button("📥 Télécharger le PDF", data=pdf_file, file_name="rapport_logistique.pdf", mime="application/octet-stream")

def simuler_livraison_temps_pluie_v2():
    st.subheader("⛈️ Simulation : Itinéraire de Livraison Météo-dépendant")
    with st.spinner("ANALYSE (IA Rekarbon): Analyse météo et état des routes..."):
        time.sleep(2)
    st.info("MÉTÉO: Pluies fortes détectées sur l'itinéraire principal (Route du Littoral).")
    st.subheader("⚖️ Matrice de Décision de l'IA")
    decision_data = {'Option': ['Plan A: Maintenir', 'Plan B: Détourner'], 'Risque de retard': ['Élevé (85%)', 'Faible (10%)'], 'Coût Carburant': ['135 €', '165 €'], 'Satisfaction Client': ['-40 pts', '+5 pts']}
    st.table(pd.DataFrame(decision_data))
    with st.spinner("DÉCISION (IA Rekarbon): Sélection du plan B..."):
        time.sleep(2)
    st.success("✅ NOUVEL ITINÉRAIRE DÉFINI: Camion redirigé via la Plaine des Palmistes.")
    report_content = {"Alerte": "Pluies fortes", "Itinéraire initial": "Route du Littoral (Risque 85%)", "Décision IA": "Redirection via Plaine des Palmistes (Risque 10%)", "Impact": "Retard estimé de 25min, satisfaction client préservée."}
    if st.button("📄 Générer le Rapport de Trajet", key="pdf_livraison"):
        pdf_file = generate_pdf("Rapport de Livraison", report_content)
        st.download_button("📥 Télécharger le PDF", data=pdf_file, file_name="rapport_livraison.pdf", mime="application/octet-stream")

def simuler_vente_et_tokenisation_v2():
    st.subheader("🔥 Simulation : Vente de Biochar & Tokenisation")
    quantite_vendue = 25; prix_tonne = 600
    valeur_transaction = quantite_vendue * prix_tonne
    tokens_generes = int(valeur_transaction / 10)
    st.info(f"TRANSACTION: Vente de **{quantite_vendue} tonnes** de biochar à 'Client Industriel SAS'.")
    col1, col2 = st.columns(2)
    col1.metric("Montant de la Vente", f"€ {valeur_transaction:,.0f}")
    col2.metric("Tokens REKAR Générés", f"{tokens_generes} REKAR", "Récompense")
    with st.spinner("DÉCISION (IA Rekarbon): Enregistrement sur la blockchain..."):
        time.sleep(2)
    id_tx = f"0x{secrets.token_hex(30)}"
    st.success(f"TOKENISATION RÉUSSIE: {tokens_generes} tokens 'REKAR' assignés au client.")
    st.code(f"ID de Transaction Blockchain: {id_tx}")
    st.metric("Prévision de valeur du token REKAR à 6 mois", "13.80 €", "+15%")
    report_content = {"Client": "Client Industriel SAS", "Produit": "Biochar", "Quantité": f"{quantite_vendue} tonnes", "Montant": f"{valeur_transaction:,.0f} €", "Tokens REKAR générés": tokens_generes, "ID Transaction": id_tx}
    if st.button("📄 Générer la Facture", key="pdf_vente"):
        pdf_file = generate_pdf("Facture de Vente Biochar", report_content)
        st.download_button("📥 Télécharger le PDF", data=pdf_file, file_name="facture_biochar.pdf", mime="application/octet-stream")

def simuler_reforestation_et_carbone_v2():
    st.subheader("🌳 Simulation : Reforestation & Crédits Carbone")
    with st.spinner("ANALYSE (IA Rekarbon): Traitement des images satellites..."):
        time.sleep(2.5)
    total_hectares_reboises = 120; hectares_valides_maturite = 87
    taux_maturite = int((hectares_valides_maturite / total_hectares_reboises) * 100)
    total_carbone_sequestre = hectares_valides_maturite * 15.5
    prix_credit_carbone = 35
    valorisation = total_carbone_sequestre * prix_credit_carbone
    st.info(f"**Analyse de la parcelle 'REK-AF-01' ({total_hectares_reboises} ha)**")
    st.write(f"**Taux de maturité des arbres :**"); st.progress(taux_maturite)
    st.subheader("📊 Bilan de Séquestration Carbone")
    col1, col2, col3 = st.columns(3)
    col1.metric("Hectares Matures", f"{hectares_valides_maturite} ha", "Certifiés")
    col2.metric("CO2 Séquestré", f"{total_carbone_sequestre:,.0f} tonnes", "Annuel")
    col3.metric("Valorisation", f"€ {valorisation:,.0f}", f"à {prix_credit_carbone}€/t")
    with st.spinner("DÉCISION (IA Rekarbon): Préparation du dossier de certification..."):
        time.sleep(2)
    st.success("✅ DOSSIER PRÊT: Le rapport de certification est généré.")
    report_content = {"Parcelle": "REK-AF-01", "Hectares matures": f"{hectares_valides_maturite} ha", "CO2 séquestré (annuel)": f"{total_carbone_sequestre:,.0f} t", "Valorisation potentielle": f"{valorisation:,.0f} €"}
    if st.button("📄 Générer le Certificat", key="pdf_reforestation"):
        pdf_file = generate_pdf("Certificat de Crédits Carbone", report_content)
        st.download_button("📥 Télécharger le PDF", data=pdf_file, file_name="certificat_carbone.pdf", mime="application/octet-stream")

def simuler_cession_token():
    st.subheader("🔁 Simulation : Cession de Tokens B2B")
    valeur_token = 12; tokens_cedes = 500; montant_total = valeur_token * tokens_cedes
    st.info("Contexte : **Client A** cède des tokens REKAR à **Client B**.")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Cédant : Client A"); st.metric("Tokens Cédés", f"- {tokens_cedes} REKAR")
    with col2:
        st.subheader("Acquéreur : Client B"); st.metric("Tokens Reçus", f"+ {tokens_cedes} REKAR")
    st.metric("Montant Total", f"€ {montant_total:,.0f}");
    st.success("CESSION VALIDÉE ET ENREGISTRÉE."); st.code(f"ID de Transaction: 0x{secrets.token_hex(30)}")
    report_content = {"Cédant": "Client A", "Acquéreur": "Client B", "Quantité": f"{tokens_cedes} REKAR", "Valeur": f"{montant_total:,.0f} €"}
    if st.button("📄 Générer l'Ordre de Transfert", key="pdf_cession"):
        pdf_file = generate_pdf("Ordre de Transfert de Tokens", report_content)
        st.download_button("📥 Télécharger le PDF", data=pdf_file, file_name="ordre_transfert_rekar.pdf", mime="application/octet-stream")

def simuler_rapport_fmi():
    st.subheader("🌍 Rapport : Demande de Financement FMI (Maurice)")
    st.info("Objectif : Obtenir 8,5M € pour le déploiement national.")
    with st.expander(" 🌱 Secteur Agricole & Énergie"):
        st.markdown("- Valorisation des déchets.\n- Vente de biochar subventionné.")
    with st.expander("💻 Secteur Numérique & Emploi"):
        st.markdown("- Création d’un réseau IA-native.\n- Objectif : +1000 emplois verts.")
    st.subheader("📈 Objectifs Clés 2030")
    col1, col2, col3 = st.columns(3)
    col1.metric("Réduction Émissions", "-25%"); col2.metric("Emplois Créés", "+1000"); col3.metric("Autosuffisance Énergétique", "+15%")
    st.success("✅ DEMANDE VALIDÉE PAR L'IA: Projet conforme aux critères de financement vert.")
    report_content = {"Porteur de projet": "Rekarbon (Maurice)", "Financement demandé": "8,5M € (FMI - Green Fund)", "Objectifs 2030": ["-25% émissions CO2", "+1000 emplois verts", "+15% autosuffisance énergétique"]}
    if st.button("📄 Générer la Synthèse pour le FMI", key="pdf_fmi"):
        pdf_file = generate_pdf("Synthèse Exécutive - Projet Rekarbon Maurice", report_content)
        st.download_button("📥 Télécharger le PDF", data=pdf_file, file_name="synthese_fmi_rekarbon.pdf", mime="application/octet-stream")

def simuler_rapport_commune():
    st.subheader("🇷🇪 Rapport : Financement Européen (Saint-Paul)")
    st.info("Objectif : Obtenir 460 000 € du programme FEDER.")
    st.subheader("Actions Réalisées")
    st.markdown("- ✅ Étude des gisements de déchets bois.\n- ✅ Comité local Rekarbon créé.\n- ✅ Site test à Savannah.")
    st.subheader("Résultats Attendus sur 2 Ans")
    col1, col2, col3 = st.columns(3)
    col1.metric("CO₂ Réduit", "300 t/an"); col2.metric("Emplois Créés", "10"); col3.metric("Tokens Générés", "12 000 REKAR")
    st.success("✅ PROJET ÉLIGIBLE: L'IA confirme la forte valeur ajoutée locale.")
    report_content = {"Commune": "Saint-Paul, La Réunion", "Financement demandé": "460 000 € (FEDER)", "Résultats attendus (2 ans)": ["300 t/an CO2 réduit", "10 emplois directs", "12 000 REKAR pour la communauté"]}
    if st.button("📄 Générer la Fiche Projet", key="pdf_commune"):
        pdf_file = generate_pdf("Fiche Projet FEDER - Rekarbon Saint-Paul", report_content)
        st.download_button("📥 Télécharger le PDF", data=pdf_file, file_name="fiche_projet_stpaul.pdf", mime="application/octet-stream")

def simuler_vente_bio_huile():
    st.subheader("🧴 Simulation : Vente Produit Fini (Bio-Huile)")
    st.info("Vente avec traçabilité carbone via token.")
    col1, col2 = st.columns([3, 1]); 
    with col1:
        st.write("**Produit :** Bio-huile 'Source des Hauts' 5L"); st.write("**Client :** 'Cosmétiques des Cimes'")
    with col2:
        st.metric("Prix", "42 €")
    st.success("✅ TOKEN DE TRAÇABILITÉ ASSOCIÉ : 1,2 REKAR")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/QR_code_for_mobile_English_Wikipedia.svg/1200px-QR_code_for_mobile_English_Wikipedia.svg.png", width=100)
    report_content = {"Produit": "Bio-huile 'Source des Hauts' 5L", "Client": "Cosmétiques des Cimes", "Prix": "42 €", "Token de traçabilité": "1,2 REKAR"}
    if st.button("📄 Générer le Bon de Livraison", key="pdf_biohuile"):
        pdf_file = generate_pdf("Bon de Livraison - Bio-huile", report_content)
        st.download_button("📥 Télécharger le PDF", data=pdf_file, file_name="bl_biohuile.pdf", mime="application/octet-stream")

def simuler_reforestation_ciblee():
    st.subheader("🌲 Simulation : Reforestation Ciblée (Grand-Coude)")
    location_data = pd.DataFrame({'lat': [-21.2958], 'lon': [55.5694]})
    st.info("Objectif : Planter 1000 arbres endémiques.")
    st.map(location_data, zoom=11)
    col1, col2, col3 = st.columns(3)
    col1.metric("Surface", "4 ha"); col2.metric("Essences", "2"); col3.metric("CO₂ Séquestré (10a)", "75 tonnes")
    st.success("✅ PROJET ENREGISTRÉ : 75 tokens REKAR pré-alloués.")
    report_content = {"Localisation": "Grand-Coude, La Réunion", "Objectif": "1000 arbres endémiques", "Surface": "4 ha", "CO2 estimé (10 ans)": "75 tonnes"}
    if st.button("📄 Générer le Certificat de Plantation", key="pdf_reforestation_ciblee"):
        pdf_file = generate_pdf("Certificat de Plantation", report_content)
        st.download_button("📥 Télécharger le PDF", data=pdf_file, file_name="certificat_plantation.pdf", mime="application/octet-stream")

# ===================================================================
# DICTIONNAIRE FINAL AVEC LES 10 SIMULATIONS
# ===================================================================
simulations = {
    "Maintenance Prédictive": simuler_maintenance_predictive_v2,
    "Optimisation Logistique": simuler_optimisation_logistique_v2,
    "Livraison (Météo)": simuler_livraison_temps_pluie_v2,
    "Vente & Tokenisation": simuler_vente_et_tokenisation_v2,
    "Reforestation & Carbone": simuler_reforestation_et_carbone_v2,
    "Cession de Tokens (B2B)": simuler_cession_token,
    "Rapport FMI (Maurice)": simuler_rapport_fmi,
    "Rapport Local (St-Paul)": simuler_rapport_commune,
    "Vente Produit (Bio-Huile)": simuler_vente_bio_huile,
    "Reforestation (Grand-Coude)": simuler_reforestation_ciblee,
}

# ===================================================================
# INTERFACE UTILISATEUR
# ===================================================================
st.title("Tableau de Bord de Contrôle Global - Rekarbon")
st.sidebar.title("MENU SIMULATIONS")
choix = st.sidebar.selectbox("Choisissez une simulation à lancer :", list(simulations.keys()))

if choix == "Maintenance Prédictive":
    scenario_choisi = st.sidebar.radio("Choisissez un état pour le système :", ('Normal', 'Alerte'), key='maintenance_scenario')
    if st.button(f"▶️ Lancer la simulation : {choix} ({scenario_choisi})"):
        simuler_maintenance_predictive_v2(scenario=scenario_choisi)
else:
    if st.button(f"▶️ Lancer la simulation : {choix}"):
        fonction_a_lancer = simulations[choix]
        fonction_a_lancer()