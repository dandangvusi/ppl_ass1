# Generated from c:\Local Disk (D)\StudyMaterial\4thSemester\NL_NNLT\assignment\BKIT\assignment1\initial\src\main\bkit\parser\BKIT.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2F")
        buf.write("\u023c\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\3\2\3\2\3\3\3\3\3\4\3")
        buf.write("\4\3\5\3\5\3\6\3\6\3\7\3\7\3\7\3\7\5\7\u00b2\n\7\3\b\3")
        buf.write("\b\3\b\3\b\5\b\u00b8\n\b\3\t\3\t\3\t\7\t\u00bd\n\t\f\t")
        buf.write("\16\t\u00c0\13\t\5\t\u00c2\n\t\3\n\3\n\7\n\u00c6\n\n\f")
        buf.write("\n\16\n\u00c9\13\n\3\13\3\13\5\13\u00cd\n\13\3\13\3\13")
        buf.write("\3\13\7\13\u00d2\n\13\f\13\16\13\u00d5\13\13\5\13\u00d7")
        buf.write("\n\13\3\f\3\f\3\f\3\r\3\r\3\r\3\16\3\16\3\16\7\16\u00e2")
        buf.write("\n\16\f\16\16\16\u00e5\13\16\5\16\u00e7\n\16\3\17\3\17")
        buf.write("\3\17\5\17\u00ec\n\17\3\17\3\17\7\17\u00f0\n\17\f\17\16")
        buf.write("\17\u00f3\13\17\3\20\3\20\3\20\7\20\u00f8\n\20\f\20\16")
        buf.write("\20\u00fb\13\20\3\21\3\21\3\21\5\21\u0100\n\21\3\21\5")
        buf.write("\21\u0103\n\21\3\22\3\22\5\22\u0107\n\22\3\23\3\23\3\23")
        buf.write("\3\23\7\23\u010d\n\23\f\23\16\23\u0110\13\23\3\23\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\5\24\u011c\n")
        buf.write("\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\5\24\u0125\n\24")
        buf.write("\7\24\u0127\n\24\f\24\16\24\u012a\13\24\3\24\3\24\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37")
        buf.write("\3\37\3\37\3 \3 \3 \3 \3 \3 \3 \3 \3 \3!\3!\3!\3\"\3\"")
        buf.write("\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3#")
        buf.write("\3$\3$\3$\3$\3$\3%\3%\3%\3%\3&\3&\3&\3&\3&\3&\3\'\3\'")
        buf.write("\3\'\3\'\3\'\3(\3(\3(\3(\3(\3(\3)\3)\3)\3)\3)\3)\3*\3")
        buf.write("*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3/\3\60\3\60\3\60\3\61")
        buf.write("\3\61\3\61\3\62\3\62\3\62\3\63\3\63\3\63\3\64\3\64\3\64")
        buf.write("\3\65\3\65\3\66\3\66\3\67\3\67\3\67\38\38\38\39\39\39")
        buf.write("\39\3:\3:\3:\3;\3;\3;\3<\3<\3<\3<\3=\3=\3=\3=\3>\3>\3")
        buf.write("?\3?\3?\3@\3@\3@\3A\3A\3B\3B\3C\3C\3D\3D\3E\3E\3F\3F\3")
        buf.write("G\3G\3H\3H\3I\3I\3J\3J\3K\3K\3L\3L\7L\u0208\nL\fL\16L")
        buf.write("\u020b\13L\3M\3M\3M\3M\7M\u0211\nM\fM\16M\u0214\13M\3")
        buf.write("M\3M\3M\3M\3M\3N\6N\u021c\nN\rN\16N\u021d\3N\3N\3O\3O")
        buf.write("\3O\3O\7O\u0226\nO\fO\16O\u0229\13O\3O\3O\3O\3O\3P\3P")
        buf.write("\3P\3P\7P\u0233\nP\fP\16P\u0236\13P\3P\3P\3Q\3Q\3Q\3\u0212")
        buf.write("\2R\3\2\5\2\7\2\t\2\13\2\r\2\17\2\21\2\23\2\25\2\27\2")
        buf.write("\31\2\33\3\35\4\37\5!\6#\7%\b\'\t)\n+\13-\f/\r\61\16\63")
        buf.write("\17\65\20\67\219\22;\23=\24?\25A\26C\27E\30G\31I\32K\33")
        buf.write("M\34O\35Q\36S\37U W!Y\"[#]$_%a&c\'e(g)i*k+m,o-q.s/u\60")
        buf.write("w\61y\62{\63}\64\177\65\u0081\66\u0083\67\u00858\u0087")
        buf.write("9\u0089:\u008b;\u008d<\u008f=\u0091>\u0093?\u0095@\u0097")
        buf.write("A\u0099B\u009bC\u009dD\u009fE\u00a1F\3\2\16\3\2\62;\3")
        buf.write("\2\63;\3\2\629\3\2\639\3\2CH\4\2GGgg\4\2--//\t\2))^^d")
        buf.write("dhhppttvv\6\2\f\f\17\17$$^^\5\2C\\aac|\6\2\62;C\\aac|")
        buf.write("\5\2\13\f\17\17\"\"\2\u0257\2\33\3\2\2\2\2\35\3\2\2\2")
        buf.write("\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2")
        buf.write("\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61")
        buf.write("\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2")
        buf.write("\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3")
        buf.write("\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M")
        buf.write("\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2")
        buf.write("W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2")
        buf.write("\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2")
        buf.write("\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2")
        buf.write("\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3")
        buf.write("\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2")
        buf.write("\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b")
        buf.write("\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2")
        buf.write("\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2\2\2\u0099")
        buf.write("\3\2\2\2\2\u009b\3\2\2\2\2\u009d\3\2\2\2\2\u009f\3\2\2")
        buf.write("\2\2\u00a1\3\2\2\2\3\u00a3\3\2\2\2\5\u00a5\3\2\2\2\7\u00a7")
        buf.write("\3\2\2\2\t\u00a9\3\2\2\2\13\u00ab\3\2\2\2\r\u00b1\3\2")
        buf.write("\2\2\17\u00b7\3\2\2\2\21\u00c1\3\2\2\2\23\u00c3\3\2\2")
        buf.write("\2\25\u00ca\3\2\2\2\27\u00d8\3\2\2\2\31\u00db\3\2\2\2")
        buf.write("\33\u00e6\3\2\2\2\35\u00e8\3\2\2\2\37\u00f4\3\2\2\2!\u00fc")
        buf.write("\3\2\2\2#\u0106\3\2\2\2%\u0108\3\2\2\2\'\u0114\3\2\2\2")
        buf.write(")\u012d\3\2\2\2+\u0132\3\2\2\2-\u0138\3\2\2\2/\u0141\3")
        buf.write("\2\2\2\61\u0144\3\2\2\2\63\u0149\3\2\2\2\65\u0150\3\2")
        buf.write("\2\2\67\u0158\3\2\2\29\u015e\3\2\2\2;\u0165\3\2\2\2=\u016e")
        buf.write("\3\2\2\2?\u0172\3\2\2\2A\u017b\3\2\2\2C\u017e\3\2\2\2")
        buf.write("E\u0188\3\2\2\2G\u018f\3\2\2\2I\u0194\3\2\2\2K\u0198\3")
        buf.write("\2\2\2M\u019e\3\2\2\2O\u01a3\3\2\2\2Q\u01a9\3\2\2\2S\u01af")
        buf.write("\3\2\2\2U\u01b1\3\2\2\2W\u01b3\3\2\2\2Y\u01b5\3\2\2\2")
        buf.write("[\u01b7\3\2\2\2]\u01b9\3\2\2\2_\u01bc\3\2\2\2a\u01bf\3")
        buf.write("\2\2\2c\u01c2\3\2\2\2e\u01c5\3\2\2\2g\u01c8\3\2\2\2i\u01cb")
        buf.write("\3\2\2\2k\u01cd\3\2\2\2m\u01cf\3\2\2\2o\u01d2\3\2\2\2")
        buf.write("q\u01d5\3\2\2\2s\u01d9\3\2\2\2u\u01dc\3\2\2\2w\u01df\3")
        buf.write("\2\2\2y\u01e3\3\2\2\2{\u01e7\3\2\2\2}\u01e9\3\2\2\2\177")
        buf.write("\u01ec\3\2\2\2\u0081\u01ef\3\2\2\2\u0083\u01f1\3\2\2\2")
        buf.write("\u0085\u01f3\3\2\2\2\u0087\u01f5\3\2\2\2\u0089\u01f7\3")
        buf.write("\2\2\2\u008b\u01f9\3\2\2\2\u008d\u01fb\3\2\2\2\u008f\u01fd")
        buf.write("\3\2\2\2\u0091\u01ff\3\2\2\2\u0093\u0201\3\2\2\2\u0095")
        buf.write("\u0203\3\2\2\2\u0097\u0205\3\2\2\2\u0099\u020c\3\2\2\2")
        buf.write("\u009b\u021b\3\2\2\2\u009d\u0221\3\2\2\2\u009f\u022e\3")
        buf.write("\2\2\2\u00a1\u0239\3\2\2\2\u00a3\u00a4\t\2\2\2\u00a4\4")
        buf.write("\3\2\2\2\u00a5\u00a6\t\3\2\2\u00a6\6\3\2\2\2\u00a7\u00a8")
        buf.write("\t\4\2\2\u00a8\b\3\2\2\2\u00a9\u00aa\t\5\2\2\u00aa\n\3")
        buf.write("\2\2\2\u00ab\u00ac\t\6\2\2\u00ac\f\3\2\2\2\u00ad\u00ae")
        buf.write("\7\62\2\2\u00ae\u00b2\7Z\2\2\u00af\u00b0\7\62\2\2\u00b0")
        buf.write("\u00b2\7z\2\2\u00b1\u00ad\3\2\2\2\u00b1\u00af\3\2\2\2")
        buf.write("\u00b2\16\3\2\2\2\u00b3\u00b4\7\62\2\2\u00b4\u00b8\7Q")
        buf.write("\2\2\u00b5\u00b6\7\62\2\2\u00b6\u00b8\7q\2\2\u00b7\u00b3")
        buf.write("\3\2\2\2\u00b7\u00b5\3\2\2\2\u00b8\20\3\2\2\2\u00b9\u00c2")
        buf.write("\7\62\2\2\u00ba\u00be\t\3\2\2\u00bb\u00bd\t\2\2\2\u00bc")
        buf.write("\u00bb\3\2\2\2\u00bd\u00c0\3\2\2\2\u00be\u00bc\3\2\2\2")
        buf.write("\u00be\u00bf\3\2\2\2\u00bf\u00c2\3\2\2\2\u00c0\u00be\3")
        buf.write("\2\2\2\u00c1\u00b9\3\2\2\2\u00c1\u00ba\3\2\2\2\u00c2\22")
        buf.write("\3\2\2\2\u00c3\u00c7\7\60\2\2\u00c4\u00c6\t\2\2\2\u00c5")
        buf.write("\u00c4\3\2\2\2\u00c6\u00c9\3\2\2\2\u00c7\u00c5\3\2\2\2")
        buf.write("\u00c7\u00c8\3\2\2\2\u00c8\24\3\2\2\2\u00c9\u00c7\3\2")
        buf.write("\2\2\u00ca\u00cc\t\7\2\2\u00cb\u00cd\t\b\2\2\u00cc\u00cb")
        buf.write("\3\2\2\2\u00cc\u00cd\3\2\2\2\u00cd\u00d6\3\2\2\2\u00ce")
        buf.write("\u00d7\7\62\2\2\u00cf\u00d3\t\3\2\2\u00d0\u00d2\t\2\2")
        buf.write("\2\u00d1\u00d0\3\2\2\2\u00d2\u00d5\3\2\2\2\u00d3\u00d1")
        buf.write("\3\2\2\2\u00d3\u00d4\3\2\2\2\u00d4\u00d7\3\2\2\2\u00d5")
        buf.write("\u00d3\3\2\2\2\u00d6\u00ce\3\2\2\2\u00d6\u00cf\3\2\2\2")
        buf.write("\u00d7\26\3\2\2\2\u00d8\u00d9\7^\2\2\u00d9\u00da\t\t\2")
        buf.write("\2\u00da\30\3\2\2\2\u00db\u00dc\7)\2\2\u00dc\u00dd\7$")
        buf.write("\2\2\u00dd\32\3\2\2\2\u00de\u00e7\7\62\2\2\u00df\u00e3")
        buf.write("\5\5\3\2\u00e0\u00e2\5\3\2\2\u00e1\u00e0\3\2\2\2\u00e2")
        buf.write("\u00e5\3\2\2\2\u00e3\u00e1\3\2\2\2\u00e3\u00e4\3\2\2\2")
        buf.write("\u00e4\u00e7\3\2\2\2\u00e5\u00e3\3\2\2\2\u00e6\u00de\3")
        buf.write("\2\2\2\u00e6\u00df\3\2\2\2\u00e7\34\3\2\2\2\u00e8\u00eb")
        buf.write("\5\r\7\2\u00e9\u00ec\5\5\3\2\u00ea\u00ec\5\13\6\2\u00eb")
        buf.write("\u00e9\3\2\2\2\u00eb\u00ea\3\2\2\2\u00ec\u00f1\3\2\2\2")
        buf.write("\u00ed\u00f0\5\3\2\2\u00ee\u00f0\5\13\6\2\u00ef\u00ed")
        buf.write("\3\2\2\2\u00ef\u00ee\3\2\2\2\u00f0\u00f3\3\2\2\2\u00f1")
        buf.write("\u00ef\3\2\2\2\u00f1\u00f2\3\2\2\2\u00f2\36\3\2\2\2\u00f3")
        buf.write("\u00f1\3\2\2\2\u00f4\u00f5\5\17\b\2\u00f5\u00f9\5\7\4")
        buf.write("\2\u00f6\u00f8\5\t\5\2\u00f7\u00f6\3\2\2\2\u00f8\u00fb")
        buf.write("\3\2\2\2\u00f9\u00f7\3\2\2\2\u00f9\u00fa\3\2\2\2\u00fa")
        buf.write(" \3\2\2\2\u00fb\u00f9\3\2\2\2\u00fc\u0102\5\21\t\2\u00fd")
        buf.write("\u00ff\5\23\n\2\u00fe\u0100\5\25\13\2\u00ff\u00fe\3\2")
        buf.write("\2\2\u00ff\u0100\3\2\2\2\u0100\u0103\3\2\2\2\u0101\u0103")
        buf.write("\5\25\13\2\u0102\u00fd\3\2\2\2\u0102\u0101\3\2\2\2\u0103")
        buf.write("\"\3\2\2\2\u0104\u0107\5M\'\2\u0105\u0107\5O(\2\u0106")
        buf.write("\u0104\3\2\2\2\u0106\u0105\3\2\2\2\u0107$\3\2\2\2\u0108")
        buf.write("\u010e\7$\2\2\u0109\u010d\5\31\r\2\u010a\u010d\5\27\f")
        buf.write("\2\u010b\u010d\n\n\2\2\u010c\u0109\3\2\2\2\u010c\u010a")
        buf.write("\3\2\2\2\u010c\u010b\3\2\2\2\u010d\u0110\3\2\2\2\u010e")
        buf.write("\u010c\3\2\2\2\u010e\u010f\3\2\2\2\u010f\u0111\3\2\2\2")
        buf.write("\u0110\u010e\3\2\2\2\u0111\u0112\7$\2\2\u0112\u0113\b")
        buf.write("\23\2\2\u0113&\3\2\2\2\u0114\u011b\7}\2\2\u0115\u011c")
        buf.write("\5\33\16\2\u0116\u011c\5\35\17\2\u0117\u011c\5\37\20\2")
        buf.write("\u0118\u011c\5!\21\2\u0119\u011c\5%\23\2\u011a\u011c\5")
        buf.write("\'\24\2\u011b\u0115\3\2\2\2\u011b\u0116\3\2\2\2\u011b")
        buf.write("\u0117\3\2\2\2\u011b\u0118\3\2\2\2\u011b\u0119\3\2\2\2")
        buf.write("\u011b\u011a\3\2\2\2\u011c\u0128\3\2\2\2\u011d\u0124\7")
        buf.write(".\2\2\u011e\u0125\5\33\16\2\u011f\u0125\5\35\17\2\u0120")
        buf.write("\u0125\5\37\20\2\u0121\u0125\5!\21\2\u0122\u0125\5%\23")
        buf.write("\2\u0123\u0125\5\'\24\2\u0124\u011e\3\2\2\2\u0124\u011f")
        buf.write("\3\2\2\2\u0124\u0120\3\2\2\2\u0124\u0121\3\2\2\2\u0124")
        buf.write("\u0122\3\2\2\2\u0124\u0123\3\2\2\2\u0125\u0127\3\2\2\2")
        buf.write("\u0126\u011d\3\2\2\2\u0127\u012a\3\2\2\2\u0128\u0126\3")
        buf.write("\2\2\2\u0128\u0129\3\2\2\2\u0129\u012b\3\2\2\2\u012a\u0128")
        buf.write("\3\2\2\2\u012b\u012c\7\177\2\2\u012c(\3\2\2\2\u012d\u012e")
        buf.write("\7D\2\2\u012e\u012f\7q\2\2\u012f\u0130\7f\2\2\u0130\u0131")
        buf.write("\7{\2\2\u0131*\3\2\2\2\u0132\u0133\7D\2\2\u0133\u0134")
        buf.write("\7t\2\2\u0134\u0135\7g\2\2\u0135\u0136\7c\2\2\u0136\u0137")
        buf.write("\7m\2\2\u0137,\3\2\2\2\u0138\u0139\7E\2\2\u0139\u013a")
        buf.write("\7q\2\2\u013a\u013b\7p\2\2\u013b\u013c\7v\2\2\u013c\u013d")
        buf.write("\7k\2\2\u013d\u013e\7p\2\2\u013e\u013f\7w\2\2\u013f\u0140")
        buf.write("\7g\2\2\u0140.\3\2\2\2\u0141\u0142\7F\2\2\u0142\u0143")
        buf.write("\7q\2\2\u0143\60\3\2\2\2\u0144\u0145\7G\2\2\u0145\u0146")
        buf.write("\7n\2\2\u0146\u0147\7u\2\2\u0147\u0148\7g\2\2\u0148\62")
        buf.write("\3\2\2\2\u0149\u014a\7G\2\2\u014a\u014b\7n\2\2\u014b\u014c")
        buf.write("\7u\2\2\u014c\u014d\7g\2\2\u014d\u014e\7K\2\2\u014e\u014f")
        buf.write("\7h\2\2\u014f\64\3\2\2\2\u0150\u0151\7G\2\2\u0151\u0152")
        buf.write("\7p\2\2\u0152\u0153\7f\2\2\u0153\u0154\7d\2\2\u0154\u0155")
        buf.write("\7q\2\2\u0155\u0156\7f\2\2\u0156\u0157\7{\2\2\u0157\66")
        buf.write("\3\2\2\2\u0158\u0159\7G\2\2\u0159\u015a\7p\2\2\u015a\u015b")
        buf.write("\7f\2\2\u015b\u015c\7k\2\2\u015c\u015d\7h\2\2\u015d8\3")
        buf.write("\2\2\2\u015e\u015f\7G\2\2\u015f\u0160\7p\2\2\u0160\u0161")
        buf.write("\7f\2\2\u0161\u0162\7h\2\2\u0162\u0163\7q\2\2\u0163\u0164")
        buf.write("\7t\2\2\u0164:\3\2\2\2\u0165\u0166\7G\2\2\u0166\u0167")
        buf.write("\7p\2\2\u0167\u0168\7f\2\2\u0168\u0169\7y\2\2\u0169\u016a")
        buf.write("\7j\2\2\u016a\u016b\7k\2\2\u016b\u016c\7n\2\2\u016c\u016d")
        buf.write("\7g\2\2\u016d<\3\2\2\2\u016e\u016f\7H\2\2\u016f\u0170")
        buf.write("\7q\2\2\u0170\u0171\7t\2\2\u0171>\3\2\2\2\u0172\u0173")
        buf.write("\7H\2\2\u0173\u0174\7w\2\2\u0174\u0175\7p\2\2\u0175\u0176")
        buf.write("\7e\2\2\u0176\u0177\7v\2\2\u0177\u0178\7k\2\2\u0178\u0179")
        buf.write("\7q\2\2\u0179\u017a\7p\2\2\u017a@\3\2\2\2\u017b\u017c")
        buf.write("\7K\2\2\u017c\u017d\7h\2\2\u017dB\3\2\2\2\u017e\u017f")
        buf.write("\7R\2\2\u017f\u0180\7c\2\2\u0180\u0181\7t\2\2\u0181\u0182")
        buf.write("\7c\2\2\u0182\u0183\7o\2\2\u0183\u0184\7g\2\2\u0184\u0185")
        buf.write("\7v\2\2\u0185\u0186\7g\2\2\u0186\u0187\7t\2\2\u0187D\3")
        buf.write("\2\2\2\u0188\u0189\7T\2\2\u0189\u018a\7g\2\2\u018a\u018b")
        buf.write("\7v\2\2\u018b\u018c\7w\2\2\u018c\u018d\7t\2\2\u018d\u018e")
        buf.write("\7p\2\2\u018eF\3\2\2\2\u018f\u0190\7V\2\2\u0190\u0191")
        buf.write("\7j\2\2\u0191\u0192\7g\2\2\u0192\u0193\7p\2\2\u0193H\3")
        buf.write("\2\2\2\u0194\u0195\7X\2\2\u0195\u0196\7c\2\2\u0196\u0197")
        buf.write("\7t\2\2\u0197J\3\2\2\2\u0198\u0199\7Y\2\2\u0199\u019a")
        buf.write("\7j\2\2\u019a\u019b\7k\2\2\u019b\u019c\7n\2\2\u019c\u019d")
        buf.write("\7g\2\2\u019dL\3\2\2\2\u019e\u019f\7V\2\2\u019f\u01a0")
        buf.write("\7t\2\2\u01a0\u01a1\7w\2\2\u01a1\u01a2\7g\2\2\u01a2N\3")
        buf.write("\2\2\2\u01a3\u01a4\7H\2\2\u01a4\u01a5\7c\2\2\u01a5\u01a6")
        buf.write("\7n\2\2\u01a6\u01a7\7u\2\2\u01a7\u01a8\7g\2\2\u01a8P\3")
        buf.write("\2\2\2\u01a9\u01aa\7G\2\2\u01aa\u01ab\7p\2\2\u01ab\u01ac")
        buf.write("\7f\2\2\u01ac\u01ad\7f\2\2\u01ad\u01ae\7q\2\2\u01aeR\3")
        buf.write("\2\2\2\u01af\u01b0\7-\2\2\u01b0T\3\2\2\2\u01b1\u01b2\7")
        buf.write("/\2\2\u01b2V\3\2\2\2\u01b3\u01b4\7,\2\2\u01b4X\3\2\2\2")
        buf.write("\u01b5\u01b6\7^\2\2\u01b6Z\3\2\2\2\u01b7\u01b8\7\'\2\2")
        buf.write("\u01b8\\\3\2\2\2\u01b9\u01ba\7-\2\2\u01ba\u01bb\7\60\2")
        buf.write("\2\u01bb^\3\2\2\2\u01bc\u01bd\7/\2\2\u01bd\u01be\7\60")
        buf.write("\2\2\u01be`\3\2\2\2\u01bf\u01c0\7,\2\2\u01c0\u01c1\7\60")
        buf.write("\2\2\u01c1b\3\2\2\2\u01c2\u01c3\7^\2\2\u01c3\u01c4\7\60")
        buf.write("\2\2\u01c4d\3\2\2\2\u01c5\u01c6\7?\2\2\u01c6\u01c7\7?")
        buf.write("\2\2\u01c7f\3\2\2\2\u01c8\u01c9\7#\2\2\u01c9\u01ca\7?")
        buf.write("\2\2\u01cah\3\2\2\2\u01cb\u01cc\7>\2\2\u01ccj\3\2\2\2")
        buf.write("\u01cd\u01ce\7@\2\2\u01cel\3\2\2\2\u01cf\u01d0\7>\2\2")
        buf.write("\u01d0\u01d1\7?\2\2\u01d1n\3\2\2\2\u01d2\u01d3\7@\2\2")
        buf.write("\u01d3\u01d4\7?\2\2\u01d4p\3\2\2\2\u01d5\u01d6\7?\2\2")
        buf.write("\u01d6\u01d7\7\61\2\2\u01d7\u01d8\7?\2\2\u01d8r\3\2\2")
        buf.write("\2\u01d9\u01da\7>\2\2\u01da\u01db\7\60\2\2\u01dbt\3\2")
        buf.write("\2\2\u01dc\u01dd\7@\2\2\u01dd\u01de\7\60\2\2\u01dev\3")
        buf.write("\2\2\2\u01df\u01e0\7>\2\2\u01e0\u01e1\7?\2\2\u01e1\u01e2")
        buf.write("\7\60\2\2\u01e2x\3\2\2\2\u01e3\u01e4\7@\2\2\u01e4\u01e5")
        buf.write("\7?\2\2\u01e5\u01e6\7\60\2\2\u01e6z\3\2\2\2\u01e7\u01e8")
        buf.write("\7#\2\2\u01e8|\3\2\2\2\u01e9\u01ea\7(\2\2\u01ea\u01eb")
        buf.write("\7(\2\2\u01eb~\3\2\2\2\u01ec\u01ed\7~\2\2\u01ed\u01ee")
        buf.write("\7~\2\2\u01ee\u0080\3\2\2\2\u01ef\u01f0\7?\2\2\u01f0\u0082")
        buf.write("\3\2\2\2\u01f1\u01f2\7]\2\2\u01f2\u0084\3\2\2\2\u01f3")
        buf.write("\u01f4\7_\2\2\u01f4\u0086\3\2\2\2\u01f5\u01f6\7*\2\2\u01f6")
        buf.write("\u0088\3\2\2\2\u01f7\u01f8\7+\2\2\u01f8\u008a\3\2\2\2")
        buf.write("\u01f9\u01fa\7}\2\2\u01fa\u008c\3\2\2\2\u01fb\u01fc\7")
        buf.write("\177\2\2\u01fc\u008e\3\2\2\2\u01fd\u01fe\7=\2\2\u01fe")
        buf.write("\u0090\3\2\2\2\u01ff\u0200\7<\2\2\u0200\u0092\3\2\2\2")
        buf.write("\u0201\u0202\7.\2\2\u0202\u0094\3\2\2\2\u0203\u0204\7")
        buf.write("\60\2\2\u0204\u0096\3\2\2\2\u0205\u0209\t\13\2\2\u0206")
        buf.write("\u0208\t\f\2\2\u0207\u0206\3\2\2\2\u0208\u020b\3\2\2\2")
        buf.write("\u0209\u0207\3\2\2\2\u0209\u020a\3\2\2\2\u020a\u0098\3")
        buf.write("\2\2\2\u020b\u0209\3\2\2\2\u020c\u020d\7,\2\2\u020d\u020e")
        buf.write("\7,\2\2\u020e\u0212\3\2\2\2\u020f\u0211\13\2\2\2\u0210")
        buf.write("\u020f\3\2\2\2\u0211\u0214\3\2\2\2\u0212\u0213\3\2\2\2")
        buf.write("\u0212\u0210\3\2\2\2\u0213\u0215\3\2\2\2\u0214\u0212\3")
        buf.write("\2\2\2\u0215\u0216\7,\2\2\u0216\u0217\7,\2\2\u0217\u0218")
        buf.write("\3\2\2\2\u0218\u0219\bM\3\2\u0219\u009a\3\2\2\2\u021a")
        buf.write("\u021c\t\r\2\2\u021b\u021a\3\2\2\2\u021c\u021d\3\2\2\2")
        buf.write("\u021d\u021b\3\2\2\2\u021d\u021e\3\2\2\2\u021e\u021f\3")
        buf.write("\2\2\2\u021f\u0220\bN\3\2\u0220\u009c\3\2\2\2\u0221\u0227")
        buf.write("\7$\2\2\u0222\u0226\5\31\r\2\u0223\u0226\5\27\f\2\u0224")
        buf.write("\u0226\n\n\2\2\u0225\u0222\3\2\2\2\u0225\u0223\3\2\2\2")
        buf.write("\u0225\u0224\3\2\2\2\u0226\u0229\3\2\2\2\u0227\u0225\3")
        buf.write("\2\2\2\u0227\u0228\3\2\2\2\u0228\u022a\3\2\2\2\u0229\u0227")
        buf.write("\3\2\2\2\u022a\u022b\7^\2\2\u022b\u022c\n\t\2\2\u022c")
        buf.write("\u022d\bO\4\2\u022d\u009e\3\2\2\2\u022e\u0234\7$\2\2\u022f")
        buf.write("\u0233\5\31\r\2\u0230\u0233\5\27\f\2\u0231\u0233\n\n\2")
        buf.write("\2\u0232\u022f\3\2\2\2\u0232\u0230\3\2\2\2\u0232\u0231")
        buf.write("\3\2\2\2\u0233\u0236\3\2\2\2\u0234\u0232\3\2\2\2\u0234")
        buf.write("\u0235\3\2\2\2\u0235\u0237\3\2\2\2\u0236\u0234\3\2\2\2")
        buf.write("\u0237\u0238\bP\5\2\u0238\u00a0\3\2\2\2\u0239\u023a\13")
        buf.write("\2\2\2\u023a\u023b\bQ\6\2\u023b\u00a2\3\2\2\2 \2\u00b1")
        buf.write("\u00b7\u00be\u00c1\u00c7\u00cc\u00d3\u00d6\u00e3\u00e6")
        buf.write("\u00eb\u00ef\u00f1\u00f9\u00ff\u0102\u0106\u010c\u010e")
        buf.write("\u011b\u0124\u0128\u0209\u0212\u021d\u0225\u0227\u0232")
        buf.write("\u0234\7\3\23\2\b\2\2\3O\3\3P\4\3Q\5")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    DEC_INT_LIT = 1
    HEX_INT_LIT = 2
    OCT_INT_LIT = 3
    FLT_LIT = 4
    BOOL_LIT = 5
    STR_LIT = 6
    ARRAY_LIT = 7
    BODY = 8
    BREAK = 9
    CONTINUE = 10
    DO = 11
    ELSE = 12
    ELSEIF = 13
    ENDBODY = 14
    ENDIF = 15
    ENDFOR = 16
    ENDWHILE = 17
    FOR = 18
    FUNCTION = 19
    IF = 20
    PARAMETER = 21
    RETURN = 22
    THEN = 23
    VAR = 24
    WHILE = 25
    TRUE = 26
    FALSE = 27
    ENDDO = 28
    ADD_I = 29
    SUB_I = 30
    MUL_I = 31
    DIV_I = 32
    MOD_I = 33
    ADD_F = 34
    SUB_F = 35
    MUL_F = 36
    DIV_F = 37
    EQ_I = 38
    NEQ_I = 39
    LT_I = 40
    GT_I = 41
    LTE_I = 42
    GTE_I = 43
    NEQ_F = 44
    LT_F = 45
    GT_F = 46
    LTE_F = 47
    GTE_F = 48
    NOT = 49
    AND = 50
    OR = 51
    ASSIGN = 52
    LS = 53
    RS = 54
    LB = 55
    RB = 56
    LC = 57
    RC = 58
    SEMI = 59
    COLON = 60
    COMMA = 61
    DOT = 62
    ID = 63
    COMMENT = 64
    WS = 65
    ILLEGAL_ESCAPE = 66
    UNCLOSE_STRING = 67
    ERROR_CHAR = 68

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Body'", "'Break'", "'Continue'", "'Do'", "'Else'", "'ElseIf'", 
            "'Endbody'", "'Endif'", "'Endfor'", "'Endwhile'", "'For'", "'Function'", 
            "'If'", "'Parameter'", "'Return'", "'Then'", "'Var'", "'While'", 
            "'True'", "'False'", "'Enddo'", "'+'", "'-'", "'*'", "'\\'", 
            "'%'", "'+.'", "'-.'", "'*.'", "'\\.'", "'=='", "'!='", "'<'", 
            "'>'", "'<='", "'>='", "'=/='", "'<.'", "'>.'", "'<=.'", "'>=.'", 
            "'!'", "'&&'", "'||'", "'='", "'['", "']'", "'('", "')'", "'{'", 
            "'}'", "';'", "':'", "','", "'.'" ]

    symbolicNames = [ "<INVALID>",
            "DEC_INT_LIT", "HEX_INT_LIT", "OCT_INT_LIT", "FLT_LIT", "BOOL_LIT", 
            "STR_LIT", "ARRAY_LIT", "BODY", "BREAK", "CONTINUE", "DO", "ELSE", 
            "ELSEIF", "ENDBODY", "ENDIF", "ENDFOR", "ENDWHILE", "FOR", "FUNCTION", 
            "IF", "PARAMETER", "RETURN", "THEN", "VAR", "WHILE", "TRUE", 
            "FALSE", "ENDDO", "ADD_I", "SUB_I", "MUL_I", "DIV_I", "MOD_I", 
            "ADD_F", "SUB_F", "MUL_F", "DIV_F", "EQ_I", "NEQ_I", "LT_I", 
            "GT_I", "LTE_I", "GTE_I", "NEQ_F", "LT_F", "GT_F", "LTE_F", 
            "GTE_F", "NOT", "AND", "OR", "ASSIGN", "LS", "RS", "LB", "RB", 
            "LC", "RC", "SEMI", "COLON", "COMMA", "DOT", "ID", "COMMENT", 
            "WS", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "ERROR_CHAR" ]

    ruleNames = [ "DEGIT", "DEGIT_NO_ZERO", "OCT_DEGIT", "OCT_DEGIT_NO_ZERO", 
                  "HEX_CHAR", "HEX_PREFIX", "OCT_PREFIX", "FLT_INT_PART", 
                  "FLT_DEC_PART", "FLT_EXP_PART", "ESCAPE_CHAR", "DOUBLE_QUOTE_CHAR", 
                  "DEC_INT_LIT", "HEX_INT_LIT", "OCT_INT_LIT", "FLT_LIT", 
                  "BOOL_LIT", "STR_LIT", "ARRAY_LIT", "BODY", "BREAK", "CONTINUE", 
                  "DO", "ELSE", "ELSEIF", "ENDBODY", "ENDIF", "ENDFOR", 
                  "ENDWHILE", "FOR", "FUNCTION", "IF", "PARAMETER", "RETURN", 
                  "THEN", "VAR", "WHILE", "TRUE", "FALSE", "ENDDO", "ADD_I", 
                  "SUB_I", "MUL_I", "DIV_I", "MOD_I", "ADD_F", "SUB_F", 
                  "MUL_F", "DIV_F", "EQ_I", "NEQ_I", "LT_I", "GT_I", "LTE_I", 
                  "GTE_I", "NEQ_F", "LT_F", "GT_F", "LTE_F", "GTE_F", "NOT", 
                  "AND", "OR", "ASSIGN", "LS", "RS", "LB", "RB", "LC", "RC", 
                  "SEMI", "COLON", "COMMA", "DOT", "ID", "COMMENT", "WS", 
                  "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "ERROR_CHAR" ]

    grammarFileName = "BKIT.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        result = super().emit()
        if tk == self.UNCLOSE_STRING:       
            raise UncloseString(result.text)
        elif tk == self.ILLEGAL_ESCAPE:
            raise IllegalEscape(result.text)
        elif tk == self.ERROR_CHAR:
            raise ErrorToken(result.text)
        else:
            return result;


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[17] = self.STR_LIT_action 
            actions[77] = self.ILLEGAL_ESCAPE_action 
            actions[78] = self.UNCLOSE_STRING_action 
            actions[79] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STR_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:-1]
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                raise IllegalEscape(self.text[1:])

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            	raise UncloseString(self.text[1:])

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            	raise ErrorToken(self.text);

     


