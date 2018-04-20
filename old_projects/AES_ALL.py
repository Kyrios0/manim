# -*- coding: utf-8 -*-
"""
AES algorithm video demo for cryptography homework
Part1: Sub_bytes by Kyr1os, Whatever
Part2: Shift_row by Kyr1os, Whatever
Part3: Mix_col by Whatever
Part4: Add_round_key by Whatever
K: Key_schedule by Kyr1os
author: Kyr1os, Whatever
v0.01 has finished @ 18.04.16
v0.10 has finished @ 18.04.19
"""

import json
from AES_lib import *

get_hex = lambda x: eval("0x"+x)
'''
init_cipher = [["%02x" % ((ord(urandom(1)))) for row in range(4)] for column in range(4)]
with open("tmp_file", 'w') as f:
    f.write(json.dumps(init_cipher))
'''

init_key = [["%02x" % ((ord(urandom(1)))) for row in range(4)] for column in range(4)]
rcon = [["01", "02", "04", "08"], ["10", "20", "40", "80"]]
s = [103, 172, 53, 159, 102, 168, 133, 197, 174, 182, 41, 164, 220, 58, 118, 63, 161, 50, 89, 242, 253, 74, 250, 119, 108, 122, 120, 216, 60, 208, 178, 20, 180, 187, 117, 213, 48, 90, 218, 46, 190, 188, 111, 252, 56, 77, 169, 232, 135, 72, 44, 115, 130, 57, 96, 155, 105, 181, 83, 0, 204, 139, 9, 7, 138, 23, 145, 97, 185, 13, 254, 69, 24, 34, 158, 76, 222, 165, 2, 247, 226, 6, 183, 116, 206, 21, 225, 210, 219, 36, 129, 100, 141, 62, 198, 28, 207, 84, 184, 99, 160, 215, 52, 73, 153, 42, 191, 26, 162, 194, 235, 81, 238, 110, 43, 214, 234, 221, 70, 80, 148, 176, 251, 245, 151, 244, 132, 14, 29, 94, 137, 131, 189, 31, 231, 47, 68, 8, 11, 249, 243, 37, 203, 200, 202, 255, 236, 112, 51, 10, 98, 79, 19, 59, 228, 177, 192, 75, 85, 45, 121, 27, 147, 179, 1, 201, 123, 18, 167, 166, 239, 146, 49, 196, 163, 109, 15, 143, 144, 150, 65, 106, 25, 124, 54, 241, 16, 92, 227, 217, 104, 173, 223, 86, 113, 39, 157, 199, 126, 71, 33, 61, 38, 142, 87, 22, 237, 152, 55, 212, 248, 175, 149, 170, 246, 88, 17, 64, 209, 171, 240, 224, 154, 211, 78, 93, 205, 114, 136, 12, 40, 101, 5, 95, 233, 35, 186, 195, 230, 127, 91, 229, 193, 32, 30, 4, 140, 66, 134, 128, 125, 82, 3, 67, 107, 156]
g_sbox = ["%02x" % (i) for i in s]


