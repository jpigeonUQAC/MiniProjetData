#CODE GÉNÉRÉ AUTOMATIQUEMENT PAR CHATGPT COMME MENTIONNÉ À FAIRE EN CLASSE.
#PIGJ10119809 Jérome Pigeon

import pandas as pd
import streamlit as st
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt


# Charger les données avec le nouveau cache
@st.cache_data
def load_data():
    data_raw = pd.read_csv("healthcare_dataset.csv")
    data = data_raw.copy()
    data["Name"] = data["Name"].str.title()
    data["Date of Admission"] = pd.to_datetime(data["Date of Admission"], format='%Y-%m-%d')
    data["Discharge Date"] = pd.to_datetime(data["Discharge Date"], format='%Y-%m-%d')
    data = data.drop_duplicates()
    # Vérifier et corriger les montants négatifs dans la colonne 'Billing Amount'
    data['Billing Amount'] = data['Billing Amount'].abs()
    data["Hospital"] = data["Hospital"].str.strip()
    data["Hospital"] = data["Hospital"].str.lower()
    data["Hospital"] = data["Hospital"].apply(lambda x: " ".join(sorted(x.split())))
    data["Hospital"] = data["Hospital"].str.title()

    return data


data = load_data()

# Titre de l'application
st.title("Analyse des Données Hospitalières")

# Ajouter une barre latérale pour les boutons
st.sidebar.title("Options")

# Boutons dans la sidebar
show_boxplot = st.sidebar.button("Répartition des âges par genre")
show_condition_gender = st.sidebar.button("Répartition des conditions médicales par genre")
show_insurance = st.sidebar.button("Répartition des patients par assurance")
show_abnormal = st.sidebar.button("Cas abnormaux par condition médicale")
show_cost = st.sidebar.button("Répartition des coûts des patients")
show_top_hospitals = st.sidebar.button("Top 10 des Hôpitaux")
show_assurance_montant = st.sidebar.button("Montant moyen par fournisseur d'assurance")
show_abnormal_age = st.sidebar.button("Répartition des cas abnormaux par âge")
show_summary = st.sidebar.button("Résumé des données")

# Comparaison hommes vs femmes par âge
if show_boxplot:
    fig, ax = plt.subplots(figsize=(10, 6))  # Créer une figure explicitement
    sns.boxplot(data=data, x='Gender', y='Age', hue='Gender', palette='Set2', legend=False, ax=ax)
    ax.set_title("Distribution des âges par genre")
    ax.set_xlabel("Genre")
    ax.set_ylabel("Âge")
    st.pyplot(fig)  # Passer la figure explicitement à st.pyplot()

    st.write(""" 
    Nous constatons que les résultats sont assez similaires. La médiane est à 52 ans environ et la majorité des données sont entre 35 et 70 ans (Q1 et Q3).
    Toutefois, les Q3 des femmes sont environ 1-2 ans plus élevés que ceux des hommes.
    """)

# Répartition des conditions médicales par genre
if show_condition_gender:
    fig_condition_gender_1 = px.bar(data.groupby(["Gender", "Medical Condition"]).size().reset_index(name="Count"),
                                    x="Medical Condition", y="Count", color="Gender", barmode="group",
                                    title="Répartition des conditions médicales par genre",
                                    labels={"Medical Condition": "Condition Médicale", "Count": "Nombre de Patients"})
    fig_condition_gender_1.update_yaxes(range=[4400, 4800])
    st.plotly_chart(fig_condition_gender_1)

    st.write(
        """ On constate, encore une fois, que les répartitions sont trop similaires encore une fois. Toutefois, on constate qu'il y a un peu plus de femmes avec de l'arthrite et d'hommes avec de l'asthme.""")

# Répartition des patients par assurance
if show_insurance:
    stat_assurance = data["Insurance Provider"].value_counts()
    fig_assurance = px.pie(names=stat_assurance.index, values=stat_assurance.values,
                           title="Répartition des compagnies d'assurance")
    fig_assurance.update_layout(title_x=0.5)
    st.plotly_chart(fig_assurance)

    st.write(""" 
    On constate que Cigna est l'assurance la plus populaire assez significativement.
    """)

