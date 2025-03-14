# Predefined code templates
def get_code_template():
    return {
        "Data Analysis (Python with pandas)": """import pandas as pd
# Read the CSV file
data = pd.read_csv('data.csv')
# Data analysis code here
print(data.head())""",

        "Web Development (HTML)": """<!DOCTYPE html>
<html>
<head>
    <title>Sample Page</title>
</head>
<body>
    <h1>Hello, World!</h1>
</body>
</html>""",

        "Machine Learning (Python)": """from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
# Load dataset
data = # Load your dataset
X = data.drop('target', axis=1)
y = data['target']
# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# Initialize model
model = RandomForestClassifier()
model.fit(X_train, y_train)
# Evaluate model
print(model.score(X_test, y_test))""",

        "API Request (Python)": """import requests
response = requests.get('https://api.openweathermap.org/data/2.5/weather?q=London&appid=YOUR_API_KEY')
print(response.json())"""
    }
