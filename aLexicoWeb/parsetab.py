
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'CADENA COMA DIVISION END ID IGUAL INT LLAVE_L LLAVE_R MAS MAYOR MENOR MENOS MULTIPLICACION NUM PAREN_L PAREN_R PRINTF PROGRAM PUNTO_Y_COMA READ SUMAprogram : PROGRAM ID LLAVE_L declaraciones LLAVE_R ENDdeclaraciones : declaraciones declaracion\n                     | declaraciondeclaracion : INT ID PUNTO_Y_COMA\n                   | READ ID PUNTO_Y_COMA\n                   | PRINTF CADENA PUNTO_Y_COMA\n                   | ID IGUAL expresion PUNTO_Y_COMAexpresion : ID MAS ID\n                 | ID MENOS ID\n                 | ID MULTIPLICACION ID\n                 | ID DIVISION ID\n                 | NUM'
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,20,],[0,-1,]),'ID':([2,4,6,7,8,9,11,13,21,22,23,24,25,26,27,28,],[3,5,5,-3,14,15,17,-2,-4,-5,-6,29,30,31,32,-7,]),'LLAVE_L':([3,],[4,]),'INT':([4,6,7,13,21,22,23,28,],[8,8,-3,-2,-4,-5,-6,-7,]),'READ':([4,6,7,13,21,22,23,28,],[9,9,-3,-2,-4,-5,-6,-7,]),'PRINTF':([4,6,7,13,21,22,23,28,],[10,10,-3,-2,-4,-5,-6,-7,]),'IGUAL':([5,],[11,]),'LLAVE_R':([6,7,13,21,22,23,28,],[12,-3,-2,-4,-5,-6,-7,]),'CADENA':([10,],[16,]),'NUM':([11,],[19,]),'END':([12,],[20,]),'PUNTO_Y_COMA':([14,15,16,18,19,29,30,31,32,],[21,22,23,28,-12,-8,-9,-10,-11,]),'MAS':([17,],[24,]),'MENOS':([17,],[25,]),'MULTIPLICACION':([17,],[26,]),'DIVISION':([17,],[27,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'declaraciones':([4,],[6,]),'declaracion':([4,6,],[7,13,]),'expresion':([11,],[18,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAM ID LLAVE_L declaraciones LLAVE_R END','program',6,'p_program','app.py',73),
  ('declaraciones -> declaraciones declaracion','declaraciones',2,'p_declaraciones','app.py',77),
  ('declaraciones -> declaracion','declaraciones',1,'p_declaraciones','app.py',78),
  ('declaracion -> INT ID PUNTO_Y_COMA','declaracion',3,'p_declaracion','app.py',81),
  ('declaracion -> READ ID PUNTO_Y_COMA','declaracion',3,'p_declaracion','app.py',82),
  ('declaracion -> PRINTF CADENA PUNTO_Y_COMA','declaracion',3,'p_declaracion','app.py',83),
  ('declaracion -> ID IGUAL expresion PUNTO_Y_COMA','declaracion',4,'p_declaracion','app.py',84),
  ('expresion -> ID MAS ID','expresion',3,'p_expresion','app.py',87),
  ('expresion -> ID MENOS ID','expresion',3,'p_expresion','app.py',88),
  ('expresion -> ID MULTIPLICACION ID','expresion',3,'p_expresion','app.py',89),
  ('expresion -> ID DIVISION ID','expresion',3,'p_expresion','app.py',90),
  ('expresion -> NUM','expresion',1,'p_expresion','app.py',91),
]