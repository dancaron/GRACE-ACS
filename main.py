import streamlit as st

# App description
st.title("GRACE ACS Risk and Mortality Calculator")
st.write("""
This app calculates the in-hospital and 6-month mortality risk for patients with Acute Coronary Syndrome (ACS) based on the GRACE risk model. 
Please input the required clinical data to obtain the risk scores.
""")

# Input fields for clinical data
age = st.number_input("Age (years)", min_value=18, max_value=120, value=60)
heart_rate = st.number_input("Heart Rate (bpm)", min_value=20, max_value=200, value=70)
systolic_bp = st.number_input("Systolic Blood Pressure (mmHg)", min_value=50, max_value=250, value=120)
creatinine = st.number_input("Serum Creatinine (mg/dL)", min_value=0.1, max_value=10.0, value=1.0)
killip_class = st.selectbox("Killip Class", options=[1, 2, 3, 4], index=0)
cardiac_arrest = st.radio("Cardiac Arrest at Admission", ["No", "Yes"], index=0)
st_segment_deviation = st.radio("ST Segment Deviation", ["No", "Yes"], index=0)
elevated_troponin = st.radio("Elevated Cardiac Enzymes (Troponin)", ["No", "Yes"], index=0)

# Risk calculation logic (simplified model for demonstration)
# Add real-world GRACE calculations based on actual GRACE formula or weights

def calculate_risk(age, heart_rate, systolic_bp, creatinine, killip_class, cardiac_arrest, st_segment_deviation, elevated_troponin):
    risk_score = (
        age * 0.2 +
        heart_rate * 0.1 +
        (140 - systolic_bp) * 0.15 +
        creatinine * 0.3 +
        (1 if cardiac_arrest == "Yes" else 0) * 3 +
        (1 if st_segment_deviation == "Yes" else 0) * 2 +
        (1 if elevated_troponin == "Yes" else 0) * 1.5 +
        killip_class * 1.2
    )
    # In-hospital mortality
    in_hospital_mortality = round(risk_score * 0.02, 2)
    # 6-month mortality (simplified for demo purposes)
    six_month_mortality = round(risk_score * 0.04, 2)
    
    return in_hospital_mortality, six_month_mortality

# Calculate the risk
if st.button("Calculate Risk"):
    in_hospital_risk, six_month_risk = calculate_risk(
        age, heart_rate, systolic_bp, creatinine, killip_class, cardiac_arrest, st_segment_deviation, elevated_troponin
    )
    
    # Display results
    st.subheader("Risk Results")
    st.write(f"In-Hospital Mortality Risk: {in_hospital_risk}%")
    st.write(f"6-Month Mortality Risk: {six_month_risk}%")
