import os
import random
import csv


def load_handles(csv_file_path):
    """Load twitter handles from csv file"""
    with open(csv_file_path) as fin:
        csv_reader = csv.reader(fin)
        return [
            handle[0]
            for handle in csv_reader
            if handle[0].startswith('@')
        ]


def make_selection(population, choice_count):
    """returns a list of random selection"""
    return random.sample(population, k=choice_count)
