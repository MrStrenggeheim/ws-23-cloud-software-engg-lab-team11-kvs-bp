# Key-Value Storage Basic Exercise

Get familiar with the key-value storage concept using [sqlitedict](https://pypi.org/project/sqlitedict/)

## Introduction

In this basic exercise, students are asked to implement `FileFolder` - file folder with limitted storage space. The folder supports basic [CRUD operations](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete) such as `get`, `put`, `remove` and `list`

## Exercise Structure

- `example.py`: A quick start into few core operations supported in `sqlitedict`
- `filefolder.py`: Implementation of file folder `FileFolder`
- `/test`: Testsuits for the file folder implementation
- `main.py`: A simple usage scenario of file folder

## Setup & Installation

In order to work with this exercise, you need to install Python on your machine. More information how to install and setup Python can be found [here](https://www.python.org/)

Once Python is installed on your machine, install the requirements for the exercise by running the following command in the exercise directory `pip install -r requirements.txt`

**Optional**: If you want to have separated working environment, you can setup the virtual environment (more [details](https://docs.python.org/3/library/venv.html))

## Execution commands

In the exercise directory `/basic`

- Run the example: `python example.py`
- Run the testsuits: `python -m unittest test/test_filefolder_1.py test/test_filefolder_2.py`
