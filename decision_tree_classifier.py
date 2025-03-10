# -*- coding: utf-8 -*-
"""decision tree classifier

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mj1orTVfKoBDjglI6M5WlMn-DdG2042q
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
#import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score
# import accuracy score
import matplotlib.pyplot as plt

# Load the dataset
data=pd.read_csv("/content/iris.csv")

# Separate features(X) and target variable(Y)
X=data.drop("species",axis=1)
# Assuming species is the target variable
Y=data["species"]

# Split data into training and test datasets
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2, random_state=42)

# Initialize and train the Decision tree classifier
model=DecisionTreeClassifier(random_state=42)
# We can add parameters like depth
model.fit(X_train,Y_train)

# Make predictions on the test set
Y_pred=model.predict(X_test)

# Evaluate the model
accuracy=accuracy_score(Y_test,Y_pred)
print(f"Accuracy:{accuracy:.4f}")

# Plot the Decision Tree
# Plot the Decision Tree
plt.figure(figsize=(12,8))
# Adjust the figure size if needed
plot_tree(model,feature_names=X.columns, class_names=model.classes_, filled=True, rounded=True)
plt.show()