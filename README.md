# Analysis

Simple statistical analysis from Go-Stop Data.

# Environment setup

```sh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

You should also configure the .env file with the DB username and password.

# Running Statistical tests

If you want to only run tests from python files `file1.py` and `file2.py` (as an
example), then run

```
./analyze.py file1 file2
```

If all tests should be run, execute

```sh
./analyze.py --all
```
