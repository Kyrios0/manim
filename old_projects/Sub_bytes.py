# -*- coding: utf-8 -*-
"""
AES algorithm video demo for cryptography homework
author: Kyr1os, Whatever
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


"""class Text_square(VGroup):
    def __init__(self, text='', side_length=1):
        self.box = VGroup()
        # self.text = text # for debug
        self.box.add(Square(side_length=side_length))
        self.box.add(TextMobject(text).scale(1.2*side_length))
        self.box.arrange_submobjects(OUT)"""

class Text_square(VGroup):
    def __init__(self, text = '', side_length = 1):
        VGroup.__init__(self)
        self.add(Square(side_length=side_length))
        self.add(TextMobject(text).scale(1.2 * side_length))
        self.arrange_submobjects(OUT)


class Sub_bytes(Scene):
    def construct(self):
        self.init_plain()

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

        Trans_box = copy.deepcopy(cipher_box)
        """for i in range(4):
            row_box = VGroup()
            for j in range(4):
                one = Square(side_length=1.2)
                row_box.add(one)
            row_box.arrange_submobjects(RIGHT,buff=0)
            Trans_box.add(row_box)
        Trans_box.arrange_submobjects(DOWN,buff=0)
        Trans_box.shift(3*LEFT)
        """

        row = Trans_box[0]
        r2 = cipher_box[0]
        for i in range(4):
            row[i].shift(1.5 * UP)
            self.play(ReplacementTransform(cipher_box,Trans_box),time=2)
            r2[i].shift(1.5 * DOWN)
            self.play(ReplacementTransform(Trans_box, cipher_box),time=2)


        # 左边加个图片，然后换掉里面的hex表示s盒替换


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
        for i in range(4):
            # self.shift_row(i)
            for j in range(i):
                row = VGroup()
                for k in range(3):
                    # self.cipher_box[i][k+1].shift(self.cipher_box[i][k+1][0].side_length * LEFT)
                    # box = copy.deepcopy(self.cipher_box[i][k+1])
                    # row.add(box)
                    row.add(self.cipher_box[i][k+1])
                    row[-1].shift(row[-1][0].side_length * LEFT)
                # self.cipher_box[i][k+1].update_text(self.cipher_box[i][3].text)
                # self.cipher_box[i][0].shift(self.cipher_box[i][0][0].side_length * 3 * RIGHT)
                # box = copy.deepcopy(self.cipher_box[i][0])
                # row.add(box)
                row.add(self.cipher_box[i][0])
                row[-1].shift(row[-1][0].side_length * 3 * RIGHT)
                self.play(Transform(self.cipher_box[i], row))
                # self.play()

    """def shift_row(self, num):
        for j in range(num):
            row = VGroup()
            for i in range(3):
                row.add(self.cipher_box[num][i+1])
            row.add(self.cipher_box[num][0])

            self.play(ReplacementTransform(self.cipher_box[num], row))
            for k in range(4):
                for l in range(4):
                    print self.cipher_box[k][l][1].text"""

        #self.play(ReplacementTransform(begin,trans))
        #self.wait(1)

class Demo(Scene):
    def construct(self):
        self.cipher_box = VGroup()
        for i in range(4):
            row_box = VGroup()
            for j in range(4):
                one = Text_square(text = str(i)+str(j), side_length = 1)
                row_box.add(one)
            row_box.arrange_submobjects(RIGHT, buff = 0)
            self.cipher_box.add(row_box)
        self.cipher_box.arrange_submobjects(DOWN, buff = 0)
        self.cipher_box.shift(3 * LEFT)
        self.play(Write(self.cipher_box), time = 3)
        self.wait(1)
        for i in range(4):
            self.shift_row(i)

    def shift_row(self,num):
        for j in range(num):
            row = VGroup()
            for i in range(3):
                row.add(self.cipher_box[num][i+1])
            row.add(self.cipher_box[num][0])

            self.play(ReplacementTransform(self.cipher_box[num], row))
