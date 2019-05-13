import moon.utils.load_data as load_data
import numpy as np
from moon.models.base_model import BaseModel
from sklearn.metrics import accuracy_score, auc, confusion_matrix, mean_squared_error
from sklearn.model_selection import train_test_split

import xgboost as xgb

data = load_data.numpy()
x_train, x_test, y_train, y_test = train_test_split(
    np.reshape(data["climbs"], (len(data["climbs"]), 18 * 18)).astype(int),
    data["grades"],
    test_size=0.2,
    random_state=42,
)

xgb_model = xgb.XGBClassifier(objective="multi:softprob", random_state=42)
xgb_model.fit(x_train, y_train)

y_pred = xgb_model.predict(x_test)

print(accuracy_score(y_test, y_pred))
print(mean_squared_error(y_test, y_pred))
