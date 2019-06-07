import numpy as np
from sklearn.metrics import accuracy_score, mean_squared_error

from moon.analytics.metrics import expected_diff
from moon.models import keras_lstm_grade, keras_mlp, random_forest, xgboost


def evaluate(model_name, values):
    x_test, y_test, predictions = values

    if len(predictions.shape) == 2:
        predictions = np.argmax(predictions, axis=1)

    diff = expected_diff(y_test, predictions)
    accuracy = accuracy_score(y_test, predictions)
    mse = mean_squared_error(y_test, predictions)

    print(
        f"""
Scores for {model_name}:
Accuracy            {100*accuracy:.2f}%
Expected Diff       {diff:.3f}
Mean Squared Error  {mse:.3f}"""
    )


models = {
    "keras multi layer percepetron": keras_mlp.Model(),
    "xgboost": xgboost.Model(),
    "random forest": random_forest.Model(),
    "keras lstm": keras_lstm_grade.Model(),
}

samples = {k: v.load_sample() for k, v in models.items()}
for model_name, values in samples.items():
    evaluate(model_name, values)
