# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2=")
        buf.write("\u01df\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\3\2\3\2\3\3\6\3\u008d\n\3\r\3\16\3\u008e\3\4\5")
        buf.write("\4\u0092\n\4\3\5\3\5\5\5\u0096\n\5\3\6\3\6\3\6\3\7\3\7")
        buf.write("\7\7\u009d\n\7\f\7\16\7\u00a0\13\7\3\b\3\b\3\b\5\b\u00a5")
        buf.write("\n\b\3\b\3\b\5\b\u00a9\n\b\3\b\3\b\3\t\3\t\5\t\u00af\n")
        buf.write("\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16")
        buf.write("\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22")
        buf.write("\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\24")
        buf.write("\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\35\3\35")
        buf.write("\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3 \3 \3 \7 \u0134\n \f \16 \u0137")
        buf.write("\13 \3 \3 \3 \7 \u013c\n \f \16 \u013f\13 \7 \u0141\n")
        buf.write(" \f \16 \u0144\13 \3 \5 \u0147\n \3!\3!\3!\5!\u014c\n")
        buf.write("!\3!\5!\u014f\n!\3!\3!\3!\5!\u0154\n!\3!\3!\3\"\3\"\7")
        buf.write("\"\u015a\n\"\f\"\16\"\u015d\13\"\3\"\3\"\3\"\3#\3#\3#")
        buf.write("\7#\u0165\n#\f#\16#\u0168\13#\3$\3$\3%\3%\3&\3&\3\'\3")
        buf.write("\'\3(\3(\3)\3)\3*\3*\3*\3+\3+\3+\3,\3,\3,\3-\3-\3.\3.")
        buf.write("\3.\3/\3/\3/\3\60\3\60\3\61\3\61\3\61\3\62\3\62\3\63\3")
        buf.write("\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\38\3")
        buf.write("8\39\39\3:\3:\3;\3;\3<\3<\3=\3=\3>\3>\3>\3>\7>\u01a9\n")
        buf.write(">\f>\16>\u01ac\13>\3>\3>\3?\3?\3?\3?\7?\u01b4\n?\f?\16")
        buf.write("?\u01b7\13?\3?\3?\3?\3?\3?\3@\6@\u01bf\n@\r@\16@\u01c0")
        buf.write("\3@\3@\3A\3A\3A\3B\3B\7B\u01ca\nB\fB\16B\u01cd\13B\3B")
        buf.write("\3B\3B\3C\3C\3C\7C\u01d5\nC\fC\16C\u01d8\13C\3C\3C\3C")
        buf.write("\3D\3D\3D\4\u015b\u01b5\2E\3\2\5\2\7\2\t\2\13\2\r\2\17")
        buf.write("\2\21\3\23\4\25\5\27\6\31\7\33\b\35\t\37\n!\13#\f%\r\'")
        buf.write("\16)\17+\20-\21/\22\61\23\63\24\65\25\67\269\27;\30=\31")
        buf.write("?\32A\33C\34E\35G\36I\37K M!O\"Q#S$U%W&Y\'[(])_*a+c,e")
        buf.write("-g.i/k\60m\61o\62q\63s\64u\65w\66y\67{8}9\177:\u0081\2")
        buf.write("\u0083;\u0085<\u0087=\3\2\f\3\2\62;\5\2C\\aac|\6\2\n\f")
        buf.write("\16\17$$^^\n\2$$))^^ddhhppttvv\4\2GGgg\4\2--//\3\2\63")
        buf.write(";\3\2\f\f\5\2\13\f\17\17\"\"\3\2$$\2\u01ec\2\21\3\2\2")
        buf.write("\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2")
        buf.write("\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#")
        buf.write("\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2")
        buf.write("\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65")
        buf.write("\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2")
        buf.write("\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2")
        buf.write("\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2")
        buf.write("\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3")
        buf.write("\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e")
        buf.write("\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2")
        buf.write("o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2")
        buf.write("\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0083")
        buf.write("\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\3\u0089\3\2\2")
        buf.write("\2\5\u008c\3\2\2\2\7\u0091\3\2\2\2\t\u0095\3\2\2\2\13")
        buf.write("\u0097\3\2\2\2\r\u009a\3\2\2\2\17\u00a4\3\2\2\2\21\u00ae")
        buf.write("\3\2\2\2\23\u00b0\3\2\2\2\25\u00b5\3\2\2\2\27\u00ba\3")
        buf.write("\2\2\2\31\u00c0\3\2\2\2\33\u00c8\3\2\2\2\35\u00cb\3\2")
        buf.write("\2\2\37\u00d0\3\2\2\2!\u00d6\3\2\2\2#\u00dc\3\2\2\2%\u00e0")
        buf.write("\3\2\2\2\'\u00e9\3\2\2\2)\u00ec\3\2\2\2+\u00f4\3\2\2\2")
        buf.write("-\u00fb\3\2\2\2/\u0102\3\2\2\2\61\u0107\3\2\2\2\63\u010d")
        buf.write("\3\2\2\2\65\u0112\3\2\2\2\67\u0116\3\2\2\29\u011f\3\2")
        buf.write("\2\2;\u0122\3\2\2\2=\u012a\3\2\2\2?\u0146\3\2\2\2A\u0153")
        buf.write("\3\2\2\2C\u0157\3\2\2\2E\u0161\3\2\2\2G\u0169\3\2\2\2")
        buf.write("I\u016b\3\2\2\2K\u016d\3\2\2\2M\u016f\3\2\2\2O\u0171\3")
        buf.write("\2\2\2Q\u0173\3\2\2\2S\u0175\3\2\2\2U\u0178\3\2\2\2W\u017b")
        buf.write("\3\2\2\2Y\u017e\3\2\2\2[\u0180\3\2\2\2]\u0183\3\2\2\2")
        buf.write("_\u0186\3\2\2\2a\u0188\3\2\2\2c\u018b\3\2\2\2e\u018d\3")
        buf.write("\2\2\2g\u0190\3\2\2\2i\u0192\3\2\2\2k\u0194\3\2\2\2m\u0196")
        buf.write("\3\2\2\2o\u0198\3\2\2\2q\u019a\3\2\2\2s\u019c\3\2\2\2")
        buf.write("u\u019e\3\2\2\2w\u01a0\3\2\2\2y\u01a2\3\2\2\2{\u01a4\3")
        buf.write("\2\2\2}\u01af\3\2\2\2\177\u01be\3\2\2\2\u0081\u01c4\3")
        buf.write("\2\2\2\u0083\u01c7\3\2\2\2\u0085\u01d1\3\2\2\2\u0087\u01dc")
        buf.write("\3\2\2\2\u0089\u008a\t\2\2\2\u008a\4\3\2\2\2\u008b\u008d")
        buf.write("\5\3\2\2\u008c\u008b\3\2\2\2\u008d\u008e\3\2\2\2\u008e")
        buf.write("\u008c\3\2\2\2\u008e\u008f\3\2\2\2\u008f\6\3\2\2\2\u0090")
        buf.write("\u0092\t\3\2\2\u0091\u0090\3\2\2\2\u0092\b\3\2\2\2\u0093")
        buf.write("\u0096\n\4\2\2\u0094\u0096\5\13\6\2\u0095\u0093\3\2\2")
        buf.write("\2\u0095\u0094\3\2\2\2\u0096\n\3\2\2\2\u0097\u0098\7^")
        buf.write("\2\2\u0098\u0099\t\5\2\2\u0099\f\3\2\2\2\u009a\u009e\5")
        buf.write("w<\2\u009b\u009d\5\3\2\2\u009c\u009b\3\2\2\2\u009d\u00a0")
        buf.write("\3\2\2\2\u009e\u009c\3\2\2\2\u009e\u009f\3\2\2\2\u009f")
        buf.write("\16\3\2\2\2\u00a0\u009e\3\2\2\2\u00a1\u00a2\5w<\2\u00a2")
        buf.write("\u00a3\5\5\3\2\u00a3\u00a5\3\2\2\2\u00a4\u00a1\3\2\2\2")
        buf.write("\u00a4\u00a5\3\2\2\2\u00a5\u00a6\3\2\2\2\u00a6\u00a8\t")
        buf.write("\6\2\2\u00a7\u00a9\t\7\2\2\u00a8\u00a7\3\2\2\2\u00a8\u00a9")
        buf.write("\3\2\2\2\u00a9\u00aa\3\2\2\2\u00aa\u00ab\5\5\3\2\u00ab")
        buf.write("\20\3\2\2\2\u00ac\u00af\5/\30\2\u00ad\u00af\5\37\20\2")
        buf.write("\u00ae\u00ac\3\2\2\2\u00ae\u00ad\3\2\2\2\u00af\22\3\2")
        buf.write("\2\2\u00b0\u00b1\7o\2\2\u00b1\u00b2\7c\2\2\u00b2\u00b3")
        buf.write("\7k\2\2\u00b3\u00b4\7p\2\2\u00b4\24\3\2\2\2\u00b5\u00b6")
        buf.write("\7c\2\2\u00b6\u00b7\7w\2\2\u00b7\u00b8\7v\2\2\u00b8\u00b9")
        buf.write("\7q\2\2\u00b9\26\3\2\2\2\u00ba\u00bb\7d\2\2\u00bb\u00bc")
        buf.write("\7t\2\2\u00bc\u00bd\7g\2\2\u00bd\u00be\7c\2\2\u00be\u00bf")
        buf.write("\7m\2\2\u00bf\30\3\2\2\2\u00c0\u00c1\7d\2\2\u00c1\u00c2")
        buf.write("\7q\2\2\u00c2\u00c3\7q\2\2\u00c3\u00c4\7n\2\2\u00c4\u00c5")
        buf.write("\7g\2\2\u00c5\u00c6\7c\2\2\u00c6\u00c7\7p\2\2\u00c7\32")
        buf.write("\3\2\2\2\u00c8\u00c9\7f\2\2\u00c9\u00ca\7q\2\2\u00ca\34")
        buf.write("\3\2\2\2\u00cb\u00cc\7g\2\2\u00cc\u00cd\7n\2\2\u00cd\u00ce")
        buf.write("\7u\2\2\u00ce\u00cf\7g\2\2\u00cf\36\3\2\2\2\u00d0\u00d1")
        buf.write("\7h\2\2\u00d1\u00d2\7c\2\2\u00d2\u00d3\7n\2\2\u00d3\u00d4")
        buf.write("\7u\2\2\u00d4\u00d5\7g\2\2\u00d5 \3\2\2\2\u00d6\u00d7")
        buf.write("\7h\2\2\u00d7\u00d8\7n\2\2\u00d8\u00d9\7q\2\2\u00d9\u00da")
        buf.write("\7c\2\2\u00da\u00db\7v\2\2\u00db\"\3\2\2\2\u00dc\u00dd")
        buf.write("\7h\2\2\u00dd\u00de\7q\2\2\u00de\u00df\7t\2\2\u00df$\3")
        buf.write("\2\2\2\u00e0\u00e1\7h\2\2\u00e1\u00e2\7w\2\2\u00e2\u00e3")
        buf.write("\7p\2\2\u00e3\u00e4\7e\2\2\u00e4\u00e5\7v\2\2\u00e5\u00e6")
        buf.write("\7k\2\2\u00e6\u00e7\7q\2\2\u00e7\u00e8\7p\2\2\u00e8&\3")
        buf.write("\2\2\2\u00e9\u00ea\7k\2\2\u00ea\u00eb\7h\2\2\u00eb(\3")
        buf.write("\2\2\2\u00ec\u00ed\7k\2\2\u00ed\u00ee\7p\2\2\u00ee\u00ef")
        buf.write("\7v\2\2\u00ef\u00f0\7g\2\2\u00f0\u00f1\7i\2\2\u00f1\u00f2")
        buf.write("\7g\2\2\u00f2\u00f3\7t\2\2\u00f3*\3\2\2\2\u00f4\u00f5")
        buf.write("\7t\2\2\u00f5\u00f6\7g\2\2\u00f6\u00f7\7v\2\2\u00f7\u00f8")
        buf.write("\7w\2\2\u00f8\u00f9\7t\2\2\u00f9\u00fa\7p\2\2\u00fa,\3")
        buf.write("\2\2\2\u00fb\u00fc\7u\2\2\u00fc\u00fd\7v\2\2\u00fd\u00fe")
        buf.write("\7t\2\2\u00fe\u00ff\7k\2\2\u00ff\u0100\7p\2\2\u0100\u0101")
        buf.write("\7i\2\2\u0101.\3\2\2\2\u0102\u0103\7v\2\2\u0103\u0104")
        buf.write("\7t\2\2\u0104\u0105\7w\2\2\u0105\u0106\7g\2\2\u0106\60")
        buf.write("\3\2\2\2\u0107\u0108\7y\2\2\u0108\u0109\7j\2\2\u0109\u010a")
        buf.write("\7k\2\2\u010a\u010b\7n\2\2\u010b\u010c\7g\2\2\u010c\62")
        buf.write("\3\2\2\2\u010d\u010e\7x\2\2\u010e\u010f\7q\2\2\u010f\u0110")
        buf.write("\7k\2\2\u0110\u0111\7f\2\2\u0111\64\3\2\2\2\u0112\u0113")
        buf.write("\7q\2\2\u0113\u0114\7w\2\2\u0114\u0115\7v\2\2\u0115\66")
        buf.write("\3\2\2\2\u0116\u0117\7e\2\2\u0117\u0118\7q\2\2\u0118\u0119")
        buf.write("\7p\2\2\u0119\u011a\7v\2\2\u011a\u011b\7k\2\2\u011b\u011c")
        buf.write("\7p\2\2\u011c\u011d\7w\2\2\u011d\u011e\7g\2\2\u011e8\3")
        buf.write("\2\2\2\u011f\u0120\7q\2\2\u0120\u0121\7h\2\2\u0121:\3")
        buf.write("\2\2\2\u0122\u0123\7k\2\2\u0123\u0124\7p\2\2\u0124\u0125")
        buf.write("\7j\2\2\u0125\u0126\7g\2\2\u0126\u0127\7t\2\2\u0127\u0128")
        buf.write("\7k\2\2\u0128\u0129\7v\2\2\u0129<\3\2\2\2\u012a\u012b")
        buf.write("\7c\2\2\u012b\u012c\7t\2\2\u012c\u012d\7t\2\2\u012d\u012e")
        buf.write("\7c\2\2\u012e\u012f\7{\2\2\u012f>\3\2\2\2\u0130\u0147")
        buf.write("\7\62\2\2\u0131\u0135\t\b\2\2\u0132\u0134\t\2\2\2\u0133")
        buf.write("\u0132\3\2\2\2\u0134\u0137\3\2\2\2\u0135\u0133\3\2\2\2")
        buf.write("\u0135\u0136\3\2\2\2\u0136\u0142\3\2\2\2\u0137\u0135\3")
        buf.write("\2\2\2\u0138\u0139\7a\2\2\u0139\u013d\t\2\2\2\u013a\u013c")
        buf.write("\t\2\2\2\u013b\u013a\3\2\2\2\u013c\u013f\3\2\2\2\u013d")
        buf.write("\u013b\3\2\2\2\u013d\u013e\3\2\2\2\u013e\u0141\3\2\2\2")
        buf.write("\u013f\u013d\3\2\2\2\u0140\u0138\3\2\2\2\u0141\u0144\3")
        buf.write("\2\2\2\u0142\u0140\3\2\2\2\u0142\u0143\3\2\2\2\u0143\u0145")
        buf.write("\3\2\2\2\u0144\u0142\3\2\2\2\u0145\u0147\b \2\2\u0146")
        buf.write("\u0130\3\2\2\2\u0146\u0131\3\2\2\2\u0147@\3\2\2\2\u0148")
        buf.write("\u014b\5? \2\u0149\u014c\5\r\7\2\u014a\u014c\5\17\b\2")
        buf.write("\u014b\u0149\3\2\2\2\u014b\u014a\3\2\2\2\u014c\u0154\3")
        buf.write("\2\2\2\u014d\u014f\5? \2\u014e\u014d\3\2\2\2\u014e\u014f")
        buf.write("\3\2\2\2\u014f\u0150\3\2\2\2\u0150\u0151\5\r\7\2\u0151")
        buf.write("\u0152\5\17\b\2\u0152\u0154\3\2\2\2\u0153\u0148\3\2\2")
        buf.write("\2\u0153\u014e\3\2\2\2\u0154\u0155\3\2\2\2\u0155\u0156")
        buf.write("\b!\3\2\u0156B\3\2\2\2\u0157\u015b\7$\2\2\u0158\u015a")
        buf.write("\5\t\5\2\u0159\u0158\3\2\2\2\u015a\u015d\3\2\2\2\u015b")
        buf.write("\u015c\3\2\2\2\u015b\u0159\3\2\2\2\u015c\u015e\3\2\2\2")
        buf.write("\u015d\u015b\3\2\2\2\u015e\u015f\7$\2\2\u015f\u0160\b")
        buf.write("\"\4\2\u0160D\3\2\2\2\u0161\u0166\5\7\4\2\u0162\u0165")
        buf.write("\5\7\4\2\u0163\u0165\5\3\2\2\u0164\u0162\3\2\2\2\u0164")
        buf.write("\u0163\3\2\2\2\u0165\u0168\3\2\2\2\u0166\u0164\3\2\2\2")
        buf.write("\u0166\u0167\3\2\2\2\u0167F\3\2\2\2\u0168\u0166\3\2\2")
        buf.write("\2\u0169\u016a\7-\2\2\u016aH\3\2\2\2\u016b\u016c\7/\2")
        buf.write("\2\u016cJ\3\2\2\2\u016d\u016e\7,\2\2\u016eL\3\2\2\2\u016f")
        buf.write("\u0170\7\61\2\2\u0170N\3\2\2\2\u0171\u0172\7\'\2\2\u0172")
        buf.write("P\3\2\2\2\u0173\u0174\7#\2\2\u0174R\3\2\2\2\u0175\u0176")
        buf.write("\7(\2\2\u0176\u0177\7(\2\2\u0177T\3\2\2\2\u0178\u0179")
        buf.write("\7~\2\2\u0179\u017a\7~\2\2\u017aV\3\2\2\2\u017b\u017c")
        buf.write("\7#\2\2\u017c\u017d\7?\2\2\u017dX\3\2\2\2\u017e\u017f")
        buf.write("\7>\2\2\u017fZ\3\2\2\2\u0180\u0181\7>\2\2\u0181\u0182")
        buf.write("\7?\2\2\u0182\\\3\2\2\2\u0183\u0184\7@\2\2\u0184\u0185")
        buf.write("\7?\2\2\u0185^\3\2\2\2\u0186\u0187\7@\2\2\u0187`\3\2\2")
        buf.write("\2\u0188\u0189\7?\2\2\u0189\u018a\7?\2\2\u018ab\3\2\2")
        buf.write("\2\u018b\u018c\7?\2\2\u018cd\3\2\2\2\u018d\u018e\7<\2")
        buf.write("\2\u018e\u018f\7<\2\2\u018ff\3\2\2\2\u0190\u0191\7*\2")
        buf.write("\2\u0191h\3\2\2\2\u0192\u0193\7+\2\2\u0193j\3\2\2\2\u0194")
        buf.write("\u0195\7]\2\2\u0195l\3\2\2\2\u0196\u0197\7_\2\2\u0197")
        buf.write("n\3\2\2\2\u0198\u0199\7}\2\2\u0199p\3\2\2\2\u019a\u019b")
        buf.write("\7\177\2\2\u019br\3\2\2\2\u019c\u019d\7<\2\2\u019dt\3")
        buf.write("\2\2\2\u019e\u019f\7.\2\2\u019fv\3\2\2\2\u01a0\u01a1\7")
        buf.write("\60\2\2\u01a1x\3\2\2\2\u01a2\u01a3\7=\2\2\u01a3z\3\2\2")
        buf.write("\2\u01a4\u01a5\7\61\2\2\u01a5\u01a6\7\61\2\2\u01a6\u01aa")
        buf.write("\3\2\2\2\u01a7\u01a9\n\t\2\2\u01a8\u01a7\3\2\2\2\u01a9")
        buf.write("\u01ac\3\2\2\2\u01aa\u01a8\3\2\2\2\u01aa\u01ab\3\2\2\2")
        buf.write("\u01ab\u01ad\3\2\2\2\u01ac\u01aa\3\2\2\2\u01ad\u01ae\b")
        buf.write(">\5\2\u01ae|\3\2\2\2\u01af\u01b0\7\61\2\2\u01b0\u01b1")
        buf.write("\7,\2\2\u01b1\u01b5\3\2\2\2\u01b2\u01b4\13\2\2\2\u01b3")
        buf.write("\u01b2\3\2\2\2\u01b4\u01b7\3\2\2\2\u01b5\u01b6\3\2\2\2")
        buf.write("\u01b5\u01b3\3\2\2\2\u01b6\u01b8\3\2\2\2\u01b7\u01b5\3")
        buf.write("\2\2\2\u01b8\u01b9\7,\2\2\u01b9\u01ba\7\61\2\2\u01ba\u01bb")
        buf.write("\3\2\2\2\u01bb\u01bc\b?\5\2\u01bc~\3\2\2\2\u01bd\u01bf")
        buf.write("\t\n\2\2\u01be\u01bd\3\2\2\2\u01bf\u01c0\3\2\2\2\u01c0")
        buf.write("\u01be\3\2\2\2\u01c0\u01c1\3\2\2\2\u01c1\u01c2\3\2\2\2")
        buf.write("\u01c2\u01c3\b@\5\2\u01c3\u0080\3\2\2\2\u01c4\u01c5\7")
        buf.write("^\2\2\u01c5\u01c6\n\5\2\2\u01c6\u0082\3\2\2\2\u01c7\u01cb")
        buf.write("\7$\2\2\u01c8\u01ca\5\t\5\2\u01c9\u01c8\3\2\2\2\u01ca")
        buf.write("\u01cd\3\2\2\2\u01cb\u01c9\3\2\2\2\u01cb\u01cc\3\2\2\2")
        buf.write("\u01cc\u01ce\3\2\2\2\u01cd\u01cb\3\2\2\2\u01ce\u01cf\5")
        buf.write("\u0081A\2\u01cf\u01d0\bB\6\2\u01d0\u0084\3\2\2\2\u01d1")
        buf.write("\u01d6\7$\2\2\u01d2\u01d5\5\t\5\2\u01d3\u01d5\n\13\2\2")
        buf.write("\u01d4\u01d2\3\2\2\2\u01d4\u01d3\3\2\2\2\u01d5\u01d8\3")
        buf.write("\2\2\2\u01d6\u01d4\3\2\2\2\u01d6\u01d7\3\2\2\2\u01d7\u01d9")
        buf.write("\3\2\2\2\u01d8\u01d6\3\2\2\2\u01d9\u01da\7\2\2\3\u01da")
        buf.write("\u01db\bC\7\2\u01db\u0086\3\2\2\2\u01dc\u01dd\13\2\2\2")
        buf.write("\u01dd\u01de\bD\b\2\u01de\u0088\3\2\2\2\32\2\u008e\u0091")
        buf.write("\u0095\u009e\u00a4\u00a8\u00ae\u0135\u013d\u0142\u0146")
        buf.write("\u014b\u014e\u0153\u015b\u0164\u0166\u01aa\u01b5\u01c0")
        buf.write("\u01cb\u01d4\u01d6\t\3 \2\3!\3\3\"\4\b\2\2\3B\5\3C\6\3")
        buf.write("D\7")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    BOOLLIT = 1
    MAIN = 2
    AUTO = 3
    BREAK = 4
    BOOLEAN = 5
    DO = 6
    ELSE = 7
    FALSE = 8
    FLOAT = 9
    FOR = 10
    FUNCTION = 11
    IF = 12
    INTEGER = 13
    RETURN = 14
    STRING = 15
    TRUE = 16
    WHILE = 17
    VOID = 18
    OUT = 19
    CONTINUE = 20
    OF = 21
    INHERIT = 22
    ARRAY = 23
    INTLIT = 24
    FLOATLIT = 25
    STRINGLIT = 26
    ID = 27
    PLUS = 28
    SUB = 29
    MUL = 30
    DIV = 31
    MOD = 32
    NOT = 33
    AND = 34
    OR = 35
    NEQ = 36
    LT = 37
    LEQ = 38
    GEQ = 39
    GT = 40
    EQ = 41
    ASSIGN = 42
    CONCAT = 43
    LB = 44
    RB = 45
    LSB = 46
    RSB = 47
    LCB = 48
    RCB = 49
    COLON = 50
    CM = 51
    DOT = 52
    SM = 53
    COMMENT_LINE = 54
    COMMENT_MULTYLINE = 55
    WS = 56
    ILLEGAL_ESCAPE = 57
    UNCLOSE_STRING = 58
    ERROR_CHAR = 59

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'main'", "'auto'", "'break'", "'boolean'", "'do'", "'else'", 
            "'false'", "'float'", "'for'", "'function'", "'if'", "'integer'", 
            "'return'", "'string'", "'true'", "'while'", "'void'", "'out'", 
            "'continue'", "'of'", "'inherit'", "'array'", "'+'", "'-'", 
            "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", "'!='", "'<'", "'<='", 
            "'>='", "'>'", "'=='", "'='", "'::'", "'('", "')'", "'['", "']'", 
            "'{'", "'}'", "':'", "','", "'.'", "';'" ]

    symbolicNames = [ "<INVALID>",
            "BOOLLIT", "MAIN", "AUTO", "BREAK", "BOOLEAN", "DO", "ELSE", 
            "FALSE", "FLOAT", "FOR", "FUNCTION", "IF", "INTEGER", "RETURN", 
            "STRING", "TRUE", "WHILE", "VOID", "OUT", "CONTINUE", "OF", 
            "INHERIT", "ARRAY", "INTLIT", "FLOATLIT", "STRINGLIT", "ID", 
            "PLUS", "SUB", "MUL", "DIV", "MOD", "NOT", "AND", "OR", "NEQ", 
            "LT", "LEQ", "GEQ", "GT", "EQ", "ASSIGN", "CONCAT", "LB", "RB", 
            "LSB", "RSB", "LCB", "RCB", "COLON", "CM", "DOT", "SM", "COMMENT_LINE", 
            "COMMENT_MULTYLINE", "WS", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", 
            "ERROR_CHAR" ]

    ruleNames = [ "Digit", "Digits", "Letter", "StringChar", "Escape_Seq", 
                  "DECPART", "EXPART", "BOOLLIT", "MAIN", "AUTO", "BREAK", 
                  "BOOLEAN", "DO", "ELSE", "FALSE", "FLOAT", "FOR", "FUNCTION", 
                  "IF", "INTEGER", "RETURN", "STRING", "TRUE", "WHILE", 
                  "VOID", "OUT", "CONTINUE", "OF", "INHERIT", "ARRAY", "INTLIT", 
                  "FLOATLIT", "STRINGLIT", "ID", "PLUS", "SUB", "MUL", "DIV", 
                  "MOD", "NOT", "AND", "OR", "NEQ", "LT", "LEQ", "GEQ", 
                  "GT", "EQ", "ASSIGN", "CONCAT", "LB", "RB", "LSB", "RSB", 
                  "LCB", "RCB", "COLON", "CM", "DOT", "SM", "COMMENT_LINE", 
                  "COMMENT_MULTYLINE", "WS", "Esc_illigal", "ILLEGAL_ESCAPE", 
                  "UNCLOSE_STRING", "ERROR_CHAR" ]

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[30] = self.INTLIT_action 
            actions[31] = self.FLOATLIT_action 
            actions[32] = self.STRINGLIT_action 
            actions[64] = self.ILLEGAL_ESCAPE_action 
            actions[65] = self.UNCLOSE_STRING_action 
            actions[66] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INTLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace("_", "")
     

    def FLOATLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.replace("_", "")
     

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            t = str(self.text) ; self.text = t[1:-1]
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            	t = self.text
            	raise IllegalEscape(t[1:])

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

            	t = self.text;
            	raise UncloseString(t[1:]);

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
            raise ErrorToken(self.text)
     


