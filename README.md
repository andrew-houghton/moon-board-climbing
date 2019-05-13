## What is it?

It's a way to create new climbs for the [moon board](https://www.moonboard.com/) and grade climbs using machine learning!

## Setup

1. Clone the repo
2. Install python dependencies by running:

```sh
virtualenv -p python3 venv
source venv/bin/activate
pip install .
```

## Climb Generation Models

### LSTM

1. Complete setup.
2. Train LSTM

`python training_utils/train_LSTM.py`

3. Sample LSTM

`python sampling_utils/sample_LSTM.py`

A new window will open up. Play around and look at the climbs.

<img src="climb_viewer/Ui.png" width="400">

https://github.com/sherjilozair/char-rnn-tensorflow

### HyperGAN

1. Compete setup.
2. Install the hypergan package (https://github.com/255BITS/HyperGAN)
3. `hypergan new mymodel`
4. Start the model training. Ideally use a GPU for this. I don't have one so I just used my laptop cpu for a couple of hours.

`hypergan train data/images/ -s 18x18 -f png -c mymodel`

5. `TODO insert sampling command here` 

Hypergn will generate new samples. Eg.

![Hypergan sample](https://github.com/andrew-houghton/moon-board-climbing/blob/master/climb_viewer/temp.png)

https://github.com/255BITS/HyperGAN

## Climb Grading Models

todo
