#  Retail Customer Intelligence System

### Customer Segmentation & Churn Prediction using Dunnhumby Dataset

---

##  Project Overview

Retailers generate large volumes of transactional data but often struggle to proactively identify customers at risk of churn. Losing customers directly impacts revenue, marketing efficiency, and long-term growth.

This project builds an end-to-end customer intelligence system using the Dunnhumby “Complete Journey” dataset to:

* Segment customers based on purchasing behavior
* Predict customer churn probability
* Identify key behavioral drivers influencing churn
* Generate actionable insights for targeted retention strategies

---

##  Dataset

**Source:** Dunnhumby – The Complete Journey (Kaggle)

* ~2,500 households
* 2.5M+ transaction records
* Multi-year retail purchase history
* Includes transaction, product, and demographic data

Dataset link:
[https://www.kaggle.com/datasets/frtgnn/dunnhumby-the-complete-journey](https://www.kaggle.com/datasets/frtgnn/dunnhumby-the-complete-journey)

---

##  Problem Statement

Develop a machine learning system to segment retail customers and predict churn risk using historical transaction data, enabling data-driven retention strategies.

Churn Definition:

> A customer is labeled as churned if no purchase activity is observed in the last 90 days.

---

##  Project Pipeline

1. Data Understanding & Cleaning
2. Customer-Level Feature Engineering
3. Customer Segmentation (K-Means Clustering)
4. Churn Label Creation
5. Predictive Modeling
6. Threshold Optimization
7. Model Interpretation & Business Insights

---

##  Feature Engineering

Transaction-level data was aggregated to customer level using the RFM framework.

### Core Behavioral Features

* **Frequency** – Total number of transactions per customer
* **Monetary** – Total spend across all transactions
* **Total Quantity** – Total units purchased
* **Average Spend per Transaction**

### Recency

* Used only for churn labeling
* Excluded from model training to prevent target leakage

All numerical features were scaled before training logistic regression.

---

##  Customer Segmentation

Applied K-Means clustering (k=4) on RFM features.

Identified four distinct customer segments:

* Elite Customers
* Loyal High-Value Customers
* Regular Customers
* Churned / Inactive Customers

Segmentation provides behavioral grouping for targeted marketing strategies.

---

##  Churn Prediction Modeling

### Model Used

Logistic Regression

### Why Logistic Regression?

* Strong performance
* Interpretable coefficients
* Business-friendly explainability

### Class Imbalance Handling

* Dataset was imbalanced (~7% churn rate)
* Evaluated model beyond accuracy
* Threshold tuning applied to optimize churn recall

---

##  Model Performance

* ROC-AUC: **0.81**
* Recall (Churn) @ 0.1 threshold: **0.74**
* Accuracy @ 0.1 threshold: 0.73

The model demonstrates strong ranking ability and practical recall performance for churn detection.

---

##  Key Insights

* Frequency is the strongest driver of retention.
* Higher total spending significantly reduces churn probability.
* Engagement intensity is more predictive than average basket size.
* Threshold adjustment allows business-controlled trade-off between recall and precision.

---

##  Business Impact

This system enables retailers to:

* Identify high-risk customers early
* Optimize retention campaign targeting
* Allocate marketing budget efficiently
* Understand behavioral drivers of churn

---

##  Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib / Seaborn
* Joblib

---

##  Project Structure

```
retail-customer-intelligence/
│
├── notebooks/
├── images/
├── models/
├── data/
├── requirements.txt
└── README.md
```

---

##  Future Improvements

* Incorporate demographic features
* Add campaign and coupon response modeling
* Implement time-based train/test split
* Evaluate XGBoost and ensemble models
* Deploy interactive dashboard

---

##  Author

Swati Yadav

---

