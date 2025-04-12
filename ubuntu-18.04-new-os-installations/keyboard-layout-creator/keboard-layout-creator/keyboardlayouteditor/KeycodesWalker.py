# $ANTLR 3.1.2 KeycodesWalker.g 2020-05-10 06:02:52

import sys
from antlr3 import *
from antlr3.tree import *
from antlr3.compat import set, frozenset


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




class KeycodesWalker(TreeParser):
    grammarFileName = "KeycodesWalker.g"
    antlr_version = version_str_to_tuple("3.1.2")
    antlr_version_str = "3.1.2"
    tokenNames = tokenNames

    def __init__(self, input, state=None):
        if state is None:
            state = RecognizerSharedState()

        TreeParser.__init__(self, input, state)







                


        



    # $ANTLR start "keycodedoc"
    # KeycodesWalker.g:15:1: keycodedoc : ^( KEYCODEDOC ( keycodelist )+ ) ;
    def keycodedoc(self, ):

        try:
            try:
                # KeycodesWalker.g:16:2: ( ^( KEYCODEDOC ( keycodelist )+ ) )
                # KeycodesWalker.g:16:4: ^( KEYCODEDOC ( keycodelist )+ )
                pass 
                self.match(self.input, KEYCODEDOC, self.FOLLOW_KEYCODEDOC_in_keycodedoc72)

                self.match(self.input, DOWN, None)
                # KeycodesWalker.g:16:17: ( keycodelist )+
                cnt1 = 0
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 == KEYCODELIST) :
                        alt1 = 1


                    if alt1 == 1:
                        # KeycodesWalker.g:16:17: keycodelist
                        pass 
                        self._state.following.append(self.FOLLOW_keycodelist_in_keycodedoc74)
                        self.keycodelist()

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

    # $ANTLR end "keycodedoc"


    # $ANTLR start "keycodelist"
    # KeycodesWalker.g:19:1: keycodelist : ^( KEYCODELIST keycodelisttype ^( KEYCODEMATERIAL ( keycodeMaterial )+ ) ) ;
    def keycodelist(self, ):

        try:
            try:
                # KeycodesWalker.g:20:2: ( ^( KEYCODELIST keycodelisttype ^( KEYCODEMATERIAL ( keycodeMaterial )+ ) ) )
                # KeycodesWalker.g:20:4: ^( KEYCODELIST keycodelisttype ^( KEYCODEMATERIAL ( keycodeMaterial )+ ) )
                pass 
                self.match(self.input, KEYCODELIST, self.FOLLOW_KEYCODELIST_in_keycodelist90)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_keycodelisttype_in_keycodelist92)
                self.keycodelisttype()

                self._state.following.pop()
                self.match(self.input, KEYCODEMATERIAL, self.FOLLOW_KEYCODEMATERIAL_in_keycodelist95)

                self.match(self.input, DOWN, None)
                # KeycodesWalker.g:20:52: ( keycodeMaterial )+
                cnt2 = 0
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if ((INCLUDE <= LA2_0 <= KEYCODE)) :
                        alt2 = 1


                    if alt2 == 1:
                        # KeycodesWalker.g:20:52: keycodeMaterial
                        pass 
                        self._state.following.append(self.FOLLOW_keycodeMaterial_in_keycodelist97)
                        self.keycodeMaterial()

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

    # $ANTLR end "keycodelist"


    # $ANTLR start "keycodelisttype"
    # KeycodesWalker.g:23:1: keycodelisttype : ^( KEYCODELISTTYPE ^( KEYCODELISTOPTIONS ( KEYCODELISTOPTS )+ ) ^( KEYCODELISTNAME DQSTRING ) ) ;
    def keycodelisttype(self, ):

        try:
            try:
                # KeycodesWalker.g:24:2: ( ^( KEYCODELISTTYPE ^( KEYCODELISTOPTIONS ( KEYCODELISTOPTS )+ ) ^( KEYCODELISTNAME DQSTRING ) ) )
                # KeycodesWalker.g:24:4: ^( KEYCODELISTTYPE ^( KEYCODELISTOPTIONS ( KEYCODELISTOPTS )+ ) ^( KEYCODELISTNAME DQSTRING ) )
                pass 
                self.match(self.input, KEYCODELISTTYPE, self.FOLLOW_KEYCODELISTTYPE_in_keycodelisttype113)

                self.match(self.input, DOWN, None)
                self.match(self.input, KEYCODELISTOPTIONS, self.FOLLOW_KEYCODELISTOPTIONS_in_keycodelisttype116)

                self.match(self.input, DOWN, None)
                # KeycodesWalker.g:24:43: ( KEYCODELISTOPTS )+
                cnt3 = 0
                while True: #loop3
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if (LA3_0 == KEYCODELISTOPTS) :
                        alt3 = 1


                    if alt3 == 1:
                        # KeycodesWalker.g:24:43: KEYCODELISTOPTS
                        pass 
                        self.match(self.input, KEYCODELISTOPTS, self.FOLLOW_KEYCODELISTOPTS_in_keycodelisttype118)


                    else:
                        if cnt3 >= 1:
                            break #loop3

                        eee = EarlyExitException(3, self.input)
                        raise eee

                    cnt3 += 1



                self.match(self.input, UP, None)
                self.match(self.input, KEYCODELISTNAME, self.FOLLOW_KEYCODELISTNAME_in_keycodelisttype123)

                self.match(self.input, DOWN, None)
                self.match(self.input, DQSTRING, self.FOLLOW_DQSTRING_in_keycodelisttype125)

                self.match(self.input, UP, None)

                self.match(self.input, UP, None)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "keycodelisttype"


    # $ANTLR start "keycodeMaterial"
    # KeycodesWalker.g:27:1: keycodeMaterial : ( ^( INCLUDE DQSTRING ) | ^( MINIMUM NAME ) | ^( MAXIMUM NAME ) | ^( ALIAS ( NAME )+ ) | ^( KEYCODE ( NAME )+ ) | ^( INDICATOR NAME DQSTRING ) );
    def keycodeMaterial(self, ):

        try:
            try:
                # KeycodesWalker.g:28:2: ( ^( INCLUDE DQSTRING ) | ^( MINIMUM NAME ) | ^( MAXIMUM NAME ) | ^( ALIAS ( NAME )+ ) | ^( KEYCODE ( NAME )+ ) | ^( INDICATOR NAME DQSTRING ) )
                alt6 = 6
                LA6 = self.input.LA(1)
                if LA6 == INCLUDE:
                    alt6 = 1
                elif LA6 == MINIMUM:
                    alt6 = 2
                elif LA6 == MAXIMUM:
                    alt6 = 3
                elif LA6 == ALIAS:
                    alt6 = 4
                elif LA6 == KEYCODE:
                    alt6 = 5
                elif LA6 == INDICATOR:
                    alt6 = 6
                else:
                    nvae = NoViableAltException("", 6, 0, self.input)

                    raise nvae

                if alt6 == 1:
                    # KeycodesWalker.g:28:4: ^( INCLUDE DQSTRING )
                    pass 
                    self.match(self.input, INCLUDE, self.FOLLOW_INCLUDE_in_keycodeMaterial140)

                    self.match(self.input, DOWN, None)
                    self.match(self.input, DQSTRING, self.FOLLOW_DQSTRING_in_keycodeMaterial142)

                    self.match(self.input, UP, None)


                elif alt6 == 2:
                    # KeycodesWalker.g:29:4: ^( MINIMUM NAME )
                    pass 
                    self.match(self.input, MINIMUM, self.FOLLOW_MINIMUM_in_keycodeMaterial149)

                    self.match(self.input, DOWN, None)
                    self.match(self.input, NAME, self.FOLLOW_NAME_in_keycodeMaterial151)

                    self.match(self.input, UP, None)


                elif alt6 == 3:
                    # KeycodesWalker.g:30:4: ^( MAXIMUM NAME )
                    pass 
                    self.match(self.input, MAXIMUM, self.FOLLOW_MAXIMUM_in_keycodeMaterial158)

                    self.match(self.input, DOWN, None)
                    self.match(self.input, NAME, self.FOLLOW_NAME_in_keycodeMaterial160)

                    self.match(self.input, UP, None)


                elif alt6 == 4:
                    # KeycodesWalker.g:31:4: ^( ALIAS ( NAME )+ )
                    pass 
                    self.match(self.input, ALIAS, self.FOLLOW_ALIAS_in_keycodeMaterial167)

                    self.match(self.input, DOWN, None)
                    # KeycodesWalker.g:31:12: ( NAME )+
                    cnt4 = 0
                    while True: #loop4
                        alt4 = 2
                        LA4_0 = self.input.LA(1)

                        if (LA4_0 == NAME) :
                            alt4 = 1


                        if alt4 == 1:
                            # KeycodesWalker.g:31:12: NAME
                            pass 
                            self.match(self.input, NAME, self.FOLLOW_NAME_in_keycodeMaterial169)


                        else:
                            if cnt4 >= 1:
                                break #loop4

                            eee = EarlyExitException(4, self.input)
                            raise eee

                        cnt4 += 1



                    self.match(self.input, UP, None)


                elif alt6 == 5:
                    # KeycodesWalker.g:32:4: ^( KEYCODE ( NAME )+ )
                    pass 
                    self.match(self.input, KEYCODE, self.FOLLOW_KEYCODE_in_keycodeMaterial177)

                    self.match(self.input, DOWN, None)
                    # KeycodesWalker.g:32:14: ( NAME )+
                    cnt5 = 0
                    while True: #loop5
                        alt5 = 2
                        LA5_0 = self.input.LA(1)

                        if (LA5_0 == NAME) :
                            alt5 = 1


                        if alt5 == 1:
                            # KeycodesWalker.g:32:14: NAME
                            pass 
                            self.match(self.input, NAME, self.FOLLOW_NAME_in_keycodeMaterial179)


                        else:
                            if cnt5 >= 1:
                                break #loop5

                            eee = EarlyExitException(5, self.input)
                            raise eee

                        cnt5 += 1



                    self.match(self.input, UP, None)


                elif alt6 == 6:
                    # KeycodesWalker.g:33:4: ^( INDICATOR NAME DQSTRING )
                    pass 
                    self.match(self.input, INDICATOR, self.FOLLOW_INDICATOR_in_keycodeMaterial187)

                    self.match(self.input, DOWN, None)
                    self.match(self.input, NAME, self.FOLLOW_NAME_in_keycodeMaterial189)
                    self.match(self.input, DQSTRING, self.FOLLOW_DQSTRING_in_keycodeMaterial191)

                    self.match(self.input, UP, None)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "keycodeMaterial"


    # Delegated rules


 

    FOLLOW_KEYCODEDOC_in_keycodedoc72 = frozenset([2])
    FOLLOW_keycodelist_in_keycodedoc74 = frozenset([3, 5])
    FOLLOW_KEYCODELIST_in_keycodelist90 = frozenset([2])
    FOLLOW_keycodelisttype_in_keycodelist92 = frozenset([10])
    FOLLOW_KEYCODEMATERIAL_in_keycodelist95 = frozenset([2])
    FOLLOW_keycodeMaterial_in_keycodelist97 = frozenset([3, 11, 12, 13, 14, 15, 16])
    FOLLOW_KEYCODELISTTYPE_in_keycodelisttype113 = frozenset([2])
    FOLLOW_KEYCODELISTOPTIONS_in_keycodelisttype116 = frozenset([2])
    FOLLOW_KEYCODELISTOPTS_in_keycodelisttype118 = frozenset([3, 8])
    FOLLOW_KEYCODELISTNAME_in_keycodelisttype123 = frozenset([2])
    FOLLOW_DQSTRING_in_keycodelisttype125 = frozenset([3])
    FOLLOW_INCLUDE_in_keycodeMaterial140 = frozenset([2])
    FOLLOW_DQSTRING_in_keycodeMaterial142 = frozenset([3])
    FOLLOW_MINIMUM_in_keycodeMaterial149 = frozenset([2])
    FOLLOW_NAME_in_keycodeMaterial151 = frozenset([3])
    FOLLOW_MAXIMUM_in_keycodeMaterial158 = frozenset([2])
    FOLLOW_NAME_in_keycodeMaterial160 = frozenset([3])
    FOLLOW_ALIAS_in_keycodeMaterial167 = frozenset([2])
    FOLLOW_NAME_in_keycodeMaterial169 = frozenset([3, 18])
    FOLLOW_KEYCODE_in_keycodeMaterial177 = frozenset([2])
    FOLLOW_NAME_in_keycodeMaterial179 = frozenset([3, 18])
    FOLLOW_INDICATOR_in_keycodeMaterial187 = frozenset([2])
    FOLLOW_NAME_in_keycodeMaterial189 = frozenset([17])
    FOLLOW_DQSTRING_in_keycodeMaterial191 = frozenset([3])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import WalkerMain
    main = WalkerMain(KeycodesWalker)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
