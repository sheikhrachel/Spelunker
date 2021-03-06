# Spelunker

Spelunker is a tool that will parse through your codebase and automatically generate mocks in a test folder

![alt text](img/logo.png "Logo")

## Features
- Autogenerates a 'test' folder if one does not exist

- Skips over functions that have 'spelunker_skip' above the definition

- Generates individual mock files with corresponding test methods (currently only supporting the requests library)

![alt text](img/demo_file.png "Input File")
![alt text](img/demo_output2.png "Output File")

## Prerequisites

Ensure you are running a Python version >= 3.6

```zsh
$ python3 --version # returns 'Python 3.7.7' or a version >= 'Python 3.6'
```

## Usage

Run in terminal from the file (I will eventually publish this project up to pip for install/run directly)

```zsh
$ python3 [PATH TO SPELUNKER DIR]/src/Spelunker.py
```

## Contact Info

```python
self.name = 'Rachel Sheikh'
self.email = 'sheikhrachel97@gmail.com'
self.site = 'https://rachel-sheikh.com'
```
