# This Python file uses the following encoding: utf-8
from locale import getdefaultlocale
import json
import os

strings = []


def get_lang():
    global strings

    lang = getdefaultlocale()[0]
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/langs/'

    if lang == 'ru_RU':
        with open(path + 'ru_RU.json', 'r') as f:
            strings = json.load(f)
    else:
        with open(path + 'en_GB.json', 'r') as f:
            strings = json.load(f)
