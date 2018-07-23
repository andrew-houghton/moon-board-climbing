## How to generate climbs

1. Clone the repo
2. Install python dependencies.

    Run:
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

* The data folder holds data files such as .txt or .json files.
* The tests folder holds unit tests which are used the check the qulity of code written.
* The types folder holds the files which define the types used in this project. Climbs are stored as instances of the 'Climb' class within the project.
* The util folder holds files which can be run to perform changes and data processing tasks mostly.
