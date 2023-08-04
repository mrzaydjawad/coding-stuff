import tkinter as tk
import ttkbootstrap as ttk

def convert():
    mile_input = entry_int.get()
    km_output = mile_input * 1.61
    km_output_rounded = round(km_output,3)
    output_string.set(km_output_rounded)

#windows
window = ttk.Window(themename = 'darkly')
window.title('miles to km')
window.geometry('300x150')

#title
title_label = ttk.Label(master = window, text = 'miles to km',font =  'calibri 24 bold')
title_label.pack()

#input field
input_frame = ttk.Frame(master = window)
entry_int = tk.IntVar()
entry = ttk.Entry(master = input_frame,textvariable = entry_int)
button = ttk.Button(master = input_frame,text = 'Convert',command = convert)
entry.pack(side = 'left',padx =10)
button.pack(side = 'left')
input_frame.pack(pady = 10)

#output
output_string = tk.StringVar()
output_label = ttk.Label(master = window,text = 'x',font = 'calibri 24',textvariable = output_string)
output_label.pack(pady = 3)
#run
window.mainloop()