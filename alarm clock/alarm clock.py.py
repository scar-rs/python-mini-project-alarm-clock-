import time
from tkinter import *
import multiprocessing
from tkinter import ttk, messagebox
from playsound import playsound
from threading import *
from PIL import Image, ImageTk
from tkinter import ttk

hour_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 
15, 16, 17, 18, 19, 20, 21, 22, 23, 24]

min_sec_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 
15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 
30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44,
45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 
]
class CountDown:
    def __init__(self, root):
       
        self.window = root
        self.window.geometry("480x320+0+0")
        self.window.title('Sakshis CountDown Timer')       
        self.window.resizable(width = False, height = False)
        
        time_label = Label(self.window, text="Set Time", 
        font=("times new roman",20,"bold"),fg='yellow')
        time_label.place(x=180, y=30)
        self.button_frame = Frame(self.window, bg="RosyBrown1", \
        width=180, height=40)
        self.button_frame.place(x=230, y=150)
        global start_button
        global pause_button        
        start_button = Button(text='Start', font=('Comic Sans MS',12), bg="IndianRed1", fg="white", command=self.Threading)
        start_button.place(x=240, y=150)
        pause_button = Button(text='Pause', font=('Comic Sans MS',12), bg="IndianRed1", fg="white", command=self.pause_time)
        pause_button.place(x=340, y=150)
        pause_button['state'] = 'disabled'
        start_button['state'] = 'disabled'
        time_label = Label(self.window, text="Set Time", 
        font=("Arial Rounded MT Bold",20, "bold"), bg='RosyBrown1',fg='black')
        time_label.place(x=180, y=30)
        hour_label = Label(self.window, text="Hour", 
        font=("Comic Sans MS",15), bg='RosyBrown1', fg='black')
        hour_label.place(x=50, y=70)
        minute_label = Label(self.window, text="Minute", 
        font=("Comic Sans MS",15), bg='RosyBrown1', fg='black')
        minute_label.place(x=200, y=70)
        second_label = Label(self.window, text="Second", 
        font=("Comic Sans MS",15), bg='RosyBrown1', fg='black')
        second_label.place(x=350, y=70)
        self.hour = IntVar()
        self.hour_combobox = ttk.Combobox(self.window, width=8, 
        height=10, textvariable=self.hour, 
        font=("times new roman",15))
        self.hour_combobox['values'] = hour_list
        self.hour_combobox.current(0)
        self.hour_combobox.place(x=50,y=110)
        self.minute = IntVar()
        self.minute_combobox = ttk.Combobox(self.window, width=8, 
        height=10, textvariable=self.minute, 
        font=("times new roman",15))
        self.minute_combobox['values'] = min_sec_list
        self.minute_combobox.current(0)
        self.minute_combobox.place(x=200,y=110)
        self.second = IntVar()
        self.second_combobox = ttk.Combobox(self.window, width=8, 
        height=10, textvariable=self.second, 
        font=("times new roman",15))
        self.second_combobox['values'] = min_sec_list
        self.second_combobox.current(0)
        self.second_combobox.place(x=350,y=110)

        cancel_button = Button(self.window, text='Stop', 
        font=('Comic Sans MS',12), bg="white", fg="black", 
        command=self.Cancel)
        cancel_button.place(x=70, y=150)

        global set_button
        set_button = Button(self.window, text='Set', 
        font=('Comic Sans MS',12), bg="white", fg="black", 
        command=self.Get_Time)
        set_button.place(x=160, y=150)

        reset=Button(self.window, text='Reset', font=('Comic Sans MS',12), bg="white", fg="black", command=self.Reset)
        reset.place(x=70, y=200)  
        

    def Reset(self):
        self.hour_combobox.current(0)
        self.minute_combobox.current(0)
        self.second_combobox.current(0)
        self.pause = True 
        self.time_display.destroy()
        pause_button['state'] = 'disabled'
        start_button['state'] = 'disabled'
        start_button['text'] = 'Start'

     
    def Cancel(self):
        self.pause = True
        self.window.destroy()

    def Get_Time(self):
        self.time_display = Label(self.window, image=img1,compound=CENTER,
        font=('Comic Sans MS', 18 , "bold"), 
        fg = 'black')
        self.time_display.place(x=228, y=229)

        try:
            
            h = (int(self.hour_combobox.get())*3600)
            m = (int(self.minute_combobox.get())*60)
            s = (int(self.second_combobox.get()))
            self.time_left = h + m + s

            
            if s == 0 and m == 0 and h == 0:
                messagebox.showwarning('Warning!',\
                'Please select a right time to set')
            else:
                pause_button['state'] = 'disabled'
                start_button['state'] = 'normal'
                self.pause = False
        except Exception as es:
            messagebox.showerror("Error!", \
            f"Error due to {es}")

    def Threading(self):
        global start_button
        start_button['text']='resume'
        self.x = Thread(target=self.start_time, daemon=True)
        self.x.start()
        start_button['state']='disabled'
        pause_button['state']='normal'

   
    def Clear_Screen(self):
        for widget in self.button_frame.winfo_children():
            widget.destroy()

    def pause_time(self):
        self.pause = True
        start_button['state']='normal'
        pause_button['state']='disabled'
        mins, secs = divmod(self.time_left, 60)
        hours = 0
        if mins > 60:
          
            hours, mins = divmod(mins, 60)

        self.time_display.config(text=f"Time Left: {hours}: {mins}: {secs}")
        self.time_display.update()


    def start_time(self):
        self.pause = False
        while self.time_left > 0:
            mins, secs = divmod(self.time_left, 60)

            hours = 0
            if mins > 60:
                
                hours, mins = divmod(mins, 60)

            self.time_display.config(text=f"Time Left: {hours}: {mins}: {secs}")
            self.time_display.update()
            
            time.sleep(1)
            self.time_left = self.time_left -1
           
            if self.time_left <= 0:
                process = multiprocessing.Process(target=playsound, 
                args=('Loud Alarm Clock Buzzer Sound Effect.mp3',))
                process.start()
                pause_button['state'] = 'disabled'
                start_button['state'] = 'disabled'
                start_button['text'] = 'Start'
                self.time_display.config(text=f"Time Left: 0: 0: 0")
                messagebox.showinfo('Time Over','Please ENTER to stop playing')
                process.terminate()
                self.Clear_Screen()
           
            if self.pause == True:
                break

if __name__ == "__main__":
    root = Tk()
        
    canvas = Canvas(root, width = 480, height = 320)      
    canvas.pack()    
    img = PhotoImage(file="apple.png") 
    img1 = PhotoImage(file="apple1.png")  
    canvas.create_image(0,0, anchor=NW, image=img)
    obj = CountDown(root)
    root.mainloop()