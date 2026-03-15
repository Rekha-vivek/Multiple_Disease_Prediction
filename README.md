# 🏥 Multiple Disease Prediction System

## 📌 Project Overview

This project is a Machine Learning based web application that predicts the risk of multiple diseases using patient medical parameters.

The system currently predicts the following diseases:

- 🩺 Liver Disease  
- 🧠 Parkinson’s Disease  
- 🩸 Kidney Disease  

Users can enter medical parameters through a web interface and the system predicts whether the patient is likely to have the disease.

The models were trained, evaluated, tuned, and deployed using **Python, Scikit-learn, and Streamlit**.



---

# 🎯 Objective

The goal of this project is to build machine learning models that can assist in predicting diseases using medical data.

The objectives of this project include:

- Building predictive machine learning models for multiple diseases  
- Performing proper data preprocessing and feature engineering  
- Comparing different machine learning algorithms  
- Evaluating model performance using classification metrics  
- Deploying the trained models using Streamlit for real-time prediction  



---

# 📊 Datasets Used

Three medical datasets were used in this project.

## Liver Disease Dataset

The Indian Liver Patient Dataset contains medical laboratory test results of patients.

Features include:

- Age  
- Total Bilirubin  
- Direct Bilirubin  
- Alkaline Phosphotase  
- Alanine Aminotransferase  
- Aspartate Aminotransferase  
- Total Proteins  
- Albumin  
- Albumin and Globulin Ratio  

The target variable indicates whether the patient has liver disease.



## Parkinson’s Disease Dataset

The Parkinson’s dataset contains biomedical voice measurements that help detect Parkinson’s disease.

Features include measurements such as:

- Jitter  
- Shimmer  
- Noise-to-Harmonics Ratio  
- Harmonics-to-Noise Ratio  
- Spread measurements  
- DFA  
- PPE  

These features help detect patterns in voice signals associated with Parkinson’s disease.



## Kidney Disease Dataset

The Chronic Kidney Disease dataset contains laboratory and clinical parameters such as:

- Blood Pressure  
- Blood Glucose  
- Serum Creatinine  
- Hemoglobin  
- Packed Cell Volume  
- White Blood Cell Count  
- Red Blood Cell Count  

These parameters help determine whether a patient has kidney disease.



---

# ⚙️ Data Preprocessing

Before training the machine learning models, several preprocessing steps were performed.

## Handling Missing Values

Missing values were identified using Pandas functions.

Numerical columns were filled using the **median value**.

Categorical columns were filled using the **most frequent value**.

This ensured the dataset remained consistent for model training.



## Encoding Categorical Variables

Categorical columns were converted into numerical values using **Label Encoding**.

Machine learning algorithms require numerical inputs for computation.



## Feature Scaling

Feature scaling was performed using **StandardScaler**.

Scaling ensures that features are normalized and prevents large-value features from dominating the model.



---

# 🔀 Train Test Split

The datasets were divided into training and testing sets.

- **80% Training Data**  
- **20% Testing Data**

The training data was used to train the machine learning models.

The testing data was used to evaluate how well the models perform on unseen data.



---

# 🤖 Machine Learning Models Used

Three machine learning algorithms were trained and compared.

## Logistic Regression

Logistic Regression was used as a baseline model for classification.

It estimates the probability that a patient belongs to a disease class.

For the **liver disease dataset**, Logistic Regression achieved an accuracy of approximately **72%**.

The confusion matrix showed that the model correctly identified many disease cases but also misclassified some healthy patients.

Precision was relatively good, meaning that when the model predicted disease, it was often correct.

However, recall indicated that some disease cases were still missed.



## Random Forest

Random Forest is an ensemble learning algorithm that builds multiple decision trees and combines their predictions.

For the **liver disease dataset**, Random Forest achieved an accuracy of approximately **73%**.

The confusion matrix showed that Random Forest detected more disease cases correctly compared to Logistic Regression.

Precision and recall were more balanced, indicating better overall performance.

Random Forest handled the dataset’s non-linear relationships more effectively.



## XGBoost

XGBoost is a gradient boosting algorithm that builds models sequentially to improve prediction accuracy.

For the **liver disease dataset**, XGBoost achieved an accuracy of approximately **71%**.

Although it detected many positive disease cases, it misclassified some healthy cases.

Overall, Random Forest performed slightly better than XGBoost for this dataset.



---

# 📈 Model Evaluation Results

The models were evaluated using several classification metrics.

## Confusion Matrix

The confusion matrix helps understand prediction behavior.

- True Positive → correctly predicted disease cases  
- True Negative → correctly predicted healthy cases  
- False Positive → healthy patient predicted as diseased  
- False Negative → diseased patient predicted as healthy  

In medical prediction systems, minimizing **false negatives** is important because missing a disease case can be risky.



## Precision and Recall

Precision indicates how many predicted disease cases were actually correct.

Recall measures how many actual disease cases were correctly detected by the model.

Balancing both precision and recall is important for medical prediction systems.



---

# 🩺 Liver Disease Model Results

Three models were evaluated for liver disease prediction.

- Logistic Regression Accuracy ≈ **72%**  
- Random Forest Accuracy ≈ **73%**  
- XGBoost Accuracy ≈ **71%**

Random Forest performed slightly better than the other models.

The ROC-AUC score for the liver disease model was approximately **0.76**, indicating moderate classification performance.



---

# 🧠 Parkinson’s Disease Model Results

The Parkinson’s dataset showed very strong predictive patterns.

- Logistic Regression Accuracy ≈ **98%**  
- Random Forest Accuracy ≈ **99%**  
- XGBoost Accuracy ≈ **98%**

Random Forest achieved the best performance.

The ROC-AUC score was approximately **0.98**, indicating excellent classification ability.



---

# 🩸 Kidney Disease Model Results

The kidney disease dataset produced very strong results.

- Logistic Regression Accuracy ≈ **98%**  
- Random Forest Accuracy ≈ **99%**  
- XGBoost Accuracy ≈ **98%**

Random Forest again achieved the best performance.

The ROC-AUC score was approximately **0.99**, indicating excellent classification capability.



---

# 📊 Overall Model Comparison

| Disease | Best Model | Accuracy | ROC-AUC |
|-------|-------|-------|-------|
| Liver Disease | Random Forest | ~73% | 0.76 |
| Parkinson’s Disease | Random Forest | ~99% | 0.98 |
| Kidney Disease | Random Forest | ~99% | 0.99 |

Random Forest performed best across most datasets because it combines multiple decision trees and captures complex patterns effectively.



---

# 💻 Deployment

The trained models were deployed using **Streamlit**.

The Streamlit application performs the following steps:

1. Accepts medical inputs from the user  
2. Converts the inputs into the required feature format  
3. Applies the saved feature scaler  
4. Sends the processed data to the trained model  
5. Displays the prediction result and probability



---

# 🧰 Technologies Used

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

During this project the following machine learning concepts were applied:

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

This project demonstrates how machine learning models can be used to predict diseases using medical datasets.

By combining data preprocessing, model training, evaluation, and deployment, a complete end-to-end machine learning system was developed.

The system allows users to input medical parameters and receive disease predictions instantly through a user-friendly web interface.



---

# 👩‍💻 Author

Rekha 
