from sklearn.ensemble import RandomForestClassifier

from moon.models.base_model import GradingModel


class Model(GradingModel):
    def name(self):
        return "Random Forest"

    def train(self, x_train, y_train):
        self.model = RandomForestClassifier(
            n_estimators=20, max_depth=70, random_state=0
        )
        print("Training")
        self.model.fit(x_train, y_train)
        print("Finished training")

    def sample(self, x):
        return self.model.predict(x)
