# $ANTLR 3.1.2 XKBGrammarWalker.g 2020-05-10 06:02:53

import sys
from antlr3 import *
from antlr3.tree import *
from antlr3.compat import set, frozenset


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
T__59=59
KEYCODEX=19
T__55=55
T__56=56
T__57=57
KEYCODE=18
T__58=58
T__51=51
T__53=53
T__54=54
T__60=60
T__61=61
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
ELEM_OVERLAY=52
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
    "'virtual_modifiers'", "'type'", "'symbols'", "'virtualMods'", "ELEM_OVERLAY", 
    "'default'", "'hidden'", "'partial'", "'alphanumeric_keys'", "'keypad_keys'", 
    "'function_keys'", "'modifier_keys'", "'alternate_group'", "'xkb_symbols'"
]




class XKBGrammarWalker(TreeParser):
    grammarFileName = "XKBGrammarWalker.g"
    antlr_version = version_str_to_tuple("3.1.2")
    antlr_version_str = "3.1.2"
    tokenNames = tokenNames

    def __init__(self, input, state=None):
        if state is None:
            state = RecognizerSharedState()

        TreeParser.__init__(self, input, state)







                


        



    # $ANTLR start "layout"
    # XKBGrammarWalker.g:14:1: layout : ^( LAYOUT ( symbols )+ ) ;
    def layout(self, ):

        try:
            try:
                # XKBGrammarWalker.g:15:3: ( ^( LAYOUT ( symbols )+ ) )
                # XKBGrammarWalker.g:15:5: ^( LAYOUT ( symbols )+ )
                pass 
                self.match(self.input, LAYOUT, self.FOLLOW_LAYOUT_in_layout73)

                self.match(self.input, DOWN, None)
                # XKBGrammarWalker.g:15:14: ( symbols )+
                cnt1 = 0
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 == SYMBOLS) :
                        alt1 = 1


                    if alt1 == 1:
                        # XKBGrammarWalker.g:15:14: symbols
                        pass 
                        self._state.following.append(self.FOLLOW_symbols_in_layout75)
                        self.symbols()

                        self._state.following.pop()


                    else:
                        if cnt1 >= 1:
                            break #loop1

                        eee = EarlyExitException(1, self.input)
                        raise eee

                    cnt1 += 1



                self.match(self.input, UP, None)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "layout"


    # $ANTLR start "symbols"
    # XKBGrammarWalker.g:18:1: symbols : ^( SYMBOLS mapType ^( MAPMATERIAL ( mapMaterial )+ ) ) ;
    def symbols(self, ):

        try:
            try:
                # XKBGrammarWalker.g:19:3: ( ^( SYMBOLS mapType ^( MAPMATERIAL ( mapMaterial )+ ) ) )
                # XKBGrammarWalker.g:19:5: ^( SYMBOLS mapType ^( MAPMATERIAL ( mapMaterial )+ ) )
                pass 
                self.match(self.input, SYMBOLS, self.FOLLOW_SYMBOLS_in_symbols94)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_mapType_in_symbols96)
                self.mapType()

                self._state.following.pop()
                self.match(self.input, MAPMATERIAL, self.FOLLOW_MAPMATERIAL_in_symbols99)

                self.match(self.input, DOWN, None)
                # XKBGrammarWalker.g:19:37: ( mapMaterial )+
                cnt2 = 0
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if ((TOKEN_INCLUDE <= LA2_0 <= TOKEN_KEY) or LA2_0 == TOKEN_MODIFIER_MAP or LA2_0 == TOKEN_VIRTUAL_MODIFIERS) :
                        alt2 = 1


                    if alt2 == 1:
                        # XKBGrammarWalker.g:19:37: mapMaterial
                        pass 
                        self._state.following.append(self.FOLLOW_mapMaterial_in_symbols101)
                        self.mapMaterial()

                        self._state.following.pop()


                    else:
                        if cnt2 >= 1:
                            break #loop2

                        eee = EarlyExitException(2, self.input)
                        raise eee

                    cnt2 += 1



                self.match(self.input, UP, None)

                self.match(self.input, UP, None)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "symbols"


    # $ANTLR start "mapType"
    # XKBGrammarWalker.g:22:1: mapType : ^( MAPTYPE ^( MAPOPTIONS ( MAPOPTS )+ ) ^( MAPNAME DQSTRING ) ) ;
    def mapType(self, ):

        try:
            try:
                # XKBGrammarWalker.g:23:3: ( ^( MAPTYPE ^( MAPOPTIONS ( MAPOPTS )+ ) ^( MAPNAME DQSTRING ) ) )
                # XKBGrammarWalker.g:23:5: ^( MAPTYPE ^( MAPOPTIONS ( MAPOPTS )+ ) ^( MAPNAME DQSTRING ) )
                pass 
                self.match(self.input, MAPTYPE, self.FOLLOW_MAPTYPE_in_mapType118)

                self.match(self.input, DOWN, None)
                self.match(self.input, MAPOPTIONS, self.FOLLOW_MAPOPTIONS_in_mapType121)

                self.match(self.input, DOWN, None)
                # XKBGrammarWalker.g:23:28: ( MAPOPTS )+
                cnt3 = 0
                while True: #loop3
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if (LA3_0 == MAPOPTS) :
                        alt3 = 1


                    if alt3 == 1:
                        # XKBGrammarWalker.g:23:28: MAPOPTS
                        pass 
                        self.match(self.input, MAPOPTS, self.FOLLOW_MAPOPTS_in_mapType123)


                    else:
                        if cnt3 >= 1:
                            break #loop3

                        eee = EarlyExitException(3, self.input)
                        raise eee

                    cnt3 += 1



                self.match(self.input, UP, None)
                self.match(self.input, MAPNAME, self.FOLLOW_MAPNAME_in_mapType128)

                self.match(self.input, DOWN, None)
                self.match(self.input, DQSTRING, self.FOLLOW_DQSTRING_in_mapType130)

                self.match(self.input, UP, None)

                self.match(self.input, UP, None)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "mapType"


    # $ANTLR start "mapMaterial"
    # XKBGrammarWalker.g:26:1: mapMaterial : ( ^( TOKEN_INCLUDE DQSTRING ) | ^( TOKEN_NAME DQSTRING ) | ^( TOKEN_KEY_TYPE ( NAME )? ^( VALUE DQSTRING ) ) | ^( TOKEN_KEY ( OVERRIDE )? ^( KEYCODEX NAME ) ( keyelements )+ ) | ^( TOKEN_MODIFIER_MAP STATE ( keycode )+ ) | ^( TOKEN_VIRTUAL_MODIFIERS ( NAME )+ ) );
    def mapMaterial(self, ):

        try:
            try:
                # XKBGrammarWalker.g:27:3: ( ^( TOKEN_INCLUDE DQSTRING ) | ^( TOKEN_NAME DQSTRING ) | ^( TOKEN_KEY_TYPE ( NAME )? ^( VALUE DQSTRING ) ) | ^( TOKEN_KEY ( OVERRIDE )? ^( KEYCODEX NAME ) ( keyelements )+ ) | ^( TOKEN_MODIFIER_MAP STATE ( keycode )+ ) | ^( TOKEN_VIRTUAL_MODIFIERS ( NAME )+ ) )
                alt9 = 6
                LA9 = self.input.LA(1)
                if LA9 == TOKEN_INCLUDE:
                    alt9 = 1
                elif LA9 == TOKEN_NAME:
                    alt9 = 2
                elif LA9 == TOKEN_KEY_TYPE:
                    alt9 = 3
                elif LA9 == TOKEN_KEY:
                    alt9 = 4
                elif LA9 == TOKEN_MODIFIER_MAP:
                    alt9 = 5
                elif LA9 == TOKEN_VIRTUAL_MODIFIERS:
                    alt9 = 6
                else:
                    nvae = NoViableAltException("", 9, 0, self.input)

                    raise nvae

                if alt9 == 1:
                    # XKBGrammarWalker.g:27:5: ^( TOKEN_INCLUDE DQSTRING )
                    pass 
                    self.match(self.input, TOKEN_INCLUDE, self.FOLLOW_TOKEN_INCLUDE_in_mapMaterial147)

                    self.match(self.input, DOWN, None)
                    self.match(self.input, DQSTRING, self.FOLLOW_DQSTRING_in_mapMaterial149)

                    self.match(self.input, UP, None)


                elif alt9 == 2:
                    # XKBGrammarWalker.g:28:5: ^( TOKEN_NAME DQSTRING )
                    pass 
                    self.match(self.input, TOKEN_NAME, self.FOLLOW_TOKEN_NAME_in_mapMaterial157)

                    self.match(self.input, DOWN, None)
                    self.match(self.input, DQSTRING, self.FOLLOW_DQSTRING_in_mapMaterial159)

                    self.match(self.input, UP, None)


                elif alt9 == 3:
                    # XKBGrammarWalker.g:29:5: ^( TOKEN_KEY_TYPE ( NAME )? ^( VALUE DQSTRING ) )
                    pass 
                    self.match(self.input, TOKEN_KEY_TYPE, self.FOLLOW_TOKEN_KEY_TYPE_in_mapMaterial167)

                    self.match(self.input, DOWN, None)
                    # XKBGrammarWalker.g:29:22: ( NAME )?
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if (LA4_0 == NAME) :
                        alt4 = 1
                    if alt4 == 1:
                        # XKBGrammarWalker.g:29:22: NAME
                        pass 
                        self.match(self.input, NAME, self.FOLLOW_NAME_in_mapMaterial169)



                    self.match(self.input, VALUE, self.FOLLOW_VALUE_in_mapMaterial173)

                    self.match(self.input, DOWN, None)
                    self.match(self.input, DQSTRING, self.FOLLOW_DQSTRING_in_mapMaterial175)

                    self.match(self.input, UP, None)

                    self.match(self.input, UP, None)


                elif alt9 == 4:
                    # XKBGrammarWalker.g:30:5: ^( TOKEN_KEY ( OVERRIDE )? ^( KEYCODEX NAME ) ( keyelements )+ )
                    pass 
                    self.match(self.input, TOKEN_KEY, self.FOLLOW_TOKEN_KEY_in_mapMaterial184)

                    self.match(self.input, DOWN, None)
                    # XKBGrammarWalker.g:30:17: ( OVERRIDE )?
                    alt5 = 2
                    LA5_0 = self.input.LA(1)

                    if (LA5_0 == OVERRIDE) :
                        alt5 = 1
                    if alt5 == 1:
                        # XKBGrammarWalker.g:30:17: OVERRIDE
                        pass 
                        self.match(self.input, OVERRIDE, self.FOLLOW_OVERRIDE_in_mapMaterial186)



                    self.match(self.input, KEYCODEX, self.FOLLOW_KEYCODEX_in_mapMaterial190)

                    self.match(self.input, DOWN, None)
                    self.match(self.input, NAME, self.FOLLOW_NAME_in_mapMaterial192)

                    self.match(self.input, UP, None)
                    # XKBGrammarWalker.g:30:44: ( keyelements )+
                    cnt6 = 0
                    while True: #loop6
                        alt6 = 2
                        LA6_0 = self.input.LA(1)

                        if ((ELEM_KEYSYMGROUP <= LA6_0 <= ELEM_VIRTUALMODS) or LA6_0 == ELEM_OVERLAY) :
                            alt6 = 1


                        if alt6 == 1:
                            # XKBGrammarWalker.g:30:44: keyelements
                            pass 
                            self._state.following.append(self.FOLLOW_keyelements_in_mapMaterial195)
                            self.keyelements()

                            self._state.following.pop()


                        else:
                            if cnt6 >= 1:
                                break #loop6

                            eee = EarlyExitException(6, self.input)
                            raise eee

                        cnt6 += 1



                    self.match(self.input, UP, None)


                elif alt9 == 5:
                    # XKBGrammarWalker.g:31:5: ^( TOKEN_MODIFIER_MAP STATE ( keycode )+ )
                    pass 
                    self.match(self.input, TOKEN_MODIFIER_MAP, self.FOLLOW_TOKEN_MODIFIER_MAP_in_mapMaterial204)

                    self.match(self.input, DOWN, None)
                    self.match(self.input, STATE, self.FOLLOW_STATE_in_mapMaterial206)
                    # XKBGrammarWalker.g:31:32: ( keycode )+
                    cnt7 = 0
                    while True: #loop7
                        alt7 = 2
                        LA7_0 = self.input.LA(1)

                        if ((KEYCODE <= LA7_0 <= KEYCODEX)) :
                            alt7 = 1


                        if alt7 == 1:
                            # XKBGrammarWalker.g:31:32: keycode
                            pass 
                            self._state.following.append(self.FOLLOW_keycode_in_mapMaterial208)
                            self.keycode()

                            self._state.following.pop()


                        else:
                            if cnt7 >= 1:
                                break #loop7

                            eee = EarlyExitException(7, self.input)
                            raise eee

                        cnt7 += 1



                    self.match(self.input, UP, None)


                elif alt9 == 6:
                    # XKBGrammarWalker.g:32:5: ^( TOKEN_VIRTUAL_MODIFIERS ( NAME )+ )
                    pass 
                    self.match(self.input, TOKEN_VIRTUAL_MODIFIERS, self.FOLLOW_TOKEN_VIRTUAL_MODIFIERS_in_mapMaterial217)

                    self.match(self.input, DOWN, None)
                    # XKBGrammarWalker.g:32:31: ( NAME )+
                    cnt8 = 0
                    while True: #loop8
                        alt8 = 2
                        LA8_0 = self.input.LA(1)

                        if (LA8_0 == NAME) :
                            alt8 = 1


                        if alt8 == 1:
                            # XKBGrammarWalker.g:32:31: NAME
                            pass 
                            self.match(self.input, NAME, self.FOLLOW_NAME_in_mapMaterial219)


                        else:
                            if cnt8 >= 1:
                                break #loop8

                            eee = EarlyExitException(8, self.input)
                            raise eee

                        cnt8 += 1



                    self.match(self.input, UP, None)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "mapMaterial"


    # $ANTLR start "keycode"
    # XKBGrammarWalker.g:35:1: keycode : ( ^( KEYCODE NAME ) | ^( KEYCODEX NAME ) );
    def keycode(self, ):

        try:
            try:
                # XKBGrammarWalker.g:36:3: ( ^( KEYCODE NAME ) | ^( KEYCODEX NAME ) )
                alt10 = 2
                LA10_0 = self.input.LA(1)

                if (LA10_0 == KEYCODE) :
                    alt10 = 1
                elif (LA10_0 == KEYCODEX) :
                    alt10 = 2
                else:
                    nvae = NoViableAltException("", 10, 0, self.input)

                    raise nvae

                if alt10 == 1:
                    # XKBGrammarWalker.g:36:5: ^( KEYCODE NAME )
                    pass 
                    self.match(self.input, KEYCODE, self.FOLLOW_KEYCODE_in_keycode236)

                    self.match(self.input, DOWN, None)
                    self.match(self.input, NAME, self.FOLLOW_NAME_in_keycode238)

                    self.match(self.input, UP, None)


                elif alt10 == 2:
                    # XKBGrammarWalker.g:37:5: ^( KEYCODEX NAME )
                    pass 
                    self.match(self.input, KEYCODEX, self.FOLLOW_KEYCODEX_in_keycode246)

                    self.match(self.input, DOWN, None)
                    self.match(self.input, NAME, self.FOLLOW_NAME_in_keycode248)

                    self.match(self.input, UP, None)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "keycode"


    # $ANTLR start "keyelements"
    # XKBGrammarWalker.g:40:1: keyelements : ( ^( ELEM_KEYSYMS DQSTRING ) | ^( ELEM_KEYSYMGROUP ^( VALUE ( NAME )+ ) ) | ^( ELEM_VIRTUALMODS NAME ) | ^( ELEM_OVERLAY NAME keycode ) );
    def keyelements(self, ):

        try:
            try:
                # XKBGrammarWalker.g:41:3: ( ^( ELEM_KEYSYMS DQSTRING ) | ^( ELEM_KEYSYMGROUP ^( VALUE ( NAME )+ ) ) | ^( ELEM_VIRTUALMODS NAME ) | ^( ELEM_OVERLAY NAME keycode ) )
                alt12 = 4
                LA12 = self.input.LA(1)
                if LA12 == ELEM_KEYSYMS:
                    alt12 = 1
                elif LA12 == ELEM_KEYSYMGROUP:
                    alt12 = 2
                elif LA12 == ELEM_VIRTUALMODS:
                    alt12 = 3
                elif LA12 == ELEM_OVERLAY:
                    alt12 = 4
                else:
                    nvae = NoViableAltException("", 12, 0, self.input)

                    raise nvae

                if alt12 == 1:
                    # XKBGrammarWalker.g:41:5: ^( ELEM_KEYSYMS DQSTRING )
                    pass 
                    self.match(self.input, ELEM_KEYSYMS, self.FOLLOW_ELEM_KEYSYMS_in_keyelements263)

                    self.match(self.input, DOWN, None)
                    self.match(self.input, DQSTRING, self.FOLLOW_DQSTRING_in_keyelements265)

                    self.match(self.input, UP, None)


                elif alt12 == 2:
                    # XKBGrammarWalker.g:42:5: ^( ELEM_KEYSYMGROUP ^( VALUE ( NAME )+ ) )
                    pass 
                    self.match(self.input, ELEM_KEYSYMGROUP, self.FOLLOW_ELEM_KEYSYMGROUP_in_keyelements273)

                    self.match(self.input, DOWN, None)
                    self.match(self.input, VALUE, self.FOLLOW_VALUE_in_keyelements276)

                    self.match(self.input, DOWN, None)
                    # XKBGrammarWalker.g:42:32: ( NAME )+
                    cnt11 = 0
                    while True: #loop11
                        alt11 = 2
                        LA11_0 = self.input.LA(1)

                        if (LA11_0 == NAME) :
                            alt11 = 1


                        if alt11 == 1:
                            # XKBGrammarWalker.g:42:32: NAME
                            pass 
                            self.match(self.input, NAME, self.FOLLOW_NAME_in_keyelements278)


                        else:
                            if cnt11 >= 1:
                                break #loop11

                            eee = EarlyExitException(11, self.input)
                            raise eee

                        cnt11 += 1



                    self.match(self.input, UP, None)

                    self.match(self.input, UP, None)


                elif alt12 == 3:
                    # XKBGrammarWalker.g:43:5: ^( ELEM_VIRTUALMODS NAME )
                    pass 
                    self.match(self.input, ELEM_VIRTUALMODS, self.FOLLOW_ELEM_VIRTUALMODS_in_keyelements288)

                    self.match(self.input, DOWN, None)
                    self.match(self.input, NAME, self.FOLLOW_NAME_in_keyelements290)

                    self.match(self.input, UP, None)


                elif alt12 == 4:
                    # XKBGrammarWalker.g:44:5: ^( ELEM_OVERLAY NAME keycode )
                    pass 
                    self.match(self.input, ELEM_OVERLAY, self.FOLLOW_ELEM_OVERLAY_in_keyelements298)

                    self.match(self.input, DOWN, None)
                    self.match(self.input, NAME, self.FOLLOW_NAME_in_keyelements300)
                    self._state.following.append(self.FOLLOW_keycode_in_keyelements302)
                    self.keycode()

                    self._state.following.pop()

                    self.match(self.input, UP, None)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "keyelements"


    # $ANTLR start "mapopts"
    # XKBGrammarWalker.g:47:1: mapopts : ( 'default' | 'hidden' | 'partial' | 'alphanumeric_keys' | 'keypad_keys' | 'function_keys' | 'modifier_keys' | 'alternate_group' | 'xkb_symbols' );
    def mapopts(self, ):

        try:
            try:
                # XKBGrammarWalker.g:48:9: ( 'default' | 'hidden' | 'partial' | 'alphanumeric_keys' | 'keypad_keys' | 'function_keys' | 'modifier_keys' | 'alternate_group' | 'xkb_symbols' )
                # XKBGrammarWalker.g:
                pass 
                if (53 <= self.input.LA(1) <= 61):
                    self.input.consume()
                    self._state.errorRecovery = False

                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse






            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "mapopts"


    # Delegated rules


 

    FOLLOW_LAYOUT_in_layout73 = frozenset([2])
    FOLLOW_symbols_in_layout75 = frozenset([3, 13])
    FOLLOW_SYMBOLS_in_symbols94 = frozenset([2])
    FOLLOW_mapType_in_symbols96 = frozenset([17])
    FOLLOW_MAPMATERIAL_in_symbols99 = frozenset([2])
    FOLLOW_mapMaterial_in_symbols101 = frozenset([3, 4, 5, 6, 7, 9, 11])
    FOLLOW_MAPTYPE_in_mapType118 = frozenset([2])
    FOLLOW_MAPOPTIONS_in_mapType121 = frozenset([2])
    FOLLOW_MAPOPTS_in_mapType123 = frozenset([3, 28])
    FOLLOW_MAPNAME_in_mapType128 = frozenset([2])
    FOLLOW_DQSTRING_in_mapType130 = frozenset([3])
    FOLLOW_TOKEN_INCLUDE_in_mapMaterial147 = frozenset([2])
    FOLLOW_DQSTRING_in_mapMaterial149 = frozenset([3])
    FOLLOW_TOKEN_NAME_in_mapMaterial157 = frozenset([2])
    FOLLOW_DQSTRING_in_mapMaterial159 = frozenset([3])
    FOLLOW_TOKEN_KEY_TYPE_in_mapMaterial167 = frozenset([2])
    FOLLOW_NAME_in_mapMaterial169 = frozenset([20])
    FOLLOW_VALUE_in_mapMaterial173 = frozenset([2])
    FOLLOW_DQSTRING_in_mapMaterial175 = frozenset([3])
    FOLLOW_TOKEN_KEY_in_mapMaterial184 = frozenset([2])
    FOLLOW_OVERRIDE_in_mapMaterial186 = frozenset([19])
    FOLLOW_KEYCODEX_in_mapMaterial190 = frozenset([2])
    FOLLOW_NAME_in_mapMaterial192 = frozenset([3])
    FOLLOW_keyelements_in_mapMaterial195 = frozenset([3, 22, 23, 24, 52])
    FOLLOW_TOKEN_MODIFIER_MAP_in_mapMaterial204 = frozenset([2])
    FOLLOW_STATE_in_mapMaterial206 = frozenset([18, 19])
    FOLLOW_keycode_in_mapMaterial208 = frozenset([3, 18, 19])
    FOLLOW_TOKEN_VIRTUAL_MODIFIERS_in_mapMaterial217 = frozenset([2])
    FOLLOW_NAME_in_mapMaterial219 = frozenset([3, 30])
    FOLLOW_KEYCODE_in_keycode236 = frozenset([2])
    FOLLOW_NAME_in_keycode238 = frozenset([3])
    FOLLOW_KEYCODEX_in_keycode246 = frozenset([2])
    FOLLOW_NAME_in_keycode248 = frozenset([3])
    FOLLOW_ELEM_KEYSYMS_in_keyelements263 = frozenset([2])
    FOLLOW_DQSTRING_in_keyelements265 = frozenset([3])
    FOLLOW_ELEM_KEYSYMGROUP_in_keyelements273 = frozenset([2])
    FOLLOW_VALUE_in_keyelements276 = frozenset([2])
    FOLLOW_NAME_in_keyelements278 = frozenset([3, 30])
    FOLLOW_ELEM_VIRTUALMODS_in_keyelements288 = frozenset([2])
    FOLLOW_NAME_in_keyelements290 = frozenset([3])
    FOLLOW_ELEM_OVERLAY_in_keyelements298 = frozenset([2])
    FOLLOW_NAME_in_keyelements300 = frozenset([18, 19])
    FOLLOW_keycode_in_keyelements302 = frozenset([3])
    FOLLOW_set_in_mapopts0 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import WalkerMain
    main = WalkerMain(XKBGrammarWalker)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
