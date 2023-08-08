import tkinter as tk
class Stopwatch(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("stopwatch")
        self.geometry("300x300")
        self.time = 0
        self.running = False
        self.label = tk.Label(self,text="0:00:00",pady = "20", font=("calibri",35))
        self.label.pack()
        self.start_butoon = tk.Button(self,text="start",width=10,height= 2,font = ("calibri",14),command=self.start)
        self.start_butoon.pack()
        self.stop_button = tk.Button(self,text="stop",width=10,height = 2,font = ("calibri",14),command=self.stop)
        self.stop_button.pack()
        self.reset_button = tk.Button(self,text="reset",width=10,height = 2,font = ("calibri",14),command=self.reset)
        self.reset_button.pack()
    def start(self):
        self.running = True
        self.count()
    def stop(self):
        self.running = False
    def reset(self):
        self.running = False
        self.time = 0
        self.label.config(text = "0:00:00")
    def count(self):
        if self.running:
            self.time+=1
            minutes, seconds = divmod(self.time, 60)
            hours, minutes = divmod(minutes, 60)
            self.label.config(text="{:01d}:{:02d}:{:02d}".format(hours ,minutes,seconds))
            self.after(1000, self.count)
if __name__ == '__main__':
    stopwatch = Stopwatch()
    stopwatch.mainloop()