from sklearn.ensemble import RandomForestClassifier


class Model:
    def name(self):
        return "Random Forest"

    def train(self, x_train, y_train):
        self.model = RandomForestClassifier(n_estimators=100, max_depth=200, random_state=0)
        self.model.fit(x_train, y_train)

    def sample(self, x):
        return self.model.predict(x)
