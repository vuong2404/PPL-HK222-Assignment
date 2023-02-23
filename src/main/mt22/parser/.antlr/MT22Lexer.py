# Generated from c:\Users\Admin\Documents\assignment1-initial\src\main\mt22\parser\MT22.g4 by ANTLR 4.9.2
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
        buf.write("\u01ba\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\3\2\3\2\3\3")
        buf.write("\7\3\u0087\n\3\f\3\16\3\u008a\13\3\3\4\5\4\u008d\n\4\3")
        buf.write("\5\3\5\3\5\3\6\3\6\5\6\u0094\n\6\3\6\3\6\5\6\u0098\n\6")
        buf.write("\3\6\3\6\3\7\3\7\3\7\3\7\7\7\u00a0\n\7\f\7\16\7\u00a3")
        buf.write("\13\7\3\b\3\b\3\b\3\b\7\b\u00a9\n\b\f\b\16\b\u00ac\13")
        buf.write("\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\21")
        buf.write("\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\32\3\32")
        buf.write("\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37\5\37\u0133\n")
        buf.write("\37\3\37\3\37\3\37\3\37\3\37\7\37\u013a\n\37\f\37\16\37")
        buf.write("\u013d\13\37\3\37\3\37\5\37\u0141\n\37\3 \3 \3 \5 \u0146")
        buf.write("\n \3 \3 \3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3")
        buf.write("!\3!\3!\3!\7!\u015c\n!\f!\16!\u015f\13!\3!\3!\3!\3\"\3")
        buf.write("\"\3\"\7\"\u0167\n\"\f\"\16\"\u016a\13\"\3#\3#\3$\3$\3")
        buf.write("%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3+\3")
        buf.write(",\3,\3-\3-\3-\3.\3.\3.\3/\3/\3\60\3\60\3\60\3\61\3\61")
        buf.write("\3\62\3\62\3\62\3\63\3\63\3\63\3\64\3\64\3\64\3\65\3\65")
        buf.write("\3\66\3\66\3\67\3\67\38\38\39\39\3:\3:\3;\3;\3<\3<\3=")
        buf.write("\3=\3>\6>\u01ac\n>\r>\16>\u01ad\3>\3>\3?\3?\3?\3?\3@\3")
        buf.write("@\3@\3A\3A\3\u00aa\2B\3\2\5\2\7\2\t\2\13\2\r\3\17\4\21")
        buf.write("\5\23\6\25\7\27\b\31\t\33\n\35\13\37\f!\r#\16%\17\'\20")
        buf.write(")\21+\22-\23/\24\61\25\63\26\65\27\67\309\31;\32=\33?")
        buf.write("\34A\35C\36E\37G I!K\"M#O$Q%S&U\'W(Y)[*]+_,a-c.e/g\60")
        buf.write("i\61k\62m\63o\64q\65s\66u\67w8y9{:};\177<\u0081=\3\2\t")
        buf.write("\3\2\62;\5\2C\\aac|\4\2GGgg\3\2\f\f\3\2\63;\3\2$$\5\2")
        buf.write("\13\f\17\17\"\"\2\u01c9\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2")
        buf.write("\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2")
        buf.write("\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2")
        buf.write("\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2")
        buf.write("\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3")
        buf.write("\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q")
        buf.write("\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2")
        buf.write("[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2")
        buf.write("\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2")
        buf.write("\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2")
        buf.write("\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2")
        buf.write("\u0081\3\2\2\2\3\u0083\3\2\2\2\5\u0088\3\2\2\2\7\u008c")
        buf.write("\3\2\2\2\t\u008e\3\2\2\2\13\u0093\3\2\2\2\r\u009b\3\2")
        buf.write("\2\2\17\u00a4\3\2\2\2\21\u00b0\3\2\2\2\23\u00b5\3\2\2")
        buf.write("\2\25\u00ba\3\2\2\2\27\u00c0\3\2\2\2\31\u00c8\3\2\2\2")
        buf.write("\33\u00cb\3\2\2\2\35\u00d0\3\2\2\2\37\u00d6\3\2\2\2!\u00dc")
        buf.write("\3\2\2\2#\u00e0\3\2\2\2%\u00e9\3\2\2\2\'\u00ec\3\2\2\2")
        buf.write(")\u00f4\3\2\2\2+\u00fb\3\2\2\2-\u0102\3\2\2\2/\u0107\3")
        buf.write("\2\2\2\61\u010d\3\2\2\2\63\u0112\3\2\2\2\65\u0116\3\2")
        buf.write("\2\2\67\u011f\3\2\2\29\u0122\3\2\2\2;\u012a\3\2\2\2=\u0140")
        buf.write("\3\2\2\2?\u0142\3\2\2\2A\u0149\3\2\2\2C\u0163\3\2\2\2")
        buf.write("E\u016b\3\2\2\2G\u016d\3\2\2\2I\u016f\3\2\2\2K\u0171\3")
        buf.write("\2\2\2M\u0173\3\2\2\2O\u0175\3\2\2\2Q\u0177\3\2\2\2S\u017a")
        buf.write("\3\2\2\2U\u017d\3\2\2\2W\u0180\3\2\2\2Y\u0182\3\2\2\2")
        buf.write("[\u0185\3\2\2\2]\u0188\3\2\2\2_\u018a\3\2\2\2a\u018d\3")
        buf.write("\2\2\2c\u018f\3\2\2\2e\u0192\3\2\2\2g\u0195\3\2\2\2i\u0198")
        buf.write("\3\2\2\2k\u019a\3\2\2\2m\u019c\3\2\2\2o\u019e\3\2\2\2")
        buf.write("q\u01a0\3\2\2\2s\u01a2\3\2\2\2u\u01a4\3\2\2\2w\u01a6\3")
        buf.write("\2\2\2y\u01a8\3\2\2\2{\u01ab\3\2\2\2}\u01b1\3\2\2\2\177")
        buf.write("\u01b5\3\2\2\2\u0081\u01b8\3\2\2\2\u0083\u0084\t\2\2\2")
        buf.write("\u0084\4\3\2\2\2\u0085\u0087\5\3\2\2\u0086\u0085\3\2\2")
        buf.write("\2\u0087\u008a\3\2\2\2\u0088\u0086\3\2\2\2\u0088\u0089")
        buf.write("\3\2\2\2\u0089\6\3\2\2\2\u008a\u0088\3\2\2\2\u008b\u008d")
        buf.write("\t\3\2\2\u008c\u008b\3\2\2\2\u008d\b\3\2\2\2\u008e\u008f")
        buf.write("\7\60\2\2\u008f\u0090\5\5\3\2\u0090\n\3\2\2\2\u0091\u0092")
        buf.write("\7\60\2\2\u0092\u0094\5\5\3\2\u0093\u0091\3\2\2\2\u0093")
        buf.write("\u0094\3\2\2\2\u0094\u0095\3\2\2\2\u0095\u0097\t\4\2\2")
        buf.write("\u0096\u0098\7/\2\2\u0097\u0096\3\2\2\2\u0097\u0098\3")
        buf.write("\2\2\2\u0098\u0099\3\2\2\2\u0099\u009a\5\5\3\2\u009a\f")
        buf.write("\3\2\2\2\u009b\u009c\7\61\2\2\u009c\u009d\7\61\2\2\u009d")
        buf.write("\u00a1\3\2\2\2\u009e\u00a0\n\5\2\2\u009f\u009e\3\2\2\2")
        buf.write("\u00a0\u00a3\3\2\2\2\u00a1\u009f\3\2\2\2\u00a1\u00a2\3")
        buf.write("\2\2\2\u00a2\16\3\2\2\2\u00a3\u00a1\3\2\2\2\u00a4\u00a5")
        buf.write("\7\61\2\2\u00a5\u00a6\7,\2\2\u00a6\u00aa\3\2\2\2\u00a7")
        buf.write("\u00a9\13\2\2\2\u00a8\u00a7\3\2\2\2\u00a9\u00ac\3\2\2")
        buf.write("\2\u00aa\u00ab\3\2\2\2\u00aa\u00a8\3\2\2\2\u00ab\u00ad")
        buf.write("\3\2\2\2\u00ac\u00aa\3\2\2\2\u00ad\u00ae\7,\2\2\u00ae")
        buf.write("\u00af\7\61\2\2\u00af\20\3\2\2\2\u00b0\u00b1\7o\2\2\u00b1")
        buf.write("\u00b2\7c\2\2\u00b2\u00b3\7k\2\2\u00b3\u00b4\7p\2\2\u00b4")
        buf.write("\22\3\2\2\2\u00b5\u00b6\7c\2\2\u00b6\u00b7\7w\2\2\u00b7")
        buf.write("\u00b8\7v\2\2\u00b8\u00b9\7q\2\2\u00b9\24\3\2\2\2\u00ba")
        buf.write("\u00bb\7d\2\2\u00bb\u00bc\7t\2\2\u00bc\u00bd\7g\2\2\u00bd")
        buf.write("\u00be\7c\2\2\u00be\u00bf\7m\2\2\u00bf\26\3\2\2\2\u00c0")
        buf.write("\u00c1\7d\2\2\u00c1\u00c2\7q\2\2\u00c2\u00c3\7q\2\2\u00c3")
        buf.write("\u00c4\7n\2\2\u00c4\u00c5\7g\2\2\u00c5\u00c6\7c\2\2\u00c6")
        buf.write("\u00c7\7p\2\2\u00c7\30\3\2\2\2\u00c8\u00c9\7f\2\2\u00c9")
        buf.write("\u00ca\7q\2\2\u00ca\32\3\2\2\2\u00cb\u00cc\7g\2\2\u00cc")
        buf.write("\u00cd\7n\2\2\u00cd\u00ce\7u\2\2\u00ce\u00cf\7g\2\2\u00cf")
        buf.write("\34\3\2\2\2\u00d0\u00d1\7h\2\2\u00d1\u00d2\7c\2\2\u00d2")
        buf.write("\u00d3\7n\2\2\u00d3\u00d4\7u\2\2\u00d4\u00d5\7g\2\2\u00d5")
        buf.write("\36\3\2\2\2\u00d6\u00d7\7h\2\2\u00d7\u00d8\7n\2\2\u00d8")
        buf.write("\u00d9\7q\2\2\u00d9\u00da\7c\2\2\u00da\u00db\7v\2\2\u00db")
        buf.write(" \3\2\2\2\u00dc\u00dd\7h\2\2\u00dd\u00de\7q\2\2\u00de")
        buf.write("\u00df\7t\2\2\u00df\"\3\2\2\2\u00e0\u00e1\7h\2\2\u00e1")
        buf.write("\u00e2\7w\2\2\u00e2\u00e3\7p\2\2\u00e3\u00e4\7e\2\2\u00e4")
        buf.write("\u00e5\7v\2\2\u00e5\u00e6\7k\2\2\u00e6\u00e7\7q\2\2\u00e7")
        buf.write("\u00e8\7p\2\2\u00e8$\3\2\2\2\u00e9\u00ea\7k\2\2\u00ea")
        buf.write("\u00eb\7h\2\2\u00eb&\3\2\2\2\u00ec\u00ed\7k\2\2\u00ed")
        buf.write("\u00ee\7p\2\2\u00ee\u00ef\7v\2\2\u00ef\u00f0\7g\2\2\u00f0")
        buf.write("\u00f1\7i\2\2\u00f1\u00f2\7g\2\2\u00f2\u00f3\7t\2\2\u00f3")
        buf.write("(\3\2\2\2\u00f4\u00f5\7t\2\2\u00f5\u00f6\7g\2\2\u00f6")
        buf.write("\u00f7\7v\2\2\u00f7\u00f8\7w\2\2\u00f8\u00f9\7t\2\2\u00f9")
        buf.write("\u00fa\7p\2\2\u00fa*\3\2\2\2\u00fb\u00fc\7u\2\2\u00fc")
        buf.write("\u00fd\7v\2\2\u00fd\u00fe\7t\2\2\u00fe\u00ff\7k\2\2\u00ff")
        buf.write("\u0100\7p\2\2\u0100\u0101\7i\2\2\u0101,\3\2\2\2\u0102")
        buf.write("\u0103\7v\2\2\u0103\u0104\7t\2\2\u0104\u0105\7w\2\2\u0105")
        buf.write("\u0106\7g\2\2\u0106.\3\2\2\2\u0107\u0108\7y\2\2\u0108")
        buf.write("\u0109\7j\2\2\u0109\u010a\7k\2\2\u010a\u010b\7n\2\2\u010b")
        buf.write("\u010c\7g\2\2\u010c\60\3\2\2\2\u010d\u010e\7x\2\2\u010e")
        buf.write("\u010f\7q\2\2\u010f\u0110\7k\2\2\u0110\u0111\7f\2\2\u0111")
        buf.write("\62\3\2\2\2\u0112\u0113\7q\2\2\u0113\u0114\7w\2\2\u0114")
        buf.write("\u0115\7v\2\2\u0115\64\3\2\2\2\u0116\u0117\7e\2\2\u0117")
        buf.write("\u0118\7q\2\2\u0118\u0119\7p\2\2\u0119\u011a\7v\2\2\u011a")
        buf.write("\u011b\7k\2\2\u011b\u011c\7p\2\2\u011c\u011d\7w\2\2\u011d")
        buf.write("\u011e\7g\2\2\u011e\66\3\2\2\2\u011f\u0120\7q\2\2\u0120")
        buf.write("\u0121\7h\2\2\u01218\3\2\2\2\u0122\u0123\7k\2\2\u0123")
        buf.write("\u0124\7p\2\2\u0124\u0125\7j\2\2\u0125\u0126\7g\2\2\u0126")
        buf.write("\u0127\7t\2\2\u0127\u0128\7k\2\2\u0128\u0129\7v\2\2\u0129")
        buf.write(":\3\2\2\2\u012a\u012b\7c\2\2\u012b\u012c\7t\2\2\u012c")
        buf.write("\u012d\7t\2\2\u012d\u012e\7c\2\2\u012e\u012f\7{\2\2\u012f")
        buf.write("<\3\2\2\2\u0130\u0141\7\62\2\2\u0131\u0133\7/\2\2\u0132")
        buf.write("\u0131\3\2\2\2\u0132\u0133\3\2\2\2\u0133\u0134\3\2\2\2")
        buf.write("\u0134\u0135\t\6\2\2\u0135\u013b\5\5\3\2\u0136\u0137\7")
        buf.write("a\2\2\u0137\u0138\t\6\2\2\u0138\u013a\5\5\3\2\u0139\u0136")
        buf.write("\3\2\2\2\u013a\u013d\3\2\2\2\u013b\u0139\3\2\2\2\u013b")
        buf.write("\u013c\3\2\2\2\u013c\u013e\3\2\2\2\u013d\u013b\3\2\2\2")
        buf.write("\u013e\u013f\b\37\2\2\u013f\u0141\3\2\2\2\u0140\u0130")
        buf.write("\3\2\2\2\u0140\u0132\3\2\2\2\u0141>\3\2\2\2\u0142\u0145")
        buf.write("\5=\37\2\u0143\u0146\5\t\5\2\u0144\u0146\5\13\6\2\u0145")
        buf.write("\u0143\3\2\2\2\u0145\u0144\3\2\2\2\u0146\u0147\3\2\2\2")
        buf.write("\u0147\u0148\b \3\2\u0148@\3\2\2\2\u0149\u015d\7$\2\2")
        buf.write("\u014a\u014b\7^\2\2\u014b\u015c\7d\2\2\u014c\u014d\7^")
        buf.write("\2\2\u014d\u015c\7h\2\2\u014e\u014f\7^\2\2\u014f\u015c")
        buf.write("\7t\2\2\u0150\u0151\7^\2\2\u0151\u015c\7p\2\2\u0152\u0153")
        buf.write("\7^\2\2\u0153\u015c\7v\2\2\u0154\u0155\7^\2\2\u0155\u015c")
        buf.write("\7)\2\2\u0156\u0157\7^\2\2\u0157\u015c\7^\2\2\u0158\u0159")
        buf.write("\7^\2\2\u0159\u015c\7$\2\2\u015a\u015c\n\7\2\2\u015b\u014a")
        buf.write("\3\2\2\2\u015b\u014c\3\2\2\2\u015b\u014e\3\2\2\2\u015b")
        buf.write("\u0150\3\2\2\2\u015b\u0152\3\2\2\2\u015b\u0154\3\2\2\2")
        buf.write("\u015b\u0156\3\2\2\2\u015b\u0158\3\2\2\2\u015b\u015a\3")
        buf.write("\2\2\2\u015c\u015f\3\2\2\2\u015d\u015b\3\2\2\2\u015d\u015e")
        buf.write("\3\2\2\2\u015e\u0160\3\2\2\2\u015f\u015d\3\2\2\2\u0160")
        buf.write("\u0161\7$\2\2\u0161\u0162\b!\4\2\u0162B\3\2\2\2\u0163")
        buf.write("\u0168\5\7\4\2\u0164\u0167\5\7\4\2\u0165\u0167\5\3\2\2")
        buf.write("\u0166\u0164\3\2\2\2\u0166\u0165\3\2\2\2\u0167\u016a\3")
        buf.write("\2\2\2\u0168\u0166\3\2\2\2\u0168\u0169\3\2\2\2\u0169D")
        buf.write("\3\2\2\2\u016a\u0168\3\2\2\2\u016b\u016c\7-\2\2\u016c")
        buf.write("F\3\2\2\2\u016d\u016e\7/\2\2\u016eH\3\2\2\2\u016f\u0170")
        buf.write("\7,\2\2\u0170J\3\2\2\2\u0171\u0172\7\61\2\2\u0172L\3\2")
        buf.write("\2\2\u0173\u0174\7\'\2\2\u0174N\3\2\2\2\u0175\u0176\7")
        buf.write("#\2\2\u0176P\3\2\2\2\u0177\u0178\7(\2\2\u0178\u0179\7")
        buf.write("(\2\2\u0179R\3\2\2\2\u017a\u017b\7~\2\2\u017b\u017c\7")
        buf.write("~\2\2\u017cT\3\2\2\2\u017d\u017e\7#\2\2\u017e\u017f\7")
        buf.write("?\2\2\u017fV\3\2\2\2\u0180\u0181\7>\2\2\u0181X\3\2\2\2")
        buf.write("\u0182\u0183\7>\2\2\u0183\u0184\7?\2\2\u0184Z\3\2\2\2")
        buf.write("\u0185\u0186\7@\2\2\u0186\u0187\7?\2\2\u0187\\\3\2\2\2")
        buf.write("\u0188\u0189\7@\2\2\u0189^\3\2\2\2\u018a\u018b\7?\2\2")
        buf.write("\u018b\u018c\7?\2\2\u018c`\3\2\2\2\u018d\u018e\7?\2\2")
        buf.write("\u018eb\3\2\2\2\u018f\u0190\7-\2\2\u0190\u0191\7-\2\2")
        buf.write("\u0191d\3\2\2\2\u0192\u0193\7<\2\2\u0193\u0194\7<\2\2")
        buf.write("\u0194f\3\2\2\2\u0195\u0196\7/\2\2\u0196\u0197\7/\2\2")
        buf.write("\u0197h\3\2\2\2\u0198\u0199\7*\2\2\u0199j\3\2\2\2\u019a")
        buf.write("\u019b\7+\2\2\u019bl\3\2\2\2\u019c\u019d\7]\2\2\u019d")
        buf.write("n\3\2\2\2\u019e\u019f\7_\2\2\u019fp\3\2\2\2\u01a0\u01a1")
        buf.write("\7}\2\2\u01a1r\3\2\2\2\u01a2\u01a3\7\177\2\2\u01a3t\3")
        buf.write("\2\2\2\u01a4\u01a5\7<\2\2\u01a5v\3\2\2\2\u01a6\u01a7\7")
        buf.write(".\2\2\u01a7x\3\2\2\2\u01a8\u01a9\7=\2\2\u01a9z\3\2\2\2")
        buf.write("\u01aa\u01ac\t\b\2\2\u01ab\u01aa\3\2\2\2\u01ac\u01ad\3")
        buf.write("\2\2\2\u01ad\u01ab\3\2\2\2\u01ad\u01ae\3\2\2\2\u01ae\u01af")
        buf.write("\3\2\2\2\u01af\u01b0\b>\5\2\u01b0|\3\2\2\2\u01b1\u01b2")
        buf.write("\7$\2\2\u01b2\u01b3\13\2\2\2\u01b3\u01b4\b?\6\2\u01b4")
        buf.write("~\3\2\2\2\u01b5\u01b6\13\2\2\2\u01b6\u01b7\b@\7\2\u01b7")
        buf.write("\u0080\3\2\2\2\u01b8\u01b9\13\2\2\2\u01b9\u0082\3\2\2")
        buf.write("\2\22\2\u0088\u008c\u0093\u0097\u00a1\u00aa\u0132\u013b")
        buf.write("\u0140\u0145\u015b\u015d\u0166\u0168\u01ad\b\3\37\2\3")
        buf.write(" \3\3!\4\b\2\2\3?\5\3@\6")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    COMMENT_LINE = 1
    COMMENT_MULTYLINE = 2
    MAIN = 3
    AUTO = 4
    BREAK = 5
    BOOLEAN = 6
    DO = 7
    ELSE = 8
    FALSE = 9
    FLOAT = 10
    FOR = 11
    FUNCTION = 12
    IF = 13
    INTEGER = 14
    RETURN = 15
    STRING = 16
    TRUE = 17
    WHILE = 18
    VOID = 19
    OUT = 20
    CONTINUE = 21
    OF = 22
    INHERIT = 23
    ARRAY = 24
    INTLIT = 25
    FLOATLIT = 26
    STRINGLIT = 27
    ID = 28
    PLUS = 29
    MINUS = 30
    MUL = 31
    DIV = 32
    MOD = 33
    NOT = 34
    AND = 35
    OR = 36
    NOT_EQUAL = 37
    LESS = 38
    LESS_EQUAL = 39
    GREATER_EQUAL = 40
    GREATER = 41
    EQUAL = 42
    ASSIGN = 43
    INCREMENT = 44
    CONCAT = 45
    DECREMENT = 46
    LB = 47
    RB = 48
    LSB = 49
    RSB = 50
    LCB = 51
    RCB = 52
    COLON = 53
    COMMA = 54
    SEMI = 55
    WS = 56
    UNCLOSE_STRING = 57
    ERROR_CHAR = 58
    ILLEGAL_ESCAPE = 59

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'main'", "'auto'", "'break'", "'boolean'", "'do'", "'else'", 
            "'false'", "'float'", "'for'", "'function'", "'if'", "'integer'", 
            "'return'", "'string'", "'true'", "'while'", "'void'", "'out'", 
            "'continue'", "'of'", "'inherit'", "'array'", "'+'", "'-'", 
            "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", "'!='", "'<'", "'<='", 
            "'>='", "'>'", "'=='", "'='", "'++'", "'::'", "'--'", "'('", 
            "')'", "'['", "']'", "'{'", "'}'", "':'", "','", "';'" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT_LINE", "COMMENT_MULTYLINE", "MAIN", "AUTO", "BREAK", 
            "BOOLEAN", "DO", "ELSE", "FALSE", "FLOAT", "FOR", "FUNCTION", 
            "IF", "INTEGER", "RETURN", "STRING", "TRUE", "WHILE", "VOID", 
            "OUT", "CONTINUE", "OF", "INHERIT", "ARRAY", "INTLIT", "FLOATLIT", 
            "STRINGLIT", "ID", "PLUS", "MINUS", "MUL", "DIV", "MOD", "NOT", 
            "AND", "OR", "NOT_EQUAL", "LESS", "LESS_EQUAL", "GREATER_EQUAL", 
            "GREATER", "EQUAL", "ASSIGN", "INCREMENT", "CONCAT", "DECREMENT", 
            "LB", "RB", "LSB", "RSB", "LCB", "RCB", "COLON", "COMMA", "SEMI", 
            "WS", "UNCLOSE_STRING", "ERROR_CHAR", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "Digit", "Digits", "Letter", "DECPART", "EXPART", "COMMENT_LINE", 
                  "COMMENT_MULTYLINE", "MAIN", "AUTO", "BREAK", "BOOLEAN", 
                  "DO", "ELSE", "FALSE", "FLOAT", "FOR", "FUNCTION", "IF", 
                  "INTEGER", "RETURN", "STRING", "TRUE", "WHILE", "VOID", 
                  "OUT", "CONTINUE", "OF", "INHERIT", "ARRAY", "INTLIT", 
                  "FLOATLIT", "STRINGLIT", "ID", "PLUS", "MINUS", "MUL", 
                  "DIV", "MOD", "NOT", "AND", "OR", "NOT_EQUAL", "LESS", 
                  "LESS_EQUAL", "GREATER_EQUAL", "GREATER", "EQUAL", "ASSIGN", 
                  "INCREMENT", "CONCAT", "DECREMENT", "LB", "RB", "LSB", 
                  "RSB", "LCB", "RCB", "COLON", "COMMA", "SEMI", "WS", "UNCLOSE_STRING", 
                  "ERROR_CHAR", "ILLEGAL_ESCAPE" ]

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
            actions[29] = self.INTLIT_action 
            actions[30] = self.FLOATLIT_action 
            actions[31] = self.STRINGLIT_action 
            actions[61] = self.UNCLOSE_STRING_action 
            actions[62] = self.ERROR_CHAR_action 
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
            self.text = self.text[1:-1]
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise UncloseString(self.text)
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            raise ErrorToken(self.text)
     


