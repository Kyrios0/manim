# -*- coding: utf-8 -*-

"""

AES algorithm video demo for cryptography homework

Part1: Sub_bytes

Part2: Shift_row

author: Kyr1os, Whatever

v1.0 has finished @ 18.04.16

"""

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



class Sub_bytes(Scene):

    def construct(self):

        self.init_plain()

        self.mov_box()



    def init_plain(self):

        cipher_box = VGroup()

        for i in range(4):

            row_box = VGroup()

            for j in range(4):

                one = Square(side_length = 1.2)

                row_box.add(one)

            row_box.arrange_submobjects(RIGHT, buff = 0)

            cipher_box.add(row_box)

        cipher_box.arrange_submobjects(DOWN, buff = 0)

        cipher_box.shift(3 * LEFT)

        self.play(ShowCreation(cipher_box), time = 3)

        self.wait(2)



    def mov_box(self):

        Trans_box = copy.deepcopy(cipher_box)



        row = Trans_box[0]

        r2 = cipher_box[0]

        for i in range(4):

            row[i].shift(1.5 * UP)

            self.play(ReplacementTransform(cipher_box,Trans_box),time=2)

            r2[i].shift(1.5 * DOWN)

            self.play(ReplacementTransform(Trans_box, cipher_box),time=2)



        # To-Do: Add S-Box.jpg





class Shift_row(Scene):

    def construct(self):

        self.init_cipher_box()

        self.shift_box()



    def init_cipher_box(self):

        self.cipher_box = VGroup()

        for i in range(4):

            row_box = VGroup()

            for j in range(4):

                one = Text_square(text = str(i)+str(j), side_length = 1.5)

                row_box.add(one)

            row_box.arrange_submobjects(RIGHT, buff = 0)

            self.cipher_box.add(row_box)

        self.cipher_box.arrange_submobjects(DOWN, buff = 0)

        self.cipher_box.shift(3 * LEFT)

        self.play(ShowCreation(self.cipher_box), time = 3)

        self.wait(1)



    def shift_box(self):

        """

        it's not perfect transform anime 

        but Kyr1os is still trying to fix here

        """

        for row_index in range(4):

            for shift_round in range(row_index):

                row = VGroup()

                for k in range(3):

                    # delete deepcopy to get another effect

                    row.add(copy.deepcopy(self.cipher_box[row_index][k+1]))

                    row[-1].shift(row[-1][0].side_length * LEFT)

                row.add(copy.deepcopy(self.cipher_box[row_index][0]))

                row[-1].shift(row[-1][0].side_length * 3 * RIGHT)

                self.play(Transform(self.cipher_box[row_index], row))