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
with open("tmp_file", 'w') as f:
    f.write(json.dumps(init_cipher))

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
            self.play(ReplacementTransform(self.cipher_box,Trans_box),time=2)
            r2[i].shift(1.5 * DOWN)
            self.play(ReplacementTransform(Trans_box, self.cipher_box),time=2)

    def init_sbox(self):
        self.sbox_array = [['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'], ['67', 'ac', '35', '9f', '66', 'a8', '85', 'c5', 'ae', 'b6', '29', 'a4', 'dc', '3a', '76', '3f'], ['a1', '32', '59', 'f2', 'fd', '4a', 'fa', '77', '6c', '7a', '78', 'd8', '3c', 'd0', 'b2', '14'], ['b4', 'bb', '75', 'd5', '30', '5a', 'da', '2e', 'be', 'bc', '6f', 'fc', '38', '4d', 'a9', 'e8'], ['87', '48', '2c', '73', '82', '39', '60', '9b', '69', 'b5', '53', '0', 'cc', '8b', '9', '7'], ['8a', '17', '91', '61', 'b9', 'd', 'fe', '45', '18', '22', '9e', '4c', 'de', 'a5', '2', 'f7'], ['e2', '6', 'b7', '74', 'ce', '15', 'e1', 'd2', 'db', '24', '81', '64', '8d', '3e', 'c6', '1c'], ['cf', '54', 'b8', '63', 'a0', 'd7', '34', '49', '99', '2a', 'bf', '1a', 'a2', 'c2', 'eb', '51'], ['ee', '6e', '2b', 'd6', 'ea', 'dd', '46', '50', '94', 'b0', 'fb', 'f5', '97', 'f4', '84', 'e'], ['1d', '5e', '89', '83', 'bd', '1f', 'e7', '2f', '44', '8', 'b', 'f9', 'f3', '25', 'cb', 'c8'], ['ca', 'ff', 'ec', '70', '33', 'a', '62', '4f', '13', '3b', 'e4', 'b1', 'c0', '4b', '55', '2d'], ['79', '1b', '93', 'b3', '1', 'c9', '7b', '12', 'a7', 'a6', 'ef', '92', '31', 'c4', 'a3', '6d'], ['f', '8f', '90', '96', '41', '6a', '19', '7c', '36', 'f1', '10', '5c', 'e3', 'd9', '68', 'ad'], ['df', '56', '71', '27', '9d', 'c7', '7e', '47', '21', '3d', '26', '8e', '57', '16', 'ed', '98'], ['37', 'd4', 'f8', 'af', '95', 'aa', 'f6', '58', '11', '40', 'd1', 'ab', 'f0', 'e0', '9a', 'd3'], ['4e', '5d', 'cd', '72', '88', 'c', '28', '65', '5', '5f', 'e9', '23', 'ba', 'c3', 'e6', '7f'], ['5b', 'e5', 'c1', '20', '1e', '4', '8c', '42', '86', '80', '7d', '52', '3', '43', '6b', '9c']]
        self.sbox_array[0].insert(0, ' ')
        for num in range(len(self.sbox_array)):
            if num==0:
                pass
            else:
                self.sbox_array[num].insert(0, str(hex(num-1))[2:])
        self.sbox = Table_box(rows = 17, cols = 17, text_arr = self.sbox_array, side_length = 0.3)
        self.sbox.shift(RIGHT * 3)
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
        it's not perfect transform anime 
        but Kyr1os is still trying to fix here
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

        self.play(FadeIn(text))
        self.play(FadeIn(sign))
        self.wait(1)
        self.play(FadeOut(text), FadeOut(self.matrax), FadeOut(self.new_col), FadeOut(sign), FadeIn(self.first_col_xor))
        self.wait(1)
        new = copy.deepcopy(self.first_col_xor)
        new.next_to(self.new_col, OUT)
        new.shift(LEFT * 5)
        self.play(ReplacementTransform(self.first_col_xor, new))

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
        res_box.next_to(self.new_col, OUT)
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
        self.key = [['db', '45', '2e', '9b'], ['ef', '9c', 'c4', '2a'], ['98', '95', '72', '87'], ['6f', '36', '5d', '69']]
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
