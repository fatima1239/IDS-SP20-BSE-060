# 25-11-2023
# CSC461 – Assignment3 – Machine Learning
# Fatima Kazmi
# SP20-BSE-060


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

# Upload the "gender-prediction.csv" file in Google Colab
from google.colab import files
uploaded = files.upload()

# Read the CSV file into a DataFrame
import io
df = pd.read_csv(io.StringIO(uploaded['gender-prediction.csv'].decode('utf-8')))

# Display the first few rows of the dataset
print(df.head())

# Separate features (X) and target variable (y)
X = df.drop('gender', axis=1)
y = df['gender']

# Split the data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train Logistic Regression
logreg = LogisticRegression(max_iter=1000)
logreg.fit(X_train_scaled, y_train)

# Make predictions
y_pred = logreg.predict(X_test_scaled)

# Evaluate accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Logistic Regression Accuracy:", accuracy)
# Task : Name 2 attributes that you believe are the most "powerful" in the prediction task. Explain why?
# let's assume that 'Height' and 'Weight' are considered the most powerful attributes.
# These attributes could be influential in predicting gender as they often show differences between males and females.

# Task : Try to exclude these 2 attributes(s) from the dataset. Rerun the experiment with 80/20 train/test split.
# Check for any change in the results and explain.

# Your code for excluding attributes and rerunning the experiment
X_excluded = X.drop(['Height', 'Weight'], axis=1)

X_train_excluded, X_test_excluded, y_train_excluded, y_test_excluded = train_test_split(X_excluded, y, test_size=0.2, random_state=42)

# Apply Logistic Regression without the excluded attributes
lr_model_excluded = LogisticRegression()
lr_model_excluded.fit(X_train_excluded, y_train_excluded)
lr_predictions_excluded = lr_model_excluded.predict(X_test_excluded)
lr_accuracy_excluded = accuracy_score(y_test_excluded, lr_predictions_excluded)

# Apply Support Vector Machines without the excluded attributes
svm_model_excluded = SVC()
svm_model_excluded.fit(X_train_excluded, y_train_excluded)
svm_predictions_excluded = svm_model_excluded.predict(X_test_excluded)
svm_accuracy_excluded = accuracy_score(y_test_excluded, svm_predictions_excluded)

# Apply Multilayer Perceptron without the excluded attributes
mlp_model_excluded = MLPClassifier()
mlp_model_excluded.fit(X_train_excluded, y_train_excluded)
mlp_predictions_excluded = mlp_model_excluded.predict(X_test_excluded)
mlp_accuracy_excluded = accuracy_score(y_test_excluded, mlp_predictions_excluded)

# Print results for the excluded attributes
print("\nTask 6: Results after excluding 'Height' and 'Weight':")
print("Logistic Regression Accuracy:", lr_accuracy_excluded)
print("Support Vector Machines Accuracy:", svm_accuracy_excluded)
print("Multilayer Perceptron Accuracy:", mlp_accuracy_excluded)

#  Print the number of instances incorrectly classified for each model without the excluded attributes
incorrect_lr_excluded = (y_test_excluded != lr_predictions_excluded).sum()
incorrect_svm_excluded = (y_test_excluded != svm_predictions_excluded).sum()
incorrect_mlp_excluded = (y_test_excluded != mlp_predictions_excluded).sum()

print("\nTask 6: Number of instances incorrectly classified without 'Height' and 'Weight':")
print("Logistic Regression:", incorrect_lr_excluded)
print("Support Vector Machines:", incorrect_svm_excluded)
print("Multilayer Perceptron:", incorrect_mlp_excluded)

#  Explanation for any change in the results
# The exclusion of 'Height' and 'Weight' might lead to a change in the results, as these attributes were assumed to be powerful.
# If the accuracy or incorrect classifications change significantly, it suggests that these attributes were indeed influential in the prediction task.
