## How to generate climbs

1. Clone the repo
2. Install python dependencies by running:

    `virtualenv -p python3 venv`

    `source venv/bin/activate`

    `pip install -r requirements.txt`

3. Run setup script

    `python setup.py`

4. Train LSTM

    `python training_utils/train_LSTM.py`

5. Sample LSTM

    `python sampling_utils/sample_LSTM.py`

### File system description.

* The data for training the models
* The tests folder holds unit tests which are used the check the qulity of code written.
* The types folder holds the files which define the types used in this project. Climbs are stored as instances of the 'Climb' class within the project.
* The training_utils, and sampling_utils folder holds files which can be run to perform changes and data processing tasks mostly, and call for the model to be trained.
* The models folder holds the code for the neural nets which I use. They've just been tweaked so they can be called by my methods buy I haven't changed them too much.

## Models used

I've used `https://github.com/sherjilozair/char-rnn-tensorflow` and `https://github.com/255BITS/HyperGAN` for the models.
