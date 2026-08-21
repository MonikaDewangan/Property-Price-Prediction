import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("housing_data.csv")

# -----------------------------
# Prepare Data
# -----------------------------
X = df[["MedInc"]]
y = df["Price"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -----------------------------
# Train Model
# -----------------------------
model = LinearRegression()
model.fit(X_train, y_train)

# -----------------------------
# Streamlit UI
# -----------------------------
st.title("🏠 Property Price Prediction")

st.write(
    "This app predicts property price using Simple Linear Regression "
    "based on Median Income (MedInc)."
)

st.subheader("Enter Property Details")

med_inc = st.number_input(
    "Median Income (MedInc)",
    min_value=0.5,
    max_value=15.0,
    value=8.6,
    step=0.1
)

# -----------------------------
# Prediction
# -----------------------------
if st.button("Predict Price"):

    prediction = model.predict([[med_inc]])[0]

    st.success(
        f"💰 Predicted Property Price: ${prediction:,.2f}"
    )

# -----------------------------
# Model Performance
# -----------------------------
y_pred = model.predict(X_test)
r2 = r2_score(y_test, y_pred)

st.subheader("Model Performance")
st.write(f"R² Score: **{r2:.3f}**")

st.info(
    "Model: Simple Linear Regression\n\n"
    "Input Feature: MedInc\n\n"
    "Target: Price"
)

