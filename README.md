## What is it?

It's a way to create new climbs for the [moon board](https://www.moonboard.com/) and grade climbs using machine learning!

## Automatic Grading
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

<!-- 
## Creating new climbs
### Setup

1. Clone the repo
2. Install python dependencies by running:
```sh
virtualenv -p python3.7 venv
source venv/bin/activate
pip install -r requirements-generate.txt
```
 -->

### Climb Generation Models

* https://github.com/sherjilozair/char-rnn-tensorflow
* https://github.com/255BITS/HyperGAN
