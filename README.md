# AI Payment Recovery

## Project Overview

AI Payment Recovery is a machine learning prototype designed to predict the probability of recovering a failed payment and recommend an appropriate recovery action.

## Problem Statement

Failed payments can lead to lost revenue. The goal of this project is to use payment and customer information to identify recovery opportunities and help prioritize recovery actions.

## Objective

The objective is to build a machine learning classification model that:

- Predicts whether a failed payment can be recovered.
- Estimates the probability of recovery.
- Provides a recommended recovery action based on the predicted probability.

## Dataset

This project uses synthetic payment data created for the prototype. It is not real Razorpay customer or transaction data.

The dataset contains information such as:

- Payment amount
- Payment method
- Failure reason
- Previous successful payments
- Previous failed payments
- Retry count
- Customer tenure
- Transaction hour
- Day of week
- Recovery outcome

## Exploratory Data Analysis

The project analyzes recovery patterns based on:

- Payment method
- Failure reason
- Retry count
- Payment amount
- Numerical feature correlations

## Machine Learning

Two classification models were evaluated:

1. Logistic Regression
2. Random Forest

### Model Results

| Model | Accuracy | Precision | Recall | F1 Score |
|------|----------|-----------|--------|----------|
| Logistic Regression | 73.5% | 74.2% | 95.5% | 83.5% |
| Random Forest | 71.3% | 73.1% | 93.6% | 82.1% |

Logistic Regression was selected because it achieved better results on the test dataset.

## Recovery Recommendation

The model's recovery probability is converted into a simple business recommendation:

- **80% or higher:** Retry Payment
- **50%–79%:** Try Alternate Payment Method
- **Below 50%:** Do Not Retry Immediately

## Example

A payment with an estimated recovery probability of **86.26%** receives the recommendation:

**Retry Payment**

## Project Files

- `app.py` — application code
- `payment_recovery_model.pkl` — trained machine learning model

## Limitations

- The dataset is synthetic.
- The model has moderate overall accuracy.
- Performance for the non-recovery class is weaker than for the recovery class.
- The prototype has not been validated using real payment transaction data.

## Technologies Used

- Python
- Pandas
- Scikit-learn
- Joblib
- Streamlit prototype

## Conclusion

This project demonstrates an end-to-end machine learning approach for payment recovery prediction, from data analysis and model training to recovery probability estimation and business recommendations.
