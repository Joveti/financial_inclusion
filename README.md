# Financial Inclusion in Africa – Bank Account Prediction

This data science project predicts whether individuals across African countries have access to bank accounts. The objective is to support financial inclusion efforts using data-driven insights.


## 🗂️ Dataset Overview

- **Source:** Financial inclusion survey across African countries
- **Target:** `bank_account` (binary: 0 = No Account, 1 = Has Account)
- **Features:** Demographic and socioeconomic indicators (age, education, job type, access to cellphone, etc.)



## 🚀 Deployment

- Built with **Streamlit** for interactive visualization.
- Model serialized using **Pickle** (`rf_model.pkl`) for quick loading.

## 📦 Installation

```bash
git clone https://github.com/your-username/financial-inclusion-project
cd financial-inclusion-project
pip install -r requirements.txt
streamlit run 03_deployment/streamlit_app.py


