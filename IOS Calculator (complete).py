import customtkinter as ctk
import CalcSettings as cs

class Display(ctk.CTkFrame):
    def __init__(display, parent):
        super().__init__(parent)
        display.configure(fg_color='transparent')
        display.rowconfigure(tuple([x for x in range(cs.MAIN_ROWS)]), weight=1, uniform='a')
        display.columnconfigure(tuple([y for y in range(cs.MAIN_COLUMNS)]), weight=1, uniform='a')

        display.MakingNumbers()
        display.MakingOperators()
        display.MakingCommands()

        display.show_string = ''
        display.display_string = '0'
        display.MakingDisplay()

        display.pack(expand=True, fill='both')
        # Makes all of the buttons, adds them to the frame and packs it in the display.

    def MakingDisplay(display):
        big_label = ctk.CTkLabel(display,
                                 text=display.display_string,
                                 font=(cs.FONT, cs.OUTPUT_FONT_SIZE, 'bold'),
                                 fg_color='transparent',
                                 text_color='white',
                                 anchor='e')

        small_label = ctk.CTkLabel(display,
                                   text=f'{display.show_string}',
                                   font=(cs.FONT, cs.DISPLAY_FONT_SIZE, 'bold'),
                                   fg_color='transparent',
                                   text_color='white',
                                   anchor='e')

        big_label.grid(column=cs.DISPLAY['big']['col'] - 1,
                       row=cs.DISPLAY['big']['row'] - 1,
                       columnspan=cs.DISPLAY['big']['span'],
                       sticky='news')

        small_label.grid(column=cs.DISPLAY['small']['col'] - 1,
                       row=cs.DISPLAY['small']['row'] - 1,
                       columnspan=cs.DISPLAY['small']['span'],
                       sticky='news')
    # Creates the label widgets for displaying the calculations and results.

    def MakingCommands(display):
        for key in cs.COMMANDS:
            if key == '+/-':
                ctk.CTkButton(display,
                              text=key,
                              font=(cs.FONT, cs.DISPLAY_FONT_SIZE, 'bold'),
                              fg_color=cs.COLOURS['command']['fg_color'],
                              hover_color=cs.COLOURS['command']['hover_color'],
                              text_color=cs.COLOURS['command']['text_color'],
                              corner_radius=0,
                              command=lambda n=key:display.InverseSign()
                              ).grid(column=cs.COMMANDS[key]['col'] - 1,
                                     row=cs.COMMANDS[key]['row'] - 1,
                                     columnspan=cs.COMMANDS[key]['span'],
                                     sticky='news',
                                     padx=1,
                                     pady=1)

            elif key == '%':
                ctk.CTkButton(display,
                              text=key,
                              font=(cs.FONT, cs.DISPLAY_FONT_SIZE, 'bold'),
                              fg_color=cs.COLOURS['command']['fg_color'],
                              hover_color=cs.COLOURS['command']['hover_color'],
                              text_color=cs.COLOURS['command']['text_color'],
                              corner_radius=0,
                              command=lambda: display.Percentage()
                              ).grid(column=cs.COMMANDS[key]['col'] - 1,
                                     row=cs.COMMANDS[key]['row'] - 1,
                                     columnspan=cs.COMMANDS[key]['span'],
                                     sticky='news',
                                     padx=1,
                                     pady=1)

            elif key == 'AC':
                ctk.CTkButton(display,
                              text=key,
                              font=(cs.FONT, cs.DISPLAY_FONT_SIZE, 'bold'),
                              fg_color=cs.COLOURS['command']['fg_color'],
                              hover_color=cs.COLOURS['command']['hover_color'],
                              text_color=cs.COLOURS['command']['text_color'],
                              corner_radius=0,
                              command=lambda:display.ClearingDisplay()
                              ).grid(column=cs.COMMANDS[key]['col'] - 1,
                                     row=cs.COMMANDS[key]['row'] - 1,
                                     columnspan=cs.COMMANDS[key]['span'],
                                     sticky='news',
                                     padx=1,
                                     pady=1)
    # Makes all of the command buttons (i.e. AC, +/-, %). Adds them to the right position based on the settings file.

    def ClearingDisplay(display):
        display.display_string='0'
        display.show_string= ''
        display.MakingDisplay()
    # Clears the variables that the label displays. Refreshes it so that it displays the default text.

    def Percentage(display):
        display.display_string = eval(display.display_string + '/100')
        display.MakingDisplay()
    # Takes the number in the large display and divides it by 100 for the percentage value. Refreshes display to update
    # values.

    def InverseSign(display):
        sign_change = True
        if '-' == str(display.display_string)[0]:
            display.display_string = str(display.display_string)[1:]
            sign_change = False

        if sign_change is False:
            pass
        elif sign_change is True:
            display.display_string = '-' + str(display.display_string)

        display.MakingDisplay()
    """
    Makes a boolean variable and checks if there's a negative sign at the beginning of the number. If true, then it 
    removes the sign and makes the need for a sign change false. If false, then it adds a negative sign at the end of 
    the string to make it negative.
    """

    def MakingOperators(display):
        for key in cs.OPERATIONS:
            if key == '=':
                ctk.CTkButton(display,
                              text=cs.OPERATIONS[key]['character'],
                              font=(cs.FONT, cs.DISPLAY_FONT_SIZE, 'bold'),
                              fg_color=cs.COLOURS['operator']['fg_color'],
                              hover_color=cs.COLOURS['operator']['hover_color'],
                              text_color=cs.COLOURS['operator']['text_color'],
                              corner_radius=0,
                              command=lambda n=key: display.CompletingCalculation()
                              ).grid(column=cs.OPERATIONS[key]['col'] - 1,
                                     row=cs.OPERATIONS[key]['row'] - 1,
                                     columnspan=cs.OPERATIONS[key]['span'],
                                     sticky='news',
                                     padx=1,
                                     pady=1)
            else:
                ctk.CTkButton(display,
                              text=cs.OPERATIONS[key]['character'],
                              font=(cs.FONT, cs.DISPLAY_FONT_SIZE, 'bold'),
                              fg_color=cs.COLOURS['operator']['fg_color'],
                              hover_color=cs.COLOURS['operator']['hover_color'],
                              text_color=cs.COLOURS['operator']['text_color'],
                              corner_radius=0,
                              command=lambda n=key :display.PreppingDisplay(n, 'operator')
                              ).grid(column=cs.OPERATIONS[key]['col'] - 1,
                                     row=cs.OPERATIONS[key]['row'] - 1,
                                     columnspan=cs.OPERATIONS[key]['span'],
                                     sticky='news',
                                     padx=1,
                                     pady=1)
    # Makes all of the operator buttons (i.e. +, -, ÷, x). Adds them to the right positon based on the settings file.

    def CompletingCalculation(display):
        display.final_calculation = display.show_string + display.display_string
        if display.final_calculation[-1] == '0':
            display.show_string=''
            display.display_string='N/A'
            display.MakingDisplay()
        else:
            display.display_string = round(eval(display.final_calculation), 4)
            display.MakingDisplay()
    # Adds the full calculation string a new variable; it checks if it's dividing by zero (throws up an error if so) -
    # if not, then it evaluates the calculation string and refreshes the display with the result.

    def MakingNumbers(display):
        for key in cs.MATHS:
            ctk.CTkButton(display,
                          text=key,
                          font=(cs.FONT, cs.DISPLAY_FONT_SIZE, 'bold'),
                          fg_color=cs.COLOURS['number']['fg_color'],
                          hover_color=cs.COLOURS['number']['hover_color'],
                          text_color=cs.COLOURS['number']['text_color'],
                          corner_radius=0,
                          command = lambda n=key :display.PreppingDisplay(n, 'number')).grid(
                                 column=cs.MATHS[key]['col'] - 1,
                                 row=cs.MATHS[key]['row'] - 1,
                                 columnspan=cs.MATHS[key]['span'],
                                 sticky='news',
                                 padx=1,
                                 pady=1)
    # Makes all of the number buttons. Adds them to the right position based on the settings file.

    def PreppingDisplay(display, button_name, button_type):
        try:
            if len(display.display_string) == 0:
                pass
            else:
                if display.display_string[0] == '0':
                    display.display_string = display.display_string[1:]
        except:
            pass

    # It tries to check the length of the string; if it's more than zero, it then checks if the first value in the
    # string is 0 - if this is also true, it removes the value so that only the actual number is left. This prevents any
    # issues with evaluating the calculation string (it throws an error w/ numbers like '0789').

        display.operator = ''
        if button_type == 'operator':
            display.operator += button_name
        else:
            display.display_string += str(button_name)

        if display.operator != '':
            display.show_string = ''
            display.show_string += str(display.display_string) + ' '
            display.display_string = ''
            display.show_string += display.operator + ' '

        display.MakingDisplay()
    # Clears the operator string. Checks if the type is an operator, and if so adds the type of operator to the
    # op_string. If not, it just adds the number to the display string. After, it checks if an operator has/hasn't
    # been added to the op_list - if an operator is present, it clears what might be there already in the small label,
    # and then adds the number and operator to the small label. After all of this, it refreshes the display.

class App(ctk.CTk):
    def __init__(app):
        super().__init__()
        app.title('Calculator')
        app.minsize(width=cs.APP_SIZE[0], height=cs.APP_SIZE[1])
        app.geometry(f'{cs.APP_SIZE[0]}x{cs.APP_SIZE[1]}')
        app.configure(fg_color=cs.BLACK)
        Display(app)
        app.mainloop()
        # Configures size, title and displays everything.

IOS_Calculator = App()
# Initialises app.