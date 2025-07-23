# NovaCred: Cred Predictor

## Project Overview

This project provides a comprehensive credit risk modeling application designed to help financial institutions assess borrower creditworthiness and predict the likelihood of loan default. The application is built with a powerful XGBoost machine learning model and features a user-friendly frontend created with Streamlit.

The intuitive UI allows loan officers and risk analysts to input borrower information, receive real-time risk assessments, and gain insights into the model's predictions. The backend is supported by a robust set of utilities for data preprocessing and credit score calculation, making it a scalable and reliable tool for financial decision-making.

## Features

- **Interactive UI**: A clean and efficient user interface built with Streamlit, organized into tabs for easy navigation.
- **Real-Time Predictions**: Instantly calculates default probability, a credit score (300-900), and a risk rating.
- **Model Transparency**: Includes visualizations for feature importance and model performance (ROC curve) to help users understand the predictions.
- **Robust Backend**: Powered by an XGBoost model and a modular utility script for data handling.
- **Easy Setup**: A straightforward installation process with a `requirements.txt` file to manage dependencies.

## Technologies Used

- **Backend**: Python, Pandas, NumPy, Scikit-learn
- **Frontend**: Streamlit
- **Machine Learning**: XGBoost, Optuna
- **Development**: Git, GitHub, VS Code

## Project Structure

```
├── finding-documents/         # Contains project reports and presentations
├── images/                    # Stores images used in the app and documentation
├── notebooks/                 # Jupyter notebooks for analysis and model development
├── project-root/              # Main application source code
│   ├── model/                 # Trained model and scaler
│   ├── .streamlit/            # Streamlit configuration
│   ├── NovaCred.JPG           # Project logo
│   ├── main.py                # Streamlit frontend
│   ├── utils.py               # Backend data processing and prediction
│   └── requirements.txt       # Project dependencies
└── README.md                  # This file
```

## Application Interface

The application is organized into a clean and intuitive interface, allowing for seamless user interaction.

### Input Tabs

Credit applicant information is collected across three dedicated tabs: "Personal Info," "Loan Details," and "Credit History."

### Risk Assessment Results

After submitting the details, the application displays the risk assessment, including the default probability, credit score, and a clear risk rating.

![Results Display](./images/cred_prediction_app_ss.jpg)

---

## Documentation for `main.py`

The `main.py` script serves as the frontend of the Cred Predictor application. Built with Streamlit, it provides an interactive interface for users to input borrower details and receive a comprehensive risk assessment.

### Key Components:

-   **Page Configuration**: Sets up the application with a wide layout and a clear title.
-   **Sidebar**: Contains the company logo and instructions for using the app.
-   **Input Tabs**: Organizes input fields into three logical sections:
    1.  **Personal Info**: Captures age, income, and residence type.
    2.  **Loan Details**: Collects loan amount, purpose, tenure, and type.
    3.  **Credit History**: Gathers credit-related metrics like DPD, DMTLM, and credit utilization.
-   **Action Button**: A primary button, "Calculate Risk," triggers the prediction.
-   **Results Display**: Presents the default probability, credit score, and risk rating using `st.metric` for a clear and professional look.
-   **Expandable Sections**:
    -   **Understanding the Prediction**: Displays a feature importance plot to explain which factors most influence the model's decision.
    -   **Model Performance**: Shows the ROC curve to provide transparency about the model's accuracy.

---

## Documentation for `utils.py`

This utility script supports the credit scoring system by handling data preprocessing, prediction, and credit score calculation.

### Key Functions:

-   **`data_preparation(...)`**:
    -   Transforms raw user input into a pandas DataFrame.
    -   Performs one-hot encoding for categorical features.
    -   Standardizes numerical features using a pre-fitted `StandardScaler`.
-   **`calculate_credit_score(...)`**:
    -   Computes the default and non-default probabilities using the trained model.
    -   Converts the non-default probability into a credit score scaled between 300 and 900.
    -   Assigns a risk rating (Poor, Average, Good, Excellent) based on the score.
-   **`predict(...)`**:
    -   Orchestrates the entire process by calling the data preparation and credit score functions.
    -   Returns the final probability, score, and rating to the main application.

---

## Documentation for Tuned Hyperparameters

The XGBoost model has been fine-tuned using Optuna to optimize its performance. The key hyperparameters are:

-   **`eta` (Learning Rate)**: `0.0396`
-   **`max_depth`**: `3`
-   **`subsample`**: `0.627`
-   **`colsample_bytree`**: `0.714`
-   **`n_estimators`**: `388`

These settings balance predictive accuracy with computational efficiency, ensuring the model is both powerful and robust.
