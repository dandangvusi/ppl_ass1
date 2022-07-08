# Generated from c:\Local Disk (D)\StudyMaterial\4thSemester\NL_NNLT\assignment\BKIT\assignment1\initial\src\main\bkit\parser\BKIT.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3F")
        buf.write("\7\4\2\t\2\3\2\3\2\3\2\2\2\3\2\2\2\2\5\2\4\3\2\2\2\4\5")
        buf.write("\7\2\2\3\5\3\3\2\2\2\2")
        return buf.getvalue()


class BKITParser ( Parser ):

    grammarFileName = "BKIT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'Body'", "'Break'", "'Continue'", "'Do'", "'Else'", 
                     "'Elself'", "'Endbody'", "'Endif'", "'Endfor'", "'Endwhile'", 
                     "'For'", "'Function'", "'If'", "'Parameter'", "'Return'", 
                     "'Then'", "'Var'", "'While'", "'True'", "'False'", 
                     "'Enddo'", "'+'", "'-'", "'*'", "'\\'", "'%'", "'+.'", 
                     "'-.'", "'*.'", "'\\.'", "'=='", "'!='", "'<'", "'>'", 
                     "'<='", "'>='", "'=/='", "'<.'", "'>.'", "'<=.'", "'>=.'", 
                     "'!'", "'&&'", "'||'", "'='", "'['", "']'", "'('", 
                     "')'", "'{'", "'}'", "';'", "':'", "','", "'.'" ]

    symbolicNames = [ "<INVALID>", "DEC_INT_LIT", "HEX_INT_LIT", "OCT_INT_LIT", 
                      "FLT_LIT", "BOOL_LIT", "STRLIT", "ARRAY_LIT", "BODY", 
                      "BREAK", "CONTINUE", "DO", "ELSE", "ELSELF", "ENDBODY", 
                      "ENDIF", "ENDFOR", "ENDWHILE", "FOR", "FUNCTION", 
                      "IF", "PARAMETER", "RETURN", "THEN", "VAR", "WHILE", 
                      "TRUE", "FALSE", "ENDDO", "ADD_I", "SUB_I", "MUL_I", 
                      "DIV_I", "MOD_I", "ADD_F", "SUB_F", "MUL_F", "DIV_F", 
                      "EQ_I", "NEQ_I", "LT_I", "GT_I", "LTE_I", "GTE_I", 
                      "NEQ_F", "LT_F", "GT_F", "LTE_F", "GTE_F", "NOT", 
                      "AND", "OR", "ASSIGN", "LS", "RS", "LB", "RB", "LC", 
                      "RC", "SEMI", "COLON", "COMMA", "DOT", "ID", "COMMENT", 
                      "WS", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "ERROR_CHAR" ]

    RULE_program = 0

    ruleNames =  [ "program" ]

    EOF = Token.EOF
    DEC_INT_LIT=1
    HEX_INT_LIT=2
    OCT_INT_LIT=3
    FLT_LIT=4
    BOOL_LIT=5
    STRLIT=6
    ARRAY_LIT=7
    BODY=8
    BREAK=9
    CONTINUE=10
    DO=11
    ELSE=12
    ELSELF=13
    ENDBODY=14
    ENDIF=15
    ENDFOR=16
    ENDWHILE=17
    FOR=18
    FUNCTION=19
    IF=20
    PARAMETER=21
    RETURN=22
    THEN=23
    VAR=24
    WHILE=25
    TRUE=26
    FALSE=27
    ENDDO=28
    ADD_I=29
    SUB_I=30
    MUL_I=31
    DIV_I=32
    MOD_I=33
    ADD_F=34
    SUB_F=35
    MUL_F=36
    DIV_F=37
    EQ_I=38
    NEQ_I=39
    LT_I=40
    GT_I=41
    LTE_I=42
    GTE_I=43
    NEQ_F=44
    LT_F=45
    GT_F=46
    LTE_F=47
    GTE_F=48
    NOT=49
    AND=50
    OR=51
    ASSIGN=52
    LS=53
    RS=54
    LB=55
    RB=56
    LC=57
    RC=58
    SEMI=59
    COLON=60
    COMMA=61
    DOT=62
    ID=63
    COMMENT=64
    WS=65
    ILLEGAL_ESCAPE=66
    UNCLOSE_STRING=67
    ERROR_CHAR=68

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(BKITParser.EOF, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_program




    def program(self):

        localctx = BKITParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2
            self.match(BKITParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





