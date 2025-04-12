# $ANTLR 3.1.2 XKBGrammar.g 2020-05-10 06:02:53

import sys
from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.tree import *



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
ELEM_KEYSYMGROUP=22
T__50=50
TOKEN_NAME=6
VALUE=20
KEYELEMENTS=25
OVERLAY=27
TOKEN_KEY_TYPE=5
KEYCODEX=19
KEYCODE=18
T__51=51
MAPMATERIAL=17
NAME=30
LINE_COMMENT=33
TOKEN_SYMBOL=10
TOKEN_INCLUDE=4
ELEM_VIRTUALMODS=24
TOKEN_KEY=7
LAYOUT=12
STATE=21
DQSTRING=29
COMMENT=32
MAPTYPE=14
T__37=37
T__38=38
T__39=39
T__34=34
TOKEN_TYPE=8
T__35=35
T__36=36
SYMBOLS=13
WS=31
EOF=-1
TOKEN_VIRTUAL_MODIFIERS=11
MAPOPTIONS=16
MAPOPTS=28
ELEM_KEYSYMS=23
TOKEN_MODIFIER_MAP=9
MAPNAME=15
OVERRIDE=26
T__48=48
T__49=49
T__44=44
T__45=45
T__46=46
T__47=47
T__40=40
T__41=41
T__42=42
T__43=43

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "TOKEN_INCLUDE", "TOKEN_KEY_TYPE", "TOKEN_NAME", "TOKEN_KEY", "TOKEN_TYPE", 
    "TOKEN_MODIFIER_MAP", "TOKEN_SYMBOL", "TOKEN_VIRTUAL_MODIFIERS", "LAYOUT", 
    "SYMBOLS", "MAPTYPE", "MAPNAME", "MAPOPTIONS", "MAPMATERIAL", "KEYCODE", 
    "KEYCODEX", "VALUE", "STATE", "ELEM_KEYSYMGROUP", "ELEM_KEYSYMS", "ELEM_VIRTUALMODS", 
    "KEYELEMENTS", "OVERRIDE", "OVERLAY", "MAPOPTS", "DQSTRING", "NAME", 
    "WS", "COMMENT", "LINE_COMMENT", "'{'", "'}'", "';'", "'include'", "'name'", 
    "'['", "']'", "'='", "'key.type'", "'key'", "'<'", "'>'", "','", "'modifier_map'", 
    "'virtual_modifiers'", "'type'", "'symbols'", "'virtualMods'"
]




