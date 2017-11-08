# Generating rock climbs for the Moon Board

Using Neural Networks to generate new rock climbs for the moon board.

## Details

An [LSTM](https://github.com/karpathy/char-rnn) and [HyperGAN](https://github.com/255BITS/HyperGAN) were used to generate new climbs.

In order to collect the training dataset a small python script to send POST requests was used.
This collected 13000 climbs as json objects.
These were processed and converted into .png files and strings before they were sent to the neural networks for training.

**Example Climb:**

G2,J7,J8,D8,D10,A5,A13,F6,D16,C18_13

## Training Models

### Character based LSTM

**Training;**

To train the model run the command

```python train.py --data_dir data/climbs/```

**Sampling;**

To get new climbs from the model run the command

```python sample.py```