# Cas abnormaux par condition médicale
if show_abnormal:
    abnormal_data = data[data["Test Results"] == "Abnormal"]
    fig_abnormal_condition = px.histogram(abnormal_data, x="Medical Condition", color="Medical Condition",
                                          title="Répartition des cas abnormaux par condition médicale",
                                          labels={"Medical Condition": "Condition Médicale",
                                                  "count": "Nombre de cas abnormaux"})
    fig_abnormal_condition.update_layout(title_x=0.5, xaxis_title="Condition médicale",
                                         yaxis_title="Nombre de cas abnormaux")
    st.plotly_chart(fig_abnormal_condition)

    st.write(""" 
    Les cas abnormaux semblent répartis assez uniformément selon les conditions médicales. Cependant, l'obésité, l'arthrite et le diabète
    semblent légèrement plus fréquents dans les cas abnormaux.
    """)

# Répartition des coûts des patients
if show_cost:
    fig, ax = plt.subplots(figsize=(10, 6))  # Créer une figure explicitement
    sns.boxplot(x=data["Billing Amount"], ax=ax)  # Passer explicitement l'ax à seaborn
    ax.set_title("Répartition des coûts des patients")
    ax.set_xlabel("Montant")
    st.pyplot(fig)  # Passer la figure explicitement à st.pyplot()

    st.write(""" 
    On constate que la majorité des valeurs se situent entre 12500 et 37500.
    """)

# Montant moyen par fournisseur d'assurance
if show_assurance_montant:
    montant_assurance_moyenne = data.groupby("Insurance Provider")["Billing Amount"].mean().reset_index()
    montant_assurance_somme = data.groupby("Insurance Provider")["Billing Amount"].sum().reset_index()
    # Graphique : Montant moyen par fournisseur
    fig_assurance_montant = px.bar(montant_assurance_moyenne, x="Insurance Provider", y="Billing Amount",
                                   title="Montant moyen selon le fournisseur d'assurance",
                                   labels={"Insurance Provider": "Assurance", "Billing Amount": "Montant en $"},
                                   color="Insurance Provider")
    fig_assurance_montant.update_yaxes(range=[25000, 26000])
    fig_assurance_montant.update_layout(title_x=0.5)
    st.plotly_chart(fig_assurance_montant)

# Répartition des cas abnormaux par âge
if show_abnormal_age:
    abnormal_data = data[data["Test Results"] == "Abnormal"]
    fig_abnormal_age = px.histogram(abnormal_data, x="Age", title="Répartition des cas abnormaux par âge",
                                    labels={"Age": "Âge", "count": "Nombre de cas abnormaux"})
    fig_abnormal_age.update_layout(title_x=0.5, xaxis_title="Âge", yaxis_title="Nombre de cas abnormaux")
    st.plotly_chart(fig_abnormal_age)

    age_abnormal_moyenne = abnormal_data["Age"].mean()

    # Afficher le résultat
    st.write(
        f"L'âge moyen des cas abnormaux est : {age_abnormal_moyenne:.2f} ans. Ceci est similaire à l'âge moyen des patients. Il n'y a pas de lien et la répartition est similaire")

# Résumé des données
if show_summary:
    st.write("### Résumé des données")
    st.write(f"- Nombre de patients : {len(data)}")
    st.write(f"- Age moyen des patients : {data['Age'].mean():.2f} ans")
    st.write(f"- Voici quelques données statistiques sur l'âge des patients : {data['Age'].describe()}")
    st.write(f"- Coût moyen par patient : {data['Billing Amount'].mean():.2f} $")
    st.write(f"- Voici quelques données statistiques sur les couts des patients : {data['Billing Amount'].describe()}")
    st.write(f"- Durée moyenne d'hospitalisation : {((data['Discharge Date'] - data['Date of Admission']).dt.days).mean():.2f} jours")

    st.write(f"- On constate que la moyenne est autour de 25 000 $.")
    
    st.write(f"- Coût moyen par patient : {data['Billing Amount'].mean():.2f} $")
    
if show_top_hospitals:
    # Statistiques sur les hôpitaux
    stat_hopital = data["Hospital"].value_counts()
    
    # Sélectionner les 10 hôpitaux les plus fréquents
    top_10_hopitaux = stat_hopital.head(10)

    # Créer le graphique en camembert
    fig_hopital = px.pie(names=top_10_hopitaux.index, values=top_10_hopitaux.values, title="Top 10 des hôpitaux")
    fig_hopital.update_layout(title_x=0.5)
    
    # Afficher le graphique dans Streamlit
    st.plotly_chart(fig_hopital)
