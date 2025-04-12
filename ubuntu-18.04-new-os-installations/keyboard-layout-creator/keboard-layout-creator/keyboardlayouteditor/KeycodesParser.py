# $ANTLR 3.1.2 Keycodes.g 2020-05-10 06:02:52

import sys
from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.tree import *



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
KEYCODEDOC=4
KEYCODELIST=5
ALIAS=14
KEYCODEMATERIAL=10
INDICATOR=15
DQSTRING=17
COMMENT=20
KEYCODELISTTYPE=6
MINIMUM=12
KEYCODE=16
INCLUDE=11
WS=19
EOF=-1
T__30=30
KEYCODELISTNAME=9
T__31=31
T__32=32
KEYCODELISTOPTS=8
MAXIMUM=13
NAME=18
KEYCODELISTOPTIONS=7
LINE_COMMENT=21
T__26=26
T__27=27
T__28=28
T__29=29
T__22=22
T__23=23
T__24=24
T__25=25

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "KEYCODEDOC", "KEYCODELIST", "KEYCODELISTTYPE", "KEYCODELISTOPTIONS", 
    "KEYCODELISTOPTS", "KEYCODELISTNAME", "KEYCODEMATERIAL", "INCLUDE", 
    "MINIMUM", "MAXIMUM", "ALIAS", "INDICATOR", "KEYCODE", "DQSTRING", "NAME", 
    "WS", "COMMENT", "LINE_COMMENT", "'{'", "'}'", "';'", "'include'", "'minimum'", 
    "'='", "'maximum'", "'alias'", "'<'", "'>'", "'indicator'"
]




