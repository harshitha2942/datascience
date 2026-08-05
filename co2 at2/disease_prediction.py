# ============================================
# Disease Prediction System using Decision Tree
# ============================================

# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# --------------------------------------------
# Load Dataset
# --------------------------------------------
data = pd.read_csv("patient_data.csv")

print("\n========== DATASET ==========\n")
print(data)

# --------------------------------------------
# Check Dataset Information
# --------------------------------------------
print("\n========== DATA INFORMATION ==========\n")
print(data.info())

print("\n========== MISSING VALUES ==========\n")
print(data.isnull().sum())

# --------------------------------------------
# Separate Features and Target
# --------------------------------------------
X = data[['Age', 'BloodPressure', 'SugarLevel', 'Cholesterol']]
y = data['Disease']

# --------------------------------------------
# Split Dataset
# --------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# --------------------------------------------
# Train Decision Tree Model
# --------------------------------------------
model = DecisionTreeClassifier(random_state=42)

model.fit(X_train, y_train)

# --------------------------------------------
# Prediction
# --------------------------------------------
y_pred = model.predict(X_test)

# --------------------------------------------
# Accuracy
# --------------------------------------------
accuracy = accuracy_score(y_test, y_pred)

print("\n========== RESULTS ==========\n")
print("Accuracy :", round(accuracy * 100, 2), "%")

print("\nClassification Report\n")
print(classification_report(y_test, y_pred))

# --------------------------------------------
# Confusion Matrix
# --------------------------------------------
cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(5,4))
sns.heatmap(cm,
            annot=True,
            fmt='d',
            cmap='Blues')

plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

# --------------------------------------------
# Disease Prediction for New Patient
# --------------------------------------------
print("\n===================================")
print("   DISEASE PREDICTION SYSTEM")
print("===================================")

age = int(input("Enter Age : "))
bp = int(input("Enter Blood Pressure : "))
sugar = int(input("Enter Sugar Level : "))
chol = int(input("Enter Cholesterol : "))

new_patient = np.array([[age, bp, sugar, chol]])

prediction = model.predict(new_patient)

print("\n========== PREDICTION ==========\n")

if prediction[0] == 1:
    print("Disease Detected")
else:
    print("No Disease Detected")

# --------------------------------------------
# Predict Probability (Optional)
# --------------------------------------------
probability = model.predict_proba(new_patient)

print("\nPrediction Probability")
print("No Disease :", round(probability[0][0] * 100, 2), "%")
print("Disease    :", round(probability[0][1] * 100, 2), "%")