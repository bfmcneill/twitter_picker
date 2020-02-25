# Purpose:
- Feed a csv of twitter handles to the machine - get back a random selection


# Setup
1. clone repo
2. create virtual environment (on linux: ```make setup```)
3. activate virtual environment
4. update pip & setuptools & install requirements.txt (on linux: ```make install```)





## Usage-Exmaple 1
```bash
twpicker
```
***output***
```bash
Usage: twpicker [OPTIONS] COMMAND [ARGS]...

  Main Entrypoint

Options:
  --help  Show this message and exit.

Commands:
  random-choices  Make random choices
```

## Usage-Example 2
```bash
twpicker random-choices --help
```
***output***
```bash
Usage: twpicker random-choices [OPTIONS]

  Make random choices

Options:
  -i, --filepath PATH     specify the file path containing list of handles
                          [default: /c/src/twitter_picker/handles.csv]
  -n, --n-select INTEGER  Specify how many selections to make  [default: 5;
                          required]
  --help                  Show this message and exit.
```





# version history

## 0.0.2
 - changed structure to split cli from twitter picker package, removed the need for if name == "main"
 - command option added for user to specify path to CSV, defaults to handles.csv in project root
 - command option added for user to specify number or random choices, defaults to 5
 - removed redundant comments, added basic function doc strings
 - removed create_message, created a constant interpolated by format
 - removed print_results, changed functionality to a list comprehension that click.echo handles
 - removed map, replaced with list comprehension
 - added setup.py, shifted from pipenv to pip with requirements.txt

## 0.0.1
- basic cli
- see version 0.0.1 in action on a [live stream](https://youtu.be/XomBuBHhfhg?t=512)

# help wanted
- push the csv data into a set before making random selection to ensure one entry per handle
- allow user to specify if source file has a header or not
- detect if the calling environment can handle emojis - we want emojis in the message!!!