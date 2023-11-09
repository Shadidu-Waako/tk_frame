from tkinter import *


my_window = Tk()

# 36. ADDING FRAMES TO A PYTHON TKINTER WINDOW
# FRAME 1.
frame_name = Frame(my_window)

label_first = Label(frame_name, text='First Name')
label_middle = Label(frame_name, text='Middle Name')
label_surname = Label(frame_name, text='SurName')

entry_first = Entry(frame_name)
entry_middle = Entry(frame_name)
entry_surname = Entry(frame_name)

button_submit_name = Button(frame_name, text='  Submit  ')

label_first.grid(row=0, column=0)
label_middle.grid(row=1, column=0)
label_surname.grid(row=2, column=0)

entry_first.grid(row=0, column=1)
entry_middle.grid(row=1, column=1)
entry_surname.grid(row=2, column=1)

button_submit_name.grid(row=3, columnspan=2)

# FRAME 2.
frame_name_1 = Frame(my_window)

label_line = Label(frame_name_1, text='First Line')
label_town = Label(frame_name_1, text='Town')
label_country = Label(frame_name_1, text='Country')

entry_line = Entry(frame_name_1)
entry_town = Entry(frame_name_1)
entry_country = Entry(frame_name_1)

button_submit_country = Button(frame_name_1, text='  Submit  ')

label_line.grid(row=0, column=0)
label_town.grid(row=1, column=0)
label_country.grid(row=2, column=0)

entry_line.grid(row=0, column=1)
entry_town.grid(row=1, column=1)
entry_country.grid(row=2, column=1)

button_submit_country.grid(row=3, columnspan=2)

frame_name.grid(row=0, column=0)
frame_name_1.grid(row=1, column=1)
my_window.mainloop()
