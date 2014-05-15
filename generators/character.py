#!/usr/bin/env python3

import itertools
import random
import os
import sys

NAMES_FILE = 'names.txt'

class CharacterGenerator():
    def __init__(self, data_path):
        self.data_path = data_path

    def new_character(self):
        sex = next(self._sex_generator())
        name = next(self._name_generator(sex))
        occupation = next(self._occupation_generator())
        return(Character(sex, name, occupation))

    def _name_generator(self, sex=None):
        names = []
        name_data = os.path.join(self.data_path, NAMES_FILE)
        with open(name_data, 'r') as f:
            for row in [x.split(';') for x in f.readlines()]:
                d = {}
                for k,v in [y.split('=') for y in row]:
                    d[k.strip()] = [x.strip() for x in v.split(',')]
                names.append(d)

        random.shuffle(names)

        fails = 0
        key_fails = 0
        for name in itertools.cycle(names):
            if sex:
                if fails > len(names):
                    print('No {} characters in dataset, dying'.format(sex), file=sys.stderr)
                    raise SystemExit
                try:
                    if sex in name['sex']:
                        fails = 0
                        yield name['name'][0]
                    else:
                        fails += 1
                    key_fails = 0
                except KeyError:
                    key_fails += 1
                    if(key_fails > len(names)):
                        print('No field sex', file=sys.stderr)
                        raise SystemExit
            else:
                yield name['name'][0]

    def _sex_generator(self):
        sex = ('male', 'female', 'shemale')
        while True:
            yield random.sample(sex, 1)[0]

    def _occupation_generator(self):
        occupation = ('wipping boy', 'apple pealer', 'porridge taster')
        while True:
            yield random.sample(occupation, 1)[0]

class Character():
    def __init__(self, sex, name, occupation):
        self.sex = sex
        self.name = name
        self.occupation = occupation

    def get_description(self):
        desc = '{0} is a {1} {2}'.format(self.name, self.sex, self.occupation)
        return(desc)
