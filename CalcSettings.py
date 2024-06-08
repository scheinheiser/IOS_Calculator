APP_SIZE=(400, 700)

MAIN_ROWS=7
MAIN_COLUMNS=4
# Makes the total amount of rows/columns for dividing the frame into the separate parts.

FONT='Helvetica'
OUTPUT_FONT_SIZE=70
DISPLAY_FONT_SIZE=35
BLACK='#000000'
# A bit of styling for the text and background colour of the app.

DISPLAY={
    'big': {'col':1, 'row':2, 'span':4},
    'small': {'col':1, 'row':1, 'span':4}
}
# Defines the placement of the displays, and sets how many columns they span across.

MATHS={
    '.': {'col':3, 'row':7, 'span':1},
    0: {'col':1, 'row':7, 'span':2},
    1: {'col':1, 'row':6, 'span':1},
    2: {'col':2, 'row':6, 'span':1},
    3: {'col':3, 'row':6, 'span':1},
    4: {'col':1, 'row':5, 'span':1},
    5: {'col':2, 'row':5, 'span':1},
    6: {'col':3, 'row':5, 'span':1},
    7: {'col':1, 'row':4, 'span':1},
    8: {'col':2, 'row':4, 'span':1},
    9: {'col':3, 'row':4, 'span':1}
}
# Defines the placement of numerical buttons in the grid and how many columns they span across.

OPERATIONS={
    '/': {'col':4, 'row':3, 'span':1, 'operator':'/', 'character':'÷'},
    '*': {'col':4, 'row':4, 'span':1, 'operator':'*', 'character':'X'},
    '-': {'col':4, 'row':5, 'span':1, 'operator':'-', 'character':'-'},
    '+': {'col':4, 'row':6, 'span':1, 'operator':'+', 'character':'+'},
    '=': {'col':4, 'row':7, 'span':1, 'operator':'=', 'character':'='}
}
# Defines the placement of operational buttons in the grid and how many columns they span across.

COMMANDS={
    'AC': {'col':1, 'row':3, 'span':1},
    '+/-': {'col':2, 'row':3, 'span':1},
    '%': {'col':3, 'row':3, 'span':1}
}
# Defines the placement of command buttons in the grid and how many columns they span across.

COLOURS={
    'number': {'fg_color':'#dadbd8', 'hover_color':'#f0f1ef', 'text_color':'black'},
    'command': {'fg_color':'#646464', 'hover_color':'#7b7a7a', 'text_color':'white'},
    'operator': {'fg_color':'#fca401', 'hover_color':'#febd58', 'text_color':'white'}
}
# A bit of styling for the different types of buttons.