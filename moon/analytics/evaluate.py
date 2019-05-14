import numpy as np
from moon.analytics.metrics import expected_diff
from moon.models import keras_mlp, random_forest
from sklearn.metrics import accuracy_score, auc, confusion_matrix, mean_squared_error


def evaluate(model_name, values):
    x_test, y_test, predictions = values

    if len(predictions.shape) == 2:
        predictions = np.argmax(predictions, axis=1)

    diff = expected_diff(y_test, predictions)
    accuracy = accuracy_score(y_test, predictions)
    mse = mean_squared_error(y_test, predictions)

    print(
        f"""Scores for {model_name}\nAccuracy            {accuracy}\nExpected Diff       {diff}\nMean Squared Error  {mse}"""
    )


models = {"keras multi layer percepetron": keras_mlp.Model(), "random forest": random_forest.Model()}

samples = {k: v.load_sample() for k, v in models.items()}
for model_name, values in samples.items():
    evaluate(model_name, values)
