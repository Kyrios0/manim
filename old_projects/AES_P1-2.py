# -*- coding: utf-8 -*-
"""
AES algorithm video demo for cryptography homework
Part1: Sub_bytes
Part2: Shift_row
author: Kyr1os, Whatever
v1.0 has finished @ 18.04.16
"""

from AES_lib import *

init_cipher = [["%02x" % ((ord(urandom(1)))) for row in range(4)] for column in range(4)]

class Sub_bytes(Scene):
    def construct(self):
        self.init_plain()
        self.mov_box()

    def init_plain(self):
        cipher_box = VGroup()
        for row in range(4):
            row_box = VGroup()
            for column in range(4):
                row_box.add(Text_square(text = init_cipher[row][column], side_length = 1.2))
            row_box.arrange_submobjects(RIGHT, buff = 0)
            cipher_box.add(row_box)
        cipher_box.arrange_submobjects(DOWN, buff = 0)
        cipher_box.shift(3 * LEFT)
    	self.cipher_box = cipher_box

        self.play(ShowCreation(self.cipher_box), time = 3)
        self.wait(2)

    def mov_box(self):
        Trans_box = copy.deepcopy(self.cipher_box)
        row = Trans_box[0]
        r2 = self.cipher_box[0]
        for i in range(4):
            row[i].shift(1.5 * UP)
            self.play(ReplacementTransform(self.cipher_box,Trans_box),time=2)
            r2[i].shift(1.5 * DOWN)
            self.play(ReplacementTransform(Trans_box, self.cipher_box),time=2)

        # To-Do: Add S-Box.jpg

class Shift_row(Scene):
    def construct(self):
        self.init_cipher_box()
        self.shift_box()

    def init_cipher_box(self):
        cipher_box = VGroup()
        for row in range(4):
            cipher_row_box = VGroup()
            for column in range(4):
                cipher_row_box.add(Text_square(text = init_cipher[row][column], side_length = 1.5))
            cipher_row_box.arrange_submobjects(RIGHT, buff = 0)
            cipher_box.add(cipher_row_box)
        cipher_box.arrange_submobjects(DOWN, buff = 0)
        cipher_box.shift(3 * LEFT)
        self.cipher_box = cipher_box

        self.play(ShowCreation(self.cipher_box), time = 3)
        self.wait(1)
        # self.play(FadeOut(self.cipher_box))

    def shift_box(self):
        """
        fixed by Kyr1os @ 04.18
        """
        for row_index in range(4):
            c_row = self.cipher_box[row_index]
            for shift_round in range(row_index):\
                if shift_round != 0:
                    c_row =  t_row
                t_row =  copy.deepcopy(c_row)
                
                for i in range(4):
                    if i == shift_round:
                        t_row[i].shift(3*t_row[0][0].side_length*RIGHT)
                    else:
                        t_row[i].shift(1*t_row[0][0].side_length*LEFT)
                self.play(ReplacementTransform(c_row, t_row))
