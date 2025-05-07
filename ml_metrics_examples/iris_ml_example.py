from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

"""
This program imports specific modules from the sklearn library to demonstrate a simple DecisionTreeClassifier (Classification ML model),
uses the imported dataset "load_iris" as its data source, and performs a simple machine learning model training process to compare the
test dataset to the model's prediction.

Expected output is a simple string reporting the model's level of accuracy. (example: >>> "Accuracy: 1.0")

Noted possible issue(s):
 - Depending on the user's IDE, the sklearn library may not import correctly
  -- Fix: install sklearn "locally" using "pip install -U scikit-learn"
  -- Suggested: create a virtual enviornment (venv) and install scikit-learn sequentially using the following commands:
     "python -m venv sklearn-env
      sklearn-env\Scripts\activate  # activate
      pip install -U scikit-learn"
"""


# Load iris dataset
iris = load_iris()
x = iris.data
y = iris.target

# Splir dataset in training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=42)

# Decision Tree Classifier
clf = DecisionTreeClassifier()

# Train Classifier
clf.fit(x_train, y_train)

# Make test set predictions
y_pred = clf.predict(x_test)

# Model's accuracy evaluation score(s)
accuracy = accuracy_score(y_test, y_pred)
print('Accuracy:', accuracy)