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
        buf.write("\u01d3\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("\3\7\3\b\3\b\3\b\5\b\u00a1\n\b\3\b\3\b\5\b\u00a5\n\b\3")
        buf.write("\b\3\b\3\t\3\t\5\t\u00ab\n\t\3\n\3\n\3\n\3\n\3\n\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3")
        buf.write("\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3 ")
        buf.write("\3 \3 \7 \u0130\n \f \16 \u0133\13 \3 \3 \3 \7 \u0138")
        buf.write("\n \f \16 \u013b\13 \7 \u013d\n \f \16 \u0140\13 \3 \5")
        buf.write(" \u0143\n \3!\3!\3!\5!\u0148\n!\3!\3!\3\"\3\"\7\"\u014e")
        buf.write("\n\"\f\"\16\"\u0151\13\"\3\"\3\"\3\"\3#\3#\3#\7#\u0159")
        buf.write("\n#\f#\16#\u015c\13#\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3")
        buf.write(")\3)\3*\3*\3*\3+\3+\3+\3,\3,\3,\3-\3-\3.\3.\3.\3/\3/\3")
        buf.write("/\3\60\3\60\3\61\3\61\3\61\3\62\3\62\3\63\3\63\3\63\3")
        buf.write("\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\38\38\39\39\3:")
        buf.write("\3:\3;\3;\3<\3<\3=\3=\3>\3>\3>\3>\7>\u019d\n>\f>\16>\u01a0")
        buf.write("\13>\3>\3>\3?\3?\3?\3?\7?\u01a8\n?\f?\16?\u01ab\13?\3")
        buf.write("?\3?\3?\3?\3?\3@\6@\u01b3\n@\r@\16@\u01b4\3@\3@\3A\3A")
        buf.write("\3A\3B\3B\7B\u01be\nB\fB\16B\u01c1\13B\3B\3B\3B\3C\3C")
        buf.write("\3C\7C\u01c9\nC\fC\16C\u01cc\13C\3C\3C\3C\3D\3D\3D\4\u014f")
        buf.write("\u01a9\2E\3\2\5\2\7\2\t\2\13\2\r\2\17\2\21\3\23\4\25\5")
        buf.write("\27\6\31\7\33\b\35\t\37\n!\13#\f%\r\'\16)\17+\20-\21/")
        buf.write("\22\61\23\63\24\65\25\67\269\27;\30=\31?\32A\33C\34E\35")
        buf.write("G\36I\37K M!O\"Q#S$U%W&Y\'[(])_*a+c,e-g.i/k\60m\61o\62")
        buf.write("q\63s\64u\65w\66y\67{8}9\177:\u0081\2\u0083;\u0085<\u0087")
        buf.write("=\3\2\f\3\2\62;\5\2C\\aac|\6\2\n\f\16\17$$^^\n\2$$))^")
        buf.write("^ddhhppttvv\4\2GGgg\4\2--//\3\2\63;\3\2\f\f\5\2\13\f\17")
        buf.write("\17\"\"\3\2$$\2\u01dd\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3")
        buf.write("\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2")
        buf.write("\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'")
        buf.write("\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2")
        buf.write("\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29")
        buf.write("\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2")
        buf.write("C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2")
        buf.write("\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2")
        buf.write("\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2")
        buf.write("\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3")
        buf.write("\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s")
        buf.write("\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2")
        buf.write("}\3\2\2\2\2\177\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2")
        buf.write("\2\2\u0087\3\2\2\2\3\u0089\3\2\2\2\5\u008c\3\2\2\2\7\u0091")
        buf.write("\3\2\2\2\t\u0095\3\2\2\2\13\u0097\3\2\2\2\r\u009a\3\2")
        buf.write("\2\2\17\u00a0\3\2\2\2\21\u00aa\3\2\2\2\23\u00ac\3\2\2")
        buf.write("\2\25\u00b1\3\2\2\2\27\u00b6\3\2\2\2\31\u00bc\3\2\2\2")
        buf.write("\33\u00c4\3\2\2\2\35\u00c7\3\2\2\2\37\u00cc\3\2\2\2!\u00d2")
        buf.write("\3\2\2\2#\u00d8\3\2\2\2%\u00dc\3\2\2\2\'\u00e5\3\2\2\2")
        buf.write(")\u00e8\3\2\2\2+\u00f0\3\2\2\2-\u00f7\3\2\2\2/\u00fe\3")
        buf.write("\2\2\2\61\u0103\3\2\2\2\63\u0109\3\2\2\2\65\u010e\3\2")
        buf.write("\2\2\67\u0112\3\2\2\29\u011b\3\2\2\2;\u011e\3\2\2\2=\u0126")
        buf.write("\3\2\2\2?\u0142\3\2\2\2A\u0144\3\2\2\2C\u014b\3\2\2\2")
        buf.write("E\u0155\3\2\2\2G\u015d\3\2\2\2I\u015f\3\2\2\2K\u0161\3")
        buf.write("\2\2\2M\u0163\3\2\2\2O\u0165\3\2\2\2Q\u0167\3\2\2\2S\u0169")
        buf.write("\3\2\2\2U\u016c\3\2\2\2W\u016f\3\2\2\2Y\u0172\3\2\2\2")
        buf.write("[\u0174\3\2\2\2]\u0177\3\2\2\2_\u017a\3\2\2\2a\u017c\3")
        buf.write("\2\2\2c\u017f\3\2\2\2e\u0181\3\2\2\2g\u0184\3\2\2\2i\u0186")
        buf.write("\3\2\2\2k\u0188\3\2\2\2m\u018a\3\2\2\2o\u018c\3\2\2\2")
        buf.write("q\u018e\3\2\2\2s\u0190\3\2\2\2u\u0192\3\2\2\2w\u0194\3")
        buf.write("\2\2\2y\u0196\3\2\2\2{\u0198\3\2\2\2}\u01a3\3\2\2\2\177")
        buf.write("\u01b2\3\2\2\2\u0081\u01b8\3\2\2\2\u0083\u01bb\3\2\2\2")
        buf.write("\u0085\u01c5\3\2\2\2\u0087\u01d0\3\2\2\2\u0089\u008a\t")
        buf.write("\2\2\2\u008a\4\3\2\2\2\u008b\u008d\5\3\2\2\u008c\u008b")
        buf.write("\3\2\2\2\u008d\u008e\3\2\2\2\u008e\u008c\3\2\2\2\u008e")
        buf.write("\u008f\3\2\2\2\u008f\6\3\2\2\2\u0090\u0092\t\3\2\2\u0091")
        buf.write("\u0090\3\2\2\2\u0092\b\3\2\2\2\u0093\u0096\n\4\2\2\u0094")
        buf.write("\u0096\5\13\6\2\u0095\u0093\3\2\2\2\u0095\u0094\3\2\2")
        buf.write("\2\u0096\n\3\2\2\2\u0097\u0098\7^\2\2\u0098\u0099\t\5")
        buf.write("\2\2\u0099\f\3\2\2\2\u009a\u009b\5w<\2\u009b\u009c\5\5")
        buf.write("\3\2\u009c\16\3\2\2\2\u009d\u009e\5w<\2\u009e\u009f\5")
        buf.write("\5\3\2\u009f\u00a1\3\2\2\2\u00a0\u009d\3\2\2\2\u00a0\u00a1")
        buf.write("\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2\u00a4\t\6\2\2\u00a3")
        buf.write("\u00a5\t\7\2\2\u00a4\u00a3\3\2\2\2\u00a4\u00a5\3\2\2\2")
        buf.write("\u00a5\u00a6\3\2\2\2\u00a6\u00a7\5\5\3\2\u00a7\20\3\2")
        buf.write("\2\2\u00a8\u00ab\5/\30\2\u00a9\u00ab\5\37\20\2\u00aa\u00a8")
        buf.write("\3\2\2\2\u00aa\u00a9\3\2\2\2\u00ab\22\3\2\2\2\u00ac\u00ad")
        buf.write("\7o\2\2\u00ad\u00ae\7c\2\2\u00ae\u00af\7k\2\2\u00af\u00b0")
        buf.write("\7p\2\2\u00b0\24\3\2\2\2\u00b1\u00b2\7c\2\2\u00b2\u00b3")
        buf.write("\7w\2\2\u00b3\u00b4\7v\2\2\u00b4\u00b5\7q\2\2\u00b5\26")
        buf.write("\3\2\2\2\u00b6\u00b7\7d\2\2\u00b7\u00b8\7t\2\2\u00b8\u00b9")
        buf.write("\7g\2\2\u00b9\u00ba\7c\2\2\u00ba\u00bb\7m\2\2\u00bb\30")
        buf.write("\3\2\2\2\u00bc\u00bd\7d\2\2\u00bd\u00be\7q\2\2\u00be\u00bf")
        buf.write("\7q\2\2\u00bf\u00c0\7n\2\2\u00c0\u00c1\7g\2\2\u00c1\u00c2")
        buf.write("\7c\2\2\u00c2\u00c3\7p\2\2\u00c3\32\3\2\2\2\u00c4\u00c5")
        buf.write("\7f\2\2\u00c5\u00c6\7q\2\2\u00c6\34\3\2\2\2\u00c7\u00c8")
        buf.write("\7g\2\2\u00c8\u00c9\7n\2\2\u00c9\u00ca\7u\2\2\u00ca\u00cb")
        buf.write("\7g\2\2\u00cb\36\3\2\2\2\u00cc\u00cd\7h\2\2\u00cd\u00ce")
        buf.write("\7c\2\2\u00ce\u00cf\7n\2\2\u00cf\u00d0\7u\2\2\u00d0\u00d1")
        buf.write("\7g\2\2\u00d1 \3\2\2\2\u00d2\u00d3\7h\2\2\u00d3\u00d4")
        buf.write("\7n\2\2\u00d4\u00d5\7q\2\2\u00d5\u00d6\7c\2\2\u00d6\u00d7")
        buf.write("\7v\2\2\u00d7\"\3\2\2\2\u00d8\u00d9\7h\2\2\u00d9\u00da")
        buf.write("\7q\2\2\u00da\u00db\7t\2\2\u00db$\3\2\2\2\u00dc\u00dd")
        buf.write("\7h\2\2\u00dd\u00de\7w\2\2\u00de\u00df\7p\2\2\u00df\u00e0")
        buf.write("\7e\2\2\u00e0\u00e1\7v\2\2\u00e1\u00e2\7k\2\2\u00e2\u00e3")
        buf.write("\7q\2\2\u00e3\u00e4\7p\2\2\u00e4&\3\2\2\2\u00e5\u00e6")
        buf.write("\7k\2\2\u00e6\u00e7\7h\2\2\u00e7(\3\2\2\2\u00e8\u00e9")
        buf.write("\7k\2\2\u00e9\u00ea\7p\2\2\u00ea\u00eb\7v\2\2\u00eb\u00ec")
        buf.write("\7g\2\2\u00ec\u00ed\7i\2\2\u00ed\u00ee\7g\2\2\u00ee\u00ef")
        buf.write("\7t\2\2\u00ef*\3\2\2\2\u00f0\u00f1\7t\2\2\u00f1\u00f2")
        buf.write("\7g\2\2\u00f2\u00f3\7v\2\2\u00f3\u00f4\7w\2\2\u00f4\u00f5")
        buf.write("\7t\2\2\u00f5\u00f6\7p\2\2\u00f6,\3\2\2\2\u00f7\u00f8")
        buf.write("\7u\2\2\u00f8\u00f9\7v\2\2\u00f9\u00fa\7t\2\2\u00fa\u00fb")
        buf.write("\7k\2\2\u00fb\u00fc\7p\2\2\u00fc\u00fd\7i\2\2\u00fd.\3")
        buf.write("\2\2\2\u00fe\u00ff\7v\2\2\u00ff\u0100\7t\2\2\u0100\u0101")
        buf.write("\7w\2\2\u0101\u0102\7g\2\2\u0102\60\3\2\2\2\u0103\u0104")
        buf.write("\7y\2\2\u0104\u0105\7j\2\2\u0105\u0106\7k\2\2\u0106\u0107")
        buf.write("\7n\2\2\u0107\u0108\7g\2\2\u0108\62\3\2\2\2\u0109\u010a")
        buf.write("\7x\2\2\u010a\u010b\7q\2\2\u010b\u010c\7k\2\2\u010c\u010d")
        buf.write("\7f\2\2\u010d\64\3\2\2\2\u010e\u010f\7q\2\2\u010f\u0110")
        buf.write("\7w\2\2\u0110\u0111\7v\2\2\u0111\66\3\2\2\2\u0112\u0113")
        buf.write("\7e\2\2\u0113\u0114\7q\2\2\u0114\u0115\7p\2\2\u0115\u0116")
        buf.write("\7v\2\2\u0116\u0117\7k\2\2\u0117\u0118\7p\2\2\u0118\u0119")
        buf.write("\7w\2\2\u0119\u011a\7g\2\2\u011a8\3\2\2\2\u011b\u011c")
        buf.write("\7q\2\2\u011c\u011d\7h\2\2\u011d:\3\2\2\2\u011e\u011f")
        buf.write("\7k\2\2\u011f\u0120\7p\2\2\u0120\u0121\7j\2\2\u0121\u0122")
        buf.write("\7g\2\2\u0122\u0123\7t\2\2\u0123\u0124\7k\2\2\u0124\u0125")
        buf.write("\7v\2\2\u0125<\3\2\2\2\u0126\u0127\7c\2\2\u0127\u0128")
        buf.write("\7t\2\2\u0128\u0129\7t\2\2\u0129\u012a\7c\2\2\u012a\u012b")
        buf.write("\7{\2\2\u012b>\3\2\2\2\u012c\u0143\7\62\2\2\u012d\u0131")
        buf.write("\t\b\2\2\u012e\u0130\t\2\2\2\u012f\u012e\3\2\2\2\u0130")
        buf.write("\u0133\3\2\2\2\u0131\u012f\3\2\2\2\u0131\u0132\3\2\2\2")
        buf.write("\u0132\u013e\3\2\2\2\u0133\u0131\3\2\2\2\u0134\u0135\7")
        buf.write("a\2\2\u0135\u0139\t\2\2\2\u0136\u0138\t\2\2\2\u0137\u0136")
        buf.write("\3\2\2\2\u0138\u013b\3\2\2\2\u0139\u0137\3\2\2\2\u0139")
        buf.write("\u013a\3\2\2\2\u013a\u013d\3\2\2\2\u013b\u0139\3\2\2\2")
        buf.write("\u013c\u0134\3\2\2\2\u013d\u0140\3\2\2\2\u013e\u013c\3")
        buf.write("\2\2\2\u013e\u013f\3\2\2\2\u013f\u0141\3\2\2\2\u0140\u013e")
        buf.write("\3\2\2\2\u0141\u0143\b \2\2\u0142\u012c\3\2\2\2\u0142")
        buf.write("\u012d\3\2\2\2\u0143@\3\2\2\2\u0144\u0147\5? \2\u0145")
        buf.write("\u0148\5\r\7\2\u0146\u0148\5\17\b\2\u0147\u0145\3\2\2")
        buf.write("\2\u0147\u0146\3\2\2\2\u0148\u0149\3\2\2\2\u0149\u014a")
        buf.write("\b!\3\2\u014aB\3\2\2\2\u014b\u014f\7$\2\2\u014c\u014e")
        buf.write("\5\t\5\2\u014d\u014c\3\2\2\2\u014e\u0151\3\2\2\2\u014f")
        buf.write("\u0150\3\2\2\2\u014f\u014d\3\2\2\2\u0150\u0152\3\2\2\2")
        buf.write("\u0151\u014f\3\2\2\2\u0152\u0153\7$\2\2\u0153\u0154\b")
        buf.write("\"\4\2\u0154D\3\2\2\2\u0155\u015a\5\7\4\2\u0156\u0159")
        buf.write("\5\7\4\2\u0157\u0159\5\3\2\2\u0158\u0156\3\2\2\2\u0158")
        buf.write("\u0157\3\2\2\2\u0159\u015c\3\2\2\2\u015a\u0158\3\2\2\2")
        buf.write("\u015a\u015b\3\2\2\2\u015bF\3\2\2\2\u015c\u015a\3\2\2")
        buf.write("\2\u015d\u015e\7-\2\2\u015eH\3\2\2\2\u015f\u0160\7/\2")
        buf.write("\2\u0160J\3\2\2\2\u0161\u0162\7,\2\2\u0162L\3\2\2\2\u0163")
        buf.write("\u0164\7\61\2\2\u0164N\3\2\2\2\u0165\u0166\7\'\2\2\u0166")
        buf.write("P\3\2\2\2\u0167\u0168\7#\2\2\u0168R\3\2\2\2\u0169\u016a")
        buf.write("\7(\2\2\u016a\u016b\7(\2\2\u016bT\3\2\2\2\u016c\u016d")
        buf.write("\7~\2\2\u016d\u016e\7~\2\2\u016eV\3\2\2\2\u016f\u0170")
        buf.write("\7#\2\2\u0170\u0171\7?\2\2\u0171X\3\2\2\2\u0172\u0173")
        buf.write("\7>\2\2\u0173Z\3\2\2\2\u0174\u0175\7>\2\2\u0175\u0176")
        buf.write("\7?\2\2\u0176\\\3\2\2\2\u0177\u0178\7@\2\2\u0178\u0179")
        buf.write("\7?\2\2\u0179^\3\2\2\2\u017a\u017b\7@\2\2\u017b`\3\2\2")
        buf.write("\2\u017c\u017d\7?\2\2\u017d\u017e\7?\2\2\u017eb\3\2\2")
        buf.write("\2\u017f\u0180\7?\2\2\u0180d\3\2\2\2\u0181\u0182\7<\2")
        buf.write("\2\u0182\u0183\7<\2\2\u0183f\3\2\2\2\u0184\u0185\7*\2")
        buf.write("\2\u0185h\3\2\2\2\u0186\u0187\7+\2\2\u0187j\3\2\2\2\u0188")
        buf.write("\u0189\7]\2\2\u0189l\3\2\2\2\u018a\u018b\7_\2\2\u018b")
        buf.write("n\3\2\2\2\u018c\u018d\7}\2\2\u018dp\3\2\2\2\u018e\u018f")
        buf.write("\7\177\2\2\u018fr\3\2\2\2\u0190\u0191\7<\2\2\u0191t\3")
        buf.write("\2\2\2\u0192\u0193\7.\2\2\u0193v\3\2\2\2\u0194\u0195\7")
        buf.write("\60\2\2\u0195x\3\2\2\2\u0196\u0197\7=\2\2\u0197z\3\2\2")
        buf.write("\2\u0198\u0199\7\61\2\2\u0199\u019a\7\61\2\2\u019a\u019e")
        buf.write("\3\2\2\2\u019b\u019d\n\t\2\2\u019c\u019b\3\2\2\2\u019d")
        buf.write("\u01a0\3\2\2\2\u019e\u019c\3\2\2\2\u019e\u019f\3\2\2\2")
        buf.write("\u019f\u01a1\3\2\2\2\u01a0\u019e\3\2\2\2\u01a1\u01a2\b")
        buf.write(">\5\2\u01a2|\3\2\2\2\u01a3\u01a4\7\61\2\2\u01a4\u01a5")
        buf.write("\7,\2\2\u01a5\u01a9\3\2\2\2\u01a6\u01a8\13\2\2\2\u01a7")
        buf.write("\u01a6\3\2\2\2\u01a8\u01ab\3\2\2\2\u01a9\u01aa\3\2\2\2")
        buf.write("\u01a9\u01a7\3\2\2\2\u01aa\u01ac\3\2\2\2\u01ab\u01a9\3")
        buf.write("\2\2\2\u01ac\u01ad\7,\2\2\u01ad\u01ae\7\61\2\2\u01ae\u01af")
        buf.write("\3\2\2\2\u01af\u01b0\b?\5\2\u01b0~\3\2\2\2\u01b1\u01b3")
        buf.write("\t\n\2\2\u01b2\u01b1\3\2\2\2\u01b3\u01b4\3\2\2\2\u01b4")
        buf.write("\u01b2\3\2\2\2\u01b4\u01b5\3\2\2\2\u01b5\u01b6\3\2\2\2")
        buf.write("\u01b6\u01b7\b@\5\2\u01b7\u0080\3\2\2\2\u01b8\u01b9\7")
        buf.write("^\2\2\u01b9\u01ba\n\5\2\2\u01ba\u0082\3\2\2\2\u01bb\u01bf")
        buf.write("\7$\2\2\u01bc\u01be\5\t\5\2\u01bd\u01bc\3\2\2\2\u01be")
        buf.write("\u01c1\3\2\2\2\u01bf\u01bd\3\2\2\2\u01bf\u01c0\3\2\2\2")
        buf.write("\u01c0\u01c2\3\2\2\2\u01c1\u01bf\3\2\2\2\u01c2\u01c3\5")
        buf.write("\u0081A\2\u01c3\u01c4\bB\6\2\u01c4\u0084\3\2\2\2\u01c5")
        buf.write("\u01ca\7$\2\2\u01c6\u01c9\5\t\5\2\u01c7\u01c9\n\13\2\2")
        buf.write("\u01c8\u01c6\3\2\2\2\u01c8\u01c7\3\2\2\2\u01c9\u01cc\3")
        buf.write("\2\2\2\u01ca\u01c8\3\2\2\2\u01ca\u01cb\3\2\2\2\u01cb\u01cd")
        buf.write("\3\2\2\2\u01cc\u01ca\3\2\2\2\u01cd\u01ce\7\2\2\3\u01ce")
        buf.write("\u01cf\bC\7\2\u01cf\u0086\3\2\2\2\u01d0\u01d1\13\2\2\2")
        buf.write("\u01d1\u01d2\bD\b\2\u01d2\u0088\3\2\2\2\27\2\u008e\u0091")
        buf.write("\u0095\u00a0\u00a4\u00aa\u0131\u0139\u013e\u0142\u0147")
        buf.write("\u014f\u0158\u015a\u019e\u01a9\u01b4\u01bf\u01c8\u01ca")
        buf.write("\t\3 \2\3!\3\3\"\4\b\2\2\3B\5\3C\6\3D\7")
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
    MINUS = 29
    MUL = 30
    DIV = 31
    MOD = 32
    NOT = 33
    AND = 34
    OR = 35
    NOT_EQUAL = 36
    LESS = 37
    LESS_EQUAL = 38
    GREATER_EQUAL = 39
    GREATER = 40
    EQUAL = 41
    ASSIGN = 42
    CONCAT = 43
    LB = 44
    RB = 45
    LSB = 46
    RSB = 47
    LCB = 48
    RCB = 49
    COLON = 50
    COMMA = 51
    DOT = 52
    SEMI = 53
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
            "PLUS", "MINUS", "MUL", "DIV", "MOD", "NOT", "AND", "OR", "NOT_EQUAL", 
            "LESS", "LESS_EQUAL", "GREATER_EQUAL", "GREATER", "EQUAL", "ASSIGN", 
            "CONCAT", "LB", "RB", "LSB", "RSB", "LCB", "RCB", "COLON", "COMMA", 
            "DOT", "SEMI", "COMMENT_LINE", "COMMENT_MULTYLINE", "WS", "ILLEGAL_ESCAPE", 
            "UNCLOSE_STRING", "ERROR_CHAR" ]

    ruleNames = [ "Digit", "Digits", "Letter", "StringChar", "Escape_Seq", 
                  "DECPART", "EXPART", "BOOLLIT", "MAIN", "AUTO", "BREAK", 
                  "BOOLEAN", "DO", "ELSE", "FALSE", "FLOAT", "FOR", "FUNCTION", 
                  "IF", "INTEGER", "RETURN", "STRING", "TRUE", "WHILE", 
                  "VOID", "OUT", "CONTINUE", "OF", "INHERIT", "ARRAY", "INTLIT", 
                  "FLOATLIT", "STRINGLIT", "ID", "PLUS", "MINUS", "MUL", 
                  "DIV", "MOD", "NOT", "AND", "OR", "NOT_EQUAL", "LESS", 
                  "LESS_EQUAL", "GREATER_EQUAL", "GREATER", "EQUAL", "ASSIGN", 
                  "CONCAT", "LB", "RB", "LSB", "RSB", "LCB", "RCB", "COLON", 
                  "COMMA", "DOT", "SEMI", "COMMENT_LINE", "COMMENT_MULTYLINE", 
                  "WS", "Esc_illigal", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", 
                  "ERROR_CHAR" ]

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
     