class XKBGrammarParser(Parser):
    grammarFileName = "XKBGrammar.g"
    antlr_version = version_str_to_tuple("3.1.2")
    antlr_version_str = "3.1.2"
    tokenNames = tokenNames

    def __init__(self, input, state=None):
        if state is None:
            state = RecognizerSharedState()

        Parser.__init__(self, input, state)







                
        self._adaptor = CommonTreeAdaptor()


        
    def getTreeAdaptor(self):
        return self._adaptor

    def setTreeAdaptor(self, adaptor):
        self._adaptor = adaptor

    adaptor = property(getTreeAdaptor, setTreeAdaptor)


    class layout_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "layout"
    # XKBGrammar.g:60:1: layout : ( symbols )+ EOF -> ^( LAYOUT ( symbols )+ ) ;
    def layout(self, ):

        retval = self.layout_return()
        retval.start = self.input.LT(1)

        root_0 = None

        EOF2 = None
        symbols1 = None


        EOF2_tree = None
        stream_EOF = RewriteRuleTokenStream(self._adaptor, "token EOF")
        stream_symbols = RewriteRuleSubtreeStream(self._adaptor, "rule symbols")
        try:
            try:
                # XKBGrammar.g:61:3: ( ( symbols )+ EOF -> ^( LAYOUT ( symbols )+ ) )
                # XKBGrammar.g:61:5: ( symbols )+ EOF
                pass 
                # XKBGrammar.g:61:5: ( symbols )+
                cnt1 = 0
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 == MAPOPTS) :
                        alt1 = 1


                    if alt1 == 1:
                        # XKBGrammar.g:61:5: symbols
                        pass 
                        self._state.following.append(self.FOLLOW_symbols_in_layout191)
                        symbols1 = self.symbols()

                        self._state.following.pop()
                        stream_symbols.add(symbols1.tree)


                    else:
                        if cnt1 >= 1:
                            break #loop1

                        eee = EarlyExitException(1, self.input)
                        raise eee

                    cnt1 += 1


                EOF2=self.match(self.input, EOF, self.FOLLOW_EOF_in_layout194) 
                stream_EOF.add(EOF2)

                # AST Rewrite
                # elements: symbols
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 62:3: -> ^( LAYOUT ( symbols )+ )
                # XKBGrammar.g:62:6: ^( LAYOUT ( symbols )+ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(LAYOUT, "LAYOUT"), root_1)

                # XKBGrammar.g:62:15: ( symbols )+
                if not (stream_symbols.hasNext()):
                    raise RewriteEarlyExitException()

                while stream_symbols.hasNext():
                    self._adaptor.addChild(root_1, stream_symbols.nextTree())


                stream_symbols.reset()

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "layout"

    class symbols_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "symbols"
    # XKBGrammar.g:65:1: symbols : mapType '{' ( mapMaterial )+ '}' ';' -> ^( SYMBOLS mapType ^( MAPMATERIAL ( mapMaterial )+ ) ) ;
    def symbols(self, ):

        retval = self.symbols_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal4 = None
        char_literal6 = None
        char_literal7 = None
        mapType3 = None

        mapMaterial5 = None


        char_literal4_tree = None
        char_literal6_tree = None
        char_literal7_tree = None
        stream_34 = RewriteRuleTokenStream(self._adaptor, "token 34")
        stream_35 = RewriteRuleTokenStream(self._adaptor, "token 35")
        stream_36 = RewriteRuleTokenStream(self._adaptor, "token 36")
        stream_mapMaterial = RewriteRuleSubtreeStream(self._adaptor, "rule mapMaterial")
        stream_mapType = RewriteRuleSubtreeStream(self._adaptor, "rule mapType")
        try:
            try:
                # XKBGrammar.g:66:3: ( mapType '{' ( mapMaterial )+ '}' ';' -> ^( SYMBOLS mapType ^( MAPMATERIAL ( mapMaterial )+ ) ) )
                # XKBGrammar.g:66:5: mapType '{' ( mapMaterial )+ '}' ';'
                pass 
                self._state.following.append(self.FOLLOW_mapType_in_symbols221)
                mapType3 = self.mapType()

                self._state.following.pop()
                stream_mapType.add(mapType3.tree)
                char_literal4=self.match(self.input, 34, self.FOLLOW_34_in_symbols223) 
                stream_34.add(char_literal4)
                # XKBGrammar.g:66:17: ( mapMaterial )+
                cnt2 = 0
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if (LA2_0 == OVERRIDE or (37 <= LA2_0 <= 38) or (42 <= LA2_0 <= 43) or (47 <= LA2_0 <= 48)) :
                        alt2 = 1


                    if alt2 == 1:
                        # XKBGrammar.g:66:17: mapMaterial
                        pass 
                        self._state.following.append(self.FOLLOW_mapMaterial_in_symbols225)
                        mapMaterial5 = self.mapMaterial()

                        self._state.following.pop()
                        stream_mapMaterial.add(mapMaterial5.tree)


                    else:
                        if cnt2 >= 1:
                            break #loop2

                        eee = EarlyExitException(2, self.input)
                        raise eee

                    cnt2 += 1


                char_literal6=self.match(self.input, 35, self.FOLLOW_35_in_symbols228) 
                stream_35.add(char_literal6)
                char_literal7=self.match(self.input, 36, self.FOLLOW_36_in_symbols230) 
                stream_36.add(char_literal7)

                # AST Rewrite
                # elements: mapMaterial, mapType
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 67:3: -> ^( SYMBOLS mapType ^( MAPMATERIAL ( mapMaterial )+ ) )
                # XKBGrammar.g:67:6: ^( SYMBOLS mapType ^( MAPMATERIAL ( mapMaterial )+ ) )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(SYMBOLS, "SYMBOLS"), root_1)

                self._adaptor.addChild(root_1, stream_mapType.nextTree())
                # XKBGrammar.g:67:24: ^( MAPMATERIAL ( mapMaterial )+ )
                root_2 = self._adaptor.nil()
                root_2 = self._adaptor.becomeRoot(self._adaptor.createFromType(MAPMATERIAL, "MAPMATERIAL"), root_2)

                # XKBGrammar.g:67:38: ( mapMaterial )+
                if not (stream_mapMaterial.hasNext()):
                    raise RewriteEarlyExitException()

                while stream_mapMaterial.hasNext():
                    self._adaptor.addChild(root_2, stream_mapMaterial.nextTree())


                stream_mapMaterial.reset()

                self._adaptor.addChild(root_1, root_2)

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "symbols"

    class mapType_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "mapType"
    # XKBGrammar.g:70:1: mapType : ( MAPOPTS )+ DQSTRING -> ^( MAPTYPE ^( MAPOPTIONS ( MAPOPTS )+ ) ^( MAPNAME DQSTRING ) ) ;
    def mapType(self, ):

        retval = self.mapType_return()
        retval.start = self.input.LT(1)

        root_0 = None

        MAPOPTS8 = None
        DQSTRING9 = None

        MAPOPTS8_tree = None
        DQSTRING9_tree = None
        stream_MAPOPTS = RewriteRuleTokenStream(self._adaptor, "token MAPOPTS")
        stream_DQSTRING = RewriteRuleTokenStream(self._adaptor, "token DQSTRING")

        try:
            try:
                # XKBGrammar.g:71:3: ( ( MAPOPTS )+ DQSTRING -> ^( MAPTYPE ^( MAPOPTIONS ( MAPOPTS )+ ) ^( MAPNAME DQSTRING ) ) )
                # XKBGrammar.g:71:5: ( MAPOPTS )+ DQSTRING
                pass 
                # XKBGrammar.g:71:5: ( MAPOPTS )+
                cnt3 = 0
                while True: #loop3
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if (LA3_0 == MAPOPTS) :
                        alt3 = 1


                    if alt3 == 1:
                        # XKBGrammar.g:71:5: MAPOPTS
                        pass 
                        MAPOPTS8=self.match(self.input, MAPOPTS, self.FOLLOW_MAPOPTS_in_mapType260) 
                        stream_MAPOPTS.add(MAPOPTS8)


                    else:
                        if cnt3 >= 1:
                            break #loop3

                        eee = EarlyExitException(3, self.input)
                        raise eee

                    cnt3 += 1


                DQSTRING9=self.match(self.input, DQSTRING, self.FOLLOW_DQSTRING_in_mapType263) 
                stream_DQSTRING.add(DQSTRING9)

                # AST Rewrite
                # elements: MAPOPTS, DQSTRING
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 72:3: -> ^( MAPTYPE ^( MAPOPTIONS ( MAPOPTS )+ ) ^( MAPNAME DQSTRING ) )
                # XKBGrammar.g:72:6: ^( MAPTYPE ^( MAPOPTIONS ( MAPOPTS )+ ) ^( MAPNAME DQSTRING ) )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(MAPTYPE, "MAPTYPE"), root_1)

                # XKBGrammar.g:72:16: ^( MAPOPTIONS ( MAPOPTS )+ )
                root_2 = self._adaptor.nil()
                root_2 = self._adaptor.becomeRoot(self._adaptor.createFromType(MAPOPTIONS, "MAPOPTIONS"), root_2)

                # XKBGrammar.g:72:29: ( MAPOPTS )+
                if not (stream_MAPOPTS.hasNext()):
                    raise RewriteEarlyExitException()

                while stream_MAPOPTS.hasNext():
                    self._adaptor.addChild(root_2, stream_MAPOPTS.nextNode())


                stream_MAPOPTS.reset()

                self._adaptor.addChild(root_1, root_2)
                # XKBGrammar.g:72:39: ^( MAPNAME DQSTRING )
                root_2 = self._adaptor.nil()
                root_2 = self._adaptor.becomeRoot(self._adaptor.createFromType(MAPNAME, "MAPNAME"), root_2)

                self._adaptor.addChild(root_2, stream_DQSTRING.nextNode())

                self._adaptor.addChild(root_1, root_2)

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "mapType"

    class mapMaterial_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "mapMaterial"
    # XKBGrammar.g:75:1: mapMaterial : ( line_include | line_name ';' | line_keytype ';' | line_key ';' | line_modifier_map ';' | line_virtual_modifiers ';' );
    def mapMaterial(self, ):

        retval = self.mapMaterial_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal12 = None
        char_literal14 = None
        char_literal16 = None
        char_literal18 = None
        char_literal20 = None
        line_include10 = None

        line_name11 = None

        line_keytype13 = None

        line_key15 = None

        line_modifier_map17 = None

        line_virtual_modifiers19 = None


        char_literal12_tree = None
        char_literal14_tree = None
        char_literal16_tree = None
        char_literal18_tree = None
        char_literal20_tree = None

        try:
            try:
                # XKBGrammar.g:76:3: ( line_include | line_name ';' | line_keytype ';' | line_key ';' | line_modifier_map ';' | line_virtual_modifiers ';' )
                alt4 = 6
                LA4 = self.input.LA(1)
                if LA4 == 37:
                    alt4 = 1
                elif LA4 == 38:
                    alt4 = 2
                elif LA4 == 42:
                    alt4 = 3
                elif LA4 == OVERRIDE or LA4 == 43:
                    alt4 = 4
                elif LA4 == 47:
                    alt4 = 5
                elif LA4 == 48:
                    alt4 = 6
                else:
                    nvae = NoViableAltException("", 4, 0, self.input)

                    raise nvae

                if alt4 == 1:
                    # XKBGrammar.g:76:5: line_include
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_line_include_in_mapMaterial298)
                    line_include10 = self.line_include()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, line_include10.tree)


                elif alt4 == 2:
                    # XKBGrammar.g:77:5: line_name ';'
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_line_name_in_mapMaterial305)
                    line_name11 = self.line_name()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, line_name11.tree)
                    char_literal12=self.match(self.input, 36, self.FOLLOW_36_in_mapMaterial307)


                elif alt4 == 3:
                    # XKBGrammar.g:78:5: line_keytype ';'
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_line_keytype_in_mapMaterial314)
                    line_keytype13 = self.line_keytype()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, line_keytype13.tree)
                    char_literal14=self.match(self.input, 36, self.FOLLOW_36_in_mapMaterial316)


                elif alt4 == 4:
                    # XKBGrammar.g:79:5: line_key ';'
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_line_key_in_mapMaterial323)
                    line_key15 = self.line_key()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, line_key15.tree)
                    char_literal16=self.match(self.input, 36, self.FOLLOW_36_in_mapMaterial325)


                elif alt4 == 5:
                    # XKBGrammar.g:80:5: line_modifier_map ';'
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_line_modifier_map_in_mapMaterial332)
                    line_modifier_map17 = self.line_modifier_map()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, line_modifier_map17.tree)
                    char_literal18=self.match(self.input, 36, self.FOLLOW_36_in_mapMaterial334)


                elif alt4 == 6:
                    # XKBGrammar.g:81:5: line_virtual_modifiers ';'
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_line_virtual_modifiers_in_mapMaterial341)
                    line_virtual_modifiers19 = self.line_virtual_modifiers()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, line_virtual_modifiers19.tree)
                    char_literal20=self.match(self.input, 36, self.FOLLOW_36_in_mapMaterial343)


                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "mapMaterial"

    class line_include_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "line_include"
    # XKBGrammar.g:84:1: line_include : 'include' DQSTRING -> ^( TOKEN_INCLUDE DQSTRING ) ;
    def line_include(self, ):

        retval = self.line_include_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal21 = None
        DQSTRING22 = None

        string_literal21_tree = None
        DQSTRING22_tree = None
        stream_37 = RewriteRuleTokenStream(self._adaptor, "token 37")
        stream_DQSTRING = RewriteRuleTokenStream(self._adaptor, "token DQSTRING")

        try:
            try:
                # XKBGrammar.g:85:3: ( 'include' DQSTRING -> ^( TOKEN_INCLUDE DQSTRING ) )
                # XKBGrammar.g:85:5: 'include' DQSTRING
                pass 
                string_literal21=self.match(self.input, 37, self.FOLLOW_37_in_line_include357) 
                stream_37.add(string_literal21)
                DQSTRING22=self.match(self.input, DQSTRING, self.FOLLOW_DQSTRING_in_line_include359) 
                stream_DQSTRING.add(DQSTRING22)

                # AST Rewrite
                # elements: DQSTRING
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 86:3: -> ^( TOKEN_INCLUDE DQSTRING )
                # XKBGrammar.g:86:6: ^( TOKEN_INCLUDE DQSTRING )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(TOKEN_INCLUDE, "TOKEN_INCLUDE"), root_1)

                self._adaptor.addChild(root_1, stream_DQSTRING.nextNode())

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "line_include"

    class line_name_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "line_name"
    # XKBGrammar.g:89:1: line_name : 'name' ( '[' NAME ']' )? '=' DQSTRING -> ^( TOKEN_NAME DQSTRING ) ;
    def line_name(self, ):

        retval = self.line_name_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal23 = None
        char_literal24 = None
        NAME25 = None
        char_literal26 = None
        char_literal27 = None
        DQSTRING28 = None

        string_literal23_tree = None
        char_literal24_tree = None
        NAME25_tree = None
        char_literal26_tree = None
        char_literal27_tree = None
        DQSTRING28_tree = None
        stream_38 = RewriteRuleTokenStream(self._adaptor, "token 38")
        stream_39 = RewriteRuleTokenStream(self._adaptor, "token 39")
        stream_40 = RewriteRuleTokenStream(self._adaptor, "token 40")
        stream_41 = RewriteRuleTokenStream(self._adaptor, "token 41")
        stream_DQSTRING = RewriteRuleTokenStream(self._adaptor, "token DQSTRING")
        stream_NAME = RewriteRuleTokenStream(self._adaptor, "token NAME")

        try:
            try:
                # XKBGrammar.g:90:3: ( 'name' ( '[' NAME ']' )? '=' DQSTRING -> ^( TOKEN_NAME DQSTRING ) )
                # XKBGrammar.g:90:5: 'name' ( '[' NAME ']' )? '=' DQSTRING
                pass 
                string_literal23=self.match(self.input, 38, self.FOLLOW_38_in_line_name382) 
                stream_38.add(string_literal23)
                # XKBGrammar.g:90:12: ( '[' NAME ']' )?
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if (LA5_0 == 39) :
                    alt5 = 1
                if alt5 == 1:
                    # XKBGrammar.g:90:13: '[' NAME ']'
                    pass 
                    char_literal24=self.match(self.input, 39, self.FOLLOW_39_in_line_name385) 
                    stream_39.add(char_literal24)
                    NAME25=self.match(self.input, NAME, self.FOLLOW_NAME_in_line_name387) 
                    stream_NAME.add(NAME25)
                    char_literal26=self.match(self.input, 40, self.FOLLOW_40_in_line_name389) 
                    stream_40.add(char_literal26)



                char_literal27=self.match(self.input, 41, self.FOLLOW_41_in_line_name393) 
                stream_41.add(char_literal27)
                DQSTRING28=self.match(self.input, DQSTRING, self.FOLLOW_DQSTRING_in_line_name395) 
                stream_DQSTRING.add(DQSTRING28)

                # AST Rewrite
                # elements: DQSTRING
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 91:3: -> ^( TOKEN_NAME DQSTRING )
                # XKBGrammar.g:91:6: ^( TOKEN_NAME DQSTRING )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(TOKEN_NAME, "TOKEN_NAME"), root_1)

                self._adaptor.addChild(root_1, stream_DQSTRING.nextNode())

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "line_name"

    class line_keytype_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "line_keytype"
    # XKBGrammar.g:94:1: line_keytype : 'key.type' ( '[' NAME ']' )? '=' DQSTRING -> ^( TOKEN_KEY_TYPE DQSTRING ) ;
    def line_keytype(self, ):

        retval = self.line_keytype_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal29 = None
        char_literal30 = None
        NAME31 = None
        char_literal32 = None
        char_literal33 = None
        DQSTRING34 = None

        string_literal29_tree = None
        char_literal30_tree = None
        NAME31_tree = None
        char_literal32_tree = None
        char_literal33_tree = None
        DQSTRING34_tree = None
        stream_39 = RewriteRuleTokenStream(self._adaptor, "token 39")
        stream_40 = RewriteRuleTokenStream(self._adaptor, "token 40")
        stream_41 = RewriteRuleTokenStream(self._adaptor, "token 41")
        stream_42 = RewriteRuleTokenStream(self._adaptor, "token 42")
        stream_DQSTRING = RewriteRuleTokenStream(self._adaptor, "token DQSTRING")
        stream_NAME = RewriteRuleTokenStream(self._adaptor, "token NAME")

        try:
            try:
                # XKBGrammar.g:95:3: ( 'key.type' ( '[' NAME ']' )? '=' DQSTRING -> ^( TOKEN_KEY_TYPE DQSTRING ) )
                # XKBGrammar.g:95:5: 'key.type' ( '[' NAME ']' )? '=' DQSTRING
                pass 
                string_literal29=self.match(self.input, 42, self.FOLLOW_42_in_line_keytype418) 
                stream_42.add(string_literal29)
                # XKBGrammar.g:95:16: ( '[' NAME ']' )?
                alt6 = 2
                LA6_0 = self.input.LA(1)

                if (LA6_0 == 39) :
                    alt6 = 1
                if alt6 == 1:
                    # XKBGrammar.g:95:17: '[' NAME ']'
                    pass 
                    char_literal30=self.match(self.input, 39, self.FOLLOW_39_in_line_keytype421) 
                    stream_39.add(char_literal30)
                    NAME31=self.match(self.input, NAME, self.FOLLOW_NAME_in_line_keytype423) 
                    stream_NAME.add(NAME31)
                    char_literal32=self.match(self.input, 40, self.FOLLOW_40_in_line_keytype425) 
                    stream_40.add(char_literal32)



                char_literal33=self.match(self.input, 41, self.FOLLOW_41_in_line_keytype429) 
                stream_41.add(char_literal33)
                DQSTRING34=self.match(self.input, DQSTRING, self.FOLLOW_DQSTRING_in_line_keytype431) 
                stream_DQSTRING.add(DQSTRING34)

                # AST Rewrite
                # elements: DQSTRING
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 96:3: -> ^( TOKEN_KEY_TYPE DQSTRING )
                # XKBGrammar.g:96:6: ^( TOKEN_KEY_TYPE DQSTRING )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(TOKEN_KEY_TYPE, "TOKEN_KEY_TYPE"), root_1)

                self._adaptor.addChild(root_1, stream_DQSTRING.nextNode())

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "line_keytype"

    class line_key_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "line_key"
    # XKBGrammar.g:99:1: line_key : ( OVERRIDE )? 'key' '<' NAME '>' '{' keyelements ( ',' keyelements )* '}' -> ^( TOKEN_KEY ( OVERRIDE )? ^( KEYCODEX NAME ) ( keyelements )+ ) ;
    def line_key(self, ):

        retval = self.line_key_return()
        retval.start = self.input.LT(1)

        root_0 = None

        OVERRIDE35 = None
        string_literal36 = None
        char_literal37 = None
        NAME38 = None
        char_literal39 = None
        char_literal40 = None
        char_literal42 = None
        char_literal44 = None
        keyelements41 = None

        keyelements43 = None


        OVERRIDE35_tree = None
        string_literal36_tree = None
        char_literal37_tree = None
        NAME38_tree = None
        char_literal39_tree = None
        char_literal40_tree = None
        char_literal42_tree = None
        char_literal44_tree = None
        stream_44 = RewriteRuleTokenStream(self._adaptor, "token 44")
        stream_45 = RewriteRuleTokenStream(self._adaptor, "token 45")
        stream_OVERRIDE = RewriteRuleTokenStream(self._adaptor, "token OVERRIDE")
        stream_34 = RewriteRuleTokenStream(self._adaptor, "token 34")
        stream_35 = RewriteRuleTokenStream(self._adaptor, "token 35")
        stream_46 = RewriteRuleTokenStream(self._adaptor, "token 46")
        stream_43 = RewriteRuleTokenStream(self._adaptor, "token 43")
        stream_NAME = RewriteRuleTokenStream(self._adaptor, "token NAME")
        stream_keyelements = RewriteRuleSubtreeStream(self._adaptor, "rule keyelements")
        try:
            try:
                # XKBGrammar.g:100:3: ( ( OVERRIDE )? 'key' '<' NAME '>' '{' keyelements ( ',' keyelements )* '}' -> ^( TOKEN_KEY ( OVERRIDE )? ^( KEYCODEX NAME ) ( keyelements )+ ) )
                # XKBGrammar.g:100:5: ( OVERRIDE )? 'key' '<' NAME '>' '{' keyelements ( ',' keyelements )* '}'
                pass 
                # XKBGrammar.g:100:5: ( OVERRIDE )?
                alt7 = 2
                LA7_0 = self.input.LA(1)

                if (LA7_0 == OVERRIDE) :
                    alt7 = 1
                if alt7 == 1:
                    # XKBGrammar.g:100:5: OVERRIDE
                    pass 
                    OVERRIDE35=self.match(self.input, OVERRIDE, self.FOLLOW_OVERRIDE_in_line_key454) 
                    stream_OVERRIDE.add(OVERRIDE35)



                string_literal36=self.match(self.input, 43, self.FOLLOW_43_in_line_key457) 
                stream_43.add(string_literal36)
                char_literal37=self.match(self.input, 44, self.FOLLOW_44_in_line_key459) 
                stream_44.add(char_literal37)
                NAME38=self.match(self.input, NAME, self.FOLLOW_NAME_in_line_key461) 
                stream_NAME.add(NAME38)
                char_literal39=self.match(self.input, 45, self.FOLLOW_45_in_line_key463) 
                stream_45.add(char_literal39)
                char_literal40=self.match(self.input, 34, self.FOLLOW_34_in_line_key465) 
                stream_34.add(char_literal40)
                self._state.following.append(self.FOLLOW_keyelements_in_line_key467)
                keyelements41 = self.keyelements()

                self._state.following.pop()
                stream_keyelements.add(keyelements41.tree)
                # XKBGrammar.g:100:50: ( ',' keyelements )*
                while True: #loop8
                    alt8 = 2
                    LA8_0 = self.input.LA(1)

                    if (LA8_0 == 46) :
                        alt8 = 1


                    if alt8 == 1:
                        # XKBGrammar.g:100:51: ',' keyelements
                        pass 
                        char_literal42=self.match(self.input, 46, self.FOLLOW_46_in_line_key470) 
                        stream_46.add(char_literal42)
                        self._state.following.append(self.FOLLOW_keyelements_in_line_key472)
                        keyelements43 = self.keyelements()

                        self._state.following.pop()
                        stream_keyelements.add(keyelements43.tree)


                    else:
                        break #loop8


                char_literal44=self.match(self.input, 35, self.FOLLOW_35_in_line_key476) 
                stream_35.add(char_literal44)

                # AST Rewrite
                # elements: OVERRIDE, NAME, keyelements
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 101:3: -> ^( TOKEN_KEY ( OVERRIDE )? ^( KEYCODEX NAME ) ( keyelements )+ )
                # XKBGrammar.g:101:6: ^( TOKEN_KEY ( OVERRIDE )? ^( KEYCODEX NAME ) ( keyelements )+ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(TOKEN_KEY, "TOKEN_KEY"), root_1)

                # XKBGrammar.g:101:18: ( OVERRIDE )?
                if stream_OVERRIDE.hasNext():
                    self._adaptor.addChild(root_1, stream_OVERRIDE.nextNode())


                stream_OVERRIDE.reset();
                # XKBGrammar.g:101:28: ^( KEYCODEX NAME )
                root_2 = self._adaptor.nil()
                root_2 = self._adaptor.becomeRoot(self._adaptor.createFromType(KEYCODEX, "KEYCODEX"), root_2)

                self._adaptor.addChild(root_2, stream_NAME.nextNode())

                self._adaptor.addChild(root_1, root_2)
                # XKBGrammar.g:101:45: ( keyelements )+
                if not (stream_keyelements.hasNext()):
                    raise RewriteEarlyExitException()

                while stream_keyelements.hasNext():
                    self._adaptor.addChild(root_1, stream_keyelements.nextTree())


                stream_keyelements.reset()

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "line_key"

    class line_modifier_map_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "line_modifier_map"
    # XKBGrammar.g:104:1: line_modifier_map : 'modifier_map' STATE '{' keycode ( ',' keycode )* '}' -> ^( TOKEN_MODIFIER_MAP STATE ( keycode )+ ) ;
    def line_modifier_map(self, ):

        retval = self.line_modifier_map_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal45 = None
        STATE46 = None
        char_literal47 = None
        char_literal49 = None
        char_literal51 = None
        keycode48 = None

        keycode50 = None


        string_literal45_tree = None
        STATE46_tree = None
        char_literal47_tree = None
        char_literal49_tree = None
        char_literal51_tree = None
        stream_34 = RewriteRuleTokenStream(self._adaptor, "token 34")
        stream_35 = RewriteRuleTokenStream(self._adaptor, "token 35")
        stream_46 = RewriteRuleTokenStream(self._adaptor, "token 46")
        stream_47 = RewriteRuleTokenStream(self._adaptor, "token 47")
        stream_STATE = RewriteRuleTokenStream(self._adaptor, "token STATE")
        stream_keycode = RewriteRuleSubtreeStream(self._adaptor, "rule keycode")
        try:
            try:
                # XKBGrammar.g:105:3: ( 'modifier_map' STATE '{' keycode ( ',' keycode )* '}' -> ^( TOKEN_MODIFIER_MAP STATE ( keycode )+ ) )
                # XKBGrammar.g:105:5: 'modifier_map' STATE '{' keycode ( ',' keycode )* '}'
                pass 
                string_literal45=self.match(self.input, 47, self.FOLLOW_47_in_line_modifier_map509) 
                stream_47.add(string_literal45)
                STATE46=self.match(self.input, STATE, self.FOLLOW_STATE_in_line_modifier_map511) 
                stream_STATE.add(STATE46)
                char_literal47=self.match(self.input, 34, self.FOLLOW_34_in_line_modifier_map513) 
                stream_34.add(char_literal47)
                self._state.following.append(self.FOLLOW_keycode_in_line_modifier_map515)
                keycode48 = self.keycode()

                self._state.following.pop()
                stream_keycode.add(keycode48.tree)
                # XKBGrammar.g:105:38: ( ',' keycode )*
                while True: #loop9
                    alt9 = 2
                    LA9_0 = self.input.LA(1)

                    if (LA9_0 == 46) :
                        alt9 = 1


                    if alt9 == 1:
                        # XKBGrammar.g:105:39: ',' keycode
                        pass 
                        char_literal49=self.match(self.input, 46, self.FOLLOW_46_in_line_modifier_map518) 
                        stream_46.add(char_literal49)
                        self._state.following.append(self.FOLLOW_keycode_in_line_modifier_map520)
                        keycode50 = self.keycode()

                        self._state.following.pop()
                        stream_keycode.add(keycode50.tree)


                    else:
                        break #loop9


                char_literal51=self.match(self.input, 35, self.FOLLOW_35_in_line_modifier_map524) 
                stream_35.add(char_literal51)

                # AST Rewrite
                # elements: STATE, keycode
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 106:3: -> ^( TOKEN_MODIFIER_MAP STATE ( keycode )+ )
                # XKBGrammar.g:106:6: ^( TOKEN_MODIFIER_MAP STATE ( keycode )+ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(TOKEN_MODIFIER_MAP, "TOKEN_MODIFIER_MAP"), root_1)

                self._adaptor.addChild(root_1, stream_STATE.nextNode())
                # XKBGrammar.g:106:33: ( keycode )+
                if not (stream_keycode.hasNext()):
                    raise RewriteEarlyExitException()

                while stream_keycode.hasNext():
                    self._adaptor.addChild(root_1, stream_keycode.nextTree())


                stream_keycode.reset()

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "line_modifier_map"

    class line_virtual_modifiers_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "line_virtual_modifiers"
    # XKBGrammar.g:109:1: line_virtual_modifiers : 'virtual_modifiers' NAME ( ',' NAME )* -> ^( TOKEN_VIRTUAL_MODIFIERS ( NAME )+ ) ;
    def line_virtual_modifiers(self, ):

        retval = self.line_virtual_modifiers_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal52 = None
        NAME53 = None
        char_literal54 = None
        NAME55 = None

        string_literal52_tree = None
        NAME53_tree = None
        char_literal54_tree = None
        NAME55_tree = None
        stream_46 = RewriteRuleTokenStream(self._adaptor, "token 46")
        stream_48 = RewriteRuleTokenStream(self._adaptor, "token 48")
        stream_NAME = RewriteRuleTokenStream(self._adaptor, "token NAME")

        try:
            try:
                # XKBGrammar.g:110:3: ( 'virtual_modifiers' NAME ( ',' NAME )* -> ^( TOKEN_VIRTUAL_MODIFIERS ( NAME )+ ) )
                # XKBGrammar.g:110:5: 'virtual_modifiers' NAME ( ',' NAME )*
                pass 
                string_literal52=self.match(self.input, 48, self.FOLLOW_48_in_line_virtual_modifiers550) 
                stream_48.add(string_literal52)
                NAME53=self.match(self.input, NAME, self.FOLLOW_NAME_in_line_virtual_modifiers552) 
                stream_NAME.add(NAME53)
                # XKBGrammar.g:110:30: ( ',' NAME )*
                while True: #loop10
                    alt10 = 2
                    LA10_0 = self.input.LA(1)

                    if (LA10_0 == 46) :
                        alt10 = 1


                    if alt10 == 1:
                        # XKBGrammar.g:110:31: ',' NAME
                        pass 
                        char_literal54=self.match(self.input, 46, self.FOLLOW_46_in_line_virtual_modifiers555) 
                        stream_46.add(char_literal54)
                        NAME55=self.match(self.input, NAME, self.FOLLOW_NAME_in_line_virtual_modifiers557) 
                        stream_NAME.add(NAME55)


                    else:
                        break #loop10



                # AST Rewrite
                # elements: NAME
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 111:3: -> ^( TOKEN_VIRTUAL_MODIFIERS ( NAME )+ )
                # XKBGrammar.g:111:6: ^( TOKEN_VIRTUAL_MODIFIERS ( NAME )+ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(TOKEN_VIRTUAL_MODIFIERS, "TOKEN_VIRTUAL_MODIFIERS"), root_1)

                # XKBGrammar.g:111:32: ( NAME )+
                if not (stream_NAME.hasNext()):
                    raise RewriteEarlyExitException()

                while stream_NAME.hasNext():
                    self._adaptor.addChild(root_1, stream_NAME.nextNode())


                stream_NAME.reset()

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "line_virtual_modifiers"

    class keycode_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "keycode"
    # XKBGrammar.g:114:1: keycode : ( '<' NAME '>' -> ^( KEYCODEX NAME ) | NAME -> ^( KEYCODE NAME ) );
    def keycode(self, ):

        retval = self.keycode_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal56 = None
        NAME57 = None
        char_literal58 = None
        NAME59 = None

        char_literal56_tree = None
        NAME57_tree = None
        char_literal58_tree = None
        NAME59_tree = None
        stream_44 = RewriteRuleTokenStream(self._adaptor, "token 44")
        stream_45 = RewriteRuleTokenStream(self._adaptor, "token 45")
        stream_NAME = RewriteRuleTokenStream(self._adaptor, "token NAME")

        try:
            try:
                # XKBGrammar.g:115:3: ( '<' NAME '>' -> ^( KEYCODEX NAME ) | NAME -> ^( KEYCODE NAME ) )
                alt11 = 2
                LA11_0 = self.input.LA(1)

                if (LA11_0 == 44) :
                    alt11 = 1
                elif (LA11_0 == NAME) :
                    alt11 = 2
                else:
                    nvae = NoViableAltException("", 11, 0, self.input)

                    raise nvae

                if alt11 == 1:
                    # XKBGrammar.g:115:5: '<' NAME '>'
                    pass 
                    char_literal56=self.match(self.input, 44, self.FOLLOW_44_in_keycode584) 
                    stream_44.add(char_literal56)
                    NAME57=self.match(self.input, NAME, self.FOLLOW_NAME_in_keycode586) 
                    stream_NAME.add(NAME57)
                    char_literal58=self.match(self.input, 45, self.FOLLOW_45_in_keycode588) 
                    stream_45.add(char_literal58)

                    # AST Rewrite
                    # elements: NAME
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 115:18: -> ^( KEYCODEX NAME )
                    # XKBGrammar.g:115:21: ^( KEYCODEX NAME )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(KEYCODEX, "KEYCODEX"), root_1)

                    self._adaptor.addChild(root_1, stream_NAME.nextNode())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt11 == 2:
                    # XKBGrammar.g:116:5: NAME
                    pass 
                    NAME59=self.match(self.input, NAME, self.FOLLOW_NAME_in_keycode602) 
                    stream_NAME.add(NAME59)

                    # AST Rewrite
                    # elements: NAME
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 116:10: -> ^( KEYCODE NAME )
                    # XKBGrammar.g:116:13: ^( KEYCODE NAME )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(KEYCODE, "KEYCODE"), root_1)

                    self._adaptor.addChild(root_1, stream_NAME.nextNode())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "keycode"

    class override_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "override"
    # XKBGrammar.g:119:1: override : 'override' ;
    def override(self, ):

        retval = self.override_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal60 = None

        string_literal60_tree = None

        try:
            try:
                # XKBGrammar.g:120:3: ( 'override' )
                # XKBGrammar.g:120:5: 'override'
                pass 
                root_0 = self._adaptor.nil()

                string_literal60=self.match(self.input, OVERRIDE, self.FOLLOW_OVERRIDE_in_override623)

                string_literal60_tree = self._adaptor.createWithPayload(string_literal60)
                self._adaptor.addChild(root_0, string_literal60_tree)




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "override"

    class keyelements_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "keyelements"
    # XKBGrammar.g:123:1: keyelements : ( elem_keysyms | elem_keysymgroup | elem_virtualmods | elem_overlay );
    def keyelements(self, ):

        retval = self.keyelements_return()
        retval.start = self.input.LT(1)

        root_0 = None

        elem_keysyms61 = None

        elem_keysymgroup62 = None

        elem_virtualmods63 = None

        elem_overlay64 = None



        try:
            try:
                # XKBGrammar.g:124:3: ( elem_keysyms | elem_keysymgroup | elem_virtualmods | elem_overlay )
                alt12 = 4
                LA12 = self.input.LA(1)
                if LA12 == 49:
                    alt12 = 1
                elif LA12 == 39 or LA12 == 50:
                    alt12 = 2
                elif LA12 == 51:
                    alt12 = 3
                elif LA12 == NAME:
                    alt12 = 4
                else:
                    nvae = NoViableAltException("", 12, 0, self.input)

                    raise nvae

                if alt12 == 1:
                    # XKBGrammar.g:124:5: elem_keysyms
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_elem_keysyms_in_keyelements636)
                    elem_keysyms61 = self.elem_keysyms()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, elem_keysyms61.tree)


                elif alt12 == 2:
                    # XKBGrammar.g:125:5: elem_keysymgroup
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_elem_keysymgroup_in_keyelements643)
                    elem_keysymgroup62 = self.elem_keysymgroup()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, elem_keysymgroup62.tree)


                elif alt12 == 3:
                    # XKBGrammar.g:126:5: elem_virtualmods
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_elem_virtualmods_in_keyelements649)
                    elem_virtualmods63 = self.elem_virtualmods()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, elem_virtualmods63.tree)


                elif alt12 == 4:
                    # XKBGrammar.g:127:5: elem_overlay
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_elem_overlay_in_keyelements655)
                    elem_overlay64 = self.elem_overlay()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, elem_overlay64.tree)


                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "keyelements"

    class elem_keysyms_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "elem_keysyms"
    # XKBGrammar.g:130:1: elem_keysyms : 'type' ( '[' NAME ']' )? '=' DQSTRING -> ^( ELEM_KEYSYMS DQSTRING ) ;
    def elem_keysyms(self, ):

        retval = self.elem_keysyms_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal65 = None
        char_literal66 = None
        NAME67 = None
        char_literal68 = None
        char_literal69 = None
        DQSTRING70 = None

        string_literal65_tree = None
        char_literal66_tree = None
        NAME67_tree = None
        char_literal68_tree = None
        char_literal69_tree = None
        DQSTRING70_tree = None
        stream_49 = RewriteRuleTokenStream(self._adaptor, "token 49")
        stream_39 = RewriteRuleTokenStream(self._adaptor, "token 39")
        stream_40 = RewriteRuleTokenStream(self._adaptor, "token 40")
        stream_41 = RewriteRuleTokenStream(self._adaptor, "token 41")
        stream_DQSTRING = RewriteRuleTokenStream(self._adaptor, "token DQSTRING")
        stream_NAME = RewriteRuleTokenStream(self._adaptor, "token NAME")

        try:
            try:
                # XKBGrammar.g:131:3: ( 'type' ( '[' NAME ']' )? '=' DQSTRING -> ^( ELEM_KEYSYMS DQSTRING ) )
                # XKBGrammar.g:131:5: 'type' ( '[' NAME ']' )? '=' DQSTRING
                pass 
                string_literal65=self.match(self.input, 49, self.FOLLOW_49_in_elem_keysyms668) 
                stream_49.add(string_literal65)
                # XKBGrammar.g:131:12: ( '[' NAME ']' )?
                alt13 = 2
                LA13_0 = self.input.LA(1)

                if (LA13_0 == 39) :
                    alt13 = 1
                if alt13 == 1:
                    # XKBGrammar.g:131:13: '[' NAME ']'
                    pass 
                    char_literal66=self.match(self.input, 39, self.FOLLOW_39_in_elem_keysyms671) 
                    stream_39.add(char_literal66)
                    NAME67=self.match(self.input, NAME, self.FOLLOW_NAME_in_elem_keysyms673) 
                    stream_NAME.add(NAME67)
                    char_literal68=self.match(self.input, 40, self.FOLLOW_40_in_elem_keysyms675) 
                    stream_40.add(char_literal68)



                char_literal69=self.match(self.input, 41, self.FOLLOW_41_in_elem_keysyms679) 
                stream_41.add(char_literal69)
                DQSTRING70=self.match(self.input, DQSTRING, self.FOLLOW_DQSTRING_in_elem_keysyms681) 
                stream_DQSTRING.add(DQSTRING70)

                # AST Rewrite
                # elements: DQSTRING
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 132:3: -> ^( ELEM_KEYSYMS DQSTRING )
                # XKBGrammar.g:132:6: ^( ELEM_KEYSYMS DQSTRING )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(ELEM_KEYSYMS, "ELEM_KEYSYMS"), root_1)

                self._adaptor.addChild(root_1, stream_DQSTRING.nextNode())

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "elem_keysyms"

    class elem_keysymgroup_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "elem_keysymgroup"
    # XKBGrammar.g:135:1: elem_keysymgroup : ( 'symbols' '[' NAME ']' '=' )? '[' keysym+= NAME ( ',' keysym+= NAME )* ']' -> ^( ELEM_KEYSYMGROUP ^( VALUE ( $keysym)+ ) ) ;
    def elem_keysymgroup(self, ):

        retval = self.elem_keysymgroup_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal71 = None
        char_literal72 = None
        NAME73 = None
        char_literal74 = None
        char_literal75 = None
        char_literal76 = None
        char_literal77 = None
        char_literal78 = None
        keysym = None
        list_keysym = None

        string_literal71_tree = None
        char_literal72_tree = None
        NAME73_tree = None
        char_literal74_tree = None
        char_literal75_tree = None
        char_literal76_tree = None
        char_literal77_tree = None
        char_literal78_tree = None
        keysym_tree = None
        stream_46 = RewriteRuleTokenStream(self._adaptor, "token 46")
        stream_39 = RewriteRuleTokenStream(self._adaptor, "token 39")
        stream_50 = RewriteRuleTokenStream(self._adaptor, "token 50")
        stream_40 = RewriteRuleTokenStream(self._adaptor, "token 40")
        stream_41 = RewriteRuleTokenStream(self._adaptor, "token 41")
        stream_NAME = RewriteRuleTokenStream(self._adaptor, "token NAME")

        try:
            try:
                # XKBGrammar.g:136:3: ( ( 'symbols' '[' NAME ']' '=' )? '[' keysym+= NAME ( ',' keysym+= NAME )* ']' -> ^( ELEM_KEYSYMGROUP ^( VALUE ( $keysym)+ ) ) )
                # XKBGrammar.g:136:5: ( 'symbols' '[' NAME ']' '=' )? '[' keysym+= NAME ( ',' keysym+= NAME )* ']'
                pass 
                # XKBGrammar.g:136:5: ( 'symbols' '[' NAME ']' '=' )?
                alt14 = 2
                LA14_0 = self.input.LA(1)

                if (LA14_0 == 50) :
                    alt14 = 1
                if alt14 == 1:
                    # XKBGrammar.g:136:6: 'symbols' '[' NAME ']' '='
                    pass 
                    string_literal71=self.match(self.input, 50, self.FOLLOW_50_in_elem_keysymgroup705) 
                    stream_50.add(string_literal71)
                    char_literal72=self.match(self.input, 39, self.FOLLOW_39_in_elem_keysymgroup707) 
                    stream_39.add(char_literal72)
                    NAME73=self.match(self.input, NAME, self.FOLLOW_NAME_in_elem_keysymgroup709) 
                    stream_NAME.add(NAME73)
                    char_literal74=self.match(self.input, 40, self.FOLLOW_40_in_elem_keysymgroup711) 
                    stream_40.add(char_literal74)
                    char_literal75=self.match(self.input, 41, self.FOLLOW_41_in_elem_keysymgroup713) 
                    stream_41.add(char_literal75)



                char_literal76=self.match(self.input, 39, self.FOLLOW_39_in_elem_keysymgroup717) 
                stream_39.add(char_literal76)
                keysym=self.match(self.input, NAME, self.FOLLOW_NAME_in_elem_keysymgroup721) 
                stream_NAME.add(keysym)
                if list_keysym is None:
                    list_keysym = []
                list_keysym.append(keysym)

                # XKBGrammar.g:136:52: ( ',' keysym+= NAME )*
                while True: #loop15
                    alt15 = 2
                    LA15_0 = self.input.LA(1)

                    if (LA15_0 == 46) :
                        alt15 = 1


                    if alt15 == 1:
                        # XKBGrammar.g:136:53: ',' keysym+= NAME
                        pass 
                        char_literal77=self.match(self.input, 46, self.FOLLOW_46_in_elem_keysymgroup724) 
                        stream_46.add(char_literal77)
                        keysym=self.match(self.input, NAME, self.FOLLOW_NAME_in_elem_keysymgroup728) 
                        stream_NAME.add(keysym)
                        if list_keysym is None:
                            list_keysym = []
                        list_keysym.append(keysym)



                    else:
                        break #loop15


                char_literal78=self.match(self.input, 40, self.FOLLOW_40_in_elem_keysymgroup732) 
                stream_40.add(char_literal78)

                # AST Rewrite
                # elements: keysym
                # token labels: 
                # rule labels: retval
                # token list labels: keysym
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0
                stream_keysym = RewriteRuleTokenStream(self._adaptor, "token keysym", list_keysym)

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 137:3: -> ^( ELEM_KEYSYMGROUP ^( VALUE ( $keysym)+ ) )
                # XKBGrammar.g:137:6: ^( ELEM_KEYSYMGROUP ^( VALUE ( $keysym)+ ) )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(ELEM_KEYSYMGROUP, "ELEM_KEYSYMGROUP"), root_1)

                # XKBGrammar.g:137:25: ^( VALUE ( $keysym)+ )
                root_2 = self._adaptor.nil()
                root_2 = self._adaptor.becomeRoot(self._adaptor.createFromType(VALUE, "VALUE"), root_2)

                # XKBGrammar.g:137:33: ( $keysym)+
                if not (stream_keysym.hasNext()):
                    raise RewriteEarlyExitException()

                while stream_keysym.hasNext():
                    self._adaptor.addChild(root_2, stream_keysym.nextNode())


                stream_keysym.reset()

                self._adaptor.addChild(root_1, root_2)

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "elem_keysymgroup"

    class elem_virtualmods_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "elem_virtualmods"
    # XKBGrammar.g:140:1: elem_virtualmods : ( 'virtualMods' '=' NAME ) -> ^( ELEM_VIRTUALMODS NAME ) ;
    def elem_virtualmods(self, ):

        retval = self.elem_virtualmods_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal79 = None
        char_literal80 = None
        NAME81 = None

        string_literal79_tree = None
        char_literal80_tree = None
        NAME81_tree = None
        stream_51 = RewriteRuleTokenStream(self._adaptor, "token 51")
        stream_41 = RewriteRuleTokenStream(self._adaptor, "token 41")
        stream_NAME = RewriteRuleTokenStream(self._adaptor, "token NAME")

        try:
            try:
                # XKBGrammar.g:141:3: ( ( 'virtualMods' '=' NAME ) -> ^( ELEM_VIRTUALMODS NAME ) )
                # XKBGrammar.g:141:5: ( 'virtualMods' '=' NAME )
                pass 
                # XKBGrammar.g:141:5: ( 'virtualMods' '=' NAME )
                # XKBGrammar.g:141:6: 'virtualMods' '=' NAME
                pass 
                string_literal79=self.match(self.input, 51, self.FOLLOW_51_in_elem_virtualmods763) 
                stream_51.add(string_literal79)
                char_literal80=self.match(self.input, 41, self.FOLLOW_41_in_elem_virtualmods765) 
                stream_41.add(char_literal80)
                NAME81=self.match(self.input, NAME, self.FOLLOW_NAME_in_elem_virtualmods767) 
                stream_NAME.add(NAME81)




                # AST Rewrite
                # elements: NAME
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 142:3: -> ^( ELEM_VIRTUALMODS NAME )
                # XKBGrammar.g:142:6: ^( ELEM_VIRTUALMODS NAME )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(ELEM_VIRTUALMODS, "ELEM_VIRTUALMODS"), root_1)

                self._adaptor.addChild(root_1, stream_NAME.nextNode())

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "elem_virtualmods"

    class elem_overlay_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "elem_overlay"
    # XKBGrammar.g:145:1: elem_overlay : NAME '=' keycode -> ^( OVERLAY NAME keycode ) ;
    def elem_overlay(self, ):

        retval = self.elem_overlay_return()
        retval.start = self.input.LT(1)

        root_0 = None

        NAME82 = None
        char_literal83 = None
        keycode84 = None


        NAME82_tree = None
        char_literal83_tree = None
        stream_41 = RewriteRuleTokenStream(self._adaptor, "token 41")
        stream_NAME = RewriteRuleTokenStream(self._adaptor, "token NAME")
        stream_keycode = RewriteRuleSubtreeStream(self._adaptor, "rule keycode")
        try:
            try:
                # XKBGrammar.g:146:3: ( NAME '=' keycode -> ^( OVERLAY NAME keycode ) )
                # XKBGrammar.g:146:5: NAME '=' keycode
                pass 
                NAME82=self.match(self.input, NAME, self.FOLLOW_NAME_in_elem_overlay791) 
                stream_NAME.add(NAME82)
                char_literal83=self.match(self.input, 41, self.FOLLOW_41_in_elem_overlay793) 
                stream_41.add(char_literal83)
                self._state.following.append(self.FOLLOW_keycode_in_elem_overlay795)
                keycode84 = self.keycode()

                self._state.following.pop()
                stream_keycode.add(keycode84.tree)

                # AST Rewrite
                # elements: NAME, keycode
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 147:3: -> ^( OVERLAY NAME keycode )
                # XKBGrammar.g:147:6: ^( OVERLAY NAME keycode )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(OVERLAY, "OVERLAY"), root_1)

                self._adaptor.addChild(root_1, stream_NAME.nextNode())
                self._adaptor.addChild(root_1, stream_keycode.nextTree())

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "elem_overlay"


    # Delegated rules


 

    FOLLOW_symbols_in_layout191 = frozenset([28])
    FOLLOW_EOF_in_layout194 = frozenset([1])
    FOLLOW_mapType_in_symbols221 = frozenset([34])
    FOLLOW_34_in_symbols223 = frozenset([26, 37, 38, 42, 43, 47, 48])
    FOLLOW_mapMaterial_in_symbols225 = frozenset([26, 35, 37, 38, 42, 43, 47, 48])
    FOLLOW_35_in_symbols228 = frozenset([36])
    FOLLOW_36_in_symbols230 = frozenset([1])
    FOLLOW_MAPOPTS_in_mapType260 = frozenset([28, 29])
    FOLLOW_DQSTRING_in_mapType263 = frozenset([1])
    FOLLOW_line_include_in_mapMaterial298 = frozenset([1])
    FOLLOW_line_name_in_mapMaterial305 = frozenset([36])
    FOLLOW_36_in_mapMaterial307 = frozenset([1])
    FOLLOW_line_keytype_in_mapMaterial314 = frozenset([36])
    FOLLOW_36_in_mapMaterial316 = frozenset([1])
    FOLLOW_line_key_in_mapMaterial323 = frozenset([36])
    FOLLOW_36_in_mapMaterial325 = frozenset([1])
    FOLLOW_line_modifier_map_in_mapMaterial332 = frozenset([36])
    FOLLOW_36_in_mapMaterial334 = frozenset([1])
    FOLLOW_line_virtual_modifiers_in_mapMaterial341 = frozenset([36])
    FOLLOW_36_in_mapMaterial343 = frozenset([1])
    FOLLOW_37_in_line_include357 = frozenset([29])
    FOLLOW_DQSTRING_in_line_include359 = frozenset([1])
    FOLLOW_38_in_line_name382 = frozenset([39, 41])
    FOLLOW_39_in_line_name385 = frozenset([30])
    FOLLOW_NAME_in_line_name387 = frozenset([40])
    FOLLOW_40_in_line_name389 = frozenset([41])
    FOLLOW_41_in_line_name393 = frozenset([29])
    FOLLOW_DQSTRING_in_line_name395 = frozenset([1])
    FOLLOW_42_in_line_keytype418 = frozenset([39, 41])
    FOLLOW_39_in_line_keytype421 = frozenset([30])
    FOLLOW_NAME_in_line_keytype423 = frozenset([40])
    FOLLOW_40_in_line_keytype425 = frozenset([41])
    FOLLOW_41_in_line_keytype429 = frozenset([29])
    FOLLOW_DQSTRING_in_line_keytype431 = frozenset([1])
    FOLLOW_OVERRIDE_in_line_key454 = frozenset([43])
    FOLLOW_43_in_line_key457 = frozenset([44])
    FOLLOW_44_in_line_key459 = frozenset([30])
    FOLLOW_NAME_in_line_key461 = frozenset([45])
    FOLLOW_45_in_line_key463 = frozenset([34])
    FOLLOW_34_in_line_key465 = frozenset([30, 39, 49, 50, 51])
    FOLLOW_keyelements_in_line_key467 = frozenset([35, 46])
    FOLLOW_46_in_line_key470 = frozenset([30, 39, 49, 50, 51])
    FOLLOW_keyelements_in_line_key472 = frozenset([35, 46])
    FOLLOW_35_in_line_key476 = frozenset([1])
    FOLLOW_47_in_line_modifier_map509 = frozenset([21])
    FOLLOW_STATE_in_line_modifier_map511 = frozenset([34])
    FOLLOW_34_in_line_modifier_map513 = frozenset([30, 44])
    FOLLOW_keycode_in_line_modifier_map515 = frozenset([35, 46])
    FOLLOW_46_in_line_modifier_map518 = frozenset([30, 44])
    FOLLOW_keycode_in_line_modifier_map520 = frozenset([35, 46])
    FOLLOW_35_in_line_modifier_map524 = frozenset([1])
    FOLLOW_48_in_line_virtual_modifiers550 = frozenset([30])
    FOLLOW_NAME_in_line_virtual_modifiers552 = frozenset([1, 46])
    FOLLOW_46_in_line_virtual_modifiers555 = frozenset([30])
    FOLLOW_NAME_in_line_virtual_modifiers557 = frozenset([1, 46])
    FOLLOW_44_in_keycode584 = frozenset([30])
    FOLLOW_NAME_in_keycode586 = frozenset([45])
    FOLLOW_45_in_keycode588 = frozenset([1])
    FOLLOW_NAME_in_keycode602 = frozenset([1])
    FOLLOW_OVERRIDE_in_override623 = frozenset([1])
    FOLLOW_elem_keysyms_in_keyelements636 = frozenset([1])
    FOLLOW_elem_keysymgroup_in_keyelements643 = frozenset([1])
    FOLLOW_elem_virtualmods_in_keyelements649 = frozenset([1])
    FOLLOW_elem_overlay_in_keyelements655 = frozenset([1])
    FOLLOW_49_in_elem_keysyms668 = frozenset([39, 41])
    FOLLOW_39_in_elem_keysyms671 = frozenset([30])
    FOLLOW_NAME_in_elem_keysyms673 = frozenset([40])
    FOLLOW_40_in_elem_keysyms675 = frozenset([41])
    FOLLOW_41_in_elem_keysyms679 = frozenset([29])
    FOLLOW_DQSTRING_in_elem_keysyms681 = frozenset([1])
    FOLLOW_50_in_elem_keysymgroup705 = frozenset([39])
    FOLLOW_39_in_elem_keysymgroup707 = frozenset([30])
    FOLLOW_NAME_in_elem_keysymgroup709 = frozenset([40])
    FOLLOW_40_in_elem_keysymgroup711 = frozenset([41])
    FOLLOW_41_in_elem_keysymgroup713 = frozenset([39])
    FOLLOW_39_in_elem_keysymgroup717 = frozenset([30])
    FOLLOW_NAME_in_elem_keysymgroup721 = frozenset([40, 46])
    FOLLOW_46_in_elem_keysymgroup724 = frozenset([30])
    FOLLOW_NAME_in_elem_keysymgroup728 = frozenset([40, 46])
    FOLLOW_40_in_elem_keysymgroup732 = frozenset([1])
    FOLLOW_51_in_elem_virtualmods763 = frozenset([41])
    FOLLOW_41_in_elem_virtualmods765 = frozenset([30])
    FOLLOW_NAME_in_elem_virtualmods767 = frozenset([1])
    FOLLOW_NAME_in_elem_overlay791 = frozenset([41])
    FOLLOW_41_in_elem_overlay793 = frozenset([30, 44])
    FOLLOW_keycode_in_elem_overlay795 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("XKBGrammarLexer", XKBGrammarParser)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
