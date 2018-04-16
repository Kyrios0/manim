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
        self.add(TextMobject(text).scale(1.2 * side_length))
        self.arrange_submobjects(OUT)
