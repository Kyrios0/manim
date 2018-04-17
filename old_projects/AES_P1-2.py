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

class Mix_row(Scene):
    def construct(self):
        pass
