
from moon.models.base_model import BaseModel
from sklearn.model_selection import train_test_split
import moon.utils.load_data as load_data
import numpy as np

from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification


data = load_data.numpy()
x_train, x_test, y_train, y_test = train_test_split(
    np.reshape(data['climbs'], (len(data['climbs']), 18*18)).astype(int),
    data['grades'],
    test_size=0.2,
    random_state=42
)

clf = RandomForestClassifier(
    n_estimators=100,
    max_depth=200,
    random_state=0
)

clf.fit(x_train, y_train)

RandomForestClassifier(bootstrap=True, class_weight=None, criterion='gini',
            max_depth=2, max_features='auto', max_leaf_nodes=None,
            min_impurity_decrease=0.0, min_impurity_split=None,
            min_samples_leaf=1, min_samples_split=2,
            min_weight_fraction_leaf=0.0, n_estimators=100, n_jobs=None,
            oob_score=False, random_state=0, verbose=0, warm_start=False)

print(clf.score(x_train, y_train))
print(clf.score(x_test, y_test))
