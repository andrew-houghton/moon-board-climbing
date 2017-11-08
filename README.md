# Generating rock climbs for the Moon Board

Using Neural Networks to generate new rock climbs for the moon board.

## Details

An [LSTM](https://github.com/karpathy/char-rnn) and [HyperGAN](https://github.com/255BITS/HyperGAN) were used to generate new climbs.

In order to collect the training dataset a small python script to send POST requests was used.
This collected 13000 climbs as json objects.
These were processed and converted into .png files and strings before they were sent to the neural networks for training.

**Example Climb:**

```KeGhFjIlHpKr______________2```

## Training Models

### Character based LSTM

**Training;**

To train the model run the command

```python train.py --data_dir data/climbs/```

You can view training progress by launching tensorboard and visiting the [TensorBoard Dashboard](http://localhost:6006/).

```tensorboard --logdir=./logs/```

**Sampling;**

To get new climbs from the model run the command.

```python sample.py -n 2000 --prime '|' > ../climb_text/climbs_out.txt```

This example gets 2800 characters worth of climbs, which is 100 climbs. They are saved to the file climbs_out.txt
