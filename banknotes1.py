import csv
import random

from sklearn import svm
from sklearn.linear_model import Perceptron
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier

model = Perceptron()
# model = svm.SVC()
# model = KNeighborsClassifier(n_neighbors=1)
# model = GaussianNB()


with open("banknotes.csv") as f:
    reader = csv.reader(f)
    next(reader)

    data = []
    for row in reader:
        data.append({
            "evidence": [float(cell) for cell in row[:4]],
            "label": "Authentic" if row[4] == "0" else "Counterfeit"
        })


evidence = [row["evidence"] for row in data]
labels = [row["label"] for row in data]

X_training, X_testing, y_training, y_testing = train_test_split(
    evidence, labels, test_size=0.4
)


model.fit(X_training, y_training)


predictions = model.predict(X_testing)


correct = (y_testing == predictions).sum()
incorrect = (y_testing != predictions).sum()
total = len(predictions)


print(f"Results for model {type(model).__name__}")
print(f"Correct: {correct}")
print(f"Incorrect: {incorrect}")
print(f"Accuracy: {100 * correct / total:.2f}%")
