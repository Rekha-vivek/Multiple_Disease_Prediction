# 🏥 Multiple Disease Prediction System

## 📌 Project Overview

This project is a Machine Learning based web application that predicts the risk of multiple diseases using patient medical parameters.

The system currently predicts the following diseases:

- 🩺 Liver Disease  
- 🧠 Parkinson’s Disease  
- 🩸 Kidney Disease  

Users can enter medical details through a web interface and the system will predict whether the patient is likely to have the disease.

The models were built, evaluated, tuned, and deployed using **Python, Scikit-learn, and Streamlit**.



---

# 🎯 Objective

The main objectives of this project are:

- Build predictive machine learning models for multiple diseases.

- Perform proper data preprocessing and feature engineering.

- Compare multiple machine learning algorithms.

- Evaluate model performance using classification metrics.

- Deploy trained models using Streamlit.



---

# 📊 Datasets Used

The following datasets were used for training the models:

**1. Liver Disease Dataset**

- Indian Liver Patient Dataset
- Contains biochemical test results of patients
- Target variable indicates whether the patient has liver disease

**2. Parkinson’s Disease Dataset**

- Contains biomedical voice measurements
- Used to detect Parkinson's disease in patients

**3. Kidney Disease Dataset**

- Chronic Kidney Disease dataset
- Contains laboratory test results and patient medical parameters



---

# ⚙️ Data Preprocessing

Data preprocessing is an important step in machine learning.

The following preprocessing steps were applied:

### Handling Missing Values

Missing values were identified using Pandas.

Numerical columns were filled using the **median value**.

Categorical columns were filled using the **most frequent value**.

This ensures that the dataset remains consistent and usable for model training.



### Encoding Categorical Variables

Categorical features were converted into numerical format using **Label Encoding**.

Machine learning algorithms require numerical input values.



### Feature Scaling

Feature scaling was applied using **StandardScaler**.

This step standardizes numerical features so that they have similar ranges.

Feature scaling improves the performance of algorithms such as Logistic Regression.



---

# 🔀 Train Test Split

The dataset was split into training and testing sets.

- **80% Training Data**
- **20% Testing Data**

The training data was used to train the models.

The testing data was used to evaluate model performance on unseen data.



---

# 🤖 Machine Learning Models Used

Three different machine learning algorithms were implemented and compared.

### Logistic Regression

Logistic Regression is a linear classification algorithm.

It predicts the probability that a data point belongs to a specific class.

This model serves as a baseline model for comparison.



### Random Forest

Random Forest is an ensemble learning method.

It builds multiple decision trees and combines their predictions.

Random Forest reduces overfitting and performs well on structured datasets.



### XGBoost

XGBoost is a gradient boosting algorithm.

It builds models sequentially and improves errors from previous models.

XGBoost is known for its high performance in machine learning competitions.



---

# 📈 Model Evaluation Metrics

The models were evaluated using several classification metrics.

### Accuracy

Accuracy measures the percentage of correctly classified predictions.



### Confusion Matrix

The confusion matrix shows:

- True Positives
- True Negatives
- False Positives
- False Negatives



### Precision

Precision measures how many predicted positive cases are actually correct.



### Recall

Recall measures how many actual positive cases were correctly identified.

In medical prediction, recall is important because missing a disease case can be dangerous.



### F1 Score

F1 Score is the harmonic mean of precision and recall.

It balances both precision and recall.



### ROC-AUC Score

ROC-AUC measures the model's ability to distinguish between classes.

Higher ROC-AUC values indicate better model performance.



---

# 🔧 Hyperparameter Tuning

Hyperparameter tuning was performed using **GridSearchCV**.

GridSearchCV tests different combinations of parameters to find the best performing configuration.

The following parameters were tuned for Random Forest:

- `n_estimators`
- `max_depth`
- `min_samples_split`
- `min_samples_leaf`

This process helps improve model performance and generalization.



---

# 🏆 Final Model Selection

After comparing all models, the best performing model was selected for each disease based on:

- Accuracy
- Recall
- F1 Score
- ROC-AUC Score

The final trained models were saved using **Pickle**.



---

# 💻 Model Deployment

The trained models were deployed using **Streamlit**.

The Streamlit application performs the following steps:

1. Takes user medical inputs.

2. Converts inputs into the required feature format.

3. Applies the saved scaler.

4. Sends the processed data to the trained model.

5. Displays prediction results and probability.



---

# 📊 Results

The trained models achieved reliable performance in predicting disease conditions.

Random Forest generally provided strong performance across multiple datasets.

ROC-AUC curves confirmed that the models were able to distinguish between positive and negative cases effectively.



---

# 🧰 Technologies Used

The following technologies were used in this project:

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Matplotlib
- Seaborn
- Streamlit



---

# 🚀 Key Learnings

During this project the following concepts were applied:

- Data preprocessing and cleaning
- Handling missing values
- Feature encoding
- Feature scaling
- Model comparison
- Hyperparameter tuning
- Model evaluation
- Machine learning deployment



---

# 📌 Conclusion

This project demonstrates how machine learning models can be used for early disease prediction using structured medical data.

By combining proper data preprocessing, model evaluation, hyperparameter tuning, and deployment, a complete end-to-end machine learning system was developed.



---

# 👩‍💻 Author

This project was developed as part of a **Machine Learning and Data Science learning project**.

The goal was to understand the full machine learning pipeline from data preprocessing to model deployment.
