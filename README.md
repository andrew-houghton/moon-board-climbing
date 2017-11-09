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

## Processing Data

Use mod.py, then remove_outliers.py, then padded_climbs.py to get dataset.

Then process in the LSTM to get climbs_out.txt.

Use decode_all_climbs.py to decode the climbs. Select the climb you want and use sendClimbData.py to send it to the server.

## Image Upload

### LSTM

To upload a set of LSTM samples which have been saved in the climb_text folder run 

```python decode_all_climbs.py```

This script loads the climbs, converts them from neural network format to moon board format and sends them to the moonboard site using a POST request.
Please make sure that you are careful not to upload too much because you cannot delete climbs once they are uploaded.

It is a good idea to **check the climbs are valid before you send them and check how many you will send first**.
