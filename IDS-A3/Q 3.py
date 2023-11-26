import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score, LeavePOut
from sklearn.metrics import make_scorer, f1_score
from google.colab import files

# Upload the dataset (gender-prediction.csv) to Colab
uploaded = files.upload()

# Load the dataset
df = pd.read_csv("gender-prediction.csv")

# Convert categorical variables to numerical
df['beard'] = df['beard'].map({'yes': 1, 'no': 0})
df['hair_length'] = df['hair_length'].map({'bald': 0, 'short': 1, 'medium': 2, 'long': 3})
df['scarf'] = df['scarf'].map({'yes': 1, 'no': 0})
df['eye_color'] = df['eye_color'].astype('category').cat.codes  # Convert categorical eye_color to numerical

# Split the dataset into features and target variable
X = df.drop('gender', axis=1)
y = df['gender']

# Initialize the Random Forest classifier with adjusted parameters
rf_classifier = RandomForestClassifier(n_estimators=50, max_depth=10, random_state=42)

# Monte Carlo cross-validation
num_iterations = 5
monte_carlo_scores = cross_val_score(rf_classifier, X, y, cv=num_iterations, scoring=make_scorer(f1_score, average='weighted'))

# Leave P-Out cross-validation
p_out = 3
leave_p_out = LeavePOut(p=p_out)
leave_p_out_scores = cross_val_score(rf_classifier, X, y, cv=leave_p_out, scoring=make_scorer(f1_score, average='weighted'))

# Report F1 scores for both cross-validation strategies
print(f"Monte Carlo Cross-Validation F1 Scores: {monte_carlo_scores.mean()}")
print(f"Leave P-Out Cross-Validation F1 Scores: {leave_p_out_scores.mean()}")
