## Setup

1. Clone the repo
2. Install python dependencies by running:

`virtualenv -p python3 venv`

`source venv/bin/activate`

`pip install -r requirements.txt`

3. Run setup script

`python setup.py`

## Model Training

### LSTM

1. Complete setup.
2. Train LSTM

`python training_utils/train_LSTM.py`

3. Sample LSTM

`python sampling_utils/sample_LSTM.py`

### HyperGAN

1. Compete setup.
2. `hypergan new mymodel`
3. Start the model training. Ideally use a GPU for this. I don't have one so I just used my laptop cpu for a couple of hours.

`hypergan train data/images/ -s 18x18 -f png -c mymodel`

4. 

<!-- ### File system description.

* The data folder holds data files such as .txt or .json files.
* The tests folder holds unit tests which are used the check the qulity of code written.
* The types folder holds the files which define the types used in this project. Climbs are stored as instances of the 'Climb' class within the project.
* The util folder holds files which can be run to perform changes and data processing tasks mostly.
 -->