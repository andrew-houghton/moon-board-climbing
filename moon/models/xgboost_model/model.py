import xgboost as xgb

from moon.models.base_model import GradingModel


class Model(GradingModel):
    def name(self):
        return "XGBoost"

    def train(self, x_train, y_train):
        self.model = xgb.XGBClassifier(
            objective="multi:softprob", random_state=42
        )
        print("Training")
        print(f"{x_train.shape}")
        print(f"{y_train.shape}")
        self.model.fit(x_train, y_train)
        print("Finished training")

    def sample(self, x):
        return self.model.predict(x)
