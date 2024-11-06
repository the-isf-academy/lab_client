from tkinter import font
import customtkinter
# from riddle_client import RiddlerClient

class GUI:
    def __init__(self):

        # create the riddler client object
        # self.riddler_client = RiddlerClient()
        
        # maps each entry_widget to its placeholder text
        self.entry_dictionary = {
        }

        # map each entry_widget to its label
        self.label_dictionary = {
        }

        # maps each submit button with the method it triggers
        self.submit_button_dictionary = {
        }

        # map each menu button to its entry_widgets and submit button
        self.menu_dictionary = {
        }

    def setup_application_window(self):
        # Create and Setup the application window 
        self.app = customtkinter.CTk()
        self.app.geometry("800x600")
        self.app.title("Riddler Client")

    def all_setup(self):
        # Create and Setup the application window 
        self.setup_application_window()

        # each column uses equal spacing
        self.app.grid_columnconfigure((0,1,2,3), weight=1)

        # setup menu  buttons
        self.menu_buttons = []
        self.setup_menu_buttons()

        # setup text box
        self.text_box = customtkinter.CTkTextbox(
            self.app,
            font=customtkinter.CTkFont(size=16),
            text_color="black",  
            corner_radius=10, 
        )

        # setup entry widgets
        self.entry_widgets = {}
        self.setup_entry_widgets()

        # setup entry widget labels
        self.labels = {}
        self.setup_labels()

        # setup submit buttons
        self.submit_buttons = {}
        self.setup_submit_buttons()

    def setup_menu_buttons(self):
        '''Creates menu buttons'''

        for title, method in self.menu_dictionary.items():
            button = customtkinter.CTkButton(
                self.app, 
                text = title , 
                command = method,
                font = customtkinter.CTkFont(size=16))

            self.menu_buttons.append(button)

            button.grid(row=0, column=self.menu_buttons.index(button), padx=20, pady=20, sticky="ew")
            

    def setup_entry_widgets(self):
        '''Creates entry widgets'''
        
        for label, text in self.entry_dictionary.items():
            self.entry_widgets[label] = customtkinter.CTkEntry(
                self.app,
                placeholder_text = text)

    def setup_labels(self):
        '''Creates labels for entry widgets'''

        for label, text in self.label_dictionary.items():
            self.labels[label] = customtkinter.CTkLabel(
                self.app, 
                text = text, 
                fg_color="transparent")


    def setup_submit_buttons(self):
        '''Create submit buttons for entry widgets'''

        for title, method in self.submit_button_dictionary.items():
            button = customtkinter.CTkButton(
                self.app, 
                text = 'Submit', 
                command = method,
                font = customtkinter.CTkFont(size=16),
                state='disabled')

            self.submit_buttons[title] = (button)
    
    def display_text_box(self, row_num, height):
        self.text_box.grid(row=row_num, column=0, padx=20, pady=20, sticky="ew", columnspan=5)
        self.text_box.configure(height = height) 
        self.text_box.configure(state='disabled') # sets to read-only

    def reset_textbox(self):
        '''Remove all text from textbox'''
        
        self.text_box.configure(state='normal') # sets to read
        self.text_box.delete('1.0', 'end')      # deletes all text 
        
    def clear(self):
        '''Clear all boxes that are NOT the menu
        from the grid'''

        self.reset_textbox()
        self.text_box.grid_forget()

        for title, entry_widget in self.entry_widgets.items():
            entry_widget.delete(0,'end')
            entry_widget.grid_forget()

        for title, label in self.labels.items():
            label.grid_forget()
        
        for title,button in self.submit_buttons.items():
            button.grid_forget()

    def config_entry_widget(self,widget_list, submit_button):
        self.clear()

        # Bind the entry boxes to key entry
        self.setup_entry_bind(widget_list, submit_button)

        row_num = 1
        for widget in widget_list:
            self.labels[widget].grid(row=row_num, column=0, padx=0, pady=0)
            self.entry_widgets[widget].grid(row=row_num, column=1, pady=0, padx=20,sticky="ew", columnspan=2)
            row_num += 1
      
        # Place submit button on grid
        self.submit_buttons[submit_button].grid(row=3, column=1, padx=20, pady=10,sticky="ew")

    def setup_entry_bind(self, widget_list, submit_button):
        '''Binds widgets to typing in the entry box'''

        for widget in widget_list:
            self.entry_widgets[widget].bind(
                '<KeyRelease>', 
                lambda entry: self.enable_submit_guess_button(widget_list, submit_button))

    def enable_submit_guess_button(self, entry_widgets, submit_button):
        '''Only activate submit button if 
        user has entered information into
        the entry box'''

        num_filled = 0
        
        for widget in entry_widgets:
            if self.entry_widgets[widget].get():
                num_filled += 1
        
        if num_filled == len(entry_widgets):
            self.submit_buttons[submit_button].configure(state="normal")

    def run(self):
        self.all_setup()
        self.app.mainloop()
  
    # TO BE DELETED PROBABLY ⬇️

    # def view_all_riddles(self):
    #     '''Controls how the user views all riddles'''

    #     self.clear()

    #     all_riddles_json = self.riddler_client.all_riddles()
        
    #     # loops through each riddle
    #     for riddle_dict in all_riddles_json:
    #         # adds riddle id and question to the text box
    #         self.text_box.insert('end', f"{riddle_dict['id']}# {riddle_dict['question']}")
    #         self.text_box.insert('end', f"\n\n")

    #     self.display_text_box(row_num=1, height=500)
    
    # def guess_riddle_submit(self):
    #     '''Controls when the user clicks submit 
    #     for guess a riddle'''

    #     self.reset_textbox()

    #     guess_riddle_json = self.riddler_client.guess_riddle(
    #         self.entry_widgets['id'].get(), 
    #         self.entry_widgets['guess'].get())

    #     if 'correct' in guess_riddle_json:
    #         if guess_riddle_json['correct'] == True:
    #             message = 'Correct!!'
    #         else:
    #             message = 'Incorrect'
    #     else:
    #         message = guess_riddle_json

    #     self.text_box.insert('end',f"{message}")    # adds message to text box
        
    #     self.display_text_box(row_num=4, height=50)


    # def view_one_riddle_submit(self):
    #     '''Controls when the user clicks submit 
    #     for guess a riddle'''

    #     self.reset_textbox()

    #     one_riddle_json = self.riddler_client.one_riddle(self.entry_widgets['id'].get())

    #     self.text_box.insert('end',f"{one_riddle_json}")    

    #     self.display_text_box(row_num=4, height=200)

    # def new_riddle_submit(self):
    #     '''Controls when the user clicks submit 
    #     for guess a riddle'''

    #     self.reset_textbox()

    #     new_riddle_json = self.riddler_client.new_riddle(
    #         self.entry_widgets['question'].get(), 
    #         self.entry_widgets['answer'].get())

    #     if 'correct' in new_riddle_json:
    #         if new_riddle_json['correct'] == True:
    #             message = 'Correct!!'
    #         else:
    #             message = 'Incorrect'
    #     else:
    #         message = new_riddle_json

    #     self.text_box.insert('end',f"{message}")    # adds message to text box
        
    #     self.display_text_box(row_num=4, height=50)

  