import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):
    
    ### test identifiers
    def test1(self):
        input = '0abc 1_cnca'
        expect = '0,abc,1,_cnca,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 101))
    def test2(self):
        input = 'Auto False FunCtion Do mcajc _ ___ _9312 '
        expect = 'Auto,False,FunCtion,Do,mcajc,_,___,_9312,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 102))
    def test3(self):
        input = 'cnac kcc cncoja _ca _cc ___ '
        expect = 'cnac,kcc,cncoja,_ca,_cc,___,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 103))
    def test4(self):
        input = 'Ingeger Printline readInt '
        expect = 'Ingeger,Printline,readInt,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 104))
    def test5(self):
        input = """ .adaxax"""
        expect = """.,adaxax,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 105))
    def test6(self):
        input = '_0022231 .0.1.1___3_321'
        expect = '_0022231,.,0.1,.,1,___3_321,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 106))
    def test7(self):
        input = 'Bool False Auto Integer EOF tmt'
        expect = 'Bool,False,Auto,Integer,EOF,tmt,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 107))
    def test8(self):
        input = '_auto _flaot Float floaT'
        expect = '_auto,_flaot,Float,floaT,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 108))
    def test9(self):
        input = 'printInt()'
        expect = 'printInt,(,),<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 109))
    def test10(self):
        input = 'abca()'
        expect = 'abca,(,),<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 110))
    
    ### test keywork
    def test11(self):
        input = """ auto break boolean do else false float for function if integer return string true while void out continue of inherit array"""
        expect = """auto,break,boolean,do,else,false,float,for,function,if,integer,return,string,true,while,void,out,continue,of,inherit,array,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 111))

    ### test number literal (integer, float)
    def test12(self):
        input = """ 1_8590723273.585864932393"""
        expect = """18590723273.585864932393,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 112))
    def test13(self):
        input = """ 3.10213e-13 """
        expect = """3.10213e-13,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 113))       
    def test14(self):
        input = """1_234_567 1_72 172 -172 1_2_3_4"""
        expect = '1234567,172,172,-,172,1234,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 114))    
    def test15(self):
        input = """ 1537_5_ """
        expect = """15375,_,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 115))       
    def test16(self):
        input = """ 1.7575e+8 """
        expect = """1.7575e+8,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 116))
    def test17(self):
        input = """ 3.1028e-8 """
        expect = """3.1028e-8,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 117))
    def test18(self):
        input = """ 1537_5_ """
        expect = """15375,_,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 118))
    def test19(self):
        input = """ 6.3656e+7 """
        expect = """6.3656e+7,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 119))
    def test20(self):
        input = """1.234 1.2e3 7E-10 1_234.567 -1_2_3_4e-7"""
        expect = '1.234,1.2e3,7E-10,1234.567,-,1234e-7,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 120)) 
        
    ### test string literal
    def test21(self):
        """Test 3 """
        input = """ "My string: \\"hello\\"" """
        expect = 'My string: \\"hello\\",<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 121))

    def test22(self):
        """Test 3 """
        input = """ "He asked me: \\"Where is John?\\" " """
        expect = 'He asked me: \\"Where is John?\\" ,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 122))
    
    def test23(self):
        input = """ "a`=JhyI#icm"CvAkoEj"3L[e%L48kP[" """
        expect = """a`=JhyI#icm,CvAkoEj,3L[e%L48kP[,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 123))
    
    def test24(self):
        input = """ "abchcjnj\\t" """
        expect = """abchcjnj\\t,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 124))
        
    def test25(self):
        input = """ "a`'%=JhyI#icm" """
        expect = """a`'%=JhyI#icm,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 125))
    
    def test26(self):
        input = """ "2]x#.Fvk\\"aQl.(P7$~OGr\\" 3g_" """
        expect = """2]x#.Fvk\\"aQl.(P7$~OGr\\" 3g_,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 126))

    def test27(self):
        input = """ "\\t5J|if@6"!mft[ Tr9CN/1"2~ioKnBWZ\\'" """
        expect = """\\t5J|if@6,!,mft,[,Tr9CN,/,1,2~ioKnBWZ\\',<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 127))
        
    def test28(self):
        input = """ "Y-*~M Q7}!1'nn[p7z|x-S%x{/V\\nH[E" """
        expect = """Y-*~M Q7}!1'nn[p7z|x-S%x{/V\\nH[E,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 128))
    
    def test29(self):
        input = """ ":8'0yLFM7`ss"T]"C=D8M8Pn0" """
        expect = """:8'0yLFM7`ss,T,],C=D8M8Pn0,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 129))
    
    def test30(self):
        input = """ "aaf\\"T]\\"C=f\\'a\\'\\n" """
        expect = """aaf\\"T]\\"C=f\\'a\\'\\n,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 130))
    
    ### test unclose String Error: 
    def test31(self):
        input = """ "abchcjnj\\ """
        expect = """Unclosed String: abchcjnj\\ """
        self.assertTrue(TestLexer.test(input, expect, 131))
    def test32(self):
        input = """ "My string: \\"hello\\"" """
        expect = 'My string: \\"hello\\",<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 132))

    def test33(self):
        input = """ "He asked me: \\"Where is John?\\\""""
        expect = 'Unclosed String: He asked me: \\"Where is John?\\"'
        self.assertTrue(TestLexer.test(input, expect, 133))
    
    def test34(self):
        input = """ "acm"CvAk"oEj"3LP"cdcas """
        expect = """acm,CvAk,oEj,3,LP,Unclosed String: cdcas """
        self.assertTrue(TestLexer.test(input, expect, 134))
    def test35(self):
        input = """ "abcdfe\\t\\r\\t\\r\\f\\'\\" """
        expect = """Unclosed String: abcdfe\\t\\r\\t\\r\\f\\'\\" """
        self.assertTrue(TestLexer.test(input, expect, 135))
    def test36(self):
        input = """ "abcdfe\\t\\r\\t\\r\\f\\'\\y """
        expect = """Unclosed String: abcdfe\\t\\r\\t\\r\\f\\'\\y """
        self.assertTrue(TestLexer.test(input, expect, 136))
        
    ### test escape illigal
    def test37(self):
        input = """ "abchcjnj\\y" """
        expect = """Illegal Escape In String: abchcjnj\\y"""
        self.assertTrue(TestLexer.test(input, expect, 137))
    def test38(self):
        input = """ "abchc\\t \\f \\r \\b \\n jnj\\y" """
        expect = """Illegal Escape In String: abchc\\t \\f \\r \\b \\n jnj\\y"""
        self.assertTrue(TestLexer.test(input, expect, 138))
    def test39(self):
        input = """ "string\\n\\\\p\\p" """
        expect = 'Illegal Escape In String: string\\n\\\\p\\p'
        self.assertTrue(TestLexer.test(input, expect, 139))
    
    def test40(self):
        input = """ "abchc\\t\\b\\r\\ajnj" """
        expect = """Illegal Escape In String: abchc\\t\\b\\r\\a"""
        self.assertTrue(TestLexer.test(input, expect, 140))
    def test41(self):
        input = """ "\\\\\\\\\\.'"" """
        expect = """Illegal Escape In String: \\\\\\\\\\."""
        self.assertTrue(TestLexer.test(input, expect, 141))
    def test42(self):
        input = """ "\\\\\\." """
        expect = 'Illegal Escape In String: \\\\\\.'
        self.assertTrue(TestLexer.test(input, expect, 142))
    
    ### test operator
    
    def test43(self):
        """Test operator """
        input = """+ - * / % ! && || == != < <= > >= :: """
        expect = '+,-,*,/,%,!,&&,||,==,!=,<,<=,>,>=,::,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 143))

    def test44(self):
        input = """ 10_58_9-17_55 && 1_5-1_264>11-167-193_7_8&&-17-105-62"""
        expect = """10589,-,1755,&&,15,-,1264,>,11,-,167,-,19378,&&,-,17,-,105,-,62,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 144))
        
    def test45(self):
        input = """+++---+===++==//"""
        expect = """+,+,+,-,-,-,+,==,=,+,+,==,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 145))    

    def test46(self):
        input = """***==*=*=//*/%%"""
        expect = """*,*,*,==,*,=,*,=,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 146))
        

    def test47(self):
        input = """6%23255_11*42423"""
        expect = """6,%,2325511,*,42423,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 147))
        

    def test48(self):
        input = """ 3_1_178__2||32->=-171_32__117_&&199_545_1_16_60 """
        expect = """31178,__2,||,32,-,>=,-,17132,__117_,&&,19954511660,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 148))
        

    def test49(self):
        input = """ fqwfwqf%kdwjjf8*0/4324/42342amkda """
        expect = """fqwfwqf,%,kdwjjf8,*,0,/,4324,/,42342,amkda,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 149))
        

    def test50(self):
        input = """ 8||Hw38oQ25*{cO"<"[g37.4poq%XCa*7::"}U!?"3u "C$P" """
        expect = """8,||,Hw38oQ25,*,{,cO,<,[,g37,.,4,poq,%,XCa,*,7,::,}U!?,3,u,C$P,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 150))
        

    def test51(self):
        input = """ aaa-68_9_||1250__+_+3175bbb*6904<1612_7718-1>9_6989&&104_58 """
        expect = """aaa,-,689,_,||,1250,__,+,_,+,3175,bbb,*,6904,<,16127718,-,1,>,96989,&&,10458,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 151))
        

    def test52(self):
        input = """ 1950_9112_266_1__5386&&-181690714150_3-195_67_>164092819844331144_44||16___3_-1960805-17883_1 """
        expect = """195091122661,__5386,&&,-,1816907141503,-,19567,_,>,16409281984433114444,||,16,___3_,-,1960805,-,178831,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 152))
        

    def test53(self):
        input = """ -tttva-1_8173_||ss-149_5851495642!=___&&1_5109_1__3416-1_00_18 """
        expect = """-,tttva,-,18173,_,||,ss,-,1495851495642,!=,___,&&,151091,__3416,-,10018,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 153))
        

    ### test commment
    def test54(self):
        input = """ // This iss comment line """
        expect = """<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 154))
        
    def test55(self):
        input = """// main: function integer {
               // print("hello wworld")
            // }"""
        expect = """<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 155))
    def test56(self):
        input = """
        /* this is comment mutiple line
        *line 1
        *line 2
        */"""
        expect ="""<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 156))
    def test57(self):
        input = """
        /* this is comment mutiple line
        *line 1
        *line 2
        */
        */"""
        expect ="""*,/,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 157))
    
    def test58(self):
        input = """/* main: function integer {
               print("hello wworld")
            */ }"""
        expect = """},<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 158))
    def test59(self):
        input = """ a,b,c: integer = 3,4,5 // full format declaration """
        expect = """a,,,b,,,c,:,integer,=,3,,,4,,,5,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 159))   
        
    ### test boolean literal   
    def test60(self):
        input = """ a = true || false """
        expect = """a,=,true,||,false,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 160))     
    def test61(self):
        input = """ true false """
        expect = """true,false,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 161))    

    ### test array literal
    def test62(self):
        input = """ a: array [4] of integer = {1, 5, 7, 12} """
        expect = 'a,:,array,[,4,],of,integer,=,{,1,,,5,,,7,,,12,},<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 162))
    def test63(self):
        input = """ {"Ka\\"ng\\"xi", "Yong\\n\\tzheng", "Qianlong"} """
        expect = '{,Ka\\"ng\\"xi,,,Yong\\n\\tzheng,,,Qianlong,},<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 163))
    def test64(self):
        input = """ array[0,0] = {1,2,3,4}[0]"""
        expect = 'array,[,0,,,0,],=,{,1,,,2,,,3,,,4,},[,0,],<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 164))
    def test65(self):
        input = """ a: boolean = {1 == 1, "00" == 00, false || true} """
        expect = 'a,:,boolean,=,{,1,==,1,,,00,==,0,0,,,false,||,true,},<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 165))
    def test66(self):
        input = """ {1_2,fqwc,ccqc,131,4e3}"""
        expect = '{,12,,,fqwc,,,ccqc,,,131,,,4e3,},<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 166)) 
     
    ### Error tokens
    def test67(self):
        input = """/* main: function integer {
            print("hello wworld")
        &}"""
        expect = """/,*,main,:,function,integer,{,print,(,hello wworld,),Error Token &"""
        self.assertTrue(TestLexer.test(input, expect, 167))
    def test68(self):
        input = """ a&b&c: integer = 3,4,5 // full format declaration """
        expect = """a,Error Token &"""
        self.assertTrue(TestLexer.test(input, expect, 168))   
    
    def test69(self):
        input = """ a = true | false """
        expect = """a,=,true,Error Token |"""
        self.assertTrue(TestLexer.test(input, expect, 169))     
    def test70(self):
        input = """ true | false """
        expect = """true,Error Token |"""
        self.assertTrue(TestLexer.test(input, expect, 170))    

    def test71(self):
        input = """ a: array \\ss\\ of integer = {1, 5, 7, 12} """
        expect = 'a,:,array,Error Token \\'
        self.assertTrue(TestLexer.test(input, expect, 171))
    def test72(self):
        input = """ ~{"Ka\\"ng\\"xi", "Yong\\n\\tzheng", "Qianlong"} """
        expect = 'Error Token ~'
        self.assertTrue(TestLexer.test(input, expect, 172))
    def test73(self):
        input = """ ":8'0yLFM7`ss"\\t"C=D8M8Pn0" """
        expect = ':8\'0yLFM7`ss,Error Token \\'
        self.assertTrue(TestLexer.test(input, expect, 173))
    def test74(self):
        input = """ "mckc\\t\"\\n + "acac" """
        expect = 'mckc\\t,Error Token \\'
        self.assertTrue(TestLexer.test(input, expect, 174))
    def test75(self):
        input = """ \\t """
        expect = 'Error Token \\'
        self.assertTrue(TestLexer.test(input, expect, 175))         
 
    ### ramdom testcase
    def test76(self):
        input = """ "zgZZF\\<P8zgh"5-F\\"" """
        expect = """Illegal Escape In String: zgZZF\\<"""
        self.assertTrue(TestLexer.test(input, expect, 176))
        
    def test77(self):
        input = """ "R\\53"@FdO"Tb\\tkKc#u=!y" """
        expect = """Illegal Escape In String: R\\5"""
        self.assertTrue(TestLexer.test(input, expect, 177))       

    def test78(self):
        input = """ 11671 """
        expect = """11671,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 178))

    def test79(self):
        input = """ "\\tdDTW\\nYUbA&G"bi8'ze]7qe+"uuPi-" """
        expect = """\\tdDTW\\nYUbA&G,bi8,Error Token '"""
        self.assertTrue(TestLexer.test(input, expect, 179))      

    def test80(self):
        input = """ ]"v,YC")QB\\cu TG8UDd(#,)2^ @C~s",1_27712_7_15_03:void;
    """
        expect = """],v,YC,),QB,Error Token \\"""
        self.assertTrue(TestLexer.test(input, expect, 180))
        
    def test81(self):
        input = """ continue;
    """
        expect = """continue,;,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 181))      

    def test82(self):
        input = """ for(\\"-:<;m"{^i1PV<v PDe8v="$SBTwHl$~LfkmQw};@=qNb &E(ducQ)\\"::"@~R T(O.[6"tbG>m\\n\\"9t4j=FFI",-18657-131421_7__&&-133_0-111_618_7_||-177921185_-1_2__--1930_141_31_325<-1353_16055117_7&&14187-1437_-11419&&-1_4_7-1__12-17_64-1437_-18_7_16_36,(197931___0-1_2__))return-161_9;
    """
        expect = """for,(,Error Token \\"""
        self.assertTrue(TestLexer.test(input, expect, 182))      

    def test83(self):
        input = """ (x0i&F#;ugN&5\\z"("WdjwE-\\r::"Dr[b\\"["[&L~[sACMw4BfTf'Ne") """
        expect = """(,x0i,Error Token &"""
        self.assertTrue(TestLexer.test(input, expect, 183))     

    def test84(self):
        input = """ for(Xgv+WU$IQse@es*h"-kp=6+uEV/h]C"j=#D"cSFQANl?<"!aq(B1sY+E?ph&mCI!W::"\\"aRU$<A&"uzlPL5IE*7QYS!PV",-1410717__61_462||-1533_1100213247||1372_183_710633--11943-14857101_5==132491_53814223||-19_7_186711922_||14379-1286616996+1846218795-17319,2mT\\|Jb86,Vi"fge>Y"iH",AR3,eZC{?::"+U4FH"F"SGP04:.cKA>lseGirJm)Zs}D2[r/W1c~")1379_-114_310480:1_47_=-189__;
    """
        expect = """for,(,Xgv,+,WU,Error Token $"""
        self.assertTrue(TestLexer.test(input, expect, 184))
        
    def test85(self):
        input = """ -16784 """
        expect = """-,16784,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 185))    

    def test86(self):
        input = """ \\"+E5k%q,",101_1-1_02_160_6:float=19153-15_49-12591;"""
        expect = """Error Token \\"""
        self.assertTrue(TestLexer.test(input, expect, 186))
        
    def test87(self):
        input = """ "\\"b>;"<*Kk`XO2" """
        expect = """\\"b>;,<,*,Kk,Error Token `"""
        self.assertTrue(TestLexer.test(input, expect, 187))
        
    def test88(self):
        input = """ 12197 """
        expect = """12197,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 188))
        
    def test89(self):
        input = """ 13711-1299_-1___0&&171241658010165||1_89_1_7_1-15_43+-13_7_-1_5_714_1_&&1702_-1_627-1_650--1433_17154-13433--1_7__169_416122%-1007310712>=183131864113546&&137581111_15891||19598-1588212048+1_25314140-18518&&1__51-13130-1_417+-105_91671_-16677-1_439-16005-19475*-1_603-17703 """
        expect = """13711,-,1299,_,-,1,___0,&&,171241658010165,||,189171,-,1543,+,-,137,_,-,157141,_,&&,1702,_,-,1627,-,1650,-,-,143317154,-,13433,-,-,17,__169_416122,%,-,1007310712,>=,183131864113546,&&,13758111115891,||,19598,-,1588212048,+,125314140,-,18518,&&,1,__51,-,13130,-,1417,+,-,10591671,_,-,16677,-,1439,-,16005,-,19475,*,-,1603,-,17703,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 189))
        
    def test90(self):
        input = """ n"j(!{b<A_9"n>X]t9S,,1200817845-14464:bool=1265915__016_23;"""
        expect = """n,j(!{b<A_9,n,>,X,],t9S,,,,,1200817845,-,14464,:,bool,=,1265915,__016_23,;,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 190))

    def test91(self):
        input = """ =Wl\\0hf}e$lgCa"/;t;`MVqi`R*BS#"(]H&Nih)",<"oiutzd\\tXE[P4x+RMt`"*vI>\\',\\'\\tSiBn\\fn_dP"a)OF"bU_V;{#daa,-1_35_1053_13709:float=-1919_-18933-18708,17745,-135_7-16_89-16529;"""
        expect = """=,Wl,Error Token \\"""
        self.assertTrue(TestLexer.test(input, expect, 191))    

    def test92(self):
        input = """ (#S%BRDgN\\"\\fPtS0L/("V(Sm)*|*'M.zvY0%::"ip;_\\r_2sd5o6l:7 qT"dw r"AP"p1\\n9XmS") """
        expect = """(,Error Token #"""
        self.assertTrue(TestLexer.test(input, expect, 192))     

    def test93(self):
        input = """ /'U6\\"|]"3=y7xp/Hy)_ 4:"Q@@`G0~ +W}'!Tj"?+8::"k-~?|&wI^8"aVpZs+$"W(5/,B)=`"; """
        expect = """/,Error Token '"""
        self.assertTrue(TestLexer.test(input, expect, 193))       

    def test94(self):
        input = """ do{15506-117091_559-15635}while(1448918_941468_&&1_372-1889714_4_&&15_2510_3_125_6-156_112582-1164_>-1_40_-1448418618||1_8491_78013__6||1_331109__12600+15346-18466-1_55_); """
        expect = """do,{,15506,-,117091559,-,15635,},while,(,1448918941468,_,&&,1372,-,18897144,_,&&,15251031256,-,156112582,-,1164,_,>,-,140,_,-,1448418618,||,1849178013,__6,||,1331109,__12600,+,15346,-,18466,-,155,_,),;,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 194))
        
    def test95(self):
        input = """ 122731962512334&&1__3_14043-1_7__||-1890_-195_715768+1335_-1844214_5_||19_501_22910737+-1_2__-15_47-165_9+12247-1_38_1_716%-1932815085>=15020-16___128_1||-1432_1_384-13543&&1_8191629711090--11_921_6071_028||19244-19_53192_0+-15__3124751180_--13973-15_3911587/17269-117__ """
        expect = """122731962512334,&&,1,__3_14043,-,17,__,||,-,1890,_,-,195715768,+,1335,_,-,18442145,_,||,1950122910737,+,-,12,__,-,1547,-,1659,+,12247,-,1381716,%,-,1932815085,>=,15020,-,16,___128_1,||,-,14321384,-,13543,&&,18191629711090,-,-,119216071028,||,19244,-,19531920,+,-,15,__3124751180_,-,-,13973,-,153911587,/,17269,-,117,__,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 195))
        

    def test96(self):
        input = """ (-1_73_165_9-18403||1161_-100_0125_1!=120281_723-1862_||-12_6917_12-18114) """
        expect = """(,-,1731659,-,18403,||,1161,_,-,10001251,!=,120281723,-,1862,_,||,-,12691712,-,18114,),<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 196))
    
    def test97(self):
        input = """ if(;PQ\\!"93WYA9jCZ9@tXh'!TR\\"gZ1wOoTI::"JikG]YV`1"wolN/+'<\\WAWyRZ]0e!%_"^T@k")break;"""
        expect = """if,(,;,PQ,Error Token \\"""
        self.assertTrue(TestLexer.test(input, expect, 197))    

    def test98(self):
        input = """ do{-19252-1098_-129651373_}while(132_7-11031-152_2||-161_911_3612_7_&&17_7_-10_20189__+-14046-197101087_==-1_3331475_-12368&&12_0110684-1267_&&-13456-102__1446_-16__1-182831__9_); """
        expect = """do,{,-,19252,-,1098,_,-,129651373,_,},while,(,1327,-,11031,-,1522,||,-,16191136127,_,&&,177,_,-,1020189,__,+,-,14046,-,197101087,_,==,-,13331475,_,-,12368,&&,120110684,-,1267,_,&&,-,13456,-,102,__1446_,-,16,__1,-,182831,__9_,),;,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 198))
        

    def test99(self):
        input = """ =n-'i{3S"m-:Y;5?8<tb^"i91*?7GDZ^,12_91-192_716302:integer;"""
        expect = """=,n,-,Error Token '"""
        self.assertTrue(TestLexer.test(input, expect, 199))

    def test100(self):
        input = """ ((17454-13_42-1_717)) """
        expect = """(,(,17454,-,1342,-,1717,),),<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 200))
        