class KeycodesParser(Parser):
    grammarFileName = "Keycodes.g"
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


    class keycodedoc_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "keycodedoc"
    # Keycodes.g:30:1: keycodedoc : ( keycodelist )+ EOF -> ^( KEYCODEDOC ( keycodelist )+ ) ;
    def keycodedoc(self, ):

        retval = self.keycodedoc_return()
        retval.start = self.input.LT(1)

        root_0 = None

        EOF2 = None
        keycodelist1 = None


        EOF2_tree = None
        stream_EOF = RewriteRuleTokenStream(self._adaptor, "token EOF")
        stream_keycodelist = RewriteRuleSubtreeStream(self._adaptor, "rule keycodelist")
        try:
            try:
                # Keycodes.g:31:2: ( ( keycodelist )+ EOF -> ^( KEYCODEDOC ( keycodelist )+ ) )
                # Keycodes.g:31:4: ( keycodelist )+ EOF
                pass 
                # Keycodes.g:31:4: ( keycodelist )+
                cnt1 = 0
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 == KEYCODELISTOPTS) :
                        alt1 = 1


                    if alt1 == 1:
                        # Keycodes.g:31:4: keycodelist
                        pass 
                        self._state.following.append(self.FOLLOW_keycodelist_in_keycodedoc97)
                        keycodelist1 = self.keycodelist()

                        self._state.following.pop()
                        stream_keycodelist.add(keycodelist1.tree)


                    else:
                        if cnt1 >= 1:
                            break #loop1

                        eee = EarlyExitException(1, self.input)
                        raise eee

                    cnt1 += 1


                EOF2=self.match(self.input, EOF, self.FOLLOW_EOF_in_keycodedoc100) 
                stream_EOF.add(EOF2)

                # AST Rewrite
                # elements: keycodelist
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
                # 32:2: -> ^( KEYCODEDOC ( keycodelist )+ )
                # Keycodes.g:32:5: ^( KEYCODEDOC ( keycodelist )+ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(KEYCODEDOC, "KEYCODEDOC"), root_1)

                # Keycodes.g:32:18: ( keycodelist )+
                if not (stream_keycodelist.hasNext()):
                    raise RewriteEarlyExitException()

                while stream_keycodelist.hasNext():
                    self._adaptor.addChild(root_1, stream_keycodelist.nextTree())


                stream_keycodelist.reset()

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

    # $ANTLR end "keycodedoc"

    class keycodelist_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "keycodelist"
    # Keycodes.g:35:1: keycodelist : keycodelisttype '{' ( keycodeMaterial )+ '}' ';' -> ^( KEYCODELIST keycodelisttype ^( KEYCODEMATERIAL ( keycodeMaterial )+ ) ) ;
    def keycodelist(self, ):

        retval = self.keycodelist_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal4 = None
        char_literal6 = None
        char_literal7 = None
        keycodelisttype3 = None

        keycodeMaterial5 = None


        char_literal4_tree = None
        char_literal6_tree = None
        char_literal7_tree = None
        stream_22 = RewriteRuleTokenStream(self._adaptor, "token 22")
        stream_23 = RewriteRuleTokenStream(self._adaptor, "token 23")
        stream_24 = RewriteRuleTokenStream(self._adaptor, "token 24")
        stream_keycodelisttype = RewriteRuleSubtreeStream(self._adaptor, "rule keycodelisttype")
        stream_keycodeMaterial = RewriteRuleSubtreeStream(self._adaptor, "rule keycodeMaterial")
        try:
            try:
                # Keycodes.g:36:2: ( keycodelisttype '{' ( keycodeMaterial )+ '}' ';' -> ^( KEYCODELIST keycodelisttype ^( KEYCODEMATERIAL ( keycodeMaterial )+ ) ) )
                # Keycodes.g:36:4: keycodelisttype '{' ( keycodeMaterial )+ '}' ';'
                pass 
                self._state.following.append(self.FOLLOW_keycodelisttype_in_keycodelist123)
                keycodelisttype3 = self.keycodelisttype()

                self._state.following.pop()
                stream_keycodelisttype.add(keycodelisttype3.tree)
                char_literal4=self.match(self.input, 22, self.FOLLOW_22_in_keycodelist125) 
                stream_22.add(char_literal4)
                # Keycodes.g:36:24: ( keycodeMaterial )+
                cnt2 = 0
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if ((25 <= LA2_0 <= 26) or (28 <= LA2_0 <= 30) or LA2_0 == 32) :
                        alt2 = 1


                    if alt2 == 1:
                        # Keycodes.g:36:24: keycodeMaterial
                        pass 
                        self._state.following.append(self.FOLLOW_keycodeMaterial_in_keycodelist127)
                        keycodeMaterial5 = self.keycodeMaterial()

                        self._state.following.pop()
                        stream_keycodeMaterial.add(keycodeMaterial5.tree)


                    else:
                        if cnt2 >= 1:
                            break #loop2

                        eee = EarlyExitException(2, self.input)
                        raise eee

                    cnt2 += 1


                char_literal6=self.match(self.input, 23, self.FOLLOW_23_in_keycodelist130) 
                stream_23.add(char_literal6)
                char_literal7=self.match(self.input, 24, self.FOLLOW_24_in_keycodelist132) 
                stream_24.add(char_literal7)

                # AST Rewrite
                # elements: keycodelisttype, keycodeMaterial
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
                # 37:2: -> ^( KEYCODELIST keycodelisttype ^( KEYCODEMATERIAL ( keycodeMaterial )+ ) )
                # Keycodes.g:37:5: ^( KEYCODELIST keycodelisttype ^( KEYCODEMATERIAL ( keycodeMaterial )+ ) )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(KEYCODELIST, "KEYCODELIST"), root_1)

                self._adaptor.addChild(root_1, stream_keycodelisttype.nextTree())
                # Keycodes.g:37:35: ^( KEYCODEMATERIAL ( keycodeMaterial )+ )
                root_2 = self._adaptor.nil()
                root_2 = self._adaptor.becomeRoot(self._adaptor.createFromType(KEYCODEMATERIAL, "KEYCODEMATERIAL"), root_2)

                # Keycodes.g:37:53: ( keycodeMaterial )+
                if not (stream_keycodeMaterial.hasNext()):
                    raise RewriteEarlyExitException()

                while stream_keycodeMaterial.hasNext():
                    self._adaptor.addChild(root_2, stream_keycodeMaterial.nextTree())


                stream_keycodeMaterial.reset()

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

    # $ANTLR end "keycodelist"

    class keycodelisttype_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "keycodelisttype"
    # Keycodes.g:40:1: keycodelisttype : ( KEYCODELISTOPTS )+ DQSTRING -> ^( KEYCODELISTTYPE ^( KEYCODELISTOPTIONS ( KEYCODELISTOPTS )+ ) ^( KEYCODELISTNAME DQSTRING ) ) ;
    def keycodelisttype(self, ):

        retval = self.keycodelisttype_return()
        retval.start = self.input.LT(1)

        root_0 = None

        KEYCODELISTOPTS8 = None
        DQSTRING9 = None

        KEYCODELISTOPTS8_tree = None
        DQSTRING9_tree = None
        stream_KEYCODELISTOPTS = RewriteRuleTokenStream(self._adaptor, "token KEYCODELISTOPTS")
        stream_DQSTRING = RewriteRuleTokenStream(self._adaptor, "token DQSTRING")

        try:
            try:
                # Keycodes.g:41:2: ( ( KEYCODELISTOPTS )+ DQSTRING -> ^( KEYCODELISTTYPE ^( KEYCODELISTOPTIONS ( KEYCODELISTOPTS )+ ) ^( KEYCODELISTNAME DQSTRING ) ) )
                # Keycodes.g:41:4: ( KEYCODELISTOPTS )+ DQSTRING
                pass 
                # Keycodes.g:41:4: ( KEYCODELISTOPTS )+
                cnt3 = 0
                while True: #loop3
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if (LA3_0 == KEYCODELISTOPTS) :
                        alt3 = 1


                    if alt3 == 1:
                        # Keycodes.g:41:4: KEYCODELISTOPTS
                        pass 
                        KEYCODELISTOPTS8=self.match(self.input, KEYCODELISTOPTS, self.FOLLOW_KEYCODELISTOPTS_in_keycodelisttype160) 
                        stream_KEYCODELISTOPTS.add(KEYCODELISTOPTS8)


                    else:
                        if cnt3 >= 1:
                            break #loop3

                        eee = EarlyExitException(3, self.input)
                        raise eee

                    cnt3 += 1


                DQSTRING9=self.match(self.input, DQSTRING, self.FOLLOW_DQSTRING_in_keycodelisttype163) 
                stream_DQSTRING.add(DQSTRING9)

                # AST Rewrite
                # elements: DQSTRING, KEYCODELISTOPTS
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
                # 42:2: -> ^( KEYCODELISTTYPE ^( KEYCODELISTOPTIONS ( KEYCODELISTOPTS )+ ) ^( KEYCODELISTNAME DQSTRING ) )
                # Keycodes.g:42:5: ^( KEYCODELISTTYPE ^( KEYCODELISTOPTIONS ( KEYCODELISTOPTS )+ ) ^( KEYCODELISTNAME DQSTRING ) )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(KEYCODELISTTYPE, "KEYCODELISTTYPE"), root_1)

                # Keycodes.g:42:23: ^( KEYCODELISTOPTIONS ( KEYCODELISTOPTS )+ )
                root_2 = self._adaptor.nil()
                root_2 = self._adaptor.becomeRoot(self._adaptor.createFromType(KEYCODELISTOPTIONS, "KEYCODELISTOPTIONS"), root_2)

                # Keycodes.g:42:44: ( KEYCODELISTOPTS )+
                if not (stream_KEYCODELISTOPTS.hasNext()):
                    raise RewriteEarlyExitException()

                while stream_KEYCODELISTOPTS.hasNext():
                    self._adaptor.addChild(root_2, stream_KEYCODELISTOPTS.nextNode())


                stream_KEYCODELISTOPTS.reset()

                self._adaptor.addChild(root_1, root_2)
                # Keycodes.g:42:62: ^( KEYCODELISTNAME DQSTRING )
                root_2 = self._adaptor.nil()
                root_2 = self._adaptor.becomeRoot(self._adaptor.createFromType(KEYCODELISTNAME, "KEYCODELISTNAME"), root_2)

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

    # $ANTLR end "keycodelisttype"

    class keycodeMaterial_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "keycodeMaterial"
    # Keycodes.g:45:1: keycodeMaterial : ( line_include | line_minmax ';' | line_alias ';' | line_keycode ';' | line_indicator ';' );
    def keycodeMaterial(self, ):

        retval = self.keycodeMaterial_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal12 = None
        char_literal14 = None
        char_literal16 = None
        char_literal18 = None
        line_include10 = None

        line_minmax11 = None

        line_alias13 = None

        line_keycode15 = None

        line_indicator17 = None


        char_literal12_tree = None
        char_literal14_tree = None
        char_literal16_tree = None
        char_literal18_tree = None

        try:
            try:
                # Keycodes.g:46:2: ( line_include | line_minmax ';' | line_alias ';' | line_keycode ';' | line_indicator ';' )
                alt4 = 5
                LA4 = self.input.LA(1)
                if LA4 == 25:
                    alt4 = 1
                elif LA4 == 26 or LA4 == 28:
                    alt4 = 2
                elif LA4 == 29:
                    alt4 = 3
                elif LA4 == 30:
                    alt4 = 4
                elif LA4 == 32:
                    alt4 = 5
                else:
                    nvae = NoViableAltException("", 4, 0, self.input)

                    raise nvae

                if alt4 == 1:
                    # Keycodes.g:46:4: line_include
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_line_include_in_keycodeMaterial195)
                    line_include10 = self.line_include()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, line_include10.tree)


                elif alt4 == 2:
                    # Keycodes.g:47:4: line_minmax ';'
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_line_minmax_in_keycodeMaterial201)
                    line_minmax11 = self.line_minmax()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, line_minmax11.tree)
                    char_literal12=self.match(self.input, 24, self.FOLLOW_24_in_keycodeMaterial203)


                elif alt4 == 3:
                    # Keycodes.g:48:4: line_alias ';'
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_line_alias_in_keycodeMaterial209)
                    line_alias13 = self.line_alias()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, line_alias13.tree)
                    char_literal14=self.match(self.input, 24, self.FOLLOW_24_in_keycodeMaterial211)


                elif alt4 == 4:
                    # Keycodes.g:49:4: line_keycode ';'
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_line_keycode_in_keycodeMaterial217)
                    line_keycode15 = self.line_keycode()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, line_keycode15.tree)
                    char_literal16=self.match(self.input, 24, self.FOLLOW_24_in_keycodeMaterial219)


                elif alt4 == 5:
                    # Keycodes.g:50:4: line_indicator ';'
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_line_indicator_in_keycodeMaterial225)
                    line_indicator17 = self.line_indicator()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, line_indicator17.tree)
                    char_literal18=self.match(self.input, 24, self.FOLLOW_24_in_keycodeMaterial227)


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

    # $ANTLR end "keycodeMaterial"

    class line_include_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "line_include"
    # Keycodes.g:53:1: line_include : 'include' DQSTRING -> ^( INCLUDE DQSTRING ) ;
    def line_include(self, ):

        retval = self.line_include_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal19 = None
        DQSTRING20 = None

        string_literal19_tree = None
        DQSTRING20_tree = None
        stream_25 = RewriteRuleTokenStream(self._adaptor, "token 25")
        stream_DQSTRING = RewriteRuleTokenStream(self._adaptor, "token DQSTRING")

        try:
            try:
                # Keycodes.g:54:2: ( 'include' DQSTRING -> ^( INCLUDE DQSTRING ) )
                # Keycodes.g:54:4: 'include' DQSTRING
                pass 
                string_literal19=self.match(self.input, 25, self.FOLLOW_25_in_line_include239) 
                stream_25.add(string_literal19)
                DQSTRING20=self.match(self.input, DQSTRING, self.FOLLOW_DQSTRING_in_line_include241) 
                stream_DQSTRING.add(DQSTRING20)

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
                # 55:2: -> ^( INCLUDE DQSTRING )
                # Keycodes.g:55:5: ^( INCLUDE DQSTRING )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(INCLUDE, "INCLUDE"), root_1)

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

    class line_minmax_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "line_minmax"
    # Keycodes.g:58:1: line_minmax : ( 'minimum' '=' NAME -> ^( MINIMUM NAME ) | 'maximum' '=' NAME -> ^( MAXIMUM NAME ) );
    def line_minmax(self, ):

        retval = self.line_minmax_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal21 = None
        char_literal22 = None
        NAME23 = None
        string_literal24 = None
        char_literal25 = None
        NAME26 = None

        string_literal21_tree = None
        char_literal22_tree = None
        NAME23_tree = None
        string_literal24_tree = None
        char_literal25_tree = None
        NAME26_tree = None
        stream_26 = RewriteRuleTokenStream(self._adaptor, "token 26")
        stream_27 = RewriteRuleTokenStream(self._adaptor, "token 27")
        stream_28 = RewriteRuleTokenStream(self._adaptor, "token 28")
        stream_NAME = RewriteRuleTokenStream(self._adaptor, "token NAME")

        try:
            try:
                # Keycodes.g:59:2: ( 'minimum' '=' NAME -> ^( MINIMUM NAME ) | 'maximum' '=' NAME -> ^( MAXIMUM NAME ) )
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if (LA5_0 == 26) :
                    alt5 = 1
                elif (LA5_0 == 28) :
                    alt5 = 2
                else:
                    nvae = NoViableAltException("", 5, 0, self.input)

                    raise nvae

                if alt5 == 1:
                    # Keycodes.g:59:4: 'minimum' '=' NAME
                    pass 
                    string_literal21=self.match(self.input, 26, self.FOLLOW_26_in_line_minmax261) 
                    stream_26.add(string_literal21)
                    char_literal22=self.match(self.input, 27, self.FOLLOW_27_in_line_minmax263) 
                    stream_27.add(char_literal22)
                    NAME23=self.match(self.input, NAME, self.FOLLOW_NAME_in_line_minmax265) 
                    stream_NAME.add(NAME23)

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
                    # 59:23: -> ^( MINIMUM NAME )
                    # Keycodes.g:59:26: ^( MINIMUM NAME )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(MINIMUM, "MINIMUM"), root_1)

                    self._adaptor.addChild(root_1, stream_NAME.nextNode())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt5 == 2:
                    # Keycodes.g:60:4: 'maximum' '=' NAME
                    pass 
                    string_literal24=self.match(self.input, 28, self.FOLLOW_28_in_line_minmax278) 
                    stream_28.add(string_literal24)
                    char_literal25=self.match(self.input, 27, self.FOLLOW_27_in_line_minmax280) 
                    stream_27.add(char_literal25)
                    NAME26=self.match(self.input, NAME, self.FOLLOW_NAME_in_line_minmax282) 
                    stream_NAME.add(NAME26)

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
                    # 60:23: -> ^( MAXIMUM NAME )
                    # Keycodes.g:60:26: ^( MAXIMUM NAME )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(MAXIMUM, "MAXIMUM"), root_1)

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

    # $ANTLR end "line_minmax"

    class line_alias_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "line_alias"
    # Keycodes.g:63:1: line_alias : 'alias' '<' val+= NAME '>' '=' '<' val+= NAME '>' -> ^( ALIAS ( $val)+ ) ;
    def line_alias(self, ):

        retval = self.line_alias_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal27 = None
        char_literal28 = None
        char_literal29 = None
        char_literal30 = None
        char_literal31 = None
        char_literal32 = None
        val = None
        list_val = None

        string_literal27_tree = None
        char_literal28_tree = None
        char_literal29_tree = None
        char_literal30_tree = None
        char_literal31_tree = None
        char_literal32_tree = None
        val_tree = None
        stream_27 = RewriteRuleTokenStream(self._adaptor, "token 27")
        stream_29 = RewriteRuleTokenStream(self._adaptor, "token 29")
        stream_30 = RewriteRuleTokenStream(self._adaptor, "token 30")
        stream_31 = RewriteRuleTokenStream(self._adaptor, "token 31")
        stream_NAME = RewriteRuleTokenStream(self._adaptor, "token NAME")

        try:
            try:
                # Keycodes.g:64:2: ( 'alias' '<' val+= NAME '>' '=' '<' val+= NAME '>' -> ^( ALIAS ( $val)+ ) )
                # Keycodes.g:64:4: 'alias' '<' val+= NAME '>' '=' '<' val+= NAME '>'
                pass 
                string_literal27=self.match(self.input, 29, self.FOLLOW_29_in_line_alias301) 
                stream_29.add(string_literal27)
                char_literal28=self.match(self.input, 30, self.FOLLOW_30_in_line_alias303) 
                stream_30.add(char_literal28)
                val=self.match(self.input, NAME, self.FOLLOW_NAME_in_line_alias307) 
                stream_NAME.add(val)
                if list_val is None:
                    list_val = []
                list_val.append(val)

                char_literal29=self.match(self.input, 31, self.FOLLOW_31_in_line_alias309) 
                stream_31.add(char_literal29)
                char_literal30=self.match(self.input, 27, self.FOLLOW_27_in_line_alias311) 
                stream_27.add(char_literal30)
                char_literal31=self.match(self.input, 30, self.FOLLOW_30_in_line_alias313) 
                stream_30.add(char_literal31)
                val=self.match(self.input, NAME, self.FOLLOW_NAME_in_line_alias317) 
                stream_NAME.add(val)
                if list_val is None:
                    list_val = []
                list_val.append(val)

                char_literal32=self.match(self.input, 31, self.FOLLOW_31_in_line_alias319) 
                stream_31.add(char_literal32)

                # AST Rewrite
                # elements: val
                # token labels: 
                # rule labels: retval
                # token list labels: val
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0
                stream_val = RewriteRuleTokenStream(self._adaptor, "token val", list_val)

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 65:2: -> ^( ALIAS ( $val)+ )
                # Keycodes.g:65:5: ^( ALIAS ( $val)+ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(ALIAS, "ALIAS"), root_1)

                # Keycodes.g:65:13: ( $val)+
                if not (stream_val.hasNext()):
                    raise RewriteEarlyExitException()

                while stream_val.hasNext():
                    self._adaptor.addChild(root_1, stream_val.nextNode())


                stream_val.reset()

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

    # $ANTLR end "line_alias"

    class line_keycode_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "line_keycode"
    # Keycodes.g:68:1: line_keycode : '<' val+= NAME '>' '=' val+= NAME -> ^( KEYCODE ( NAME )+ ) ;
    def line_keycode(self, ):

        retval = self.line_keycode_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal33 = None
        char_literal34 = None
        char_literal35 = None
        val = None
        list_val = None

        char_literal33_tree = None
        char_literal34_tree = None
        char_literal35_tree = None
        val_tree = None
        stream_27 = RewriteRuleTokenStream(self._adaptor, "token 27")
        stream_30 = RewriteRuleTokenStream(self._adaptor, "token 30")
        stream_31 = RewriteRuleTokenStream(self._adaptor, "token 31")
        stream_NAME = RewriteRuleTokenStream(self._adaptor, "token NAME")

        try:
            try:
                # Keycodes.g:69:2: ( '<' val+= NAME '>' '=' val+= NAME -> ^( KEYCODE ( NAME )+ ) )
                # Keycodes.g:69:4: '<' val+= NAME '>' '=' val+= NAME
                pass 
                char_literal33=self.match(self.input, 30, self.FOLLOW_30_in_line_keycode341) 
                stream_30.add(char_literal33)
                val=self.match(self.input, NAME, self.FOLLOW_NAME_in_line_keycode345) 
                stream_NAME.add(val)
                if list_val is None:
                    list_val = []
                list_val.append(val)

                char_literal34=self.match(self.input, 31, self.FOLLOW_31_in_line_keycode347) 
                stream_31.add(char_literal34)
                char_literal35=self.match(self.input, 27, self.FOLLOW_27_in_line_keycode349) 
                stream_27.add(char_literal35)
                val=self.match(self.input, NAME, self.FOLLOW_NAME_in_line_keycode353) 
                stream_NAME.add(val)
                if list_val is None:
                    list_val = []
                list_val.append(val)


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
                # 70:2: -> ^( KEYCODE ( NAME )+ )
                # Keycodes.g:70:5: ^( KEYCODE ( NAME )+ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(KEYCODE, "KEYCODE"), root_1)

                # Keycodes.g:70:15: ( NAME )+
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

    # $ANTLR end "line_keycode"

    class line_indicator_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "line_indicator"
    # Keycodes.g:73:1: line_indicator : 'indicator' NAME '=' DQSTRING -> ^( INDICATOR NAME DQSTRING ) ;
    def line_indicator(self, ):

        retval = self.line_indicator_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal36 = None
        NAME37 = None
        char_literal38 = None
        DQSTRING39 = None

        string_literal36_tree = None
        NAME37_tree = None
        char_literal38_tree = None
        DQSTRING39_tree = None
        stream_27 = RewriteRuleTokenStream(self._adaptor, "token 27")
        stream_DQSTRING = RewriteRuleTokenStream(self._adaptor, "token DQSTRING")
        stream_32 = RewriteRuleTokenStream(self._adaptor, "token 32")
        stream_NAME = RewriteRuleTokenStream(self._adaptor, "token NAME")

        try:
            try:
                # Keycodes.g:74:2: ( 'indicator' NAME '=' DQSTRING -> ^( INDICATOR NAME DQSTRING ) )
                # Keycodes.g:74:4: 'indicator' NAME '=' DQSTRING
                pass 
                string_literal36=self.match(self.input, 32, self.FOLLOW_32_in_line_indicator374) 
                stream_32.add(string_literal36)
                NAME37=self.match(self.input, NAME, self.FOLLOW_NAME_in_line_indicator376) 
                stream_NAME.add(NAME37)
                char_literal38=self.match(self.input, 27, self.FOLLOW_27_in_line_indicator378) 
                stream_27.add(char_literal38)
                DQSTRING39=self.match(self.input, DQSTRING, self.FOLLOW_DQSTRING_in_line_indicator380) 
                stream_DQSTRING.add(DQSTRING39)

                # AST Rewrite
                # elements: DQSTRING, NAME
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
                # 75:2: -> ^( INDICATOR NAME DQSTRING )
                # Keycodes.g:75:5: ^( INDICATOR NAME DQSTRING )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(INDICATOR, "INDICATOR"), root_1)

                self._adaptor.addChild(root_1, stream_NAME.nextNode())
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

    # $ANTLR end "line_indicator"


    # Delegated rules


 

    FOLLOW_keycodelist_in_keycodedoc97 = frozenset([8])
    FOLLOW_EOF_in_keycodedoc100 = frozenset([1])
    FOLLOW_keycodelisttype_in_keycodelist123 = frozenset([22])
    FOLLOW_22_in_keycodelist125 = frozenset([25, 26, 28, 29, 30, 32])
    FOLLOW_keycodeMaterial_in_keycodelist127 = frozenset([23, 25, 26, 28, 29, 30, 32])
    FOLLOW_23_in_keycodelist130 = frozenset([24])
    FOLLOW_24_in_keycodelist132 = frozenset([1])
    FOLLOW_KEYCODELISTOPTS_in_keycodelisttype160 = frozenset([8, 17])
    FOLLOW_DQSTRING_in_keycodelisttype163 = frozenset([1])
    FOLLOW_line_include_in_keycodeMaterial195 = frozenset([1])
    FOLLOW_line_minmax_in_keycodeMaterial201 = frozenset([24])
    FOLLOW_24_in_keycodeMaterial203 = frozenset([1])
    FOLLOW_line_alias_in_keycodeMaterial209 = frozenset([24])
    FOLLOW_24_in_keycodeMaterial211 = frozenset([1])
    FOLLOW_line_keycode_in_keycodeMaterial217 = frozenset([24])
    FOLLOW_24_in_keycodeMaterial219 = frozenset([1])
    FOLLOW_line_indicator_in_keycodeMaterial225 = frozenset([24])
    FOLLOW_24_in_keycodeMaterial227 = frozenset([1])
    FOLLOW_25_in_line_include239 = frozenset([17])
    FOLLOW_DQSTRING_in_line_include241 = frozenset([1])
    FOLLOW_26_in_line_minmax261 = frozenset([27])
    FOLLOW_27_in_line_minmax263 = frozenset([18])
    FOLLOW_NAME_in_line_minmax265 = frozenset([1])
    FOLLOW_28_in_line_minmax278 = frozenset([27])
    FOLLOW_27_in_line_minmax280 = frozenset([18])
    FOLLOW_NAME_in_line_minmax282 = frozenset([1])
    FOLLOW_29_in_line_alias301 = frozenset([30])
    FOLLOW_30_in_line_alias303 = frozenset([18])
    FOLLOW_NAME_in_line_alias307 = frozenset([31])
    FOLLOW_31_in_line_alias309 = frozenset([27])
    FOLLOW_27_in_line_alias311 = frozenset([30])
    FOLLOW_30_in_line_alias313 = frozenset([18])
    FOLLOW_NAME_in_line_alias317 = frozenset([31])
    FOLLOW_31_in_line_alias319 = frozenset([1])
    FOLLOW_30_in_line_keycode341 = frozenset([18])
    FOLLOW_NAME_in_line_keycode345 = frozenset([31])
    FOLLOW_31_in_line_keycode347 = frozenset([27])
    FOLLOW_27_in_line_keycode349 = frozenset([18])
    FOLLOW_NAME_in_line_keycode353 = frozenset([1])
    FOLLOW_32_in_line_indicator374 = frozenset([18])
    FOLLOW_NAME_in_line_indicator376 = frozenset([27])
    FOLLOW_27_in_line_indicator378 = frozenset([17])
    FOLLOW_DQSTRING_in_line_indicator380 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("KeycodesLexer", KeycodesParser)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
