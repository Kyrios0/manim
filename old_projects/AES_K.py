# -*- coding: utf-8 -*-
"""
AES algorithm video demo for cryptography homework
K: Key_schedule
author: Kyr1os
"""

from AES_lib import *

get_hex = lambda x: eval("0x"+x)

init_key = [["%02x" % ((ord(urandom(1)))) for row in range(4)] for column in range(4)]
rcon = [["01", "02", "04", "08"], ["10", "20", "40", "80"]]
s = [103, 172, 53, 159, 102, 168, 133, 197, 174, 182, 41, 164, 220, 58, 118, 63, 161, 50, 89, 242, 253, 74, 250, 119, 108, 122, 120, 216, 60, 208, 178, 20, 180, 187, 117, 213, 48, 90, 218, 46, 190, 188, 111, 252, 56, 77, 169, 232, 135, 72, 44, 115, 130, 57, 96, 155, 105, 181, 83, 0, 204, 139, 9, 7, 138, 23, 145, 97, 185, 13, 254, 69, 24, 34, 158, 76, 222, 165, 2, 247, 226, 6, 183, 116, 206, 21, 225, 210, 219, 36, 129, 100, 141, 62, 198, 28, 207, 84, 184, 99, 160, 215, 52, 73, 153, 42, 191, 26, 162, 194, 235, 81, 238, 110, 43, 214, 234, 221, 70, 80, 148, 176, 251, 245, 151, 244, 132, 14, 29, 94, 137, 131, 189, 31, 231, 47, 68, 8, 11, 249, 243, 37, 203, 200, 202, 255, 236, 112, 51, 10, 98, 79, 19, 59, 228, 177, 192, 75, 85, 45, 121, 27, 147, 179, 1, 201, 123, 18, 167, 166, 239, 146, 49, 196, 163, 109, 15, 143, 144, 150, 65, 106, 25, 124, 54, 241, 16, 92, 227, 217, 104, 173, 223, 86, 113, 39, 157, 199, 126, 71, 33, 61, 38, 142, 87, 22, 237, 152, 55, 212, 248, 175, 149, 170, 246, 88, 17, 64, 209, 171, 240, 224, 154, 211, 78, 93, 205, 114, 136, 12, 40, 101, 5, 95, 233, 35, 186, 195, 230, 127, 91, 229, 193, 32, 30, 4, 140, 66, 134, 128, 125, 82, 3, 67, 107, 156]
sbox = ["%02x" % (i) for i in s]

