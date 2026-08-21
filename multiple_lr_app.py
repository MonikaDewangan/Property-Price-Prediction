import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Property Price Prediction",
    page_icon="🏠",
    layout="centered"
)

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("housing_data.csv")

# -----------------------------
# Features and Target
# -----------------------------
features = [
    "MedInc",
    "HouseAge",
    "AveRooms",
    "AveOccup",
    "Latitude",
    "Longitude"
]

X = df[features]
y = df["Price"]

# -----------------------------
# Train-Test Split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# -----------------------------
# Train Multiple Linear Regression
# -----------------------------
model = LinearRegression()
model.fit(X_train, y_train)

# -----------------------------
# Streamlit UI
# -----------------------------
st.title("🏠 Property Price Prediction")

st.write(
    "Predict property prices using a Multiple Linear Regression model."
)

st.subheader("Enter Property Details")

col1, col2 = st.columns(2)

with col1:
    MedInc = st.number_input(
        "Median Income ($10,000s)",
        min_value=0.5,
        max_value=15.0,
        value=7.5,
        step=0.1,
        help="Median household income in the area. Example: 7.5 means $75,000."
    )

    HouseAge = st.number_input(
        "House Age (years)",
        min_value=1.0,
        max_value=52.0,
        value=28.0,
        step=1.0,
        help="Median age of houses in the area."
    )

    AveRooms = st.number_input(
        "Average Rooms",
        min_value=1.0,
        max_value=20.0,
        value=5.0,
        step=0.1,
        help="Average number of rooms per household."
    )

with col2:
    AveOccup = st.number_input(
        "Average Occupancy (people)",
        min_value=1.0,
        max_value=20.0,
        value=3.0,
        step=0.1,
        help="Average number of people per household."
    )

    Latitude = st.number_input(
        "Latitude (°)",
        min_value=32.0,
        max_value=43.0,
        value=37.0,
        step=0.01,
        help="Geographical latitude of the property."
    )

    Longitude = st.number_input(
        "Longitude (°)",
        min_value=-125.0,
        max_value=-114.0,
        value=-119.0,
        step=0.01,
        help="Geographical longitude of the property."
    )

# -----------------------------
# Prediction
# -----------------------------
if st.button("🔮 Predict Price", use_container_width=True):

    input_data = pd.DataFrame({
        "MedInc": [MedInc],
        "HouseAge": [HouseAge],
        "AveRooms": [AveRooms],
        "AveOccup": [AveOccup],
        "Latitude": [Latitude],
        "Longitude": [Longitude]
    })

    prediction = model.predict(input_data)[0]

    st.success(f"💰 Predicted Property Price: ${prediction:,.2f}")

# -----------------------------
# Model Performance
# -----------------------------
y_pred = model.predict(X_test)

r2 = r2_score(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)

st.subheader("📊 Model Performance")

col1, col2 = st.columns(2)

with col1:
    st.metric("R² Score", f"{r2:.3f}")

with col2:
    st.metric("Mean Squared Error", f"{mse:,.0f}")

# -----------------------------
# Model Information
# -----------------------------
with st.expander("ℹ️ About the Model"):
    st.write("**Model:** Multiple Linear Regression")
    st.write("**Target:** Property Price")
    st.write("**Features:**")
    st.write(", ".join(features))
