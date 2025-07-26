import streamlit as st
import pandas as pd
import pickle

# Load trained model
with open("models/model.pkl", "rb") as f:
    model = pickle.load(f)

# 👋 App Header
st.title("💳 Financial Inclusion Predictor")
st.markdown("This app predicts whether an individual has access to a bank account based on demographic and socioeconomic inputs.")

# 🎯 Mappings from user-friendly input to encoded values
relationship_map = {
    'Head of Household': 0,
    'Spouse': 1,
    'Child': 2,
    'Parent': 3,
    'Other Relative': 4,
    'Non-Relative': 5
}

education_map = {
    'No formal education': 0,
    'Primary education': 1,
    'Secondary education': 2,
    'Vocational/Specialised training': 3,
    'Tertiary education': 4,
    'Other/Dont know': 5
}

job_map = {
    'Unemployed': 0,
    'Self employed': 1,
    'Formally employed (Private)': 2,
    'Formally employed (Government)': 3,
    'Informally employed': 4,
    'Farming and Fishing': 5,
    'Remittance Dependent': 6,
    'Government Dependent': 7,
    'Other Income': 8,
    'Dont know': 9
}

country_map = {
    'Kenya': 6068,
    'Rwanda': 8735,
    'Tanzania': 6600,
    'Uganda': 121
}

# 📋 User inputs
with st.form("prediction_form"):
    st.header("📌 Enter Respondent Information")

    year = st.number_input("Survey Year", value=2018)
    household_size = st.slider("Household Size", 1, 20, 5)
    age = st.slider("Age of Respondent", 16, 100, 35)

    country = st.selectbox("Country", list(country_map.keys()))
    location_type = st.radio("Urban Location?", ['Yes', 'No'])
    cellphone_access = st.radio("Has Cellphone Access?", ['Yes', 'No'])
    gender = st.radio("Gender", ['Male', 'Female'])

    relationship = st.selectbox("Relationship to Head of Household", list(relationship_map.keys()))
    marital_status = st.selectbox("Marital Status", [
        'Married/Living together',
        'Single/Never Married',
        'Widowed',
        'Divorced/Separated',
        'Dont know'
    ])
    education = st.selectbox("Education Level", list(education_map.keys()))
    job = st.selectbox("Job Type", list(job_map.keys()))

    submitted = st.form_submit_button("🔎 Predict")

# 🧠 Convert inputs to model-ready format
if submitted:
    input_data = pd.DataFrame([{
        "year": year,
        "household_size": household_size,
        "age_of_respondent": age,
        "relationship_with_head": relationship_map[relationship],
        "education_level": education_map[education],
        "job_type": job_map[job],
        "country_freq": country_map[country],
        "location_type_Urban": True if location_type == "Yes" else False,
        "cellphone_access_Yes": True if cellphone_access == "Yes" else False,
        "gender_of_respondent_Male": True if gender == "Male" else False,
        "marital_status_Dont know": marital_status == 'Dont know',
        "marital_status_Married/Living together": marital_status == 'Married/Living together',
        "marital_status_Single/Never Married": marital_status == 'Single/Never Married',
        "marital_status_Widowed": marital_status == 'Widowed'
    }])

    # 🔮 Make prediction
    pred = model.predict(input_data)[0]
    result = "✅ Has Bank Account" if pred == 1 else "❌ No Bank Account"
    st.success(f"Prediction: {result}")
