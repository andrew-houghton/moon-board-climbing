# Moon Board Climbing

### What is it?

It's a way to create new climbs for the [moon board](https://www.moonboard.com/) and grade climbs using machine learning!

## Automatic Climb Grading
### Setup

1. Clone the repo
2. Install python dependencies by running:
```sh
virtualenv -p python3.7 venv
source venv/bin/activate
pip install -r requirements.txt
```
3. Run the grading script
```sh
python moon/analytics/configuration.py
```
**Expected output**
```
Using TensorFlow backend.
Generated 16 configruations.
Training Configuration: XGBoost         Climbset=2016 X=Flanders      Y=Flanders       Trained in 7.48s
Training Configuration: Random Forest   Climbset=2016 X=Flanders      Y=Flanders       Trained in 1.98s
Training Configuration: Keras LSTM      Climbset=2016 X=Categorical   Y=Categorical    Trained in 32.03s
Training Configuration: Keras MLP       Climbset=2016 X=Categorical   Y=Categorical    Trained in 5.91s
Training Configuration: Random Forest   Climbset=2016 X=Categorical   Y=Categorical    Trained in 4.18s
Training Configuration: Keras LSTM      Climbset=2016 X=Split         Y=Split          Trained in 31.11s
Training Configuration: Keras MLP       Climbset=2016 X=Split         Y=Split          Trained in 5.59s
Training Configuration: Random Forest   Climbset=2016 X=Split         Y=Split          Trained in 1.66s
Training Configuration: XGBoost         Climbset=2017 X=Flanders      Y=Flanders       Trained in 8.59s
Training Configuration: Random Forest   Climbset=2017 X=Flanders      Y=Flanders       Trained in 3.23s
Training Configuration: Keras LSTM      Climbset=2017 X=Categorical   Y=Categorical    Trained in 44.59s
Training Configuration: Keras MLP       Climbset=2017 X=Categorical   Y=Categorical    Trained in 8.46s
Training Configuration: Random Forest   Climbset=2017 X=Categorical   Y=Categorical    Trained in 6.57s
Training Configuration: Keras LSTM      Climbset=2017 X=Split         Y=Split          Trained in 43.94s
Training Configuration: Keras MLP       Climbset=2017 X=Split         Y=Split          Trained in 7.94s
Training Configuration: Random Forest   Climbset=2017 X=Split         Y=Split          Trained in 2.71s

Climbset Model                Climb Preprocessing  Grade Preprocessing  Test Accuracy        Train Accuracy
2016      XGBoost              OneHot               Flanders             0.342                0.4
2016      Random Forest        OneHot               Flanders             0.366                0.999
2016      Keras LSTM           HoldList             Categorical          0.299                0.312
2016      Keras MLP            OneHot               Categorical          0.349                0.443
2016      Random Forest        OneHot               Categorical          0.165                0.999
2016      Keras LSTM           HoldList             Split                0.649                0.65
2016      Keras MLP            OneHot               Split                0.771                0.847
2016      Random Forest        OneHot               Split                0.77                 1.0
2017      XGBoost              OneHot               Flanders             0.331                0.363
2017      Random Forest        OneHot               Flanders             0.339                0.997
2017      Keras LSTM           HoldList             Categorical          0.248                0.233
2017      Keras MLP            OneHot               Categorical          0.354                0.42
2017      Random Forest        OneHot               Categorical          0.133                0.996
2017      Keras LSTM           HoldList             Split                0.568                0.572
2017      Keras MLP            OneHot               Split                0.803                0.877
2017      Random Forest        OneHot               Split                0.786                0.999
```

### Models

* [XGBoost](https://xgboost.readthedocs.io/en/latest)
* [Keras](https://keras.io/) - Multi layer percepetron
* [Keras](https://keras.io/) - LSTM
* [Scikit-learn Random Forest](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html)

## Creating new climbs

TODO - documentation

### Climb Generation Models

* https://github.com/sherjilozair/char-rnn-tensorflow
* https://github.com/255BITS/HyperGAN
