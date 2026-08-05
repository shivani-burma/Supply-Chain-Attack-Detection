import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from imblearn.over_sampling import SMOTE

# Load dataset
df = pd.read_csv(
    "data/enhanced_final_detection_dataset.csv"
)

# Features used in final model
features = [
    "NameLength",
    "SummaryLength",
    "ReleaseCount",
    "PackageAgeDays"
]

X = df[features]
y = df["Label"]

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

X_train_balanced = X_train
y_train_balanced = y_train

# Train Decision Tree
model = DecisionTreeClassifier(
    random_state=42
)

model.fit(
    X_train_balanced,
    y_train_balanced
)

# Save model
joblib.dump(
    model,
    "models/best_supply_chain_model.pkl"
)

print("Model saved successfully.")