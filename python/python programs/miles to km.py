import tkinter as tk
import ttkbootstrap as ttk

def mile_to_km():
    mile_input = entry_int.get()
    km_output = mile_input * 1.609
    km_output_rounded = round(km_output,3)
    output_string.set(km_output_rounded)

def km_to_mile():
    km_input = entry_int_2.get()
    mile_output = km_input/1.609
    mile_output_rounded = round(mile_output,3)
    output_string_2.set(mile_output_rounded)

#windows
window = ttk.Window(themename = 'darkly')
window.title('conversion')
window.geometry('300x275')

#title
title_label = ttk.Label(master = window, text = 'conversion',font =  'calibri 24 bold')
title_label.pack()

#mile to km
input_frame = ttk.Frame(master = window)
entry_int = tk.IntVar()
entry = ttk.Entry(master = input_frame,textvariable = entry_int)
button = ttk.Button(master = input_frame,text = 'mile to km',command = mile_to_km)
entry.pack(side = 'left',padx =10)
button.pack(side = 'left')
input_frame.pack(pady = 10)

#output 1
output_string = tk.StringVar()
output_label = ttk.Label(master = window,font = 'calibri 24',textvariable = output_string)
output_label.pack(pady = 5)

#km to mile
input_frame_2 = ttk.Frame(master = window)
entry_int_2 = tk.IntVar()
entry_2 = ttk.Entry(master = input_frame_2,textvariable = entry_int_2)
button_2 = ttk.Button(master = input_frame_2,text = 'km to mile',command = km_to_mile)
entry_2.pack(side = 'left',padx =10)
button_2.pack(side = 'left')
input_frame_2.pack(pady = 10)

#output 2
output_string_2 = tk.StringVar()
output_label_2 = ttk.Label(master = window,font = 'calibri 24',textvariable = output_string_2)
output_label_2.pack(pady = 10)
#run
window.mainloop()