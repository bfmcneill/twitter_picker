import os
import random
import csv

NUMBER_OF_CHOICES = 5

def load_handles(csv_file_path):
    with open(csv_file_path) as fin:
        csv_reader = csv.reader(fin)  # list of lists [[col1, col2, col3],[col1, col2, col3]]
        return [
            handle[0] 
            for handle in csv_reader 
            if handle[0][0]=='@'
        ]    # returns a list


def make_selection(population, choice_count):
    return random.sample(population, k=choice_count)  # returns a list of random selection


def print_results(messages):    
    [
        print(msg) 
        for msg in messages
    ]


def create_message(handle):
    return f'--> {handle} has been selected'


def main():
    csv_filepath = os.path.join('.','handles.csv')
    handles = load_handles(csv_filepath)
    selection = make_selection(handles, choice_count=NUMBER_OF_CHOICES) # result in 5 items
    messages = map(create_message, selection)  # list
    print_results(messages)



if __name__ == "__main__":
    # todo: make the iterable a set so only one entry is valid
    # todo: skip the header of the csv if it has a header    
    # todo: make the choice selection dynamic
    # todo: detect if the calling environment can handle emojis - we want emojis in the message!!!1
    main()