class Sub_bytes(Scene):
    def construct(self):
        with open('tmp_file', 'r') as f:
            cipher = f.read()
        self.init_cipher = json.loads(cipher)
        self.init_plain()
        self.init_sbox()
        self.mov_box()

    def init_plain(self):
        cipher_box = VGroup()
        for row in range(4):
            row_box = VGroup()
            for column in range(4):
                row_box.add(Text_square(text = str(self.init_cipher[row][column]), side_length = 1.2))
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
            c_index = get_hex(row[i][1].tex_string.split()[-1])
            light_row = (c_index & 0xf) + 1
            light_col = (c_index >> 4) + 1
            self.play(ReplacementTransform(r2[i], row[i]),time=2)

            light_box = copy.deepcopy(self.sbox)
            for item in range(1, 17):
                light_box[light_row][item][0].set_color("BLUE")
                light_box[light_row][item][1].set_color("BLUE")
                light_box[item][light_col][0].set_color("BLUE")
                light_box[item][light_col][1].set_color("BLUE")
            light_box[light_row][light_col][0].set_color("YELLOW")
            light_box[light_row][light_col][1].set_color("YELLOW")
            self.play(Transform(self.sbox, light_box))

            nc0 = copy.deepcopy(light_box[light_row][light_col])
            nc0[0].scale(4)
            nc0[1].scale(4)

            self.play(ShowCreation(nc0))

            nc0.next_to(row[i], OUT)
            nc1 = copy.deepcopy(nc0)
            nc1.next_to(row[i], OUT)
            nc1[0].set_color("WHITE")
            nc1[1].set_color("WHITE")

            tg = VGroup()
            tg.add(nc0)
            tg.add(copy.deepcopy(row[i]))
            self.play(ReplacementTransform(tg, nc1), FadeOut(row[i]))
            for item in range(1, 17):
                self.sbox[light_row][item][0].set_color("WHITE")
                self.sbox[light_row][item][1].set_color("WHITE")
                self.sbox[item][light_col][0].set_color("WHITE")
                self.sbox[item][light_col][1].set_color("WHITE")
            self.sbox[light_row][light_col][0].set_color("WHITE")
            self.sbox[light_row][light_col][1].set_color("WHITE")
            
            self.play(Transform(light_box, self.sbox))
            r2[i].remove(r2[i][-1])
            r2[i].add(copy.deepcopy(nc1[-1]))
            r2[i].shift(1.5 * DOWN)
            
            self.play(ReplacementTransform(nc1, r2[i]), time=2)

        for row_index in range(1, 4):
            c_row = self.cipher_box[row_index]
            d_row = VGroup()
            for column in range(4):
                dtext = g_sbox[get_hex(c_row[column][1].tex_string.split()[-1])]
                d_row.add(Text_square(text = dtext, side_length = c_row[0][0].side_length))
            d_row.arrange_submobjects(RIGHT, buff = 0)

            d_row.next_to(c_row, OUT)
            self.play(Transform(c_row, d_row))
        

    def init_sbox(self):
        self.sbox_array = [ ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'], \
                            ['67', 'ac', '35', '9f', '66', 'a8', '85', 'c5', 'ae', 'b6', '29', 'a4', 'dc', '3a', '76', '3f'], \
                            ['a1', '32', '59', 'f2', 'fd', '4a', 'fa', '77', '6c', '7a', '78', 'd8', '3c', 'd0', 'b2', '14'], \
                            ['b4', 'bb', '75', 'd5', '30', '5a', 'da', '2e', 'be', 'bc', '6f', 'fc', '38', '4d', 'a9', 'e8'], \
                            ['87', '48', '2c', '73', '82', '39', '60', '9b', '69', 'b5', '53', '00', 'cc', '8b', '09', '07'], \
                            ['8a', '17', '91', '61', 'b9', '0d', 'fe', '45', '18', '22', '9e', '4c', 'de', 'a5', '02', 'f7'], \
                            ['e2', '06', 'b7', '74', 'ce', '15', 'e1', 'd2', 'db', '24', '81', '64', '8d', '3e', 'c6', '1c'], \
                            ['cf', '54', 'b8', '63', 'a0', 'd7', '34', '49', '99', '2a', 'bf', '1a', 'a2', 'c2', 'eb', '51'], \
                            ['ee', '6e', '2b', 'd6', 'ea', 'dd', '46', '50', '94', 'b0', 'fb', 'f5', '97', 'f4', '84', '0e'], \
                            ['1d', '5e', '89', '83', 'bd', '1f', 'e7', '2f', '44', '08', '0b', 'f9', 'f3', '25', 'cb', 'c8'], \
                            ['ca', 'ff', 'ec', '70', '33', '0a', '62', '4f', '13', '3b', 'e4', 'b1', 'c0', '4b', '55', '2d'], \
                            ['79', '1b', '93', 'b3', '01', 'c9', '7b', '12', 'a7', 'a6', 'ef', '92', '31', 'c4', 'a3', '6d'], \
                            ['0f', '8f', '90', '96', '41', '6a', '19', '7c', '36', 'f1', '10', '5c', 'e3', 'd9', '68', 'ad'], \
                            ['df', '56', '71', '27', '9d', 'c7', '7e', '47', '21', '3d', '26', '8e', '57', '16', 'ed', '98'], \
                            ['37', 'd4', 'f8', 'af', '95', 'aa', 'f6', '58', '11', '40', 'd1', 'ab', 'f0', 'e0', '9a', 'd3'], \
                            ['4e', '5d', 'cd', '72', '88', '0c', '28', '65', '05', '5f', 'e9', '23', 'ba', 'c3', 'e6', '7f'], \
                            ['5b', 'e5', 'c1', '20', '1e', '04', '8c', '42', '86', '80', '7d', '52', '03', '43', '6b', '9c'] ]
        self.sbox_array[0].insert(0, ' ')
        for num in range(len(self.sbox_array)):
            if num==0:
                pass
            else:
                self.sbox_array[num].insert(0, str(hex(num-1))[2:])
        self.sbox = Table_box(rows = 17, cols = 17, text_arr = self.sbox_array, side_length = 0.3)
        self.sbox.shift(RIGHT * 3)
        for item in range(17):
            self.sbox[0][item][0].set_color("GREEN")
            self.sbox[0][item][1].set_color("GREEN")
            self.sbox[item][0][0].set_color("GREEN")
            self.sbox[item][0][1].set_color("GREEN")
        self.play(ShowCreation(self.sbox))



class Shift_row(Scene):
    def construct(self):
        with open('tmp_file', 'r') as f:
            cipher = f.read()
        self.init_cipher = json.loads(cipher)

        self.init_cipher_box()
        self.shift_box()
        self.save_array()

    def init_cipher_box(self):
        cipher_box = VGroup()
        for row in range(4):
            cipher_row_box = VGroup()
            for column in range(4):
                cipher_row_box.add(Text_square(text = str(self.init_cipher[row][column]), side_length = 1.5))
            cipher_row_box.arrange_submobjects(RIGHT, buff = 0)
            cipher_box.add(cipher_row_box)
        cipher_box.arrange_submobjects(DOWN, buff = 0)
        cipher_box.shift(3 * LEFT)
        self.cipher_box = cipher_box

        self.play(ShowCreation(self.cipher_box), time = 3)
        self.wait(1)

    def shift_box(self):
        """
		fixed --Kyr1os @ 04.18
        """
        self.res = []
        for row_index in range(4):
            c_row = self.cipher_box[row_index]
            for shift_round in range(row_index):
                if shift_round != 0:
                    c_row = t_row
                t_row = copy.deepcopy(c_row)

                for i in range(4):
                    if i == shift_round:
                        t_row[i].shift(3 * t_row[0][0].side_length * RIGHT)
                    else:
                        t_row[i].shift(1 * t_row[0][0].side_length * LEFT)
                self.play(ReplacementTransform(c_row, t_row))
                self.res.append(c_row)



    def save_array(self):
        cipher_begin = self.init_cipher
        for row_index in range(len(cipher_begin)):
            for round in range(row_index):
                first_ele = cipher_begin[row_index].pop(0)
                cipher_begin[row_index].append(first_ele)
        res = cipher_begin
        with open("tmp_file", 'w') as f:
            f.write(json.dumps(res))

class Mix_col(Scene):
    def construct(self):
        self.init_plain()
        self.shift_first_col()
        self.init_matrax()
        self.calculate_first_col()
        for col_num in range(1,4):
            self.calculate_other_col(col_num)
        self.save_file()

    def init_plain(self):
        with open("tmp_file", 'r') as f:
            plain = f.read()
        self.plain = json.loads(plain)
        self.plain_box = Table_box(rows = 4, cols = 4, text_arr = self.plain)
        self.plain_box.shift(LEFT * 3)
        self.play(ShowCreation(self.plain_box), time = 2)
        self.wait(1)

    def shift_first_col(self):
        col_box = VGroup()
        for row in range(4):
            col_box.add(self.plain_box[row][0])
        self.new_col = copy.deepcopy(col_box)
        self.first_col_pos = copy.deepcopy(self.new_col)
        self.new_col.shift(RIGHT * 5)
        self.play(ReplacementTransform(col_box,self.new_col))
        self.wait(1)

    def init_matrax(self):
        self.matrax = TextMobject('''$\\left(
\\begin{array}{cccc}
    02 & 03 & 01 & 01 \\\\
    01 & 02 & 03 & 01 \\\\
    01 & 01 & 02 & 03 \\\\
    03 & 01 & 01 & 02
    \\end{array}
    \\right)$''')
        self.matrax.shift(RIGHT * 4)
        self.play(Write(self.matrax))
        self.wait(1)

    def padding(self, str1):
        return (2-len(str1)) * '0' + str1


    def calculate_first_col(self):
        # here to calculate the multiple  of matrax
        matrax = [[02, 03, 01, 01], [01, 02, 03, 01], [01, 01, 02, 03], [03, 01, 01, 02]]
        first_col = [ord(row[0].decode('hex')) for row in self.plain]
        res = []
        for row in matrax:
            for time in range(4):
                if time == 0:
                    xor_res = first_col[time] * row[time] % 256
                else:
                    xor_res ^= first_col[time] * row[time] % 256
            res.append([self.padding(str(hex(xor_res))[2:])])
        # generate the first col and use it as text_arr
        self.first_col_xor = Table_box(cols = 1, rows = 4, text_arr = res)
        self.first_col_xor.shift(RIGHT * 2)
        text = TextMobject("$GF(2^{8})$")
        text.next_to(self.matrax, DOWN)
        sign = TextMobject("$\\cross$")
        sign.next_to(self.matrax, LEFT)

        # just get the position for other cols
        self.front_place = copy.deepcopy(self.first_col_xor)
        self.sign_place = copy.deepcopy(sign)
        self.sign_place.next_to(self.front_place, RIGHT)
        self.second_place = copy.deepcopy(self.first_col_xor)
        self.second_place.next_to(self.sign_place, RIGHT)
        self.mix_pos = copy.deepcopy(self.new_col)

        self.play(FadeIn(text))
        self.play(FadeIn(sign))
        self.wait(1)
        self.play(Transform(text, self.first_col_xor), Transform(self.matrax, self.first_col_xor), Transform(self.new_col, self.first_col_xor), Transform(sign, self.first_col_xor))
        self.wait(1)
        new = copy.deepcopy(self.first_col_xor)
        new.next_to(self.first_col_pos, OUT)
        self.play(Transform(self.first_col_xor, new), Transform(text, new), Transform(self.matrax, new), Transform(self.new_col, new), Transform(sign, new))

        # self.final used as a container for the cycle
        self.final = []
        self.final.append(self.first_col_xor)

        #self.res_data used as a container of the final output file
        self.res_data = []



    def calculate_other_col(self, col_index):
        # here to calculate the xor of the first_col and others
        behind = VGroup()
        for each in range(4):
            behind.add(self.plain_box[each][col_index])
        place = copy.deepcopy(behind)
        behind_copy = copy.deepcopy(behind)
        front = VGroup()
        for one in self.final[-1]:
            front.add(copy.deepcopy(one[0]))
        front_copy = copy.deepcopy(front)
        sign = TextMobject("$\oplus$")

        # set the position
        front_copy.next_to(self.front_place, OUT)
        sign.next_to(self.sign_place, OUT)
        behind_copy.next_to(self.second_place, OUT)
        self.play(Transform(front, front_copy), Transform(behind, behind_copy))
        self.wait(1)
        self.play(FadeIn(sign))
        front_arr = []
        behind_arr = []
        for one in front:
            front_arr.append(one[1].tex_string[-2:])

        for one in behind:
            behind_arr.append(one[1].tex_string[-2:])


        res_arr = []
        # save_arr for the output file
        save_arr = []
        for num in range(4):
            value = ord(front_arr[num].decode('hex')) ^ ord(behind_arr[num].decode('hex'))
            value = self.padding(str(hex(value))[2:])
            save_arr.append(value)
            res_arr.append([value])

        if col_index == 1:
            self.res_data.append(front_arr)
            self.res_data.append(save_arr)
        else:
            self.res_data.append(save_arr)
        res_box = Table_box(rows = 4, cols = 1, text_arr = res_arr)
        res_box.next_to(self.mix_pos, OUT)
        res_box.shift(RIGHT * 2)
        #self.play(FadeOut(behind), FadeOut(front), FadeOut(sign))
        #self.play(FadeIn(res_box))
        self.play(ReplacementTransform(behind, res_box), ReplacementTransform(front, res_box), ReplacementTransform(sign, res_box))
        back = copy.deepcopy(res_box)
        back.next_to(place, OUT)
        self.play(Transform(res_box, back))
        self.wait(1)
        self.final.append(res_box)

    def save_file(self):
        with open("tmp_file", 'w') as f:
            f.write(json.dumps(self.res_data))



class Add_round_key(Scene):
    def construct(self):
        self.file_data = []
        self.key = [['5a', '55', '57', '20'], \
                    ['05', '3b', '56', '32'], \
                    ['f6', '5e', '7d', '5a'], \
                    ['e2', 'b8', '70', '17']]
        with open('tmp_file', 'r') as f:
            cipher = f.read()

        unicode_list = json.loads(cipher)

        # transform unicode to str
        self.plain = []
        for i in range(4):
            temp = []
            for j in range(4):
                temp.append(str(unicode_list[i][j]))
            self.plain.append(temp)

        self.init_plain()
        self.init_key()
        self.change_first()
        for col_index in range(1, 4):
            self.change_others(col_index)

    def init_plain(self):
        self.plain_box = Table_box(rows = 4, cols = 4, text_arr = self.plain)
        self.plain_box.shift(LEFT * 4)
        self.play(ShowCreation(self.plain_box), time = 2)
        self.wait(1)

    def init_key(self):
        self.key_box = Table_box(rows = 4, cols = 4, text_arr = self.key)
        for row in self.key_box:
            for col in row:
                col[0].set_color(color = BLUE)
        self.key_box.shift(RIGHT * 4)
        self.play(ShowCreation(self.key_box), time = 2)
        self.wait(1)

    def padding(self, str1):
        return (2-len(str1)) * '0' + str1



    def change_first(self):
        self.plain_first_col = VGroup()
        self.key_first_col = VGroup()
        for row in range(4):
            self.plain_first_col.add(self.plain_box[row][0])

        for row in range(4):
            self.key_first_col.add(self.key_box[row][0])

        self.begin_pos = copy.deepcopy(self.plain_first_col)
        res = copy.deepcopy(self.plain_first_col)
        res.shift(RIGHT * 5)
        res.shift(UP * 1)
        ### self.left_pos used to save the position
        self.left_pos = copy.deepcopy(res)
        ###
        self.play(Transform(self.plain_first_col, res))
        self.wait(1)


        xor_sign = TextMobject("$\\oplus$")
        xor_sign.next_to(self.plain_first_col, RIGHT)
        xor_sign.scale(2)
        new_key_first = copy.deepcopy(self.key_first_col)
        new_key_first.next_to(xor_sign, RIGHT)
        new_key_first.shift(LEFT * 0.18)
        ### self.right_pos used to save the position
        self.right_pos = copy.deepcopy(new_key_first)
        ###
        self.play(Transform(self.key_first_col, new_key_first))
        self.play(FadeIn(xor_sign), time=0.2)

        res_arr = []
        for index in range(4):
            plain_val = self.plain_first_col[index][1].tex_string[-2:]
            key_val = self.key_first_col[index][1].tex_string[-2:]
            res_val = ord(plain_val.decode('hex')) ^ ord(key_val.decode('hex'))
            res_val = self.padding(str(hex(res_val))[2:])
            res_arr.append(res_val)
        ### save to out file
        self.file_data.append(res_arr)
        ###
        res_box = VGroup()
        for val in res_arr:
            res_box.add(Text_square(text = val, side_length = 1))
        res_box.arrange_submobjects(DOWN, buff=0)
        res_box.next_to(self.left_pos, OUT)
        res_box.shift(RIGHT * 0.8)

        self.wait(2)
        self.play(Transform(self.plain_first_col, res_box), Transform(xor_sign, res_box), Transform(self.key_first_col, res_box), Transform(new_key_first, res_box))
        self.play(FadeIn(res_box), FadeOut(self.plain_first_col), FadeOut(xor_sign), FadeOut(new_key_first), FadeOut(self.key_first_col))
        new_plain_first = copy.deepcopy(res_box)
        new_plain_first.next_to(self.begin_pos, OUT)
        self.play(Transform(res_box, new_plain_first), Transform(self.plain_first_col, new_plain_first), Transform(xor_sign, new_plain_first), Transform(self.key_first_col, new_plain_first), Transform(new_key_first, new_plain_first))
        self.wait(1)



    def change_others(self, col_index):
        plain_first_col = VGroup()
        key_first_col = VGroup()
        for row in range(4):
            plain_first_col.add(self.plain_box[row][col_index])

        for row in range(4):
            key_first_col.add(self.key_box[row][col_index])

        self.begin_pos = copy.deepcopy(plain_first_col)
        res = copy.deepcopy(plain_first_col)
        res.next_to(self.left_pos, OUT)

        self.play(Transform(plain_first_col, res))
        self.wait(1)

        xor_sign = TextMobject("$\\oplus$")
        xor_sign.next_to(plain_first_col, RIGHT)
        xor_sign.scale(2)
        new_key_first = copy.deepcopy(key_first_col)
        new_key_first.next_to(self.right_pos, OUT)

        self.play(Transform(key_first_col, new_key_first))
        self.play(FadeIn(xor_sign), time=0.2)

        res_arr = []
        for index in range(4):
            plain_val = plain_first_col[index][1].tex_string[-2:]
            key_val = key_first_col[index][1].tex_string[-2:]
            res_val = ord(plain_val.decode('hex')) ^ ord(key_val.decode('hex'))
            res_val = self.padding(str(hex(res_val))[2:])
            res_arr.append(res_val)
        ### save to out file
        self.file_data.append(res_arr)
        ###
        res_box = VGroup()
        for val in res_arr:
            res_box.add(Text_square(text=val, side_length=1))
        res_box.arrange_submobjects(DOWN, buff=0)
        res_box.next_to(self.left_pos, OUT)
        res_box.shift(RIGHT * 0.8)

        self.wait(2)
        self.play(Transform(plain_first_col, res_box), Transform(xor_sign, res_box),
                  Transform(key_first_col, res_box), Transform(new_key_first, res_box))
        self.play(FadeIn(res_box), FadeOut(plain_first_col), FadeOut(xor_sign), FadeOut(new_key_first),
                  FadeOut(key_first_col))
        new_plain_first = copy.deepcopy(res_box)
        new_plain_first.next_to(self.begin_pos, OUT)
        self.play(Transform(res_box, new_plain_first), Transform(plain_first_col, new_plain_first),
                  Transform(xor_sign, new_plain_first), Transform(key_first_col, new_plain_first),
                  Transform(new_key_first, new_plain_first))
        self.wait(1)
		
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

                # subBytes
                
                d_row = VGroup()
                for column in range(4):
                    dtext = g_sbox[get_hex(c_row[column][1].tex_string.split()[-1])]
                    d_row.add(Text_square(text = dtext, side_length = c_row[0][0].side_length))
                d_row.arrange_submobjects(RIGHT, buff = 0)
                d_row[0].shift(3*d_row[0][0].side_length*RIGHT)
                for i in range(3):
                    d_row[i+1].shift(1*d_row[0][0].side_length*LEFT)
                d_row.next_to(c_row, OUT)

                express = TextMobject("SubBytes in S-Box").next_to(d_row, RIGHT)
                self.play(Write(express))
                self.play(ReplacementTransform(c_row, d_row))
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
            # recover p_row and c_row
            self.key_box.add(t3_row)
        last_round_key = copy.deepcopy(self.key_box[-8:])
        last_round_key.shift(3.22*UP)
        self.play(Transform(self.key_box[-8:], last_round_key))


    def schedule_all(self):
        for round in range(8):
            self.gene_next_round_key(round)
