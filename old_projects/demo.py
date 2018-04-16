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

from constants import *

from scene.scene import Scene
from utils.sounds import play_error_sound
from utils.sounds import play_finish_sound

class Divide_2_4p(Scene):
    def construct(self):
        self.init_plain()
        self.plain_2_4p()
        self.move_3_right()

    def init_plain(self):
        rect = Rectangle(height = 1, width = 8)
        rect.shift(1 * UP)
        brace = Brace(rect, UP)
        name, number = expression = TextMobject(
            "Plain", ": 16-byte"
        )
        number.set_color(YELLOW)
        expression.next_to(brace, UP)

        self.play(ShowCreation(rect))
        self.play(GrowFromCenter(brace))
        self.play(Write(expression, run_time = 1))
        self.wait(1)
        self.play(FadeOut(expression), FadeOut(brace))
        self.wait(1)

        self.plain = rect

    def plain_2_4p(self):
        subrects = VGroup()
        braces = VGroup()
        expressions = VGroup()
        for i in range(4):
            subrect = Rectangle(height = 1, width = 2)
            subrects.add(subrect)
        subrects.arrange_submobjects(RIGHT, buff = MED_SMALL_BUFF)
        subrects.shift(1 * DOWN)
        for i in range(4):
            brace = Brace(subrects[i], DOWN)
            name, id, number = expression = TextMobject(
            "Part", str(i+1), ": 4-byte"
            ).scale(0.65)
            number.set_color(YELLOW)
            expression.next_to(brace, DOWN)
            braces.add(brace)
            expressions.add(expression)


        self.play(
            ReplacementTransform(
                VGroup(self.plain),
                subrects
            )
        )
        self.play(GrowFromCenter(braces))
        self.play(Write(expressions, run_time = 1))
        self.wait(1)
        self.play(FadeOut(expressions), FadeOut(braces))
        self.wait(1)

        self.subplain = subrects
    
    def move_3_right(self):
        rect = Rectangle(height = 1, width = 4)

        self.play(Transform(self.subplain[0], rect), FadeOut(self.subplain[1:]))
        self.wait(1)

class Sbox_trans(Scene):
    def construct(self):
        self.init_sbox()
        self.subs()
    
    def init_sbox():
        pass
    
    def subs():
        pass

"""
class BreakUp2To256(Scene):
    def construct(self):
        self.initialize_bits()
        self.add_number()
        self.break_up_as_powers_of_two()
        self.break_up_as_four_billions()
        self.reorganize_four_billions()

    def initialize_bits(self):
        bits = bit_string_to_mobject("")
        bits.to_corner(UP+LEFT)
        one = TexMobject("1")[0]
        one.replace(bits[0], dim_to_match = 1)
        self.add(bits)
        self.add_foreground_mobject(VGroup(*bits[-15:]))
        self.number = 0
        self.bits = bits
        self.one = one
        self.zero = bits[0].copy()

    def add_number(self):
        brace = Brace(self.bits, RIGHT)

        number, possibilities = expression = TextMobject(
            "$2^{256}$", "possibilities"
        )
        number.set_color(YELLOW)
        expression.next_to(brace, RIGHT)

        

        self.play(
            
            GrowFromCenter(brace),
            Write(expression, run_time = 1)
        )

        self.wait()

        self.expression = expression
        self.bits_brace = brace

    def break_up_as_powers_of_two(self):
        bits = self.bits
        bits.generate_target()
        subgroups = [
            VGroup(*bits.target[32*i:32*(i+1)])
            for i in range(8)
        ]
        subexpressions = VGroup()
        for i, subgroup in enumerate(subgroups):
            subgroup.shift(i*MED_LARGE_BUFF*DOWN)
            subexpression = TextMobject(
                "$2^{32}$", "possibilities"
            )
            subexpression[0].set_color(GREEN)
            subexpression.next_to(subgroup, RIGHT)
            subexpressions.add(subexpression)

        self.play(
            FadeOut(self.bits_brace),
            ReplacementTransform(
                VGroup(self.expression),
                subexpressions
            ),
            MoveToTarget(bits)
        )
        self.wait()


        self.subexpressions = subexpressions

    def break_up_as_four_billions(self):
        new_subexpressions = VGroup()
        for subexpression in self.subexpressions:
            new_subexpression = TextMobject(
                "4 Billion", "possibilities"
            )
            new_subexpression[0].set_color(YELLOW)
            new_subexpression.move_to(subexpression, LEFT)
            new_subexpressions.add(new_subexpression)

        self.play(
            Transform(
                self.subexpressions, new_subexpressions,
                run_time = 2,
                submobject_mode = "lagged_start",
            )
        )
        self.wait(3)

    def reorganize_four_billions(self):
        target = VGroup(*[
            TextMobject(
                "$\\big($", "4 Billion", "$\\big)$",
                arg_separator = ""
            )
            for x in range(8)
        ])
        target.arrange_submobjects(RIGHT, buff = SMALL_BUFF)
        target.to_edge(UP)
        target.scale_to_fit_width(FRAME_WIDTH - LARGE_BUFF)
        parens = VGroup(*it.chain(*[
            [t[0], t[2]] for t in target
        ]))
        target_four_billions = VGroup(*[t[1] for t in target])
        target_four_billions.set_color(YELLOW)
        four_billions, to_fade = [
            VGroup(*[se[i] for se in self.subexpressions])
            for i in range(2)
        ]

        self.play(
            self.bits.to_corner, DOWN+LEFT,
            Transform(four_billions, target_four_billions),
            LaggedStart(FadeIn, parens),
            FadeOut(to_fade)
        )
        self.wait()

    def wait(self, time = 1):
        self.play(Animation(self.bits, run_time = time))

"""
