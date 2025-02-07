# Guvi Project_4
## Microsoft Classifying Cybersecurity Incidents

### INTRODUCTION
The growing volume and complexity of cybersecurity incidents have made manual triage a challenge for Security Operation Centers (SOCs). This project aims to automate the classification of incidents using machine learning, helping SOCs prioritize critical alerts and reduce false positives. Leveraging Microsoft’s **GUIDE dataset**, we built a machine learning pipeline and evaluated multiple models, with **Random Forest** emerging as the most reliable choice. The project highlights the potential of machine learning in transforming cybersecurity workflows and improving threat response efficiency.

### PROJECT OVERVIEW
This project focuses on building a machine learning model to classify incidents into **True Positive (TP), Benign Positive (BP), and False Positive (FP)** categories. By automating incident triage, the project reduces manual effort and enhances response time for cybersecurity teams. The dataset, consisting of 35 features, required significant preprocessing to handle high-cardinality categorical data and class imbalance. A custom preprocessing pipeline was created to ensure consistency across training and testing phases.

### KEY FEATURES
1. **Data Preprocessing:** Handled missing values, reduced high-cardinality categorical features, and applied label encoding.
2. **Class Imbalance Handling:** Used SMOTE to balance the training dataset.
3. **Model Evaluation:** Evaluated four models—Decision Tree, Logistic Regression, Random Forest, and XGBoost.
4. **Pipeline Integration:** Developed a custom pipeline for data transformation and sampling.
5. **Hyperparameter Tuning:** Optimized the Random Forest model for improved accuracy.

### DATASET OVERVIEW
The dataset consists of incident-level data provided by Microsoft, containing categorical and numerical features such as IncidentId, DetectorId, Category, and OSFamily.
1. **Training Data:** 15 lakh samples after preprocessing.
2. **Test Data:** 15 lakh samples for final evaluation.
3. **Target Variable:** IncidentGrade, classified as **TP, BP, or FP**.

Key challenges included handling high-cardinality features like IpAddress and balancing imbalanced classes in the target variable.

### MODEL PERFORMANCE (TRAINING Vs TESTING)
| Model                 | Macro F1-Score (Training) | Macro F1-Score (Testing) | Precision (Testing) | Recall (Testing) |
|:---------------------:|:-------------------------:|:------------------------:|:-------------------:|:----------------:|
| Decision Tree         |           0.51            |          0.51            |       0.64          |       0.52       |
| Logistic Regression   |           0.20            |          0.20            |       0.15          |       0.33       |
| Random Forest         |           0.68            |          0.53            |       0.57          |       0.53       |
| XGBoost               |           0.63            |          0.53            |       0.57          |       0.53       |

### CONCLUSION
This project demonstrates the power of machine learning in automating cybersecurity workflows. By reducing manual triage effort, the solution enables SOC analysts to focus on real threats, improving organizational security posture. The **Random Forest model**, combined with the custom data pipeline, offers scalability and reliable performance for real-world deployment.



