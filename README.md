# Heart Failure Prediction System 🫀

This is a Django-based web application designed to predict the likelihood of heart failure in patients based on clinical parameters. The model uses machine learning algorithms to assist healthcare professionals in making informed decisions.

## 🚀 Features

- Predicts risk of heart failure based on 12 input medical attributes
- Clean and responsive web interface
- Built using Django (Backend) and HTML/CSS (Frontend)
- Real-time model prediction upon form submission

## 🖼️ Screenshot


## 📋 Parameters Used

- Age
- Anaemia (Yes/No)
- Creatinine Phosphokinase
- Diabetes (Yes/No)
- Ejection Fraction
- High Blood Pressure (Yes/No)
- Platelets
- Serum Creatinine
- Serum Sodium
- Sex (Male/Female)
- Smoking (Yes/No)

## 🧠 Model

The system uses a trained machine learning model (e.g., Random Forest, Logistic Regression, etc.) on a heart failure dataset to predict the outcome.

## ⚙️ Tech Stack

- **Backend**: Django
- **Frontend**: HTML, CSS (with dark theme)
- **Model**: Scikit-learn
- **Language**: Python


## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/heart-failure-prediction.git
   cd heart-failure-prediction
   ```

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows: env\Scripts\activate
    pip install -r requirements.txt
    ```

    Install dependencies
    ```bash
    pip install -r requirements.txt
    Run the Django server
    ```

    ```bash
    py manage.py runserver
    Open in browser
    http://127.0.0.1:8000/
    ```

>✅ How to Use
    Enter the patient’s medical details in the input form.
    Click the Predict button.

### View prediction result – whether the patient is at risk of heart failure or not.

## 📦 Requirements
Django
numpy
pandas
scikit-learn
joblib


## 📌 Future Enhancements
Add charts to visualize patient health history

Store predictions in a database for record-keeping

User authentication for doctors/patients

REST API for model predictions

## 📄 License
MIT License - feel free to use and modify the code.

# Created with ❤️ using Django and ML.