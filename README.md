# 🏠 Property Price Prediction using Linear Regression

A Machine Learning project that predicts property prices using **Simple Linear Regression** and **Multiple Linear Regression**. This project demonstrates the workflow of building, training, evaluating, and interpreting linear regression models using Python and Scikit-learn.

---

## 🚀 Live Demos

### 📌 Simple Linear Regression
🔗 **[Live Demo](YOUR_SIMPLE_LINEAR_REGRESSION_LINK)**

> Replace `YOUR_SIMPLE_LINEAR_REGRESSION_LINK` with your Streamlit app URL.

### 📌 Multiple Linear Regression
🔗 **[Live Demo](YOUR_MULTIPLE_LINEAR_REGRESSION_LINK)**

> Replace `YOUR_MULTIPLE_LINEAR_REGRESSION_LINK` with your Streamlit app URL.

---

## 📌 Project Overview

This project includes two regression models:

- ✅ **Simple Linear Regression**
- ✅ **Multiple Linear Regression**

Both models use the same housing dataset and predict **Price**, but they use different numbers of input features.

---

## 🤖 Models

### 1. Simple Linear Regression

Simple Linear Regression predicts the target variable using **one feature**.

**Target Variable:**
- `Price` — House/property price

**Feature:**
- `MedInc` — Median income

```text
Price = β₀ + β₁(MedInc)
```

The model learns how the median income of an area is related to property prices.

### 2. Multiple Linear Regression

Multiple Linear Regression predicts the target variable using **multiple features**.

**Target Variable:**
- `Price` — House/property price

**Features:**
- `MedInc` — Median income
- `HouseAge` — Age of the house
- `AveRooms` — Average number of rooms
- `AveOccup` — Average occupancy
- `Latitude` — Latitude of the property
- `Longitude` — Longitude of the property

```text
Price = β₀ + β₁(MedInc) + β₂(HouseAge) + β₃(AveRooms)
        + β₄(AveOccup) + β₅(Latitude) + β₆(Longitude)
```

Using multiple features allows the model to consider different property and location characteristics when predicting the price.

---

## 📂 Project Structure

```text
Project-Property-Price-Prediction/
│
├── housing_data.csv
├── simple_lr.ipynb
├── multiple_lr.ipynb
├── app.py
├── README.md
└── requirements.txt
```

---

## 📊 Dataset Features

| Feature | Description |
|---------|-------------|
| `MedInc` | Median income |
| `HouseAge` | Age of the house |
| `AveRooms` | Average number of rooms |
| `AveOccup` | Average occupancy |
| `Latitude` | Latitude of the property |
| `Longitude` | Longitude of the property |
| `Price` | Target variable (House Price) |

---

## 🚀 Project Workflow

### Simple Linear Regression

- Import required libraries
- Load and explore the dataset
- Visualize the relationship between `MedInc` and `Price`
- Perform Train-Test Split
- Train Simple Linear Regression model
- Predict house prices
- Evaluate the model using MSE and R² Score
- Predict price for new input

### Multiple Linear Regression

- Import required libraries
- Load and explore the dataset
- Select multiple features
- Perform Train-Test Split
- Train Multiple Linear Regression model
- Predict house prices
- Evaluate the model using MSE and R² Score
- Display feature coefficients
- Predict price for new input

---

## 📈 Model Evaluation

The models are evaluated using:

- **Mean Squared Error (MSE)** — Measures the average squared difference between actual and predicted prices.
- **R² Score** — Measures how well the model explains the variation in the target variable.

---

## 🌐 Streamlit Demo

The Streamlit applications provide an interactive way to test both regression models.

### Simple Linear Regression Demo

**Input Feature:** `MedInc` (Median income)

**Target Variable:** `Price` (Property price)

### Multiple Linear Regression Demo

**Input Features:** `MedInc`, `HouseAge`, `AveRooms`, `AveOccup`, `Latitude`, `Longitude`

**Target Variable:** `Price` (Property price)

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Streamlit
- Jupyter Notebook
- VS Code
- Git & GitHub

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/MonikaDewangan/Property-Price-Prediction-LinearRegression.git
```

### 2. Navigate to the project directory

```bash
cd Property-Price-Prediction-LinearRegression
```

### 3. Install the required libraries

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit application

```bash
streamlit run app.py
```

---

## 🎯 Future Improvements

- Polynomial Regression
- Decision Tree Regression
- Random Forest Regression
- Feature Engineering
- Hyperparameter Tuning
- Model comparison and visualization

---

## 👩‍💻 Author

**Monika Dewangan**

- GitHub: https://github.com/MonikaDewangan

---

⭐ If you found this project useful, feel free to star the repository!
