# -*- coding: utf-8 -*-
"""
AES algorithm video demo for cryptography homework
K: Key_schedule
author: Kyr1os
"""

from AES_lib import *

init_key = [["%02x" % ((ord(urandom(1)))) for row in range(4)] for column in range(4)]

class Key_schedule(Scene):
    def construct(self):
        self.create_init_box()
        self.gene_2nd_round_key()
        self.schedule_all()

    def create_init_box(self):
        key_box = VGroup()
        for row in range(4):
            key_row_box = VGroup()
            for column in range(4):
                key_row_box.add(Text_square(text = init_key[row][column], side_length = 0.8))
            key_row_box.arrange_submobjects(RIGHT, buff = 0)
            key_box.add(key_row_box)
        key_box.arrange_submobjects(DOWN, buff = 0)
        key_box.to_corner(LEFT + UP)

        self.key_box = key_box
        
        self.play(ShowCreation(self.key_box), time = 3)
        self.wait(2)

    def gene_2nd_round_key(self):
        pass

    def schedule_all(self):
        pass

    
