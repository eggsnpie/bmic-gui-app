##This is a Python script for a Desktop GUI application designed to calculate and display the BMI of the user based on the inputs they provide.

#Imports the Tkinter module as "tk"
#Allows us to create and manipulate the GUI elements of the app.
import tkinter as tk

#Defines the window that the app will occupy, the title, size, and configures the background.
window = tk.Tk()
window.title('BMI Calculator')
window.geometry('400x350')
window.configure(bg= 'SkyBlue2')

#Configures 10 rows and columns to be used by the GUI elements with a weight of 1.
#A non-zero weight tells the columns/rows to grow if extra space exists. A zero for the weight would have configured the opposite.
for sections in range(10):
    window.columnconfigure(sections, weight=1)
    window.rowconfigure(sections, weight=1)

#Defines the "main" function which will be used to loop the program given certain input by the user.
def main():

    #The StringVar function allows us to set different strings as the value for the user_prompt_text variable as the script executes.
    user_prompt_text = tk.StringVar()
    user_prompt_text.set('Do you measure weight in')
    user_prompt = tk.Label(window, textvariable=user_prompt_text, font=('Trebuchet MS', 20), bg='SkyBlue2')
    
                #When the .grid method is used, we are setting the position within our defined columns and rows that the variable will be placed.
                #If a positional method(grid, paddy, padx, pack) is not used, the widget/variable will not appear in the GUI.
    user_prompt.grid(column=4, columnspan=2, row=1, sticky='s')

    user_prompt1_text = tk.StringVar()
    user_prompt1_text.set('Pounds/Lbs or Kilograms/Kgs?')
    user_prompt1 = tk.Label(window, textvariable=user_prompt1_text, font=('Trebuchet MS', 20), bg='SkyBlue2')
    user_prompt1.grid(column=4, columnspan=2, row=2, sticky='n')

    #The Entry function creates an entry box, based on the parameters given, for users to provide data to
    user_input_box = tk.Entry(window, width=15, font=('Trebuchet MS', 15))
    user_input_box.grid(column=4, columnspan=2, row=3)

    #Defines a function that will be executed once the enter button is clicked at the first prompt.
    def enter_clicked_1():
        
        #The measure_system variable in this instance will contain the data provided in the user_input_box variable.
                                        #This data is gathered using the .get method attached to the user_input_box variable.
        measure_system = user_input_box.get()

        #Begins a set of if, elif, else statements that depend on the data contained in the measure_system variable.
        if measure_system.capitalize() == 'Pounds' or measure_system.capitalize() == 'Lbs':
            
            #Configures the enter_button widget to use the enter_clicked_2_lbs function.
            enter_button.configure(command=enter_clicked_2_LBS)

            #Clears the data contained within the user_input_box from the start to the end.
            user_input_box.delete(0, tk.END)
            user_prompt_text.set('How much do you weigh?')
            user_prompt.grid(column=4, columnspan=2, row=2)

            #Removes the user_prompt1 widget from the screen but retains the grid configuration for it, if the widget were to be called upon again.
            user_prompt1.grid_remove()
        
        elif measure_system.capitalize() == 'Kilograms' or measure_system.capitalize() == 'Kgs':
            enter_button.configure(command=enter_clicked_2_KGS)
            user_input_box.delete(0, tk.END)
            user_prompt_text.set('How much do you weigh?')
            user_prompt.grid(column=4, columnspan=2, row=2)
            user_prompt1.grid_remove()
        
        else:
            user_prompt_text.set('Something went wrong.')
            user_prompt.grid(column=4, columnspan=2, row=1, sticky='s')
            user_prompt1_text.set('Try again.')
            user_prompt1.grid(column=4, columnspan=2, row=2, sticky='n')
            user_input_box.delete(0, tk.END)

    #Defines a function that will be executed once the enter button is clicked at the second prompt following the imperial system.
    def enter_clicked_2_LBS():

        #Sets the weight_lbs variable as global. This allows the variable and the data contained within it to be used outside its current function.
        global weight_lbs

        weight_lbs = user_input_box.get()
        
        #Utilizes the try and except statements to try a set of code except if there is a value error.
        try:

            #This set of if, elif, else statements allow us to account for positive floats, negative floats, and invalid inputs.
            if float(weight_lbs) > 0.0:
                enter_button.configure(command=enter_clicked_3_LBS)
                user_input_box.delete(0, tk.END)
                user_prompt_text.set('How tall are you in inches?')
                user_prompt.grid(column=4, columnspan=2, row=2)
                user_prompt1.grid_remove()
            
            elif float(weight_lbs) < 0.0:
                user_prompt_text.set('Negative numbers cannot be used.')
                user_prompt.grid(column=4, columnspan=2, row=1, sticky='s')
                user_prompt1_text.set('Try again.')
                user_prompt1.grid(column=4, columnspan=2, row=2, sticky='n')
                user_input_box.delete(0, tk.END)
            
            else:
                user_prompt_text.set('Something went wrong.')
                user_prompt.grid(column=4, columnspan=2, row=1, sticky='s')
                user_prompt1_text.set('Try again.')
                user_prompt1.grid(column=4, columnspan=2, row=2, sticky='n')
                user_input_box.delete(0, tk.END)

        except ValueError:
            user_prompt_text.set('Something went wrong.')
            user_prompt.grid(column=4, columnspan=2, row=1, sticky='s')
            user_prompt1_text.set('Do not include Pounds/Lbs.')
            user_prompt1.grid(column=4, columnspan=2, row=2, sticky='n')
            user_input_box.delete(0, tk.END)

    #Defines a function that will be executed once the enter button is clicked at the second prompt following the metric system.
    def enter_clicked_2_KGS():
        global weight_kgs
        weight_kgs = user_input_box.get()
        
        try:
            if float(weight_kgs) > 0.0:
                enter_button.configure(command=enter_clicked_3_KGS)
                user_input_box.delete(0, tk.END)
                user_prompt_text.set('How tall are you in meters?')
                user_prompt.grid(column=4, columnspan=2, row=2)
                user_prompt1.grid_remove()
            
            elif float(weight_kgs) < 0.0:
                user_prompt_text.set('Negative numbers cannot be used.')
                user_prompt.grid(column=4, columnspan=2, row=1, sticky='s')
                user_prompt1_text.set('Try again.')
                user_prompt1.grid(column=4, columnspan=2, row=2, sticky='n')
                user_input_box.delete(0, tk.END)
            
            else:
                user_prompt_text.set('Something went wrong.')
                user_prompt.grid(column=4, columnspan=2, row=1, sticky='s')
                user_prompt1_text.set('Try again.')
                user_prompt1.grid(column=4, columnspan=2, row=2, sticky='n')
                user_input_box.delete(0, tk.END)

        except ValueError:
            user_prompt_text.set('Something went wrong.')
            user_prompt.grid(column=4, columnspan=2, row=1, sticky='s')
            user_prompt1_text.set('Do not include Kilograms/Kgs.')
            user_prompt1.grid(column=4, columnspan=2, row=2, sticky='n')
            user_input_box.delete(0, tk.END)

    #Defines a function that will be executed once the enter button is clicked at the third prompt following the imperial system.
    def enter_clicked_3_LBS():
        height_inch = user_input_box.get()

        try:
            if float(height_inch) > 0.0:
                user_input_box.delete(0, tk.END)
                user_input_box.grid_remove()
                enter_button.grid_remove()
                user_prompt1.grid_remove()
                reset_button.configure(command=reset_clicked_2)

                #The next 3 variables are used to calculate the users BMI based on the data they provided.
                                             #These two variables are converted to floats so that we can account for decimal numbers being input by the user.
                bmi_imperial_formula_step1 = float(weight_lbs) / float(height_inch) **2
                inch_to_meter = 703.0
                bmi_imperial_formula_step2 = bmi_imperial_formula_step1 * inch_to_meter

                                       #Uses the round function to round the float contained in bmi_imperial_formula_step2 to the tenth's place.
                bmi_imperial_results = round(bmi_imperial_formula_step2, 1)

                #Sets our user prompt to display the BMI results for the user.
                user_prompt_text.set('Your BMI is ' + str(bmi_imperial_results))
                user_prompt.grid(column=4, columnspan=2, row=3)
            
            elif float(height_inch) < 0.0:
                user_prompt_text.set('Negative numbers cannot be used.')
                user_prompt.grid(column=4, columnspan=2, row=1, sticky='s')
                user_prompt1_text.set('Try again.')
                user_prompt1.grid(column=4, columnspan=2, row=2, sticky='n')
                user_input_box.delete(0, tk.END)
            
            elif float(height_inch) > float(weight_lbs):
                user_prompt_text.set('Impossible BMI inputs.')
                user_prompt.grid(column=4, columnspan=2, row=1, sticky='s')
                user_prompt1_text.set('Try again.')
                user_prompt1.grid(column=4, columnspan=2, row=2, sticky='n')
                user_input_box.delete(0, tk.END)
            
            else:
                user_prompt_text.set('Something went wrong.')
                user_prompt.grid(column=4, columnspan=2, row=1, sticky='s')
                user_prompt1_text.set('Try again.')
                user_prompt1.grid(column=4, columnspan=2, row=2, sticky='n')
                user_input_box.delete(0, tk.END)

        except ValueError:
            user_prompt_text.set('Something went wrong.')
            user_prompt.grid(column=4, columnspan=2, row=1, sticky='s')
            user_prompt1_text.set('Do not include inches/in.')
            user_prompt1.grid(column=4, columnspan=2, row=2, sticky='n')
            user_input_box.delete(0, tk.END)

    #Defines a function that will be executed once the enter button is clicked at the third prompt following the metric system.
    def enter_clicked_3_KGS():
        height_meter = user_input_box.get()

        try:
            if float(height_meter) > 0.0:
                user_input_box.delete(0, tk.END)
                user_input_box.grid_remove()
                enter_button.grid_remove()
                user_prompt1.grid_remove()
                reset_button.configure(command=reset_clicked_2)

                bmi_metric_formula = float(weight_kgs) / float(height_meter) **2
                bmi_metric_results = round(bmi_metric_formula, 1)

                user_prompt_text.set('Your BMI is ' + str(bmi_metric_results))
                user_prompt.grid(column=4, columnspan=2, row=3)
            
            elif float(height_meter) < 0.0:
                user_prompt_text.set('Negative numbers cannot be used.')
                user_prompt.grid(column=4, columnspan=2, row=1, sticky='s')
                user_prompt1_text.set('Try again.')
                user_prompt1.grid(column=4, columnspan=2, row=2, sticky='n')
                user_input_box.delete(0, tk.END)
            
            elif float(height_meter) > float(weight_kgs):
                user_prompt_text.set('Impossible BMI inputs.')
                user_prompt.grid(column=4, columnspan=2, row=1, sticky='s')
                user_prompt1_text.set('Try again.')
                user_prompt1.grid(column=4, columnspan=2, row=2, sticky='n')
                user_input_box.delete(0, tk.END)
            
            else:
                user_prompt_text.set('Something went wrong.')
                user_prompt.grid(column=4, columnspan=2, row=1, sticky='s')
                user_prompt1_text.set('Try again.')
                user_prompt1.grid(column=4, columnspan=2, row=2, sticky='n')
                user_input_box.delete(0, tk.END)

        except ValueError:
            user_prompt_text.set('Something went wrong.')
            user_prompt.grid(column=4, columnspan=2, row=1, sticky='s')
            user_prompt1_text.set('Do not include inches/in.')
            user_prompt1.grid(column=4, columnspan=2, row=2, sticky='n')
            user_input_box.delete(0, tk.END)

    #Defines one of two functions used to initiate a reset of the program.
    def reset_clicked_1():
        reset_button.configure(command=reset_clicked_2)
        reset_button.grid(column=4, columnspan=2, row=4)
        global reset_prompt
        reset_prompt = tk.Label(window, text='Are you sure?', font=('Trebuchet MS', 30), bg='SkyBlue2')
        reset_prompt.grid(column=4, columnspan=2, row=2)
        enter_button.grid_remove()
        user_input_box.grid_remove()
        user_prompt.grid_remove()
        user_prompt1.grid_remove()
        
        #Converts the cancel_reset_button variable to be globally available, so it can be accessed by other functions.
        global cancel_reset_button
        cancel_reset_button = tk.Button(window, text='Cancel', font=('Trebuchet MS', 12), bg='gray46')
        cancel_reset_button.grid(column=4, columnspan=2, row=5)
        cancel_reset_button.configure(command=cancel_clicked)

    #Defines the second reset function that resets the program after being given confirmation by the user.
    def reset_clicked_2():

        #We use the "for" statement here to specify that we are trying to target widgets contained in the window widget.
                             #This function is called to gather a list of all the widgets that are children of the window widget.
        for widget in window.winfo_children():

            #These three if statements call out widgets that are either tk.Label, tk.Button, or tk.Entry widgets.
            #Under each of the if statements tells the program to execute the code under to the widgets that fit that criteria.
            if isinstance(widget, tk.Label):
                       #This method destroys the widget as well as all it's descending/children widgets.
                widget.destroy()
            if isinstance(widget, tk.Button):
                widget.destroy()
            if isinstance(widget, tk.Entry):
                widget.delete(0, tk.END)
        
        #The "main" function is called here to bring the program back up to where the code begins again under where the function is defined.
        main()

    #Defines a cancel reset function that allows the user to cancel their reset and return to where they left off in the program.
    def cancel_clicked():
        reset_button.configure(command=reset_clicked_1)
        reset_button.grid(column=4, columnspan=2, row=5)
        reset_prompt.destroy()
        cancel_reset_button.destroy()

                     #Restores the grid placement of the widget it is called for long as the .grid_remove method was used initially, not .grid_forget
        enter_button.grid()
        user_input_box.grid()
        user_prompt.grid()
        user_prompt1.grid()

    enter_button = tk.Button(window, text='Enter', font=('Trebuchet MS', 12), bg='gray46')
    enter_button.grid(column=4, columnspan=2, row=4)
    enter_button.configure(command=enter_clicked_1)

    reset_button = tk.Button(window, text='Reset', font=('Trebuchet MS', 12), bg='gray46')
    reset_button.grid(column=4, columnspan=2, row=5)
    reset_button.configure(command=reset_clicked_1)


    #Constantly refreshes the window so that it can display the things being done by the user within the window instead of freezing.
    window.mainloop()

#Calls upon the "main" function here so that when the program starts, it will initiate the first run of the program code that is contained within it.
main()

window.mainloop()