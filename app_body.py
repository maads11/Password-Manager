import tkinter
import pandas
import hashlib
import json
from tkinter import messagebox


class PasswordManager:
    def __init__(self):
        # the window
        self.window = tkinter.Tk()
        self.window.geometry('450x560')
        self.window.configure(bg='white')
        self.window.title('PwdMan 1.0')
        self.window.resizable(False, False)


        # Title
        self.title = tkinter.Label(self.window, text='PassLock', bg='white', font=('Calibri', 25))
        self.title.grid(column=1, row=0, padx=90, sticky='NE')

        # Canvas
        self.canvas = tkinter.Canvas(self.window, width=300, height=400, bg='white', highlightthickness=0)
        self.canvas.grid(column=1, row=1, sticky='sw', columnspan=2)
        image = tkinter.PhotoImage(file='C:/Users/m.skvarla/PycharmProjects/Password_Manager/lock.png')
        self.canvas.create_image(150, 200, image=image)

        # username label
        self.username_label = tkinter.Label(text='Username : ', bg='white')
        self.username_label.grid(column=0, row=2, padx=5, pady=10)

        # username entry
        self.username_entry = tkinter.Entry(width=45)
        self.username_entry.grid(column=1, row=2, pady=10, sticky='sw',columnspan=2)
        self.username_entry.focus()

        # password label
        self.password_label = tkinter.Label(text='Password : ', bg='white')
        self.password_label.grid(column=0, row=3, padx=5, pady=10)

        # username entry
        self.password_entry = tkinter.Entry(width=45)
        self.password_entry.grid(column=1, row=3, padx=2, pady=10, sticky='sw', columnspan=2)

        # button to store the username and password to data file.

        def store_credentials():
            username = self.username_entry.get()
            password = self.password_entry.get()
            new_data = {username: password}
            try:
                with open('data.json', 'r') as data:
                    loaded_data = json.load(data)
            except FileNotFoundError:
                with open('data.json', 'w') as data:
                    json.dump(new_data, data, indent=4)
            else:
                loaded_data.update(new_data)
                with open('data.json', 'w') as data:
                    json.dump(loaded_data, data, indent=4)
            finally:
                self.username_entry.delete(0, len(self.username_entry.get()))
                self.password_entry.delete(0, len(self.password_entry.get()))

        self.button_to_store = tkinter.Button(text='Save', command=store_credentials, width=5)
        self.button_to_store.grid(column=2, row=3, sticky='N')

        # button to search the data
        def search():
            with open('data.json', 'r') as data:
                loaded_data = json.load(data)
                searched_value = self.username_entry.get()
                for key, value in loaded_data.items():
                    if key == searched_value:
                        tkinter.messagebox.showinfo(title=None, message=f'The password is: {loaded_data[searched_value]}')
            self.username_entry.delete(0, len(self.username_entry.get()))

        self.search_button = tkinter.Button(text='Search', command=search)
        self.search_button.grid(column=2, row=2)

        # button to show the data stored:
        def create_data_list():
            data_window = tkinter.Toplevel(self.window)
            data_window.title('The list: ')

            with open('data.json') as f:
                json_data = json.load(f)
                json_str = json.dumps(json_data, indent=4)
                text = tkinter.Text(data_window)
                text.insert('1.0', json_str)
                text.pack()

        button = tkinter.Button(self.window, text="Open Data", command=create_data_list)
        button.grid(column=0, row=4)

        self.window.mainloop()
