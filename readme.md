### File system description.

* The data folder holds data files such as .txt or .json files.
* The tests folder holds unit tests which are used the check the qulity of code written.
* The types folder holds the files which define the types used in this project. Climbs are stored as instances of the 'Climb' class within the project.
* The util folder holds files which can be run to perform changes and data processing tasks mostly.

### Steps to create new climbs

1. Clone the repo.
2. Setup python environment and install dependencies from `requirements.txt` file.
3. Run `training_utils/prep_LSTM_datasets.py` to create strings for LSTM model.
3. Run `training_utils/train_LSTM.py` to create strings for LSTM model.
4. Run `sampling_utils/sample_LSTM.py` to generate climbs from trained model LSTM.
