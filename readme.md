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
2. Install the hypergan package (https://github.com/255BITS/HyperGAN)
3. `hypergan new mymodel`
4. Start the model training. Ideally use a GPU for this. I don't have one so I just used my laptop cpu for a couple of hours.

`hypergan train data/images/ -s 18x18 -f png -c mymodel`

5.

`TODO insert sampling command here` 

### File system description.

* The training_utils, and sampling_utils folder holds files which can be run to perform changes and data processing tasks mostly, and call for the model to be trained.
* The models folder holds the code for the neural nets which I use. They've just been tweaked so they can be called by my methods buy I haven't changed them too much.

## Models used

I've used `https://github.com/sherjilozair/char-rnn-tensorflow` and `https://github.com/255BITS/HyperGAN` for the models.
