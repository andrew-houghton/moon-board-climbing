# Moon Board Climbing

### What is it?

It's a way to create new climbs for the [moon board](https://www.moonboard.com/) and grade climbs using machine learning!

## Setup

1. Clone the repo
2. Install python dependencies by running:
```sh
virtualenv -p python3.7 venv
source venv/bin/activate
pip install -r requirements.txt
```
3. Add the project directory to the PYTHONPATH so that imports work
```sh
export PYTHONPATH=$(pwd)
```
Note: On Windows set `PythonPath` environment variable to the project folder. [See Instructions here](https://www.codingdefined.com/2015/09/how-to-set-up-pythonpath-in-windows-10.html)


## Automatic Climb Grading
#### Instructions
Run the grading script
```sh
python moon/analytics/configuration.py
```
**Expected output**
```
Using TensorFlow backend.
Generated 22 configruations.
Training Configuration: XGBoost         Climbset=2016 X=Flanders      Y=Flanders       Trained in 7.56s
Training Configuration: Random Forest   Climbset=2016 X=Flanders      Y=Flanders       Trained in 2.02s
Training Configuration: Keras LSTM      Climbset=2016 X=Categorical   Y=Categorical    Trained in 33.34s
Training Configuration: Keras MLP       Climbset=2016 X=Categorical   Y=Categorical    Trained in 6.01s
Training Configuration: Random Forest   Climbset=2016 X=Categorical   Y=Categorical    Trained in 4.44s
Training Configuration: Keras LSTM      Climbset=2016 X=Split         Y=Split          Trained in 33.23s
Training Configuration: Keras MLP       Climbset=2016 X=Split         Y=Split          Trained in 5.60s
Training Configuration: Random Forest   Climbset=2016 X=Split         Y=Split          Trained in 1.64s
Training Configuration: Keras LSTM      Climbset=2016 X=HalfGrade     Y=HalfGrade      Trained in 30.87s
Training Configuration: Keras MLP       Climbset=2016 X=HalfGrade     Y=HalfGrade      Trained in 6.37s
Training Configuration: Random Forest   Climbset=2016 X=HalfGrade     Y=HalfGrade      Trained in 2.89s
Training Configuration: XGBoost         Climbset=2017 X=Flanders      Y=Flanders       Trained in 12.60s
Training Configuration: Random Forest   Climbset=2017 X=Flanders      Y=Flanders       Trained in 3.21s
Training Configuration: Keras LSTM      Climbset=2017 X=Categorical   Y=Categorical    Trained in 43.92s
Training Configuration: Keras MLP       Climbset=2017 X=Categorical   Y=Categorical    Trained in 8.62s
Training Configuration: Random Forest   Climbset=2017 X=Categorical   Y=Categorical    Trained in 6.80s
Training Configuration: Keras LSTM      Climbset=2017 X=Split         Y=Split          Trained in 47.07s
Training Configuration: Keras MLP       Climbset=2017 X=Split         Y=Split          Trained in 8.16s
Training Configuration: Random Forest   Climbset=2017 X=Split         Y=Split          Trained in 2.68s
Training Configuration: Keras LSTM      Climbset=2017 X=HalfGrade     Y=HalfGrade      Trained in 47.11s
Training Configuration: Keras MLP       Climbset=2017 X=HalfGrade     Y=HalfGrade      Trained in 8.49s
Training Configuration: Random Forest   Climbset=2017 X=HalfGrade     Y=HalfGrade      Trained in 4.69s

Climbset Model                Climb Preprocessing  Grade Preprocessing  Test Accuracy        Train Accuracy
2016      XGBoost              OneHot               Flanders             0.342                0.4
2016      Random Forest        OneHot               Flanders             0.366                0.999
2016      Keras LSTM           HoldList             Categorical          0.299                0.312
2016      Keras MLP            OneHot               Categorical          0.354                0.445
2016      Random Forest        OneHot               Categorical          0.165                0.999
2016      Keras LSTM           HoldList             Split                0.64                 0.643
2016      Keras MLP            OneHot               Split                0.769                0.848
2016      Random Forest        OneHot               Split                0.77                 1.0
2016      Keras LSTM           HoldList             HalfGrade            0.336                0.357
2016      Keras MLP            OneHot               HalfGrade            0.479                0.561
2016      Random Forest        OneHot               HalfGrade            0.197                0.999
2017      XGBoost              OneHot               Flanders             0.331                0.363
2017      Random Forest        OneHot               Flanders             0.339                0.997
2017      Keras LSTM           HoldList             Categorical          0.248                0.232
2017      Keras MLP            OneHot               Categorical          0.35                 0.428
2017      Random Forest        OneHot               Categorical          0.133                0.996
2017      Keras LSTM           HoldList             Split                0.619                0.626
2017      Keras MLP            OneHot               Split                0.791                0.878
2017      Random Forest        OneHot               Split                0.786                0.999
2017      Keras LSTM           HoldList             HalfGrade            0.284                0.276
2017      Keras MLP            OneHot               HalfGrade            0.468                0.566
2017      Random Forest        OneHot               HalfGrade            0.183                0.997
```

#### Models

* [XGBoost](https://xgboost.readthedocs.io/en/latest)
* [Keras](https://keras.io/) - Multi layer percepetron
* [Keras](https://keras.io/) - LSTM
* [Scikit-learn Random Forest](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html)

## Creating new climbs
#### Instructions
1. Run the climb generation script.
```sh
python moon/generate/generate_for_website.py
```
2. If you want to grade the climbs which were generated run the grading script.
```sh
python moon/generate/grade_for_website.py
```

#### Climb Generation Models

* [Keras](https://keras.io/) - LSTM
* https://github.com/sherjilozair/char-rnn-tensorflow - not working in with current version
* https://github.com/255BITS/HyperGAN - not working in with current version

## Website

The `website-moon` directory holds the https://ahoughton.com/moon website. See the [README](website-moon/README.md) for details.
