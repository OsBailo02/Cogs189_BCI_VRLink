# Getting Started with Neurosky Mindwave Python EEG Recording

## Make sure you are in the neurosky-template directory:

### `python --version`

Make sure it's 3.0 and above

### `python3 -m venv env`

Creates a virtual environment so you can install the packages locally (optional)

### `source env/bin/activate`

Switches to the virtual environment you just created (optional)

### `deactivate`

Switches back to your default python environment (optional)

### `pip install -r requirements.txt`

Install all the required packages

### `python neurosky.py`

Starts the script

## First time you run the script, it will create a "config.json" file

These would be read by neurosky.py and turn into constants.

`MODE` can be `'full'`, `'online'`, or `'offline'`. `'full'` would be running the entire experiment. `'online'` would skip data collection or model training if either already exists, `'offline'` will just run the offline session and stops once the data is collected.

`TRIAL_DURATION` is how long each trial lasts in ms.

`INTER_TRIAL_INTERVAL` is the time between each trial in ms.

`SESSION_NUMBER` and `SUBJECT_NUMBER` is what you need to fill out when you collect your offline data. The data you collect would be saved under `SUBJECT_NUMBER/SESSION_NUMBER`

`TARGETS` maps trial type number to the verbal description

## Known Bug
The installation process for psychopy can be tricky because it has tons of dependencies, and the fact conda can't even find psychopy doesn't help either. So if you encounter obstacles when installing, you can install miniconda and swictch between pip and conda install the failed packages until all or most of the dependencies for psychopy are installed. Then you can try to run `pip install psychopy --no-deps` to see what packages are actually required when running `python neurosky.py`. Just keep installing those packages until the window pops up.

The psychopy window for EEG data collection does not close after the session is over if you're running it on a mac. It would only close when the code itself terminates or when you Ctrl-C out of the script in the terminal. You can choose a different GUI app or frontend or break this file up into multiple files and use multithreading.

