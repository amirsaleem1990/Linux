# $ANTLR 3.1.2 Keycodes.g 2020-05-10 06:02:52

import sys
from antlr3 import *
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


class KeycodesLexer(Lexer):

    grammarFileName = "Keycodes.g"
    antlr_version = version_str_to_tuple("3.1.2")
    antlr_version_str = "3.1.2"

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        Lexer.__init__(self, input, state)

        self.dfa8 = self.DFA8(
            self, 8,
            eot = self.DFA8_eot,
            eof = self.DFA8_eof,
            min = self.DFA8_min,
            max = self.DFA8_max,
            accept = self.DFA8_accept,
            special = self.DFA8_special,
            transition = self.DFA8_transition
            )






    # $ANTLR start "T__22"
    def mT__22(self, ):

        try:
            _type = T__22
            _channel = DEFAULT_CHANNEL

            # Keycodes.g:7:7: ( '{' )
            # Keycodes.g:7:9: '{'
            pass 
            self.match(123)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__22"



    # $ANTLR start "T__23"
    def mT__23(self, ):

        try:
            _type = T__23
            _channel = DEFAULT_CHANNEL

            # Keycodes.g:8:7: ( '}' )
            # Keycodes.g:8:9: '}'
            pass 
            self.match(125)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__23"



    # $ANTLR start "T__24"
    def mT__24(self, ):

        try:
            _type = T__24
            _channel = DEFAULT_CHANNEL

            # Keycodes.g:9:7: ( ';' )
            # Keycodes.g:9:9: ';'
            pass 
            self.match(59)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__24"



    # $ANTLR start "T__25"
    def mT__25(self, ):

        try:
            _type = T__25
            _channel = DEFAULT_CHANNEL

            # Keycodes.g:10:7: ( 'include' )
            # Keycodes.g:10:9: 'include'
            pass 
            self.match("include")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__25"



    # $ANTLR start "T__26"
    def mT__26(self, ):

        try:
            _type = T__26
            _channel = DEFAULT_CHANNEL

            # Keycodes.g:11:7: ( 'minimum' )
            # Keycodes.g:11:9: 'minimum'
            pass 
            self.match("minimum")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__26"



    # $ANTLR start "T__27"
    def mT__27(self, ):

        try:
            _type = T__27
            _channel = DEFAULT_CHANNEL

            # Keycodes.g:12:7: ( '=' )
            # Keycodes.g:12:9: '='
            pass 
            self.match(61)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__27"



    # $ANTLR start "T__28"
    def mT__28(self, ):

        try:
            _type = T__28
            _channel = DEFAULT_CHANNEL

            # Keycodes.g:13:7: ( 'maximum' )
            # Keycodes.g:13:9: 'maximum'
            pass 
            self.match("maximum")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__28"



    # $ANTLR start "T__29"
    def mT__29(self, ):

        try:
            _type = T__29
            _channel = DEFAULT_CHANNEL

            # Keycodes.g:14:7: ( 'alias' )
            # Keycodes.g:14:9: 'alias'
            pass 
            self.match("alias")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__29"



    # $ANTLR start "T__30"
    def mT__30(self, ):

        try:
            _type = T__30
            _channel = DEFAULT_CHANNEL

            # Keycodes.g:15:7: ( '<' )
            # Keycodes.g:15:9: '<'
            pass 
            self.match(60)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__30"



    # $ANTLR start "T__31"
    def mT__31(self, ):

        try:
            _type = T__31
            _channel = DEFAULT_CHANNEL

            # Keycodes.g:16:7: ( '>' )
            # Keycodes.g:16:9: '>'
            pass 
            self.match(62)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__31"



    # $ANTLR start "T__32"
    def mT__32(self, ):

        try:
            _type = T__32
            _channel = DEFAULT_CHANNEL

            # Keycodes.g:17:7: ( 'indicator' )
            # Keycodes.g:17:9: 'indicator'
            pass 
            self.match("indicator")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__32"



    # $ANTLR start "KEYCODELISTOPTS"
    def mKEYCODELISTOPTS(self, ):

        try:
            _type = KEYCODELISTOPTS
            _channel = DEFAULT_CHANNEL

            # Keycodes.g:79:2: ( 'default' | 'xkb_keycodes' )
            alt1 = 2
            LA1_0 = self.input.LA(1)

            if (LA1_0 == 100) :
                alt1 = 1
            elif (LA1_0 == 120) :
                alt1 = 2
            else:
                nvae = NoViableAltException("", 1, 0, self.input)

                raise nvae

            if alt1 == 1:
                # Keycodes.g:79:4: 'default'
                pass 
                self.match("default")


            elif alt1 == 2:
                # Keycodes.g:80:4: 'xkb_keycodes'
                pass 
                self.match("xkb_keycodes")


            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "KEYCODELISTOPTS"



    # $ANTLR start "NAME"
    def mNAME(self, ):

        try:
            _type = NAME
            _channel = DEFAULT_CHANNEL

            # Keycodes.g:84:2: ( ( 'a' .. 'z' | 'A' .. 'Z' | '_' | '0' .. '9' | '+' | '-' )* )
            # Keycodes.g:84:4: ( 'a' .. 'z' | 'A' .. 'Z' | '_' | '0' .. '9' | '+' | '-' )*
            pass 
            # Keycodes.g:84:4: ( 'a' .. 'z' | 'A' .. 'Z' | '_' | '0' .. '9' | '+' | '-' )*
            while True: #loop2
                alt2 = 2
                LA2_0 = self.input.LA(1)

                if (LA2_0 == 43 or LA2_0 == 45 or (48 <= LA2_0 <= 57) or (65 <= LA2_0 <= 90) or LA2_0 == 95 or (97 <= LA2_0 <= 122)) :
                    alt2 = 1


                if alt2 == 1:
                    # Keycodes.g:
                    pass 
                    if self.input.LA(1) == 43 or self.input.LA(1) == 45 or (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 90) or self.input.LA(1) == 95 or (97 <= self.input.LA(1) <= 122):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    break #loop2





            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "NAME"



    # $ANTLR start "WS"
    def mWS(self, ):

        try:
            _type = WS
            _channel = DEFAULT_CHANNEL

            # Keycodes.g:88:2: ( ( ' ' | '\\r' | '\\t' | '\\u000C' | '\\n' ) )
            # Keycodes.g:89:2: ( ' ' | '\\r' | '\\t' | '\\u000C' | '\\n' )
            pass 
            if (9 <= self.input.LA(1) <= 10) or (12 <= self.input.LA(1) <= 13) or self.input.LA(1) == 32:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            #action start
            _channel=HIDDEN; 
            #action end



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "WS"



    # $ANTLR start "COMMENT"
    def mCOMMENT(self, ):

        try:
            _type = COMMENT
            _channel = DEFAULT_CHANNEL

            # Keycodes.g:94:6: ( '/*' ( . )* '*/' )
            # Keycodes.g:95:2: '/*' ( . )* '*/'
            pass 
            self.match("/*")
            # Keycodes.g:95:7: ( . )*
            while True: #loop3
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if (LA3_0 == 42) :
                    LA3_1 = self.input.LA(2)

                    if (LA3_1 == 47) :
                        alt3 = 2
                    elif ((0 <= LA3_1 <= 46) or (48 <= LA3_1 <= 65535)) :
                        alt3 = 1


                elif ((0 <= LA3_0 <= 41) or (43 <= LA3_0 <= 65535)) :
                    alt3 = 1


                if alt3 == 1:
                    # Keycodes.g:95:7: .
                    pass 
                    self.matchAny()


                else:
                    break #loop3


            self.match("*/")
            #action start
            _channel=HIDDEN;
            #action end



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "COMMENT"



    # $ANTLR start "LINE_COMMENT"
    def mLINE_COMMENT(self, ):

        try:
            _type = LINE_COMMENT
            _channel = DEFAULT_CHANNEL

            # Keycodes.g:99:6: ( ( '//' | '#' ) (~ ( '\\n' | '\\r' ) )* ( '\\r' )? '\\n' )
            # Keycodes.g:100:2: ( '//' | '#' ) (~ ( '\\n' | '\\r' ) )* ( '\\r' )? '\\n'
            pass 
            # Keycodes.g:100:2: ( '//' | '#' )
            alt4 = 2
            LA4_0 = self.input.LA(1)

            if (LA4_0 == 47) :
                alt4 = 1
            elif (LA4_0 == 35) :
                alt4 = 2
            else:
                nvae = NoViableAltException("", 4, 0, self.input)

                raise nvae

            if alt4 == 1:
                # Keycodes.g:100:3: '//'
                pass 
                self.match("//")


            elif alt4 == 2:
                # Keycodes.g:100:10: '#'
                pass 
                self.match(35)



            # Keycodes.g:100:16: (~ ( '\\n' | '\\r' ) )*
            while True: #loop5
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if ((0 <= LA5_0 <= 9) or (11 <= LA5_0 <= 12) or (14 <= LA5_0 <= 65535)) :
                    alt5 = 1


                if alt5 == 1:
                    # Keycodes.g:100:16: ~ ( '\\n' | '\\r' )
                    pass 
                    if (0 <= self.input.LA(1) <= 9) or (11 <= self.input.LA(1) <= 12) or (14 <= self.input.LA(1) <= 65535):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    break #loop5


            # Keycodes.g:100:32: ( '\\r' )?
            alt6 = 2
            LA6_0 = self.input.LA(1)

            if (LA6_0 == 13) :
                alt6 = 1
            if alt6 == 1:
                # Keycodes.g:100:32: '\\r'
                pass 
                self.match(13)



            self.match(10)
            #action start
            _channel=HIDDEN; 
            #action end



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LINE_COMMENT"



    # $ANTLR start "DQSTRING"
    def mDQSTRING(self, ):

        try:
            _type = DQSTRING
            _channel = DEFAULT_CHANNEL

            # Keycodes.g:108:6: ( '\"' ( ( options {greedy=false; } : ~ ( '\"' ) )* ) '\"' )
            # Keycodes.g:108:10: '\"' ( ( options {greedy=false; } : ~ ( '\"' ) )* ) '\"'
            pass 
            self.match(34)
            # Keycodes.g:108:14: ( ( options {greedy=false; } : ~ ( '\"' ) )* )
            # Keycodes.g:108:15: ( options {greedy=false; } : ~ ( '\"' ) )*
            pass 
            # Keycodes.g:108:15: ( options {greedy=false; } : ~ ( '\"' ) )*
            while True: #loop7
                alt7 = 2
                LA7_0 = self.input.LA(1)

                if ((0 <= LA7_0 <= 33) or (35 <= LA7_0 <= 65535)) :
                    alt7 = 1
                elif (LA7_0 == 34) :
                    alt7 = 2


                if alt7 == 1:
                    # Keycodes.g:108:40: ~ ( '\"' )
                    pass 
                    if (0 <= self.input.LA(1) <= 33) or (35 <= self.input.LA(1) <= 65535):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    break #loop7





            self.match(34)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DQSTRING"



    def mTokens(self):
        # Keycodes.g:1:8: ( T__22 | T__23 | T__24 | T__25 | T__26 | T__27 | T__28 | T__29 | T__30 | T__31 | T__32 | KEYCODELISTOPTS | NAME | WS | COMMENT | LINE_COMMENT | DQSTRING )
        alt8 = 17
        alt8 = self.dfa8.predict(self.input)
        if alt8 == 1:
            # Keycodes.g:1:10: T__22
            pass 
            self.mT__22()


        elif alt8 == 2:
            # Keycodes.g:1:16: T__23
            pass 
            self.mT__23()


        elif alt8 == 3:
            # Keycodes.g:1:22: T__24
            pass 
            self.mT__24()


        elif alt8 == 4:
            # Keycodes.g:1:28: T__25
            pass 
            self.mT__25()


        elif alt8 == 5:
            # Keycodes.g:1:34: T__26
            pass 
            self.mT__26()


        elif alt8 == 6:
            # Keycodes.g:1:40: T__27
            pass 
            self.mT__27()


        elif alt8 == 7:
            # Keycodes.g:1:46: T__28
            pass 
            self.mT__28()


        elif alt8 == 8:
            # Keycodes.g:1:52: T__29
            pass 
            self.mT__29()


        elif alt8 == 9:
            # Keycodes.g:1:58: T__30
            pass 
            self.mT__30()


        elif alt8 == 10:
            # Keycodes.g:1:64: T__31
            pass 
            self.mT__31()


        elif alt8 == 11:
            # Keycodes.g:1:70: T__32
            pass 
            self.mT__32()


        elif alt8 == 12:
            # Keycodes.g:1:76: KEYCODELISTOPTS
            pass 
            self.mKEYCODELISTOPTS()


        elif alt8 == 13:
            # Keycodes.g:1:92: NAME
            pass 
            self.mNAME()


        elif alt8 == 14:
            # Keycodes.g:1:97: WS
            pass 
            self.mWS()


        elif alt8 == 15:
            # Keycodes.g:1:100: COMMENT
            pass 
            self.mCOMMENT()


        elif alt8 == 16:
            # Keycodes.g:1:108: LINE_COMMENT
            pass 
            self.mLINE_COMMENT()


        elif alt8 == 17:
            # Keycodes.g:1:121: DQSTRING
            pass 
            self.mDQSTRING()







    # lookup tables for DFA #8

    DFA8_eot = DFA.unpack(
        u"\1\14\3\uffff\2\14\1\uffff\1\14\2\uffff\2\14\5\uffff\6\14\1\uffff"
        u"\22\14\1\61\6\14\1\uffff\2\14\1\72\1\14\1\74\1\75\1\76\1\14\1\uffff"
        u"\1\14\3\uffff\1\14\1\102\1\14\1\uffff\2\14\1\76"
        )

    DFA8_eof = DFA.unpack(
        u"\106\uffff"
        )

    DFA8_min = DFA.unpack(
        u"\1\11\3\uffff\1\156\1\141\1\uffff\1\154\2\uffff\1\145\1\153\2\uffff"
        u"\1\52\2\uffff\1\143\1\156\1\170\1\151\1\146\1\142\1\uffff\1\154"
        u"\3\151\2\141\1\137\1\165\1\143\2\155\1\163\1\165\1\153\1\144\1"
        u"\141\2\165\1\53\1\154\2\145\1\164\2\155\1\uffff\1\164\1\171\1\53"
        u"\1\157\3\53\1\143\1\uffff\1\162\3\uffff\1\157\1\53\1\144\1\uffff"
        u"\1\145\1\163\1\53"
        )

    DFA8_max = DFA.unpack(
        u"\1\175\3\uffff\1\156\1\151\1\uffff\1\154\2\uffff\1\145\1\153\2"
        u"\uffff\1\57\2\uffff\1\144\1\156\1\170\1\151\1\146\1\142\1\uffff"
        u"\1\154\3\151\2\141\1\137\1\165\1\143\2\155\1\163\1\165\1\153\1"
        u"\144\1\141\2\165\1\172\1\154\2\145\1\164\2\155\1\uffff\1\164\1"
        u"\171\1\172\1\157\3\172\1\143\1\uffff\1\162\3\uffff\1\157\1\172"
        u"\1\144\1\uffff\1\145\1\163\1\172"
        )

    DFA8_accept = DFA.unpack(
        u"\1\uffff\1\1\1\2\1\3\2\uffff\1\6\1\uffff\1\11\1\12\2\uffff\1\15"
        u"\1\16\1\uffff\1\20\1\21\6\uffff\1\17\31\uffff\1\10\10\uffff\1\4"
        u"\1\uffff\1\5\1\7\1\14\3\uffff\1\13\3\uffff"
        )

    DFA8_special = DFA.unpack(
        u"\106\uffff"
        )

            
    DFA8_transition = [
        DFA.unpack(u"\2\15\1\uffff\2\15\22\uffff\1\15\1\uffff\1\20\1\17\13"
        u"\uffff\1\16\13\uffff\1\3\1\10\1\6\1\11\42\uffff\1\7\2\uffff\1\12"
        u"\4\uffff\1\4\3\uffff\1\5\12\uffff\1\13\2\uffff\1\1\1\uffff\1\2"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\21"),
        DFA.unpack(u"\1\23\7\uffff\1\22"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\24"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\25"),
        DFA.unpack(u"\1\26"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\27\4\uffff\1\17"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\30\1\31"),
        DFA.unpack(u"\1\32"),
        DFA.unpack(u"\1\33"),
        DFA.unpack(u"\1\34"),
        DFA.unpack(u"\1\35"),
        DFA.unpack(u"\1\36"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\37"),
        DFA.unpack(u"\1\40"),
        DFA.unpack(u"\1\41"),
        DFA.unpack(u"\1\42"),
        DFA.unpack(u"\1\43"),
        DFA.unpack(u"\1\44"),
        DFA.unpack(u"\1\45"),
        DFA.unpack(u"\1\46"),
        DFA.unpack(u"\1\47"),
        DFA.unpack(u"\1\50"),
        DFA.unpack(u"\1\51"),
        DFA.unpack(u"\1\52"),
        DFA.unpack(u"\1\53"),
        DFA.unpack(u"\1\54"),
        DFA.unpack(u"\1\55"),
        DFA.unpack(u"\1\56"),
        DFA.unpack(u"\1\57"),
        DFA.unpack(u"\1\60"),
        DFA.unpack(u"\1\14\1\uffff\1\14\2\uffff\12\14\7\uffff\32\14\4\uffff"
        u"\1\14\1\uffff\32\14"),
        DFA.unpack(u"\1\62"),
        DFA.unpack(u"\1\63"),
        DFA.unpack(u"\1\64"),
        DFA.unpack(u"\1\65"),
        DFA.unpack(u"\1\66"),
        DFA.unpack(u"\1\67"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\70"),
        DFA.unpack(u"\1\71"),
        DFA.unpack(u"\1\14\1\uffff\1\14\2\uffff\12\14\7\uffff\32\14\4\uffff"
        u"\1\14\1\uffff\32\14"),
        DFA.unpack(u"\1\73"),
        DFA.unpack(u"\1\14\1\uffff\1\14\2\uffff\12\14\7\uffff\32\14\4\uffff"
        u"\1\14\1\uffff\32\14"),
        DFA.unpack(u"\1\14\1\uffff\1\14\2\uffff\12\14\7\uffff\32\14\4\uffff"
        u"\1\14\1\uffff\32\14"),
        DFA.unpack(u"\1\14\1\uffff\1\14\2\uffff\12\14\7\uffff\32\14\4\uffff"
        u"\1\14\1\uffff\32\14"),
        DFA.unpack(u"\1\77"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\100"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\101"),
        DFA.unpack(u"\1\14\1\uffff\1\14\2\uffff\12\14\7\uffff\32\14\4\uffff"
        u"\1\14\1\uffff\32\14"),
        DFA.unpack(u"\1\103"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\104"),
        DFA.unpack(u"\1\105"),
        DFA.unpack(u"\1\14\1\uffff\1\14\2\uffff\12\14\7\uffff\32\14\4\uffff"
        u"\1\14\1\uffff\32\14")
    ]

    # class definition for DFA #8

    DFA8 = DFA
 



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import LexerMain
    main = LexerMain(KeycodesLexer)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
