# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3D")
        buf.write("\u0196\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\3\2\5\2`\n\2\3\2\3\2\3\2\3\3\5\3f\n\3\3\4\3\4\3\4")
        buf.write("\3\4\5\4l\n\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6")
        buf.write("\5\6x\n\6\3\7\3\7\5\7|\n\7\3\b\3\b\3\b\5\b\u0081\n\b\3")
        buf.write("\t\3\t\3\t\3\t\5\t\u0087\n\t\3\n\5\n\u008a\n\n\3\13\3")
        buf.write("\13\3\13\3\13\5\13\u0090\n\13\3\f\3\f\3\f\3\f\5\f\u0096")
        buf.write("\n\f\3\f\3\f\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16")
        buf.write("\5\16\u00a3\n\16\3\17\3\17\3\17\5\17\u00a8\n\17\3\20\3")
        buf.write("\20\3\20\5\20\u00ad\n\20\3\20\3\20\3\20\3\21\5\21\u00b3")
        buf.write("\n\21\3\21\3\21\3\22\3\22\3\22\3\22\5\22\u00bb\n\22\3")
        buf.write("\23\3\23\3\23\3\23\5\23\u00c1\n\23\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\5\24\u00cc\n\24\3\25\3\25\3")
        buf.write("\25\3\25\3\25\3\26\3\26\5\26\u00d5\n\26\3\26\3\26\3\26")
        buf.write("\3\26\3\27\3\27\3\27\3\27\5\27\u00df\n\27\3\27\5\27\u00e2")
        buf.write("\n\27\3\27\3\27\5\27\u00e6\n\27\5\27\u00e8\n\27\3\27\3")
        buf.write("\27\3\27\3\30\3\30\3\30\3\30\5\30\u00f1\n\30\3\31\3\31")
        buf.write("\3\31\3\31\5\31\u00f7\n\31\3\32\3\32\3\32\3\32\3\32\3")
        buf.write("\32\3\32\3\32\3\32\3\32\3\32\3\32\5\32\u0105\n\32\3\32")
        buf.write("\3\32\3\32\3\33\3\33\3\33\3\33\5\33\u010e\n\33\3\33\3")
        buf.write("\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\35\3\35")
        buf.write("\3\36\3\36\3\37\3\37\3\37\5\37\u0121\n\37\3\37\3\37\3")
        buf.write("\37\3 \3 \5 \u0128\n \3 \3 \3!\3!\3!\3!\3!\5!\u0131\n")
        buf.write("!\3\"\3\"\3\"\3\"\3\"\3\"\7\"\u0139\n\"\f\"\16\"\u013c")
        buf.write("\13\"\3#\3#\3#\3#\3#\3#\7#\u0144\n#\f#\16#\u0147\13#\3")
        buf.write("$\3$\3$\3$\3$\3$\7$\u014f\n$\f$\16$\u0152\13$\3%\3%\3")
        buf.write("%\5%\u0157\n%\3&\3&\3&\3&\5&\u015d\n&\3\'\3\'\5\'\u0161")
        buf.write("\n\'\3\'\3\'\3(\3(\3(\3(\3(\3(\3(\3(\3(\5(\u016e\n(\3")
        buf.write(")\3)\5)\u0172\n)\3*\3*\3*\3*\3*\3*\5*\u017a\n*\3+\3+\3")
        buf.write("+\5+\u017f\n+\3+\3+\3,\3,\3,\3,\3,\5,\u0188\n,\3-\3-\3")
        buf.write(".\3.\3.\3.\5.\u0190\n.\3/\3/\3/\3/\3/\2\5BDF\60\2\4\6")
        buf.write("\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\66")
        buf.write("8:<>@BDFHJLNPRTVXZ\\\2\b\3\2&\60\3\2\62\63\4\2\35\36\"")
        buf.write("#\4\2\37!$%\4\2\36\36##\3\2\3\t\2\u0199\2_\3\2\2\2\4e")
        buf.write("\3\2\2\2\6k\3\2\2\2\bm\3\2\2\2\nw\3\2\2\2\f{\3\2\2\2\16")
        buf.write("}\3\2\2\2\20\u0082\3\2\2\2\22\u0089\3\2\2\2\24\u008f\3")
        buf.write("\2\2\2\26\u0091\3\2\2\2\30\u0099\3\2\2\2\32\u00a2\3\2")
        buf.write("\2\2\34\u00a7\3\2\2\2\36\u00a9\3\2\2\2 \u00b2\3\2\2\2")
        buf.write("\"\u00ba\3\2\2\2$\u00c0\3\2\2\2&\u00cb\3\2\2\2(\u00cd")
        buf.write("\3\2\2\2*\u00d4\3\2\2\2,\u00da\3\2\2\2.\u00f0\3\2\2\2")
        buf.write("\60\u00f2\3\2\2\2\62\u00f8\3\2\2\2\64\u0109\3\2\2\2\66")
        buf.write("\u0112\3\2\2\28\u0119\3\2\2\2:\u011b\3\2\2\2<\u011d\3")
        buf.write("\2\2\2>\u0125\3\2\2\2@\u0130\3\2\2\2B\u0132\3\2\2\2D\u013d")
        buf.write("\3\2\2\2F\u0148\3\2\2\2H\u0156\3\2\2\2J\u015c\3\2\2\2")
        buf.write("L\u0160\3\2\2\2N\u016d\3\2\2\2P\u0171\3\2\2\2R\u0179\3")
        buf.write("\2\2\2T\u017b\3\2\2\2V\u0187\3\2\2\2X\u0189\3\2\2\2Z\u018f")
        buf.write("\3\2\2\2\\\u0191\3\2\2\2^`\5\4\3\2_^\3\2\2\2_`\3\2\2\2")
        buf.write("`a\3\2\2\2ab\5\22\n\2bc\7\2\2\3c\3\3\2\2\2df\5\6\4\2e")
        buf.write("d\3\2\2\2ef\3\2\2\2f\5\3\2\2\2gh\5\b\5\2hi\5\6\4\2il\3")
        buf.write("\2\2\2jl\5\b\5\2kg\3\2\2\2kj\3\2\2\2l\7\3\2\2\2mn\7\32")
        buf.write("\2\2no\7<\2\2op\5\n\6\2pq\7;\2\2q\t\3\2\2\2rs\5\f\7\2")
        buf.write("st\7=\2\2tu\5\n\6\2ux\3\2\2\2vx\5\f\7\2wr\3\2\2\2wv\3")
        buf.write("\2\2\2x\13\3\2\2\2y|\5\16\b\2z|\5\20\t\2{y\3\2\2\2{z\3")
        buf.write("\2\2\2|\r\3\2\2\2}\u0080\7?\2\2~\177\7\64\2\2\177\u0081")
        buf.write("\5X-\2\u0080~\3\2\2\2\u0080\u0081\3\2\2\2\u0081\17\3\2")
        buf.write("\2\2\u0082\u0083\7?\2\2\u0083\u0086\5Z.\2\u0084\u0085")
        buf.write("\7\64\2\2\u0085\u0087\7\3\2\2\u0086\u0084\3\2\2\2\u0086")
        buf.write("\u0087\3\2\2\2\u0087\21\3\2\2\2\u0088\u008a\5\24\13\2")
        buf.write("\u0089\u0088\3\2\2\2\u0089\u008a\3\2\2\2\u008a\23\3\2")
        buf.write("\2\2\u008b\u008c\5\26\f\2\u008c\u008d\5\24\13\2\u008d")
        buf.write("\u0090\3\2\2\2\u008e\u0090\5\26\f\2\u008f\u008b\3\2\2")
        buf.write("\2\u008f\u008e\3\2\2\2\u0090\25\3\2\2\2\u0091\u0092\7")
        buf.write("\25\2\2\u0092\u0093\7<\2\2\u0093\u0095\7?\2\2\u0094\u0096")
        buf.write("\5\30\r\2\u0095\u0094\3\2\2\2\u0095\u0096\3\2\2\2\u0096")
        buf.write("\u0097\3\2\2\2\u0097\u0098\5\36\20\2\u0098\27\3\2\2\2")
        buf.write("\u0099\u009a\7\27\2\2\u009a\u009b\7<\2\2\u009b\u009c\5")
        buf.write("\32\16\2\u009c\31\3\2\2\2\u009d\u009e\5\34\17\2\u009e")
        buf.write("\u009f\7=\2\2\u009f\u00a0\5\32\16\2\u00a0\u00a3\3\2\2")
        buf.write("\2\u00a1\u00a3\5\34\17\2\u00a2\u009d\3\2\2\2\u00a2\u00a1")
        buf.write("\3\2\2\2\u00a3\33\3\2\2\2\u00a4\u00a8\7?\2\2\u00a5\u00a6")
        buf.write("\7?\2\2\u00a6\u00a8\5Z.\2\u00a7\u00a4\3\2\2\2\u00a7\u00a5")
        buf.write("\3\2\2\2\u00a8\35\3\2\2\2\u00a9\u00aa\7\n\2\2\u00aa\u00ac")
        buf.write("\7<\2\2\u00ab\u00ad\5 \21\2\u00ac\u00ab\3\2\2\2\u00ac")
        buf.write("\u00ad\3\2\2\2\u00ad\u00ae\3\2\2\2\u00ae\u00af\7\20\2")
        buf.write("\2\u00af\u00b0\7>\2\2\u00b0\37\3\2\2\2\u00b1\u00b3\5\"")
        buf.write("\22\2\u00b2\u00b1\3\2\2\2\u00b2\u00b3\3\2\2\2\u00b3\u00b4")
        buf.write("\3\2\2\2\u00b4\u00b5\5$\23\2\u00b5!\3\2\2\2\u00b6\u00b7")
        buf.write("\5(\25\2\u00b7\u00b8\5\"\22\2\u00b8\u00bb\3\2\2\2\u00b9")
        buf.write("\u00bb\5(\25\2\u00ba\u00b6\3\2\2\2\u00ba\u00b9\3\2\2\2")
        buf.write("\u00bb#\3\2\2\2\u00bc\u00bd\5&\24\2\u00bd\u00be\5$\23")
        buf.write("\2\u00be\u00c1\3\2\2\2\u00bf\u00c1\5&\24\2\u00c0\u00bc")
        buf.write("\3\2\2\2\u00c0\u00bf\3\2\2\2\u00c1%\3\2\2\2\u00c2\u00cc")
        buf.write("\5*\26\2\u00c3\u00cc\5,\27\2\u00c4\u00cc\5\62\32\2\u00c5")
        buf.write("\u00cc\5\64\33\2\u00c6\u00cc\5\66\34\2\u00c7\u00cc\58")
        buf.write("\35\2\u00c8\u00cc\5:\36\2\u00c9\u00cc\5<\37\2\u00ca\u00cc")
        buf.write("\5> \2\u00cb\u00c2\3\2\2\2\u00cb\u00c3\3\2\2\2\u00cb\u00c4")
        buf.write("\3\2\2\2\u00cb\u00c5\3\2\2\2\u00cb\u00c6\3\2\2\2\u00cb")
        buf.write("\u00c7\3\2\2\2\u00cb\u00c8\3\2\2\2\u00cb\u00c9\3\2\2\2")
        buf.write("\u00cb\u00ca\3\2\2\2\u00cc\'\3\2\2\2\u00cd\u00ce\7\32")
        buf.write("\2\2\u00ce\u00cf\7<\2\2\u00cf\u00d0\5\n\6\2\u00d0\u00d1")
        buf.write("\7;\2\2\u00d1)\3\2\2\2\u00d2\u00d5\7?\2\2\u00d3\u00d5")
        buf.write("\5L\'\2\u00d4\u00d2\3\2\2\2\u00d4\u00d3\3\2\2\2\u00d5")
        buf.write("\u00d6\3\2\2\2\u00d6\u00d7\7\64\2\2\u00d7\u00d8\5@!\2")
        buf.write("\u00d8\u00d9\7;\2\2\u00d9+\3\2\2\2\u00da\u00db\7\26\2")
        buf.write("\2\u00db\u00dc\5@!\2\u00dc\u00de\7\31\2\2\u00dd\u00df")
        buf.write("\5 \21\2\u00de\u00dd\3\2\2\2\u00de\u00df\3\2\2\2\u00df")
        buf.write("\u00e1\3\2\2\2\u00e0\u00e2\5.\30\2\u00e1\u00e0\3\2\2\2")
        buf.write("\u00e1\u00e2\3\2\2\2\u00e2\u00e7\3\2\2\2\u00e3\u00e5\7")
        buf.write("\16\2\2\u00e4\u00e6\5 \21\2\u00e5\u00e4\3\2\2\2\u00e5")
        buf.write("\u00e6\3\2\2\2\u00e6\u00e8\3\2\2\2\u00e7\u00e3\3\2\2\2")
        buf.write("\u00e7\u00e8\3\2\2\2\u00e8\u00e9\3\2\2\2\u00e9\u00ea\7")
        buf.write("\21\2\2\u00ea\u00eb\7>\2\2\u00eb-\3\2\2\2\u00ec\u00ed")
        buf.write("\5\60\31\2\u00ed\u00ee\5.\30\2\u00ee\u00f1\3\2\2\2\u00ef")
        buf.write("\u00f1\5\60\31\2\u00f0\u00ec\3\2\2\2\u00f0\u00ef\3\2\2")
        buf.write("\2\u00f1/\3\2\2\2\u00f2\u00f3\7\17\2\2\u00f3\u00f4\5@")
        buf.write("!\2\u00f4\u00f6\7\31\2\2\u00f5\u00f7\5 \21\2\u00f6\u00f5")
        buf.write("\3\2\2\2\u00f6\u00f7\3\2\2\2\u00f7\61\3\2\2\2\u00f8\u00f9")
        buf.write("\7\24\2\2\u00f9\u00fa\7\67\2\2\u00fa\u00fb\7?\2\2\u00fb")
        buf.write("\u00fc\7\64\2\2\u00fc\u00fd\5@!\2\u00fd\u00fe\7=\2\2\u00fe")
        buf.write("\u00ff\5@!\2\u00ff\u0100\7=\2\2\u0100\u0101\5@!\2\u0101")
        buf.write("\u0102\78\2\2\u0102\u0104\7\r\2\2\u0103\u0105\5 \21\2")
        buf.write("\u0104\u0103\3\2\2\2\u0104\u0105\3\2\2\2\u0105\u0106\3")
        buf.write("\2\2\2\u0106\u0107\7\22\2\2\u0107\u0108\7>\2\2\u0108\63")
        buf.write("\3\2\2\2\u0109\u010a\7\33\2\2\u010a\u010b\5@!\2\u010b")
        buf.write("\u010d\7\r\2\2\u010c\u010e\5 \21\2\u010d\u010c\3\2\2\2")
        buf.write("\u010d\u010e\3\2\2\2\u010e\u010f\3\2\2\2\u010f\u0110\7")
        buf.write("\23\2\2\u0110\u0111\7>\2\2\u0111\65\3\2\2\2\u0112\u0113")
        buf.write("\7\r\2\2\u0113\u0114\5 \21\2\u0114\u0115\7\33\2\2\u0115")
        buf.write("\u0116\5@!\2\u0116\u0117\7\34\2\2\u0117\u0118\7>\2\2\u0118")
        buf.write("\67\3\2\2\2\u0119\u011a\7\13\2\2\u011a9\3\2\2\2\u011b")
        buf.write("\u011c\7\f\2\2\u011c;\3\2\2\2\u011d\u011e\7?\2\2\u011e")
        buf.write("\u0120\7\67\2\2\u011f\u0121\5V,\2\u0120\u011f\3\2\2\2")
        buf.write("\u0120\u0121\3\2\2\2\u0121\u0122\3\2\2\2\u0122\u0123\7")
        buf.write("8\2\2\u0123\u0124\7;\2\2\u0124=\3\2\2\2\u0125\u0127\7")
        buf.write("\30\2\2\u0126\u0128\5@!\2\u0127\u0126\3\2\2\2\u0127\u0128")
        buf.write("\3\2\2\2\u0128\u0129\3\2\2\2\u0129\u012a\7;\2\2\u012a")
        buf.write("?\3\2\2\2\u012b\u012c\5B\"\2\u012c\u012d\t\2\2\2\u012d")
        buf.write("\u012e\5B\"\2\u012e\u0131\3\2\2\2\u012f\u0131\5B\"\2\u0130")
        buf.write("\u012b\3\2\2\2\u0130\u012f\3\2\2\2\u0131A\3\2\2\2\u0132")
        buf.write("\u0133\b\"\1\2\u0133\u0134\5D#\2\u0134\u013a\3\2\2\2\u0135")
        buf.write("\u0136\f\4\2\2\u0136\u0137\t\3\2\2\u0137\u0139\5D#\2\u0138")
        buf.write("\u0135\3\2\2\2\u0139\u013c\3\2\2\2\u013a\u0138\3\2\2\2")
        buf.write("\u013a\u013b\3\2\2\2\u013bC\3\2\2\2\u013c\u013a\3\2\2")
        buf.write("\2\u013d\u013e\b#\1\2\u013e\u013f\5F$\2\u013f\u0145\3")
        buf.write("\2\2\2\u0140\u0141\f\4\2\2\u0141\u0142\t\4\2\2\u0142\u0144")
        buf.write("\5F$\2\u0143\u0140\3\2\2\2\u0144\u0147\3\2\2\2\u0145\u0143")
        buf.write("\3\2\2\2\u0145\u0146\3\2\2\2\u0146E\3\2\2\2\u0147\u0145")
        buf.write("\3\2\2\2\u0148\u0149\b$\1\2\u0149\u014a\5H%\2\u014a\u0150")
        buf.write("\3\2\2\2\u014b\u014c\f\4\2\2\u014c\u014d\t\5\2\2\u014d")
        buf.write("\u014f\5H%\2\u014e\u014b\3\2\2\2\u014f\u0152\3\2\2\2\u0150")
        buf.write("\u014e\3\2\2\2\u0150\u0151\3\2\2\2\u0151G\3\2\2\2\u0152")
        buf.write("\u0150\3\2\2\2\u0153\u0154\7\61\2\2\u0154\u0157\5H%\2")
        buf.write("\u0155\u0157\5J&\2\u0156\u0153\3\2\2\2\u0156\u0155\3\2")
        buf.write("\2\2\u0157I\3\2\2\2\u0158\u0159\t\6\2\2\u0159\u015d\5")
        buf.write("J&\2\u015a\u015d\5L\'\2\u015b\u015d\5P)\2\u015c\u0158")
        buf.write("\3\2\2\2\u015c\u015a\3\2\2\2\u015c\u015b\3\2\2\2\u015d")
        buf.write("K\3\2\2\2\u015e\u0161\7?\2\2\u015f\u0161\5T+\2\u0160\u015e")
        buf.write("\3\2\2\2\u0160\u015f\3\2\2\2\u0161\u0162\3\2\2\2\u0162")
        buf.write("\u0163\5N(\2\u0163M\3\2\2\2\u0164\u0165\7\65\2\2\u0165")
        buf.write("\u0166\5@!\2\u0166\u0167\7\66\2\2\u0167\u016e\3\2\2\2")
        buf.write("\u0168\u0169\7\65\2\2\u0169\u016a\5@!\2\u016a\u016b\7")
        buf.write("\66\2\2\u016b\u016c\5N(\2\u016c\u016e\3\2\2\2\u016d\u0164")
        buf.write("\3\2\2\2\u016d\u0168\3\2\2\2\u016eO\3\2\2\2\u016f\u0172")
        buf.write("\5T+\2\u0170\u0172\5R*\2\u0171\u016f\3\2\2\2\u0171\u0170")
        buf.write("\3\2\2\2\u0172Q\3\2\2\2\u0173\u017a\5X-\2\u0174\u017a")
        buf.write("\7?\2\2\u0175\u0176\7\67\2\2\u0176\u0177\5@!\2\u0177\u0178")
        buf.write("\78\2\2\u0178\u017a\3\2\2\2\u0179\u0173\3\2\2\2\u0179")
        buf.write("\u0174\3\2\2\2\u0179\u0175\3\2\2\2\u017aS\3\2\2\2\u017b")
        buf.write("\u017c\7?\2\2\u017c\u017e\7\67\2\2\u017d\u017f\5V,\2\u017e")
        buf.write("\u017d\3\2\2\2\u017e\u017f\3\2\2\2\u017f\u0180\3\2\2\2")
        buf.write("\u0180\u0181\78\2\2\u0181U\3\2\2\2\u0182\u0183\5@!\2\u0183")
        buf.write("\u0184\7=\2\2\u0184\u0185\5V,\2\u0185\u0188\3\2\2\2\u0186")
        buf.write("\u0188\5@!\2\u0187\u0182\3\2\2\2\u0187\u0186\3\2\2\2\u0188")
        buf.write("W\3\2\2\2\u0189\u018a\t\7\2\2\u018aY\3\2\2\2\u018b\u018c")
        buf.write("\5\\/\2\u018c\u018d\5Z.\2\u018d\u0190\3\2\2\2\u018e\u0190")
        buf.write("\5\\/\2\u018f\u018b\3\2\2\2\u018f\u018e\3\2\2\2\u0190")
        buf.write("[\3\2\2\2\u0191\u0192\7\65\2\2\u0192\u0193\7\4\2\2\u0193")
        buf.write("\u0194\7\66\2\2\u0194]\3\2\2\2+_ekw{\u0080\u0086\u0089")
        buf.write("\u008f\u0095\u00a2\u00a7\u00ac\u00b2\u00ba\u00c0\u00cb")
        buf.write("\u00d4\u00de\u00e1\u00e5\u00e7\u00f0\u00f6\u0104\u010d")
        buf.write("\u0120\u0127\u0130\u013a\u0145\u0150\u0156\u015c\u0160")
        buf.write("\u016d\u0171\u0179\u017e\u0187\u018f")
        return buf.getvalue()


