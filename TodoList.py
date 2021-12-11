from tkinter import*
from tkinter import messagebox as msg
import  time
import pickle
from PIL import ImageTk,Image


# screen   Using OOP class
class Todo:
    def __init__(self,root):
        self.root=root
        self.root.geometry('800x600')
        self.root.title('Todo List App')
        self.root.state('zoomed')
        self.root.resizable(0,0)
        self.root.config(bg='#fff')

        # images
        self.img=Image.open('todo-bg.png')
        self.bg=ImageTk.PhotoImage(self.img)
        Label(root,image=self.bg,cursor='hand2',bg='white').pack()
        self.txt=Label(root,text='TODO LIST APP',bg='white',fg='#897',
                       font=('Verdana',17,'bold'))
        self.txt.place(x=395,y=420)

        self.txt2 = Label(root, text='DEVELOPED : ENG-CJ', bg='white', fg='#897',
                         font=('Verdana', 15, 'bold'))
        self.txt2.place(x=1030, y=660)

        # btns
        self.get_Started=Button(root,cursor='hand2',
                                text='GET STARTED',bg='#187',fg='white',
                                font=('Verdana',20,'bold'),activebackground='#187',
                                activeforeground='white',
                                command=self.todo_window)
        self.get_Started.bind('<Enter>',self._hover_)
        self.get_Started.bind('<Leave>',self._leave_)
        self.get_Started.place(x=645,y=740)

    # hover function
    def _hover_(self,e):
        self.get_Started.config(bg='#090',fg='white')
    # leave
    def _leave_(self,e):
        self.get_Started.config(bg='#187',fg='white')

    # todo screen
    def todo_window(self):
        root.destroy()
        self.window=Tk()
        self.window.focus()
        self.window.title('Todo List App || Developed By Abdulrahman Haji')
        self.window.geometry('800x600')
        self.window.resizable(0,0)
        self.window.config(bg='#fff')

        self.img2=Image.open('icon.png')
        self.resize=self.img2.resize((400,400),Image.ANTIALIAS)
        self.bg=ImageTk.PhotoImage(self.resize)
        self.img_label=Label(self.window,image=self.bg,bg='white')
        self.img_label.place(x=400,y=1)
        Label(self.window, text="WRITE YOUR TASKS", bg='white', fg='#114357',
              font=('Oswald', 18)).place(x=470, y=355)
        self.frame=Frame(self.window,width=430,bg='blue',height=400,bd=0,relief='ridge')
        self.frame.place(x=1,y=1)

        self.scrollbar=Scrollbar(self.frame,orient=VERTICAL)
        self.scrollbar.pack(fill=Y,side=RIGHT)

        self.listbox = Listbox(self.frame,font=('Verdana',17,'bold'),cursor='hand2',yscrollcommand=self.scrollbar.set,
                               width=27,
                               height=13,fg='#4b134f', bd=5, relief='groove')
        self.listbox.pack()
        self.scrollbar.config(command=self.listbox.yview)


    # btns
        # entry
        self.entry_box=Entry(self.window,width=38,bd=5,relief='groove',
                             font=('Josefin Sans',15,'bold'),fg='#4a00e0')
        self.entry_box.place(x=5,y=393)
        #______
        self.img_add=Image.open('add-icon.png')
        self.btn_resize=self.img_add.resize((70,70),Image.ANTIALIAS)
        self.add_icon=ImageTk.PhotoImage(self.btn_resize)
        self.add_btn=Button(self.window,image=self.add_icon,bg='white',bd=0,relief='ridge'
                            ,activebackground='white',cursor='hand2',command=self.add_task)

        self.add_btn.place(x=0,y=428)
        #
        # # edit icon
        self.img_edit = Image.open('delete-icon.png')
        self.edit_resize = self.img_edit.resize((45, 30), Image.ANTIALIAS)
        self.edit_icon = ImageTk.PhotoImage(self.edit_resize)
        self.edit_btn = Button(self.window, image=self.edit_icon, bg='white', bd=0, relief='ridge'
                              , activebackground='white',cursor='hand2',
                               command= self.delete)
        self.edit_btn.place(x=50, y=448)


        # save icon
        self.img_save = Image.open('save.ico')
        self.save_resize = self.img_save.resize((35, 35), Image.ANTIALIAS)
        self.save_icon = ImageTk.PhotoImage(self.save_resize)
        self.save_btn = Button(self.window, image=self.save_icon, bg='white', bd=0, relief='ridge'
                              , activebackground='white',fg='black',cursor='hand2',
                               command=self.save)
        self.save_btn.place(x=100, y=448)

        # load

        self.img_load = Image.open('load.png')
        self.load_resize = self.img_load.resize((35, 35), Image.ANTIALIAS)
        self.load_icon = ImageTk.PhotoImage(self.load_resize)
        self.load_btn = Button(self.window, image=self.load_icon, bg='white', bd=0, relief='ridge'
                               , activebackground='white', fg='black', cursor='hand2',
                               command=self.load)
        self.load_btn.place(x=150, y=448)

        # DARK
        self.img_dark = Image.open('dark0-icon.png')
        self.dark_resize = self.img_dark.resize((35, 35), Image.ANTIALIAS)
        self.dark_icon = ImageTk.PhotoImage(self.dark_resize)
        self.darkbtn = Button(self.window, image=self.dark_icon, bg='white', bd=0, relief='ridge'
                               , activebackground='white', fg='black', cursor='hand2',
                               command=self.dark)
        self.darkbtn.place(x=750, y=1)


        self.IMG_SUN = Image.open('sun-icon.png')
        self.sun_res = self.IMG_SUN.resize((35, 35), Image.ANTIALIAS)
        self.sunicon = ImageTk.PhotoImage(self.sun_res)
        self.sunbtn = Button(self.window, image=self.sunicon, bg='white', bd=0, relief='ridge'
                               , activebackground='white', fg='black', cursor='hand2',
                               command=self.dark)
        self.sunbtn.place(x=750, y=1)

        self.State=False

    def dark(self):
      pass
    def add_task(self):
        if self.entry_box.get()=='':
            msg.showerror('ERROR','Plz Enter Task Name')

        elif self.entry_box.get() in self.listbox.get(0,END):
            msg.showerror('ERR','This Task Already Exist \nEnter Another Task Name')
            self.entry_box.delete(0, END)
        else:
            self.listbox.insert(END,self.entry_box.get())
            self.entry_box.delete(0,END)

    def delete(self):
        confirm=msg.askyesno('Confirm','Are You Sure\nTo Delete This Task?')

        try:
            if confirm == 1:
                index=self.listbox.curselection()[0]
                self.listbox.delete(index)
            else:
                pass
        except:
            msg.showerror('ERR','You Must Select The Task\nYou want To Delete')

    def save(self):
        tasks=self.listbox.get(0,self.listbox.size())
        pickle.dump(tasks,open('tasks.dat','wb'))
    def load(self):
        tasks=pickle.load(open('tasks.dat','rb'))
        for task in tasks:
            self.listbox.insert(0,task)

        # scrollbar = Scrollbar(self.frame, orient=VERTICAL)
        # # scrollbar.config(yscrollcommand=scrollbar.set)
        #
        #
        # # lists box
        # self.listbox=Listbox(self.frame,yscrollcommand=scrollbar.set,width=70,height=24,bd=5,relief='groove')
        # self.listbox.place(x=0,y=0)
        # scrollbar.config(command=self.listbox.yview)
        # scrollbar.pack(fill=Y, side=RIGHT)

        # self.scrollbar


        # window.mainloop()



root=Tk()
obj=Todo(root)
root.mainloop()