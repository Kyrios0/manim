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

class Mix_col(Scene):
    def construct(self):
        self.init_plain()
        self.shift_first_col()
        self.init_matrax()
        self.calculate_first_col()
        self.first_col_back()
        for col_num in range(1,4):
            self.calculate_other_col(col_num)

    def init_plain(self):
        plain = [["%02x" % ((ord(urandom(1)))) for row in range(4)] for column in range(4)]
        self.plain_box = Table_box(rows = 4, cols = 4, text_arr = plain)
        self.plain_box.shift(LEFT * 3)
        self.play(ShowCreation(self.plain_box), time = 2)
        self.wait(1)

    def shift_first_col(self):
        col_box = VGroup()
        for row in range(4):
            col_box.add(self.plain_box[row][0])
        self.new_col = copy.deepcopy(col_box)
        self.new_col.shift(RIGHT * 5)
        self.play(ReplacementTransform(col_box,self.new_col))
        self.wait(1)

    def init_matrax(self):
        matrax_element = [["%02x" % ((ord(urandom(1)))) for row in range(4)] for column in range(4)]
        # matrax is here!
        self.matrax = Table_box(rows = 4, cols = 4, text_arr = matrax_element)
        for row in self.matrax:
            for col in self.matrax:
                pass
        # self.matrax[row][col][0].color = BLACK
        self.matrax.shift(RIGHT * 4)
        self.play(ShowCreation(self.matrax))
        self.wait(1)

    def calculate_first_col(self):
        # here to calculate the multiple  of matrax
        pass

    def first_col_back(self):
        back_col = copy.deepcopy(self.new_col)
        back_col.shift(LEFT * 5)
        self.play(ReplacementTransform(self.new_col, back_col))

    def calculate_other_col(self, col_num):
        # here to calculate the xor of the first_col and others
        pass


class Add_round_key(Scene):
    def construct(self):
        self.plain = [["%02x" % ((ord(urandom(1)))) for row in range(4)] for column in range(4)]
        self.init_plain()
        self.init_key()
        self.go_center()
        self.play_xor()
        self.back()
        self.change_others()

    def init_plain(self):
        self.plain_box = Table_box(rows = 4, cols = 4, text_arr = self.plain)
        self.plain_box.shift(LEFT * 4)
        self.play(ShowCreation(self.plain_box), time = 2)
        self.wait(1)

    def init_key(self):
        self.key_box = Table_box(rows = 4, cols = 4, text_arr = self.plain)
        self.key_box.shift(RIGHT * 4)
        self.play(ShowCreation(self.key_box), time = 2)
        self.wait(1)

    def go_center(self):
        self.plain_first_col = VGroup()
        self.key_first_col = VGroup()
        for row in range(4):
            self.plain_first_col.add(self.plain_box[row][0])

        for row in range(4):
            self.key_first_col.add(self.key_box[row][0])

        new_plain_first = copy.deepcopy(self.plain_first_col)

        new_plain_first.shift(RIGHT * 5)
        new_plain_first.shift(UP * 1)
        self.play(ReplacementTransform(self.plain_first_col, new_plain_first))
        self.wait(1)


    def play_xor(self):
        xor_sign = TextMobject("$\oplus$")
        xor_sign.next_to(self.plain_first_col, RIGHT)
        xor_sign.scale(2)
        new_key_first = copy.deepcopy(self.key_first_col)
        new_key_first.next_to(xor_sign, RIGHT)
        self.play(ShowCreation(xor_sign), time = 0.2)
        self.play(ReplacementTransform(self.key_first_col, new_key_first))
        self.wait(2)
        self.play(FadeOut(xor_sign), FadeOut(self.key_first_col), FadeOut(new_key_first))

    def back(self):
        new_plain_first = copy.deepcopy(self.plain_first_col)
        new_plain_first.shift(LEFT * 5)
        new_plain_first.shift(DOWN * 1)
        self.play(ReplacementTransform(self.plain_first_col, new_plain_first))
        self.wait(1)

    def change_others(self):
        pass
