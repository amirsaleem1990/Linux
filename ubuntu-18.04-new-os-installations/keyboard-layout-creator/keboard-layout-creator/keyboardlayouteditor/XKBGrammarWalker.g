// XKB Grammar (X.org)
// Written by Simos Xenitellis <simos.lists@googlemail.com>, 2008.
// Version 0.8

tree grammar XKBGrammarWalker;

options
{
        language = Python;
        tokenVocab = XKBGrammar;
        ASTLabelType = CommonTree;
}

layout    
  : ^(LAYOUT symbols+)
  ;
  
symbols 
  : ^(SYMBOLS mapType ^(MAPMATERIAL mapMaterial+))
  ;

mapType
  : ^(MAPTYPE ^(MAPOPTIONS MAPOPTS+) ^(MAPNAME DQSTRING))
  ;

mapMaterial 
  : ^(TOKEN_INCLUDE DQSTRING)
  | ^(TOKEN_NAME DQSTRING)
  | ^(TOKEN_KEY_TYPE NAME? ^(VALUE DQSTRING))
  | ^(TOKEN_KEY OVERRIDE? ^(KEYCODEX NAME) keyelements+)
  | ^(TOKEN_MODIFIER_MAP STATE keycode+)
  | ^(TOKEN_VIRTUAL_MODIFIERS NAME+)
  ;

keycode 
  : ^(KEYCODE NAME)
  | ^(KEYCODEX NAME)
  ;

keyelements
  : ^(ELEM_KEYSYMS DQSTRING)
  | ^(ELEM_KEYSYMGROUP ^(VALUE NAME+))
  | ^(ELEM_VIRTUALMODS NAME)
  | ^(ELEM_OVERLAY NAME keycode)
  ;

mapopts
        : 'default'
        | 'hidden'
        | 'partial'
        | 'alphanumeric_keys'
        | 'keypad_keys'
        | 'function_keys'
        | 'modifier_keys'
        | 'alternate_group'
        | 'xkb_symbols'
        ;