class Key_schedule(Scene):
    def construct(self):
        self.create_init_box()
        # self.gene_2nd_round_key()
        self.schedule_all()

    def create_init_box(self):
        key_box = VGroup()
        for row in range(4):
            key_row_box = VGroup()
            for column in range(4):
                key_row_box.add(Text_square(text = init_key[row][column], side_length = 0.75))
            key_row_box.arrange_submobjects(RIGHT, buff = 0)
            key_box.add(key_row_box)
        key_box.arrange_submobjects(DOWN, buff = 0)
        key_box.to_corner(LEFT + UP)

        rcon_box = VGroup()
        for row in range(2):
            rcon_row_box = VGroup()
            for column in range(4):
                rcon_row_box.add(Text_square(text = rcon[row][column], side_length = 0.75))
                rcon_row_box[-1].set_color(GREEN)
            rcon_row_box.arrange_submobjects(RIGHT, buff = 0)
            rcon_box.add(rcon_row_box)
        rcon_box.arrange_submobjects(DOWN, buff = 0)
        rcon_box.to_corner(RIGHT + UP, buff = 2*DEFAULT_MOBJECT_TO_EDGE_BUFFER)
        rcon_box.next_to(1,1,buff=DEFAULT_MOBJECT_TO_MOBJECT_BUFFER)

        self.key_box = key_box
        self.rcon_box = rcon_box
        
        self.play(ShowCreation(self.key_box), time = 3)
        self.play(ShowCreation(self.rcon_box))
        self.wait(2)

    def gene_next_round_key(self, gtime):
        # trans_box = copy.deepcopy(self.key_box)
        # trans_box[-1].shift(RIGHT * 4)

        # test: 2 round
        for gene_round in range(4):
            dest_buff = 0
            p_row = self.key_box[-4]
            c_row = self.key_box[-1]

            t_row = copy.deepcopy(c_row)
            t_row.shift(RIGHT * 4)
            self.play(ReplacementTransform(c_row, t_row), time = 2)
            self.wait()

            if gene_round == 0:
                c_row[0].shift(3*c_row[0][0].side_length*RIGHT)
                for i in range(3):
                    c_row[i+1].shift(1*c_row[0][0].side_length*LEFT)
                
                self.play(ReplacementTransform(t_row, c_row), time = 2)
                self.wait()

                # To-Do: subBytes
                
                d_row = VGroup()
                for column in range(4):
                    dtext = sbox[get_hex(c_row[column][1].tex_string.split()[-1])]
                    d_row.add(Text_square(text = dtext, side_length = c_row[0][0].side_length))
                d_row.arrange_submobjects(RIGHT, buff = 0)
                d_row[0].shift(3*d_row[0][0].side_length*RIGHT)
                for i in range(3):
                    d_row[i+1].shift(1*d_row[0][0].side_length*LEFT)
                d_row.next_to(c_row, OUT)

                express = TextMobject("SubBytes in S-Box").next_to(d_row, RIGHT)
                self.play(Write(express))
                self.play(ReplacementTransform(c_row, d_row))
                # tc_row, c_row = c_row, copy.deepcopy(d_row)
                c_row = d_row

                oplus = TextMobject("$\oplus$")
                oplus.next_to(c_row[1], DOWN)
                r0 = copy.deepcopy(self.rcon_box[gtime/4][gtime%4]).next_to(oplus, DOWN)

                self.play(ReplacementTransform(self.rcon_box[gtime/4][gtime%4], r0), \
                        FadeOut(express))
                self.play(FadeIn(oplus))
                self.wait()

                ans = "%02x" % (get_hex(init_key[-1][1]) ^ get_hex(rcon[0][gene_round]))
                nc0 = Text_square(text = ans, side_length = c_row[0][0].side_length)
                nc0.next_to(c_row[1], OUT)
                trans_r = VGroup()
                trans_r.add(c_row[1])
                trans_r.add(oplus)
                trans_r.add(r0)
                self.play(ReplacementTransform(trans_r, nc0))
                self.wait()

                # re_init
                # To-Do: rebuild
                c_row = VGroup()
                c_row.add(nc0)
                for i in range(3):
                    c_row.add(d_row[(i+2)%4]) # WARNING: DON'T EDIT HERE!! --Kyr1os
                self.key_box.remove(self.key_box[-1])
                self.key_box.add(c_row)

                dest_buff = 0.2

            t1_row = copy.deepcopy(p_row)
            t1_row.shift(RIGHT * 4)
            oplus = TextMobject("$\oplus$")
            oplus.next_to(t1_row, DOWN, buff = 0.75*t1_row[0][0].side_length)
            self.play(Transform(p_row, t1_row), time = 2)
            self.wait()
            self.play(FadeIn(oplus))
            self.wait()

            trans_r = VGroup()
            trans_r.add(copy.deepcopy(t1_row))
            trans_r.add(oplus)
            trans_r.add(copy.deepcopy(c_row))

            d_row = VGroup()

            for column in range(4):
                d_row_text = "%02x" % (get_hex(t1_row[column][1].tex_string.split()[-1]) ^ get_hex(c_row[column][1].tex_string.split()[-1]))
                d_row.add(Text_square(text = d_row_text, side_length = c_row[column][0].side_length).next_to(c_row[column], DOWN, buff = dest_buff))
            self.play(ReplacementTransform(trans_r, d_row), time = 2)
            # t1_row = t_row
            t1_row.shift(LEFT * 4)
            t3_row = copy.deepcopy(d_row)
            t3_row.shift(LEFT * 4) 
            if gene_round != 0:
                t2_row = c_row.shift(4*LEFT)
                c_row = t_row 
                self.play(Transform(p_row, t1_row), \
                      ReplacementTransform(c_row, t2_row), \
                      ReplacementTransform(d_row, t3_row), time = 2)
            else:
                t2_row = copy.deepcopy(c_row)
                t2_row.shift(LEFT * 4)  
                self.play(Transform(p_row, t1_row), \
                      Transform(c_row, t2_row), \
                      ReplacementTransform(d_row, t3_row), time = 2)          
            
            self.wait()
            # To-Do: recover p_row and c_row
            self.key_box.add(t3_row)
        last_round_key = copy.deepcopy(self.key_box[-8:])
        last_round_key.shift(3.22*UP)
        self.play(Transform(self.key_box[-8:], last_round_key))


    def schedule_all(self):
        for round in range(8):
            self.gene_next_round_key(round)

