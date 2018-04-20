from big_ol_pile_of_manim_imports import *
from old_projects.crypto import sha256_tex_mob, bit_string_to_mobject
import sys
import argparse
import imp
import inspect
import itertools as it
import os
import subprocess as sp
import traceback
import copy
from os import urandom
from constants import *

from scene.scene import Scene
from utils.sounds import play_error_sound
from utils.sounds import play_finish_sound

class Text_square(VGroup):
    def __init__(self, text = '', side_length = 1):
        VGroup.__init__(self)
        self.add(Square(side_length=side_length))
        self.add(TextMobject(str(text)).scale(1.2 * side_length))
        self.arrange_submobjects(OUT)

class Table_box(VGroup):
    def __init__(self, rows = 4, cols = 4, side_length = 1, text_arr = []):
    # used to create a box of row rows and columns cols
    # text arr is made of an array like this
    # [['ff', 'ff', 'ff'],
    # ['ff', 'ff', 'ff'],
    # ['ff', 'ff', 'ff']]
    # Attention: each element of the array should be string
        VGroup.__init__(self)
        for row in range(rows):
            row_table = VGroup()
            for col in range(cols):
                row_table.add(Text_square(text = text_arr[row][col], side_length = side_length))
            row_table.arrange_submobjects(RIGHT, buff = 0)
            self.add(row_table)
        self.arrange_submobjects(DOWN, buff = 0)

