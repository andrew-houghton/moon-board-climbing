import xgboost as xgb


class Model:
    def name(self):
        return "XGBoost"

    def train(self, x_train, y_train):
        self.model = xgb.XGBClassifier(objective="multi:softprob", random_state=42, nthread=-1)
        self.model.fit(x_train, y_train)

    def sample(self, x):
        return self.model.predict(x)
