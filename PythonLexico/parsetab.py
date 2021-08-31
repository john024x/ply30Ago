
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftMASMENOSleftPORDIVIDIDOrightUMENOSCORDER CORIZQ DECIMAL DIVIDIDO ENTERO MAS MENOS PARDER PARIZQ POR PTCOMA REVALUARinstrucciones    : instruccion instrucciones\n                        | instruccioninstruccion    : REVALUAR CORIZQ expresion CORDER PTCOMAexpresion    :   expresion MAS expresion\n                    |   expresion MENOS expresion\n                    |   expresion POR expresion\n                    |   expresion DIVIDIDO expresionexpresion  :   MENOS expresion %prec UMENOSexpresion  :   PARIZQ expresion PARDERexpresion    :   ENTERO\n                    |   DECIMAL'
    
_lr_action_items = {'REVALUAR':([0,2,18,],[3,3,-3,]),'$end':([1,2,4,18,],[0,-2,-1,-3,]),'CORIZQ':([3,],[5,]),'MENOS':([5,6,7,8,9,10,12,13,14,15,16,17,19,20,21,22,23,],[7,13,7,7,-10,-11,7,7,7,7,-8,13,-4,-5,-6,-7,-9,]),'PARIZQ':([5,7,8,12,13,14,15,],[8,8,8,8,8,8,8,]),'ENTERO':([5,7,8,12,13,14,15,],[9,9,9,9,9,9,9,]),'DECIMAL':([5,7,8,12,13,14,15,],[10,10,10,10,10,10,10,]),'CORDER':([6,9,10,16,19,20,21,22,23,],[11,-10,-11,-8,-4,-5,-6,-7,-9,]),'MAS':([6,9,10,16,17,19,20,21,22,23,],[12,-10,-11,-8,12,-4,-5,-6,-7,-9,]),'POR':([6,9,10,16,17,19,20,21,22,23,],[14,-10,-11,-8,14,14,14,-6,-7,-9,]),'DIVIDIDO':([6,9,10,16,17,19,20,21,22,23,],[15,-10,-11,-8,15,15,15,-6,-7,-9,]),'PARDER':([9,10,16,17,19,20,21,22,23,],[-10,-11,-8,23,-4,-5,-6,-7,-9,]),'PTCOMA':([11,],[18,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'instrucciones':([0,2,],[1,4,]),'instruccion':([0,2,],[2,2,]),'expresion':([5,7,8,12,13,14,15,],[6,16,17,19,20,21,22,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> instrucciones","S'",1,None,None,None),
  ('instrucciones -> instruccion instrucciones','instrucciones',2,'p_instrucciones_lista','gramatica.py',71),
  ('instrucciones -> instruccion','instrucciones',1,'p_instrucciones_lista','gramatica.py',72),
  ('instruccion -> REVALUAR CORIZQ expresion CORDER PTCOMA','instruccion',5,'p_instrucciones_evaluar','gramatica.py',74),
  ('expresion -> expresion MAS expresion','expresion',3,'p_rexpresion_binaria','gramatica.py',77),
  ('expresion -> expresion MENOS expresion','expresion',3,'p_rexpresion_binaria','gramatica.py',78),
  ('expresion -> expresion POR expresion','expresion',3,'p_rexpresion_binaria','gramatica.py',79),
  ('expresion -> expresion DIVIDIDO expresion','expresion',3,'p_rexpresion_binaria','gramatica.py',80),
  ('expresion -> MENOS expresion','expresion',2,'p_rexpresion_unitaria','gramatica.py',87),
  ('expresion -> PARIZQ expresion PARDER','expresion',3,'p_expresion_agrupacion','gramatica.py',90),
  ('expresion -> ENTERO','expresion',1,'p_expresion_number','gramatica.py',93),
  ('expresion -> DECIMAL','expresion',1,'p_expresion_number','gramatica.py',94),
]