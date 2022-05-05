# Compiler for TrumpScript
# 1/17/2016
import ast
from ast import *

from trparser import *
from tokenizer import *


class Compiler:
    def __init__(self):
        self.tk = Tokenizer()
        self.prs = Parser()

    def compile(self, source):
        modu = self.parse(self.tokenize(source))
        fix_missing_locations(modu)
        exec(compile(modu, filename="<ast>", mode="exec"))

    def parse(self, tokens):
        return self.prs.parse(tokens)

    def tokenize(self, filename):
        return self.tk.tokenize(filename)
