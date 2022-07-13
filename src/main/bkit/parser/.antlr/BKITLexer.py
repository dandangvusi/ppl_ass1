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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2D")
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
        buf.write("\n\13\3\f\3\f\3\f\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\5\16\u00e6\n\16\3\16\3\16\3\16\3\16\3\16\3")
        buf.write("\16\3\16\5\16\u00ef\n\16\7\16\u00f1\n\16\f\16\16\16\u00f4")
        buf.write("\13\16\3\16\3\16\3\17\3\17\3\17\7\17\u00fb\n\17\f\17\16")
        buf.write("\17\u00fe\13\17\5\17\u0100\n\17\3\20\3\20\3\20\5\20\u0105")
        buf.write("\n\20\3\20\3\20\7\20\u0109\n\20\f\20\16\20\u010c\13\20")
        buf.write("\3\21\3\21\3\21\7\21\u0111\n\21\f\21\16\21\u0114\13\21")
        buf.write("\3\22\3\22\3\22\5\22\u0119\n\22\3\22\5\22\u011c\n\22\3")
        buf.write("\23\3\23\5\23\u0120\n\23\3\24\3\24\3\24\3\24\7\24\u0126")
        buf.write("\n\24\f\24\16\24\u0129\13\24\3\24\3\24\3\24\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37")
        buf.write("\3\37\3 \3 \3 \3 \3 \3 \3 \3 \3 \3!\3!\3!\3\"\3\"\3\"")
        buf.write("\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3#\3$\3")
        buf.write("$\3$\3$\3$\3%\3%\3%\3%\3&\3&\3&\3&\3&\3&\3\'\3\'\3\'\3")
        buf.write("\'\3\'\3(\3(\3(\3(\3(\3(\3)\3)\3)\3)\3)\3)\3*\3*\3+\3")
        buf.write("+\3,\3,\3-\3-\3.\3.\3/\3/\3/\3\60\3\60\3\60\3\61\3\61")
        buf.write("\3\61\3\62\3\62\3\62\3\63\3\63\3\63\3\64\3\64\3\64\3\65")
        buf.write("\3\65\3\66\3\66\3\67\3\67\3\67\38\38\38\39\39\39\39\3")
        buf.write(":\3:\3:\3;\3;\3;\3<\3<\3<\3<\3=\3=\3=\3=\3>\3>\3?\3?\3")
        buf.write("?\3@\3@\3@\3A\3A\3B\3B\3C\3C\3D\3D\3E\3E\3F\3F\3G\3G\3")
        buf.write("H\3H\3I\3I\3J\3J\3K\3K\3L\3L\7L\u0208\nL\fL\16L\u020b")
        buf.write("\13L\3M\3M\3M\3M\7M\u0211\nM\fM\16M\u0214\13M\3M\3M\3")
        buf.write("M\3M\3M\3N\6N\u021c\nN\rN\16N\u021d\3N\3N\3O\3O\3O\3O")
        buf.write("\7O\u0226\nO\fO\16O\u0229\13O\3O\3O\3O\3O\3P\3P\3P\3P")
        buf.write("\7P\u0233\nP\fP\16P\u0236\13P\3P\3P\3Q\3Q\3Q\3\u0212\2")
        buf.write("R\3\2\5\2\7\2\t\2\13\2\r\2\17\2\21\2\23\2\25\2\27\2\31")
        buf.write("\2\33\3\35\4\37\5!\6#\7%\b\'\t)\n+\13-\f/\r\61\16\63\17")
        buf.write("\65\20\67\219\22;\23=\24?\25A\26C\27E\30G\31I\32K\33M")
        buf.write("\2O\2Q\34S\35U\36W\37Y [!]\"_#a$c%e&g\'i(k)m*o+q,s-u.")
        buf.write("w/y\60{\61}\62\177\63\u0081\64\u0083\65\u0085\66\u0087")
        buf.write("\67\u00898\u008b9\u008d:\u008f;\u0091<\u0093=\u0095>\u0097")
        buf.write("?\u0099@\u009bA\u009dB\u009fC\u00a1D\3\2\16\3\2\62;\3")
        buf.write("\2\63;\3\2\629\3\2\639\3\2CH\4\2GGgg\4\2--//\t\2))^^d")
        buf.write("dhhppttvv\6\2\f\f\17\17$$^^\3\2c|\6\2\62;C\\aac|\5\2\13")
        buf.write("\f\17\17\"\"\2\u0255\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3")
        buf.write("\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2")
        buf.write(")\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2")
        buf.write("\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2")
        buf.write(";\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2")
        buf.write("\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2Q\3\2\2")
        buf.write("\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2")
        buf.write("\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3")
        buf.write("\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o")
        buf.write("\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2")
        buf.write("y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081")
        buf.write("\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2")
        buf.write("\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f")
        buf.write("\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2")
        buf.write("\2\2\u0097\3\2\2\2\2\u0099\3\2\2\2\2\u009b\3\2\2\2\2\u009d")
        buf.write("\3\2\2\2\2\u009f\3\2\2\2\2\u00a1\3\2\2\2\3\u00a3\3\2\2")
        buf.write("\2\5\u00a5\3\2\2\2\7\u00a7\3\2\2\2\t\u00a9\3\2\2\2\13")
        buf.write("\u00ab\3\2\2\2\r\u00b1\3\2\2\2\17\u00b7\3\2\2\2\21\u00c1")
        buf.write("\3\2\2\2\23\u00c3\3\2\2\2\25\u00ca\3\2\2\2\27\u00d8\3")
        buf.write("\2\2\2\31\u00db\3\2\2\2\33\u00de\3\2\2\2\35\u00ff\3\2")
        buf.write("\2\2\37\u0101\3\2\2\2!\u010d\3\2\2\2#\u0115\3\2\2\2%\u011f")
        buf.write("\3\2\2\2\'\u0121\3\2\2\2)\u012d\3\2\2\2+\u0132\3\2\2\2")
        buf.write("-\u0138\3\2\2\2/\u0141\3\2\2\2\61\u0144\3\2\2\2\63\u0149")
        buf.write("\3\2\2\2\65\u0150\3\2\2\2\67\u0158\3\2\2\29\u015e\3\2")
        buf.write("\2\2;\u0165\3\2\2\2=\u016e\3\2\2\2?\u0172\3\2\2\2A\u017b")
        buf.write("\3\2\2\2C\u017e\3\2\2\2E\u0188\3\2\2\2G\u018f\3\2\2\2")
        buf.write("I\u0194\3\2\2\2K\u0198\3\2\2\2M\u019e\3\2\2\2O\u01a3\3")
        buf.write("\2\2\2Q\u01a9\3\2\2\2S\u01af\3\2\2\2U\u01b1\3\2\2\2W\u01b3")
        buf.write("\3\2\2\2Y\u01b5\3\2\2\2[\u01b7\3\2\2\2]\u01b9\3\2\2\2")
        buf.write("_\u01bc\3\2\2\2a\u01bf\3\2\2\2c\u01c2\3\2\2\2e\u01c5\3")
        buf.write("\2\2\2g\u01c8\3\2\2\2i\u01cb\3\2\2\2k\u01cd\3\2\2\2m\u01cf")
        buf.write("\3\2\2\2o\u01d2\3\2\2\2q\u01d5\3\2\2\2s\u01d9\3\2\2\2")
        buf.write("u\u01dc\3\2\2\2w\u01df\3\2\2\2y\u01e3\3\2\2\2{\u01e7\3")
        buf.write("\2\2\2}\u01e9\3\2\2\2\177\u01ec\3\2\2\2\u0081\u01ef\3")
        buf.write("\2\2\2\u0083\u01f1\3\2\2\2\u0085\u01f3\3\2\2\2\u0087\u01f5")
        buf.write("\3\2\2\2\u0089\u01f7\3\2\2\2\u008b\u01f9\3\2\2\2\u008d")
        buf.write("\u01fb\3\2\2\2\u008f\u01fd\3\2\2\2\u0091\u01ff\3\2\2\2")
        buf.write("\u0093\u0201\3\2\2\2\u0095\u0203\3\2\2\2\u0097\u0205\3")
        buf.write("\2\2\2\u0099\u020c\3\2\2\2\u009b\u021b\3\2\2\2\u009d\u0221")
        buf.write("\3\2\2\2\u009f\u022e\3\2\2\2\u00a1\u0239\3\2\2\2\u00a3")
        buf.write("\u00a4\t\2\2\2\u00a4\4\3\2\2\2\u00a5\u00a6\t\3\2\2\u00a6")
        buf.write("\6\3\2\2\2\u00a7\u00a8\t\4\2\2\u00a8\b\3\2\2\2\u00a9\u00aa")
        buf.write("\t\5\2\2\u00aa\n\3\2\2\2\u00ab\u00ac\t\6\2\2\u00ac\f\3")
        buf.write("\2\2\2\u00ad\u00ae\7\62\2\2\u00ae\u00b2\7Z\2\2\u00af\u00b0")
        buf.write("\7\62\2\2\u00b0\u00b2\7z\2\2\u00b1\u00ad\3\2\2\2\u00b1")
        buf.write("\u00af\3\2\2\2\u00b2\16\3\2\2\2\u00b3\u00b4\7\62\2\2\u00b4")
        buf.write("\u00b8\7Q\2\2\u00b5\u00b6\7\62\2\2\u00b6\u00b8\7q\2\2")
        buf.write("\u00b7\u00b3\3\2\2\2\u00b7\u00b5\3\2\2\2\u00b8\20\3\2")
        buf.write("\2\2\u00b9\u00c2\7\62\2\2\u00ba\u00be\t\3\2\2\u00bb\u00bd")
        buf.write("\t\2\2\2\u00bc\u00bb\3\2\2\2\u00bd\u00c0\3\2\2\2\u00be")
        buf.write("\u00bc\3\2\2\2\u00be\u00bf\3\2\2\2\u00bf\u00c2\3\2\2\2")
        buf.write("\u00c0\u00be\3\2\2\2\u00c1\u00b9\3\2\2\2\u00c1\u00ba\3")
        buf.write("\2\2\2\u00c2\22\3\2\2\2\u00c3\u00c7\7\60\2\2\u00c4\u00c6")
        buf.write("\t\2\2\2\u00c5\u00c4\3\2\2\2\u00c6\u00c9\3\2\2\2\u00c7")
        buf.write("\u00c5\3\2\2\2\u00c7\u00c8\3\2\2\2\u00c8\24\3\2\2\2\u00c9")
        buf.write("\u00c7\3\2\2\2\u00ca\u00cc\t\7\2\2\u00cb\u00cd\t\b\2\2")
        buf.write("\u00cc\u00cb\3\2\2\2\u00cc\u00cd\3\2\2\2\u00cd\u00d6\3")
        buf.write("\2\2\2\u00ce\u00d7\7\62\2\2\u00cf\u00d3\t\3\2\2\u00d0")
        buf.write("\u00d2\t\2\2\2\u00d1\u00d0\3\2\2\2\u00d2\u00d5\3\2\2\2")
        buf.write("\u00d3\u00d1\3\2\2\2\u00d3\u00d4\3\2\2\2\u00d4\u00d7\3")
        buf.write("\2\2\2\u00d5\u00d3\3\2\2\2\u00d6\u00ce\3\2\2\2\u00d6\u00cf")
        buf.write("\3\2\2\2\u00d7\26\3\2\2\2\u00d8\u00d9\7^\2\2\u00d9\u00da")
        buf.write("\t\t\2\2\u00da\30\3\2\2\2\u00db\u00dc\7)\2\2\u00dc\u00dd")
        buf.write("\7$\2\2\u00dd\32\3\2\2\2\u00de\u00e5\7}\2\2\u00df\u00e6")
        buf.write("\5\35\17\2\u00e0\u00e6\5\37\20\2\u00e1\u00e6\5!\21\2\u00e2")
        buf.write("\u00e6\5#\22\2\u00e3\u00e6\5\'\24\2\u00e4\u00e6\5\33\16")
        buf.write("\2\u00e5\u00df\3\2\2\2\u00e5\u00e0\3\2\2\2\u00e5\u00e1")
        buf.write("\3\2\2\2\u00e5\u00e2\3\2\2\2\u00e5\u00e3\3\2\2\2\u00e5")
        buf.write("\u00e4\3\2\2\2\u00e6\u00f2\3\2\2\2\u00e7\u00ee\7.\2\2")
        buf.write("\u00e8\u00ef\5\35\17\2\u00e9\u00ef\5\37\20\2\u00ea\u00ef")
        buf.write("\5!\21\2\u00eb\u00ef\5#\22\2\u00ec\u00ef\5\'\24\2\u00ed")
        buf.write("\u00ef\5\33\16\2\u00ee\u00e8\3\2\2\2\u00ee\u00e9\3\2\2")
        buf.write("\2\u00ee\u00ea\3\2\2\2\u00ee\u00eb\3\2\2\2\u00ee\u00ec")
        buf.write("\3\2\2\2\u00ee\u00ed\3\2\2\2\u00ef\u00f1\3\2\2\2\u00f0")
        buf.write("\u00e7\3\2\2\2\u00f1\u00f4\3\2\2\2\u00f2\u00f0\3\2\2\2")
        buf.write("\u00f2\u00f3\3\2\2\2\u00f3\u00f5\3\2\2\2\u00f4\u00f2\3")
        buf.write("\2\2\2\u00f5\u00f6\7\177\2\2\u00f6\34\3\2\2\2\u00f7\u0100")
        buf.write("\7\62\2\2\u00f8\u00fc\5\5\3\2\u00f9\u00fb\5\3\2\2\u00fa")
        buf.write("\u00f9\3\2\2\2\u00fb\u00fe\3\2\2\2\u00fc\u00fa\3\2\2\2")
        buf.write("\u00fc\u00fd\3\2\2\2\u00fd\u0100\3\2\2\2\u00fe\u00fc\3")
        buf.write("\2\2\2\u00ff\u00f7\3\2\2\2\u00ff\u00f8\3\2\2\2\u0100\36")
        buf.write("\3\2\2\2\u0101\u0104\5\r\7\2\u0102\u0105\5\5\3\2\u0103")
        buf.write("\u0105\5\13\6\2\u0104\u0102\3\2\2\2\u0104\u0103\3\2\2")
        buf.write("\2\u0105\u010a\3\2\2\2\u0106\u0109\5\3\2\2\u0107\u0109")
        buf.write("\5\13\6\2\u0108\u0106\3\2\2\2\u0108\u0107\3\2\2\2\u0109")
        buf.write("\u010c\3\2\2\2\u010a\u0108\3\2\2\2\u010a\u010b\3\2\2\2")
        buf.write("\u010b \3\2\2\2\u010c\u010a\3\2\2\2\u010d\u010e\5\17\b")
        buf.write("\2\u010e\u0112\5\7\4\2\u010f\u0111\5\t\5\2\u0110\u010f")
        buf.write("\3\2\2\2\u0111\u0114\3\2\2\2\u0112\u0110\3\2\2\2\u0112")
        buf.write("\u0113\3\2\2\2\u0113\"\3\2\2\2\u0114\u0112\3\2\2\2\u0115")
        buf.write("\u011b\5\21\t\2\u0116\u0118\5\23\n\2\u0117\u0119\5\25")
        buf.write("\13\2\u0118\u0117\3\2\2\2\u0118\u0119\3\2\2\2\u0119\u011c")
        buf.write("\3\2\2\2\u011a\u011c\5\25\13\2\u011b\u0116\3\2\2\2\u011b")
        buf.write("\u011a\3\2\2\2\u011c$\3\2\2\2\u011d\u0120\5M\'\2\u011e")
        buf.write("\u0120\5O(\2\u011f\u011d\3\2\2\2\u011f\u011e\3\2\2\2\u0120")
        buf.write("&\3\2\2\2\u0121\u0127\7$\2\2\u0122\u0126\5\31\r\2\u0123")
        buf.write("\u0126\5\27\f\2\u0124\u0126\n\n\2\2\u0125\u0122\3\2\2")
        buf.write("\2\u0125\u0123\3\2\2\2\u0125\u0124\3\2\2\2\u0126\u0129")
        buf.write("\3\2\2\2\u0127\u0125\3\2\2\2\u0127\u0128\3\2\2\2\u0128")
        buf.write("\u012a\3\2\2\2\u0129\u0127\3\2\2\2\u012a\u012b\7$\2\2")
        buf.write("\u012b\u012c\b\24\2\2\u012c(\3\2\2\2\u012d\u012e\7D\2")
        buf.write("\2\u012e\u012f\7q\2\2\u012f\u0130\7f\2\2\u0130\u0131\7")
        buf.write("{\2\2\u0131*\3\2\2\2\u0132\u0133\7D\2\2\u0133\u0134\7")
        buf.write("t\2\2\u0134\u0135\7g\2\2\u0135\u0136\7c\2\2\u0136\u0137")
        buf.write("\7m\2\2\u0137,\3\2\2\2\u0138\u0139\7E\2\2\u0139\u013a")
        buf.write("\7q\2\2\u013a\u013b\7p\2\2\u013b\u013c\7v\2\2\u013c\u013d")
        buf.write("\7k\2\2\u013d\u013e\7p\2\2\u013e\u013f\7w\2\2\u013f\u0140")
        buf.write("\7g\2\2\u0140.\3\2\2\2\u0141\u0142\7F\2\2\u0142\u0143")
        buf.write("\7q\2\2\u0143\60\3\2\2\2\u0144\u0145\7G\2\2\u0145\u0146")
        buf.write("\7n\2\2\u0146\u0147\7u\2\2\u0147\u0148\7g\2\2\u0148\62")
        buf.write("\3\2\2\2\u0149\u014a\7G\2\2\u014a\u014b\7n\2\2\u014b\u014c")
        buf.write("\7u\2\2\u014c\u014d\7g\2\2\u014d\u014e\7K\2\2\u014e\u014f")
        buf.write("\7h\2\2\u014f\64\3\2\2\2\u0150\u0151\7G\2\2\u0151\u0152")
        buf.write("\7p\2\2\u0152\u0153\7f\2\2\u0153\u0154\7D\2\2\u0154\u0155")
        buf.write("\7q\2\2\u0155\u0156\7f\2\2\u0156\u0157\7{\2\2\u0157\66")
        buf.write("\3\2\2\2\u0158\u0159\7G\2\2\u0159\u015a\7p\2\2\u015a\u015b")
        buf.write("\7f\2\2\u015b\u015c\7K\2\2\u015c\u015d\7h\2\2\u015d8\3")
        buf.write("\2\2\2\u015e\u015f\7G\2\2\u015f\u0160\7p\2\2\u0160\u0161")
        buf.write("\7f\2\2\u0161\u0162\7H\2\2\u0162\u0163\7q\2\2\u0163\u0164")
        buf.write("\7t\2\2\u0164:\3\2\2\2\u0165\u0166\7G\2\2\u0166\u0167")
        buf.write("\7p\2\2\u0167\u0168\7f\2\2\u0168\u0169\7Y\2\2\u0169\u016a")
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
        buf.write("\7f\2\2\u01ac\u01ad\7F\2\2\u01ad\u01ae\7q\2\2\u01aeR\3")
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
        buf.write("\u00b7\u00be\u00c1\u00c7\u00cc\u00d3\u00d6\u00e5\u00ee")
        buf.write("\u00f2\u00fc\u00ff\u0104\u0108\u010a\u0112\u0118\u011b")
        buf.write("\u011f\u0125\u0127\u0209\u0212\u021d\u0225\u0227\u0232")
        buf.write("\u0234\7\3\24\2\b\2\2\3O\3\3P\4\3Q\5")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    ARRAY_LIT = 1
    DEC_INT_LIT = 2
    HEX_INT_LIT = 3
    OCT_INT_LIT = 4
    FLT_LIT = 5
    BOOL_LIT = 6
    STR_LIT = 7
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
    ENDDO = 26
    ADD_I = 27
    SUB_I = 28
    MUL_I = 29
    DIV_I = 30
    MOD_I = 31
    ADD_F = 32
    SUB_F = 33
    MUL_F = 34
    DIV_F = 35
    EQ_I = 36
    NEQ_I = 37
    LT_I = 38
    GT_I = 39
    LTE_I = 40
    GTE_I = 41
    NEQ_F = 42
    LT_F = 43
    GT_F = 44
    LTE_F = 45
    GTE_F = 46
    NOT = 47
    AND = 48
    OR = 49
    ASSIGN = 50
    LS = 51
    RS = 52
    LB = 53
    RB = 54
    LC = 55
    RC = 56
    SEMI = 57
    COLON = 58
    COMMA = 59
    DOT = 60
    ID = 61
    COMMENT = 62
    WS = 63
    ILLEGAL_ESCAPE = 64
    UNCLOSE_STRING = 65
    ERROR_CHAR = 66

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Body'", "'Break'", "'Continue'", "'Do'", "'Else'", "'ElseIf'", 
            "'EndBody'", "'EndIf'", "'EndFor'", "'EndWhile'", "'For'", "'Function'", 
            "'If'", "'Parameter'", "'Return'", "'Then'", "'Var'", "'While'", 
            "'EndDo'", "'+'", "'-'", "'*'", "'\\'", "'%'", "'+.'", "'-.'", 
            "'*.'", "'\\.'", "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", 
            "'=/='", "'<.'", "'>.'", "'<=.'", "'>=.'", "'!'", "'&&'", "'||'", 
            "'='", "'['", "']'", "'('", "')'", "'{'", "'}'", "';'", "':'", 
            "','", "'.'" ]

    symbolicNames = [ "<INVALID>",
            "ARRAY_LIT", "DEC_INT_LIT", "HEX_INT_LIT", "OCT_INT_LIT", "FLT_LIT", 
            "BOOL_LIT", "STR_LIT", "BODY", "BREAK", "CONTINUE", "DO", "ELSE", 
            "ELSEIF", "ENDBODY", "ENDIF", "ENDFOR", "ENDWHILE", "FOR", "FUNCTION", 
            "IF", "PARAMETER", "RETURN", "THEN", "VAR", "WHILE", "ENDDO", 
            "ADD_I", "SUB_I", "MUL_I", "DIV_I", "MOD_I", "ADD_F", "SUB_F", 
            "MUL_F", "DIV_F", "EQ_I", "NEQ_I", "LT_I", "GT_I", "LTE_I", 
            "GTE_I", "NEQ_F", "LT_F", "GT_F", "LTE_F", "GTE_F", "NOT", "AND", 
            "OR", "ASSIGN", "LS", "RS", "LB", "RB", "LC", "RC", "SEMI", 
            "COLON", "COMMA", "DOT", "ID", "COMMENT", "WS", "ILLEGAL_ESCAPE", 
            "UNCLOSE_STRING", "ERROR_CHAR" ]

    ruleNames = [ "DEGIT", "DEGIT_NO_ZERO", "OCT_DEGIT", "OCT_DEGIT_NO_ZERO", 
                  "HEX_CHAR", "HEX_PREFIX", "OCT_PREFIX", "FLT_INT_PART", 
                  "FLT_DEC_PART", "FLT_EXP_PART", "ESCAPE_CHAR", "DOUBLE_QUOTE_CHAR", 
                  "ARRAY_LIT", "DEC_INT_LIT", "HEX_INT_LIT", "OCT_INT_LIT", 
                  "FLT_LIT", "BOOL_LIT", "STR_LIT", "BODY", "BREAK", "CONTINUE", 
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
            actions[18] = self.STR_LIT_action 
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

     