class BKITParser ( Parser ):

    grammarFileName = "BKIT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'Body'", "'Break'", "'Continue'", "'Do'", "'Else'", 
                     "'ElseIf'", "'EndBody'", "'EndIf'", "'EndFor'", "'EndWhile'", 
                     "'For'", "'Function'", "'If'", "'Parameter'", "'Return'", 
                     "'Then'", "'Var'", "'While'", "'EndDo'", "'+'", "'-'", 
                     "'*'", "'\\'", "'%'", "'+.'", "'-.'", "'*.'", "'\\.'", 
                     "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", "'=/='", 
                     "'<.'", "'>.'", "'<=.'", "'>=.'", "'!'", "'&&'", "'||'", 
                     "'='", "'['", "']'", "'('", "')'", "'{'", "'}'", "';'", 
                     "':'", "','", "'.'" ]

    symbolicNames = [ "<INVALID>", "ARRAY_LIT", "DEC_INT_LIT", "HEX_INT_LIT", 
                      "OCT_INT_LIT", "FLT_LIT", "BOOL_LIT", "STR_LIT", "BODY", 
                      "BREAK", "CONTINUE", "DO", "ELSE", "ELSEIF", "ENDBODY", 
                      "ENDIF", "ENDFOR", "ENDWHILE", "FOR", "FUNCTION", 
                      "IF", "PARAMETER", "RETURN", "THEN", "VAR", "WHILE", 
                      "ENDDO", "ADD_I", "SUB_I", "MUL_I", "DIV_I", "MOD_I", 
                      "ADD_F", "SUB_F", "MUL_F", "DIV_F", "EQ_I", "NEQ_I", 
                      "LT_I", "GT_I", "LTE_I", "GTE_I", "NEQ_F", "LT_F", 
                      "GT_F", "LTE_F", "GTE_F", "NOT", "AND", "OR", "ASSIGN", 
                      "LS", "RS", "LB", "RB", "LC", "RC", "SEMI", "COLON", 
                      "COMMA", "DOT", "ID", "COMMENT", "WS", "ILLEGAL_ESCAPE", 
                      "UNCLOSE_STRING", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_glob_var_decl_part = 1
    RULE_var_decl_list = 2
    RULE_var_decl = 3
    RULE_var_list = 4
    RULE_var = 5
    RULE_scalar_var = 6
    RULE_compo_var = 7
    RULE_func_decl_part = 8
    RULE_func_decl_list = 9
    RULE_func_decl = 10
    RULE_func_param = 11
    RULE_param_list = 12
    RULE_param = 13
    RULE_func_body = 14
    RULE_stmt_list = 15
    RULE_var_decl_stmt_list = 16
    RULE_other_stmt_list = 17
    RULE_other_stmt = 18
    RULE_var_decl_stmt = 19
    RULE_assign_stmt = 20
    RULE_if_stmt = 21
    RULE_else_if_list = 22
    RULE_else_if = 23
    RULE_for_stmt = 24
    RULE_while_stmt = 25
    RULE_do_while_stmt = 26
    RULE_break_stmt = 27
    RULE_continue_stmt = 28
    RULE_call_stmt = 29
    RULE_return_stmt = 30
    RULE_exp = 31
    RULE_exp1 = 32
    RULE_exp2 = 33
    RULE_exp3 = 34
    RULE_exp4 = 35
    RULE_exp5 = 36
    RULE_index_exp = 37
    RULE_index_operator = 38
    RULE_func_call_exp = 39
    RULE_operand = 40
    RULE_func_call = 41
    RULE_exp_list = 42
    RULE_literal = 43
    RULE_dimensions = 44
    RULE_dimension = 45

    ruleNames =  [ "program", "glob_var_decl_part", "var_decl_list", "var_decl", 
                   "var_list", "var", "scalar_var", "compo_var", "func_decl_part", 
                   "func_decl_list", "func_decl", "func_param", "param_list", 
                   "param", "func_body", "stmt_list", "var_decl_stmt_list", 
                   "other_stmt_list", "other_stmt", "var_decl_stmt", "assign_stmt", 
                   "if_stmt", "else_if_list", "else_if", "for_stmt", "while_stmt", 
                   "do_while_stmt", "break_stmt", "continue_stmt", "call_stmt", 
                   "return_stmt", "exp", "exp1", "exp2", "exp3", "exp4", 
                   "exp5", "index_exp", "index_operator", "func_call_exp", 
                   "operand", "func_call", "exp_list", "literal", "dimensions", 
                   "dimension" ]

    EOF = Token.EOF
    ARRAY_LIT=1
    DEC_INT_LIT=2
    HEX_INT_LIT=3
    OCT_INT_LIT=4
    FLT_LIT=5
    BOOL_LIT=6
    STR_LIT=7
    BODY=8
    BREAK=9
    CONTINUE=10
    DO=11
    ELSE=12
    ELSEIF=13
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
    ENDDO=26
    ADD_I=27
    SUB_I=28
    MUL_I=29
    DIV_I=30
    MOD_I=31
    ADD_F=32
    SUB_F=33
    MUL_F=34
    DIV_F=35
    EQ_I=36
    NEQ_I=37
    LT_I=38
    GT_I=39
    LTE_I=40
    GTE_I=41
    NEQ_F=42
    LT_F=43
    GT_F=44
    LTE_F=45
    GTE_F=46
    NOT=47
    AND=48
    OR=49
    ASSIGN=50
    LS=51
    RS=52
    LB=53
    RB=54
    LC=55
    RC=56
    SEMI=57
    COLON=58
    COMMA=59
    DOT=60
    ID=61
    COMMENT=62
    WS=63
    ILLEGAL_ESCAPE=64
    UNCLOSE_STRING=65
    ERROR_CHAR=66

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

        def func_decl_part(self):
            return self.getTypedRuleContext(BKITParser.Func_decl_partContext,0)


        def EOF(self):
            return self.getToken(BKITParser.EOF, 0)

        def glob_var_decl_part(self):
            return self.getTypedRuleContext(BKITParser.Glob_var_decl_partContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = BKITParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 92
                self.glob_var_decl_part()


            self.state = 95
            self.func_decl_part()
            self.state = 96
            self.match(BKITParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Glob_var_decl_partContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl_list(self):
            return self.getTypedRuleContext(BKITParser.Var_decl_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_glob_var_decl_part

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGlob_var_decl_part" ):
                return visitor.visitGlob_var_decl_part(self)
            else:
                return visitor.visitChildren(self)




    def glob_var_decl_part(self):

        localctx = BKITParser.Glob_var_decl_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_glob_var_decl_part)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.VAR:
                self.state = 98
                self.var_decl_list()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_decl_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl(self):
            return self.getTypedRuleContext(BKITParser.Var_declContext,0)


        def var_decl_list(self):
            return self.getTypedRuleContext(BKITParser.Var_decl_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_var_decl_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl_list" ):
                return visitor.visitVar_decl_list(self)
            else:
                return visitor.visitChildren(self)




    def var_decl_list(self):

        localctx = BKITParser.Var_decl_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_var_decl_list)
        try:
            self.state = 105
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 101
                self.var_decl()
                self.state = 102
                self.var_decl_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 104
                self.var_decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(BKITParser.VAR, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def var_list(self):
            return self.getTypedRuleContext(BKITParser.Var_listContext,0)


        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_var_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl" ):
                return visitor.visitVar_decl(self)
            else:
                return visitor.visitChildren(self)




    def var_decl(self):

        localctx = BKITParser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_var_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.match(BKITParser.VAR)
            self.state = 108
            self.match(BKITParser.COLON)
            self.state = 109
            self.var_list()
            self.state = 110
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var(self):
            return self.getTypedRuleContext(BKITParser.VarContext,0)


        def COMMA(self):
            return self.getToken(BKITParser.COMMA, 0)

        def var_list(self):
            return self.getTypedRuleContext(BKITParser.Var_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_var_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_list" ):
                return visitor.visitVar_list(self)
            else:
                return visitor.visitChildren(self)




    def var_list(self):

        localctx = BKITParser.Var_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_var_list)
        try:
            self.state = 117
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 112
                self.var()
                self.state = 113
                self.match(BKITParser.COMMA)
                self.state = 114
                self.var_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 116
                self.var()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def scalar_var(self):
            return self.getTypedRuleContext(BKITParser.Scalar_varContext,0)


        def compo_var(self):
            return self.getTypedRuleContext(BKITParser.Compo_varContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar" ):
                return visitor.visitVar(self)
            else:
                return visitor.visitChildren(self)




    def var(self):

        localctx = BKITParser.VarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_var)
        try:
            self.state = 121
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 119
                self.scalar_var()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 120
                self.compo_var()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Scalar_varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(BKITParser.ASSIGN, 0)

        def literal(self):
            return self.getTypedRuleContext(BKITParser.LiteralContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_scalar_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScalar_var" ):
                return visitor.visitScalar_var(self)
            else:
                return visitor.visitChildren(self)




    def scalar_var(self):

        localctx = BKITParser.Scalar_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_scalar_var)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.match(BKITParser.ID)
            self.state = 126
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.ASSIGN:
                self.state = 124
                self.match(BKITParser.ASSIGN)
                self.state = 125
                self.literal()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Compo_varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def dimensions(self):
            return self.getTypedRuleContext(BKITParser.DimensionsContext,0)


        def ASSIGN(self):
            return self.getToken(BKITParser.ASSIGN, 0)

        def ARRAY_LIT(self):
            return self.getToken(BKITParser.ARRAY_LIT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_compo_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompo_var" ):
                return visitor.visitCompo_var(self)
            else:
                return visitor.visitChildren(self)




    def compo_var(self):

        localctx = BKITParser.Compo_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_compo_var)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.match(BKITParser.ID)
            self.state = 129
            self.dimensions()
            self.state = 132
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.ASSIGN:
                self.state = 130
                self.match(BKITParser.ASSIGN)
                self.state = 131
                self.match(BKITParser.ARRAY_LIT)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_decl_partContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def func_decl_list(self):
            return self.getTypedRuleContext(BKITParser.Func_decl_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_func_decl_part

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_decl_part" ):
                return visitor.visitFunc_decl_part(self)
            else:
                return visitor.visitChildren(self)




    def func_decl_part(self):

        localctx = BKITParser.Func_decl_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_func_decl_part)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.FUNCTION:
                self.state = 134
                self.func_decl_list()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_decl_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def func_decl(self):
            return self.getTypedRuleContext(BKITParser.Func_declContext,0)


        def func_decl_list(self):
            return self.getTypedRuleContext(BKITParser.Func_decl_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_func_decl_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_decl_list" ):
                return visitor.visitFunc_decl_list(self)
            else:
                return visitor.visitChildren(self)




    def func_decl_list(self):

        localctx = BKITParser.Func_decl_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_func_decl_list)
        try:
            self.state = 141
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 137
                self.func_decl()
                self.state = 138
                self.func_decl_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 140
                self.func_decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(BKITParser.FUNCTION, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def func_body(self):
            return self.getTypedRuleContext(BKITParser.Func_bodyContext,0)


        def func_param(self):
            return self.getTypedRuleContext(BKITParser.Func_paramContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_func_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_decl" ):
                return visitor.visitFunc_decl(self)
            else:
                return visitor.visitChildren(self)




    def func_decl(self):

        localctx = BKITParser.Func_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_func_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self.match(BKITParser.FUNCTION)
            self.state = 144
            self.match(BKITParser.COLON)
            self.state = 145
            self.match(BKITParser.ID)
            self.state = 147
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.PARAMETER:
                self.state = 146
                self.func_param()


            self.state = 149
            self.func_body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_paramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PARAMETER(self):
            return self.getToken(BKITParser.PARAMETER, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def param_list(self):
            return self.getTypedRuleContext(BKITParser.Param_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_func_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_param" ):
                return visitor.visitFunc_param(self)
            else:
                return visitor.visitChildren(self)




    def func_param(self):

        localctx = BKITParser.Func_paramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_func_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.match(BKITParser.PARAMETER)
            self.state = 152
            self.match(BKITParser.COLON)
            self.state = 153
            self.param_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(BKITParser.ParamContext,0)


        def COMMA(self):
            return self.getToken(BKITParser.COMMA, 0)

        def param_list(self):
            return self.getTypedRuleContext(BKITParser.Param_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_param_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_list" ):
                return visitor.visitParam_list(self)
            else:
                return visitor.visitChildren(self)




    def param_list(self):

        localctx = BKITParser.Param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_param_list)
        try:
            self.state = 160
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 155
                self.param()
                self.state = 156
                self.match(BKITParser.COMMA)
                self.state = 157
                self.param_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 159
                self.param()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def dimensions(self):
            return self.getTypedRuleContext(BKITParser.DimensionsContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = BKITParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_param)
        try:
            self.state = 165
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 162
                self.match(BKITParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 163
                self.match(BKITParser.ID)
                self.state = 164
                self.dimensions()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BODY(self):
            return self.getToken(BKITParser.BODY, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def ENDBODY(self):
            return self.getToken(BKITParser.ENDBODY, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def stmt_list(self):
            return self.getTypedRuleContext(BKITParser.Stmt_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_func_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_body" ):
                return visitor.visitFunc_body(self)
            else:
                return visitor.visitChildren(self)




    def func_body(self):

        localctx = BKITParser.Func_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_func_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.match(BKITParser.BODY)
            self.state = 168
            self.match(BKITParser.COLON)
            self.state = 170
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.BREAK) | (1 << BKITParser.CONTINUE) | (1 << BKITParser.DO) | (1 << BKITParser.FOR) | (1 << BKITParser.IF) | (1 << BKITParser.RETURN) | (1 << BKITParser.VAR) | (1 << BKITParser.WHILE) | (1 << BKITParser.ID))) != 0):
                self.state = 169
                self.stmt_list()


            self.state = 172
            self.match(BKITParser.ENDBODY)
            self.state = 173
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def other_stmt_list(self):
            return self.getTypedRuleContext(BKITParser.Other_stmt_listContext,0)


        def var_decl_stmt_list(self):
            return self.getTypedRuleContext(BKITParser.Var_decl_stmt_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_stmt_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_list" ):
                return visitor.visitStmt_list(self)
            else:
                return visitor.visitChildren(self)




    def stmt_list(self):

        localctx = BKITParser.Stmt_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_stmt_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.VAR:
                self.state = 175
                self.var_decl_stmt_list()


            self.state = 178
            self.other_stmt_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_decl_stmt_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl_stmt(self):
            return self.getTypedRuleContext(BKITParser.Var_decl_stmtContext,0)


        def var_decl_stmt_list(self):
            return self.getTypedRuleContext(BKITParser.Var_decl_stmt_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_var_decl_stmt_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl_stmt_list" ):
                return visitor.visitVar_decl_stmt_list(self)
            else:
                return visitor.visitChildren(self)




    def var_decl_stmt_list(self):

        localctx = BKITParser.Var_decl_stmt_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_var_decl_stmt_list)
        try:
            self.state = 184
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 180
                self.var_decl_stmt()
                self.state = 181
                self.var_decl_stmt_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 183
                self.var_decl_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Other_stmt_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def other_stmt(self):
            return self.getTypedRuleContext(BKITParser.Other_stmtContext,0)


        def other_stmt_list(self):
            return self.getTypedRuleContext(BKITParser.Other_stmt_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_other_stmt_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOther_stmt_list" ):
                return visitor.visitOther_stmt_list(self)
            else:
                return visitor.visitChildren(self)




    def other_stmt_list(self):

        localctx = BKITParser.Other_stmt_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_other_stmt_list)
        try:
            self.state = 190
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 186
                self.other_stmt()
                self.state = 187
                self.other_stmt_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 189
                self.other_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Other_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign_stmt(self):
            return self.getTypedRuleContext(BKITParser.Assign_stmtContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(BKITParser.If_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(BKITParser.For_stmtContext,0)


        def while_stmt(self):
            return self.getTypedRuleContext(BKITParser.While_stmtContext,0)


        def do_while_stmt(self):
            return self.getTypedRuleContext(BKITParser.Do_while_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(BKITParser.Break_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(BKITParser.Continue_stmtContext,0)


        def call_stmt(self):
            return self.getTypedRuleContext(BKITParser.Call_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(BKITParser.Return_stmtContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_other_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOther_stmt" ):
                return visitor.visitOther_stmt(self)
            else:
                return visitor.visitChildren(self)




    def other_stmt(self):

        localctx = BKITParser.Other_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_other_stmt)
        try:
            self.state = 201
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 192
                self.assign_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 193
                self.if_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 194
                self.for_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 195
                self.while_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 196
                self.do_while_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 197
                self.break_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 198
                self.continue_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 199
                self.call_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 200
                self.return_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_decl_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(BKITParser.VAR, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def var_list(self):
            return self.getTypedRuleContext(BKITParser.Var_listContext,0)


        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_var_decl_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl_stmt" ):
                return visitor.visitVar_decl_stmt(self)
            else:
                return visitor.visitChildren(self)




    def var_decl_stmt(self):

        localctx = BKITParser.Var_decl_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_var_decl_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.match(BKITParser.VAR)
            self.state = 204
            self.match(BKITParser.COLON)
            self.state = 205
            self.var_list()
            self.state = 206
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(BKITParser.ASSIGN, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def index_exp(self):
            return self.getTypedRuleContext(BKITParser.Index_expContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_assign_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_stmt" ):
                return visitor.visitAssign_stmt(self)
            else:
                return visitor.visitChildren(self)




    def assign_stmt(self):

        localctx = BKITParser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 208
                self.match(BKITParser.ID)
                pass

            elif la_ == 2:
                self.state = 209
                self.index_exp()
                pass


            self.state = 212
            self.match(BKITParser.ASSIGN)
            self.state = 213
            self.exp()
            self.state = 214
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(BKITParser.IF, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def THEN(self):
            return self.getToken(BKITParser.THEN, 0)

        def ENDIF(self):
            return self.getToken(BKITParser.ENDIF, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def stmt_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Stmt_listContext)
            else:
                return self.getTypedRuleContext(BKITParser.Stmt_listContext,i)


        def else_if_list(self):
            return self.getTypedRuleContext(BKITParser.Else_if_listContext,0)


        def ELSE(self):
            return self.getToken(BKITParser.ELSE, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_if_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = BKITParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
            self.match(BKITParser.IF)
            self.state = 217
            self.exp()
            self.state = 218
            self.match(BKITParser.THEN)
            self.state = 220
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.BREAK) | (1 << BKITParser.CONTINUE) | (1 << BKITParser.DO) | (1 << BKITParser.FOR) | (1 << BKITParser.IF) | (1 << BKITParser.RETURN) | (1 << BKITParser.VAR) | (1 << BKITParser.WHILE) | (1 << BKITParser.ID))) != 0):
                self.state = 219
                self.stmt_list()


            self.state = 223
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.ELSEIF:
                self.state = 222
                self.else_if_list()


            self.state = 229
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.ELSE:
                self.state = 225
                self.match(BKITParser.ELSE)
                self.state = 227
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.BREAK) | (1 << BKITParser.CONTINUE) | (1 << BKITParser.DO) | (1 << BKITParser.FOR) | (1 << BKITParser.IF) | (1 << BKITParser.RETURN) | (1 << BKITParser.VAR) | (1 << BKITParser.WHILE) | (1 << BKITParser.ID))) != 0):
                    self.state = 226
                    self.stmt_list()




            self.state = 231
            self.match(BKITParser.ENDIF)
            self.state = 232
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_if_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def else_if(self):
            return self.getTypedRuleContext(BKITParser.Else_ifContext,0)


        def else_if_list(self):
            return self.getTypedRuleContext(BKITParser.Else_if_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_else_if_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_if_list" ):
                return visitor.visitElse_if_list(self)
            else:
                return visitor.visitChildren(self)




    def else_if_list(self):

        localctx = BKITParser.Else_if_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_else_if_list)
        try:
            self.state = 238
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 234
                self.else_if()
                self.state = 235
                self.else_if_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 237
                self.else_if()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_ifContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSEIF(self):
            return self.getToken(BKITParser.ELSEIF, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def THEN(self):
            return self.getToken(BKITParser.THEN, 0)

        def stmt_list(self):
            return self.getTypedRuleContext(BKITParser.Stmt_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_else_if

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_if" ):
                return visitor.visitElse_if(self)
            else:
                return visitor.visitChildren(self)




    def else_if(self):

        localctx = BKITParser.Else_ifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_else_if)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 240
            self.match(BKITParser.ELSEIF)
            self.state = 241
            self.exp()
            self.state = 242
            self.match(BKITParser.THEN)
            self.state = 244
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.BREAK) | (1 << BKITParser.CONTINUE) | (1 << BKITParser.DO) | (1 << BKITParser.FOR) | (1 << BKITParser.IF) | (1 << BKITParser.RETURN) | (1 << BKITParser.VAR) | (1 << BKITParser.WHILE) | (1 << BKITParser.ID))) != 0):
                self.state = 243
                self.stmt_list()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(BKITParser.FOR, 0)

        def LB(self):
            return self.getToken(BKITParser.LB, 0)

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(BKITParser.ASSIGN, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ExpContext)
            else:
                return self.getTypedRuleContext(BKITParser.ExpContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def RB(self):
            return self.getToken(BKITParser.RB, 0)

        def DO(self):
            return self.getToken(BKITParser.DO, 0)

        def ENDFOR(self):
            return self.getToken(BKITParser.ENDFOR, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def stmt_list(self):
            return self.getTypedRuleContext(BKITParser.Stmt_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_for_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt" ):
                return visitor.visitFor_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_stmt(self):

        localctx = BKITParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_for_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
            self.match(BKITParser.FOR)
            self.state = 247
            self.match(BKITParser.LB)
            self.state = 248
            self.match(BKITParser.ID)
            self.state = 249
            self.match(BKITParser.ASSIGN)
            self.state = 250
            self.exp()
            self.state = 251
            self.match(BKITParser.COMMA)
            self.state = 252
            self.exp()
            self.state = 253
            self.match(BKITParser.COMMA)
            self.state = 254
            self.exp()
            self.state = 255
            self.match(BKITParser.RB)
            self.state = 256
            self.match(BKITParser.DO)
            self.state = 258
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.BREAK) | (1 << BKITParser.CONTINUE) | (1 << BKITParser.DO) | (1 << BKITParser.FOR) | (1 << BKITParser.IF) | (1 << BKITParser.RETURN) | (1 << BKITParser.VAR) | (1 << BKITParser.WHILE) | (1 << BKITParser.ID))) != 0):
                self.state = 257
                self.stmt_list()


            self.state = 260
            self.match(BKITParser.ENDFOR)
            self.state = 261
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(BKITParser.WHILE, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def DO(self):
            return self.getToken(BKITParser.DO, 0)

        def ENDWHILE(self):
            return self.getToken(BKITParser.ENDWHILE, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def stmt_list(self):
            return self.getTypedRuleContext(BKITParser.Stmt_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_while_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_stmt" ):
                return visitor.visitWhile_stmt(self)
            else:
                return visitor.visitChildren(self)




    def while_stmt(self):

        localctx = BKITParser.While_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_while_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
            self.match(BKITParser.WHILE)
            self.state = 264
            self.exp()
            self.state = 265
            self.match(BKITParser.DO)
            self.state = 267
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.BREAK) | (1 << BKITParser.CONTINUE) | (1 << BKITParser.DO) | (1 << BKITParser.FOR) | (1 << BKITParser.IF) | (1 << BKITParser.RETURN) | (1 << BKITParser.VAR) | (1 << BKITParser.WHILE) | (1 << BKITParser.ID))) != 0):
                self.state = 266
                self.stmt_list()


            self.state = 269
            self.match(BKITParser.ENDWHILE)
            self.state = 270
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Do_while_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DO(self):
            return self.getToken(BKITParser.DO, 0)

        def stmt_list(self):
            return self.getTypedRuleContext(BKITParser.Stmt_listContext,0)


        def WHILE(self):
            return self.getToken(BKITParser.WHILE, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def ENDDO(self):
            return self.getToken(BKITParser.ENDDO, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_do_while_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDo_while_stmt" ):
                return visitor.visitDo_while_stmt(self)
            else:
                return visitor.visitChildren(self)




    def do_while_stmt(self):

        localctx = BKITParser.Do_while_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_do_while_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self.match(BKITParser.DO)
            self.state = 273
            self.stmt_list()
            self.state = 274
            self.match(BKITParser.WHILE)
            self.state = 275
            self.exp()
            self.state = 276
            self.match(BKITParser.ENDDO)
            self.state = 277
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(BKITParser.BREAK, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_break_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stmt" ):
                return visitor.visitBreak_stmt(self)
            else:
                return visitor.visitChildren(self)




    def break_stmt(self):

        localctx = BKITParser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 279
            self.match(BKITParser.BREAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(BKITParser.CONTINUE, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_continue_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_stmt" ):
                return visitor.visitContinue_stmt(self)
            else:
                return visitor.visitChildren(self)




    def continue_stmt(self):

        localctx = BKITParser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            self.match(BKITParser.CONTINUE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def LB(self):
            return self.getToken(BKITParser.LB, 0)

        def RB(self):
            return self.getToken(BKITParser.RB, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def exp_list(self):
            return self.getTypedRuleContext(BKITParser.Exp_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_call_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_stmt" ):
                return visitor.visitCall_stmt(self)
            else:
                return visitor.visitChildren(self)




    def call_stmt(self):

        localctx = BKITParser.Call_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_call_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 283
            self.match(BKITParser.ID)
            self.state = 284
            self.match(BKITParser.LB)
            self.state = 286
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ARRAY_LIT) | (1 << BKITParser.DEC_INT_LIT) | (1 << BKITParser.HEX_INT_LIT) | (1 << BKITParser.OCT_INT_LIT) | (1 << BKITParser.FLT_LIT) | (1 << BKITParser.BOOL_LIT) | (1 << BKITParser.STR_LIT) | (1 << BKITParser.SUB_I) | (1 << BKITParser.SUB_F) | (1 << BKITParser.NOT) | (1 << BKITParser.LB) | (1 << BKITParser.ID))) != 0):
                self.state = 285
                self.exp_list()


            self.state = 288
            self.match(BKITParser.RB)
            self.state = 289
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(BKITParser.RETURN, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_return_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = BKITParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 291
            self.match(BKITParser.RETURN)
            self.state = 293
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ARRAY_LIT) | (1 << BKITParser.DEC_INT_LIT) | (1 << BKITParser.HEX_INT_LIT) | (1 << BKITParser.OCT_INT_LIT) | (1 << BKITParser.FLT_LIT) | (1 << BKITParser.BOOL_LIT) | (1 << BKITParser.STR_LIT) | (1 << BKITParser.SUB_I) | (1 << BKITParser.SUB_F) | (1 << BKITParser.NOT) | (1 << BKITParser.LB) | (1 << BKITParser.ID))) != 0):
                self.state = 292
                self.exp()


            self.state = 295
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Exp1Context)
            else:
                return self.getTypedRuleContext(BKITParser.Exp1Context,i)


        def EQ_I(self):
            return self.getToken(BKITParser.EQ_I, 0)

        def NEQ_I(self):
            return self.getToken(BKITParser.NEQ_I, 0)

        def LT_I(self):
            return self.getToken(BKITParser.LT_I, 0)

        def GT_I(self):
            return self.getToken(BKITParser.GT_I, 0)

        def LTE_I(self):
            return self.getToken(BKITParser.LTE_I, 0)

        def GTE_I(self):
            return self.getToken(BKITParser.GTE_I, 0)

        def NEQ_F(self):
            return self.getToken(BKITParser.NEQ_F, 0)

        def LT_F(self):
            return self.getToken(BKITParser.LT_F, 0)

        def GT_F(self):
            return self.getToken(BKITParser.GT_F, 0)

        def LTE_F(self):
            return self.getToken(BKITParser.LTE_F, 0)

        def GTE_F(self):
            return self.getToken(BKITParser.GTE_F, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)




    def exp(self):

        localctx = BKITParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_exp)
        self._la = 0 # Token type
        try:
            self.state = 302
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 297
                self.exp1(0)
                self.state = 298
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.EQ_I) | (1 << BKITParser.NEQ_I) | (1 << BKITParser.LT_I) | (1 << BKITParser.GT_I) | (1 << BKITParser.LTE_I) | (1 << BKITParser.GTE_I) | (1 << BKITParser.NEQ_F) | (1 << BKITParser.LT_F) | (1 << BKITParser.GT_F) | (1 << BKITParser.LTE_F) | (1 << BKITParser.GTE_F))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 299
                self.exp1(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 301
                self.exp1(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp2(self):
            return self.getTypedRuleContext(BKITParser.Exp2Context,0)


        def exp1(self):
            return self.getTypedRuleContext(BKITParser.Exp1Context,0)


        def AND(self):
            return self.getToken(BKITParser.AND, 0)

        def OR(self):
            return self.getToken(BKITParser.OR, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_exp1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp1" ):
                return visitor.visitExp1(self)
            else:
                return visitor.visitChildren(self)



    def exp1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Exp1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 64
        self.enterRecursionRule(localctx, 64, self.RULE_exp1, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 305
            self.exp2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 312
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Exp1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp1)
                    self.state = 307
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 308
                    _la = self._input.LA(1)
                    if not(_la==BKITParser.AND or _la==BKITParser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 309
                    self.exp2(0) 
                self.state = 314
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp3(self):
            return self.getTypedRuleContext(BKITParser.Exp3Context,0)


        def exp2(self):
            return self.getTypedRuleContext(BKITParser.Exp2Context,0)


        def ADD_I(self):
            return self.getToken(BKITParser.ADD_I, 0)

        def ADD_F(self):
            return self.getToken(BKITParser.ADD_F, 0)

        def SUB_I(self):
            return self.getToken(BKITParser.SUB_I, 0)

        def SUB_F(self):
            return self.getToken(BKITParser.SUB_F, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_exp2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp2" ):
                return visitor.visitExp2(self)
            else:
                return visitor.visitChildren(self)



    def exp2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Exp2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 66
        self.enterRecursionRule(localctx, 66, self.RULE_exp2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 316
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 323
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Exp2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                    self.state = 318
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 319
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ADD_I) | (1 << BKITParser.SUB_I) | (1 << BKITParser.ADD_F) | (1 << BKITParser.SUB_F))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 320
                    self.exp3(0) 
                self.state = 325
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp4(self):
            return self.getTypedRuleContext(BKITParser.Exp4Context,0)


        def exp3(self):
            return self.getTypedRuleContext(BKITParser.Exp3Context,0)


        def MUL_I(self):
            return self.getToken(BKITParser.MUL_I, 0)

        def MUL_F(self):
            return self.getToken(BKITParser.MUL_F, 0)

        def DIV_I(self):
            return self.getToken(BKITParser.DIV_I, 0)

        def DIV_F(self):
            return self.getToken(BKITParser.DIV_F, 0)

        def MOD_I(self):
            return self.getToken(BKITParser.MOD_I, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_exp3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp3" ):
                return visitor.visitExp3(self)
            else:
                return visitor.visitChildren(self)



    def exp3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Exp3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 68
        self.enterRecursionRule(localctx, 68, self.RULE_exp3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 327
            self.exp4()
            self._ctx.stop = self._input.LT(-1)
            self.state = 334
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Exp3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                    self.state = 329
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 330
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.MUL_I) | (1 << BKITParser.DIV_I) | (1 << BKITParser.MOD_I) | (1 << BKITParser.MUL_F) | (1 << BKITParser.DIV_F))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 331
                    self.exp4() 
                self.state = 336
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(BKITParser.NOT, 0)

        def exp4(self):
            return self.getTypedRuleContext(BKITParser.Exp4Context,0)


        def exp5(self):
            return self.getTypedRuleContext(BKITParser.Exp5Context,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp4" ):
                return visitor.visitExp4(self)
            else:
                return visitor.visitChildren(self)




    def exp4(self):

        localctx = BKITParser.Exp4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_exp4)
        try:
            self.state = 340
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 337
                self.match(BKITParser.NOT)
                self.state = 338
                self.exp4()
                pass
            elif token in [BKITParser.ARRAY_LIT, BKITParser.DEC_INT_LIT, BKITParser.HEX_INT_LIT, BKITParser.OCT_INT_LIT, BKITParser.FLT_LIT, BKITParser.BOOL_LIT, BKITParser.STR_LIT, BKITParser.SUB_I, BKITParser.SUB_F, BKITParser.LB, BKITParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 339
                self.exp5()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp5(self):
            return self.getTypedRuleContext(BKITParser.Exp5Context,0)


        def SUB_I(self):
            return self.getToken(BKITParser.SUB_I, 0)

        def SUB_F(self):
            return self.getToken(BKITParser.SUB_F, 0)

        def index_exp(self):
            return self.getTypedRuleContext(BKITParser.Index_expContext,0)


        def func_call_exp(self):
            return self.getTypedRuleContext(BKITParser.Func_call_expContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp5" ):
                return visitor.visitExp5(self)
            else:
                return visitor.visitChildren(self)




    def exp5(self):

        localctx = BKITParser.Exp5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_exp5)
        self._la = 0 # Token type
        try:
            self.state = 346
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 342
                _la = self._input.LA(1)
                if not(_la==BKITParser.SUB_I or _la==BKITParser.SUB_F):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 343
                self.exp5()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 344
                self.index_exp()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 345
                self.func_call_exp()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_expContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def index_operator(self):
            return self.getTypedRuleContext(BKITParser.Index_operatorContext,0)


        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def func_call(self):
            return self.getTypedRuleContext(BKITParser.Func_callContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_index_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_exp" ):
                return visitor.visitIndex_exp(self)
            else:
                return visitor.visitChildren(self)




    def index_exp(self):

        localctx = BKITParser.Index_expContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_index_exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 350
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.state = 348
                self.match(BKITParser.ID)
                pass

            elif la_ == 2:
                self.state = 349
                self.func_call()
                pass


            self.state = 352
            self.index_operator()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LS(self):
            return self.getToken(BKITParser.LS, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def RS(self):
            return self.getToken(BKITParser.RS, 0)

        def index_operator(self):
            return self.getTypedRuleContext(BKITParser.Index_operatorContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_index_operator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_operator" ):
                return visitor.visitIndex_operator(self)
            else:
                return visitor.visitChildren(self)




    def index_operator(self):

        localctx = BKITParser.Index_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_index_operator)
        try:
            self.state = 363
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 354
                self.match(BKITParser.LS)
                self.state = 355
                self.exp()
                self.state = 356
                self.match(BKITParser.RS)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 358
                self.match(BKITParser.LS)
                self.state = 359
                self.exp()
                self.state = 360
                self.match(BKITParser.RS)
                self.state = 361
                self.index_operator()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_call_expContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def func_call(self):
            return self.getTypedRuleContext(BKITParser.Func_callContext,0)


        def operand(self):
            return self.getTypedRuleContext(BKITParser.OperandContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_func_call_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call_exp" ):
                return visitor.visitFunc_call_exp(self)
            else:
                return visitor.visitChildren(self)




    def func_call_exp(self):

        localctx = BKITParser.Func_call_expContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_func_call_exp)
        try:
            self.state = 367
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 365
                self.func_call()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 366
                self.operand()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(BKITParser.LiteralContext,0)


        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def LB(self):
            return self.getToken(BKITParser.LB, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def RB(self):
            return self.getToken(BKITParser.RB, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_operand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand" ):
                return visitor.visitOperand(self)
            else:
                return visitor.visitChildren(self)




    def operand(self):

        localctx = BKITParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_operand)
        try:
            self.state = 375
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.ARRAY_LIT, BKITParser.DEC_INT_LIT, BKITParser.HEX_INT_LIT, BKITParser.OCT_INT_LIT, BKITParser.FLT_LIT, BKITParser.BOOL_LIT, BKITParser.STR_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 369
                self.literal()
                pass
            elif token in [BKITParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 370
                self.match(BKITParser.ID)
                pass
            elif token in [BKITParser.LB]:
                self.enterOuterAlt(localctx, 3)
                self.state = 371
                self.match(BKITParser.LB)
                self.state = 372
                self.exp()
                self.state = 373
                self.match(BKITParser.RB)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def LB(self):
            return self.getToken(BKITParser.LB, 0)

        def RB(self):
            return self.getToken(BKITParser.RB, 0)

        def exp_list(self):
            return self.getTypedRuleContext(BKITParser.Exp_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_func_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call" ):
                return visitor.visitFunc_call(self)
            else:
                return visitor.visitChildren(self)




    def func_call(self):

        localctx = BKITParser.Func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_func_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 377
            self.match(BKITParser.ID)
            self.state = 378
            self.match(BKITParser.LB)
            self.state = 380
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ARRAY_LIT) | (1 << BKITParser.DEC_INT_LIT) | (1 << BKITParser.HEX_INT_LIT) | (1 << BKITParser.OCT_INT_LIT) | (1 << BKITParser.FLT_LIT) | (1 << BKITParser.BOOL_LIT) | (1 << BKITParser.STR_LIT) | (1 << BKITParser.SUB_I) | (1 << BKITParser.SUB_F) | (1 << BKITParser.NOT) | (1 << BKITParser.LB) | (1 << BKITParser.ID))) != 0):
                self.state = 379
                self.exp_list()


            self.state = 382
            self.match(BKITParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def COMMA(self):
            return self.getToken(BKITParser.COMMA, 0)

        def exp_list(self):
            return self.getTypedRuleContext(BKITParser.Exp_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp_list" ):
                return visitor.visitExp_list(self)
            else:
                return visitor.visitChildren(self)




    def exp_list(self):

        localctx = BKITParser.Exp_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_exp_list)
        try:
            self.state = 389
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 384
                self.exp()
                self.state = 385
                self.match(BKITParser.COMMA)
                self.state = 386
                self.exp_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 388
                self.exp()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEC_INT_LIT(self):
            return self.getToken(BKITParser.DEC_INT_LIT, 0)

        def HEX_INT_LIT(self):
            return self.getToken(BKITParser.HEX_INT_LIT, 0)

        def OCT_INT_LIT(self):
            return self.getToken(BKITParser.OCT_INT_LIT, 0)

        def FLT_LIT(self):
            return self.getToken(BKITParser.FLT_LIT, 0)

        def BOOL_LIT(self):
            return self.getToken(BKITParser.BOOL_LIT, 0)

        def STR_LIT(self):
            return self.getToken(BKITParser.STR_LIT, 0)

        def ARRAY_LIT(self):
            return self.getToken(BKITParser.ARRAY_LIT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = BKITParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 391
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ARRAY_LIT) | (1 << BKITParser.DEC_INT_LIT) | (1 << BKITParser.HEX_INT_LIT) | (1 << BKITParser.OCT_INT_LIT) | (1 << BKITParser.FLT_LIT) | (1 << BKITParser.BOOL_LIT) | (1 << BKITParser.STR_LIT))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DimensionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dimension(self):
            return self.getTypedRuleContext(BKITParser.DimensionContext,0)


        def dimensions(self):
            return self.getTypedRuleContext(BKITParser.DimensionsContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_dimensions

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDimensions" ):
                return visitor.visitDimensions(self)
            else:
                return visitor.visitChildren(self)




    def dimensions(self):

        localctx = BKITParser.DimensionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_dimensions)
        try:
            self.state = 397
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 393
                self.dimension()
                self.state = 394
                self.dimensions()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 396
                self.dimension()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DimensionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LS(self):
            return self.getToken(BKITParser.LS, 0)

        def DEC_INT_LIT(self):
            return self.getToken(BKITParser.DEC_INT_LIT, 0)

        def RS(self):
            return self.getToken(BKITParser.RS, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_dimension

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDimension" ):
                return visitor.visitDimension(self)
            else:
                return visitor.visitChildren(self)




    def dimension(self):

        localctx = BKITParser.DimensionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_dimension)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 399
            self.match(BKITParser.LS)
            self.state = 400
            self.match(BKITParser.DEC_INT_LIT)
            self.state = 401
            self.match(BKITParser.RS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[32] = self.exp1_sempred
        self._predicates[33] = self.exp2_sempred
        self._predicates[34] = self.exp3_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp1_sempred(self, localctx:Exp1Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def exp2_sempred(self, localctx:Exp2Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def exp3_sempred(self, localctx:Exp3Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




