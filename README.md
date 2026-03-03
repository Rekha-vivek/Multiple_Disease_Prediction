🏥 Multiple Disease Prediction System
📌 Project Overview

This project is a Machine Learning based web application that predicts the risk of:

🩺 Liver Disease

🧠 Parkinson’s Disease

🩸 Kidney Disease

The system allows users to enter medical parameters and get real-time predictions using trained ML models.

The models were built, evaluated, tuned, and deployed using Streamlit.

🎯 Objective

The goal of this project is to:

Build predictive ML models for multiple diseases

Perform proper data preprocessing

Evaluate models using classification metrics

Compare multiple algorithms

Deploy the best performing models using Streamlit

📊 Datasets Used

Indian Liver Patient Dataset

Parkinson’s Dataset

Chronic Kidney Disease Dataset

Each dataset contains medical features and a target variable indicating disease presence.

⚙️ Project Workflow
1️⃣ Data Preprocessing

For each dataset, the following steps were performed:

Checked for missing values

Handled missing values using:

Median (for numerical columns)

Most frequent value (for categorical columns)

Encoded categorical variables using Label Encoding

Split data into:

80% Training

20% Testing

Applied StandardScaler (for Logistic Regression)

2️⃣ Exploratory Data Analysis (EDA)

EDA included:

Correlation heatmaps

Feature distribution plots

Class imbalance checking

Crosstab analysis for categorical relationships

This helped understand which features strongly influence disease prediction.

3️⃣ Models Used

For each disease, the following models were trained:

🔹 Logistic Regression

Used as baseline model

Works well for linear separable data

Scaled features before training

🔹 Random Forest

Ensemble model using multiple decision trees

Handles non-linearity well

Generally gave strong performance

🔹 XGBoost

Gradient boosting algorithm

Optimized boosting technique

Compared performance with Random Forest

4️⃣ Model Evaluation Metrics

Models were evaluated using:

✅ Accuracy

✅ Confusion Matrix

✅ Precision

✅ Recall

✅ F1-Score

✅ ROC-AUC Score

Why These Metrics?

Accuracy shows overall correctness

Precision shows how many predicted positives are correct

Recall shows how many actual positives were detected

F1-score balances precision and recall

ROC-AUC shows overall classification performance

📈 Hyperparameter Tuning

For Random Forest, GridSearchCV was used to find optimal parameters:

n_estimators

max_depth

min_samples_split

min_samples_leaf

This helped improve generalization and avoid overfitting.

However, tuning does not always guarantee large improvement — it depends on dataset complexity.

🏆 Final Model Selection

For each disease, the model with best balance between:

Accuracy

Recall

F1-score

ROC-AUC

was selected and saved using pickle.

💻 Deployment

The final models were deployed using:

Streamlit

Pickle (for model saving)

Scaler saving

Feature column saving

Each disease has a separate Streamlit interface that:

Takes user input

Scales input

Predicts disease

Displays probability

Shows result clearly

📊 Results Summary
🧠 Parkinson’s Disease

Best model achieved strong classification performance

ROC-AUC demonstrated good separability

Balanced recall and precision

🩸 Kidney Disease

High accuracy and strong recall

Random Forest performed well

Hyperparameter tuning improved stability

🩺 Liver Disease

Moderate classification performance

Random Forest performed better than Logistic Regression

ROC-AUC indicated acceptable discrimination ability

🔧 Technologies Used

Python

Pandas

NumPy

Scikit-learn

XGBoost

Matplotlib

Seaborn

Streamlit

🚀 Key Learnings

Importance of preprocessing

Handling missing values properly

Importance of recall in medical prediction

Difference between baseline and ensemble models

Hyperparameter tuning using GridSearchCV

Deploying ML models into real-world applications

📌 Conclusion

This project demonstrates how machine learning can be used for early disease prediction using structured medical data.

By combining proper preprocessing, model comparison, tuning, and deployment, a complete end-to-end ML solution was built.
