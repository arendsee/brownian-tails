#!/usr/bin/env python3

import os
import generators.character as characters

if __name__ == '__main__':
    wk_path = os.path.split(os.path.abspath(__file__))[0]
    data_path = os.path.join(wk_path, 'data')
    chargen = characters.CharacterGenerator(data_path)
    main = chargen.new_character()
    print(main.get_description())
