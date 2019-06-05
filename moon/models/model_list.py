from moon.models import (
    keras_mlp as keras_mlp,
    keras_lstm_grade as keras_lstm_grade,
    random_forest as random_forest,
    xgboost_model as xgboost_model,
)

grading = [
    keras_mlp.Model,
    keras_lstm_grade.Model,
    random_forest.Model,
    xgboost_model.Model,
]

if __name__ == "__main__":
    for m in grading:
        m().train()
