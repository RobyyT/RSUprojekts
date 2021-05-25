from tkinter import *
from tkcalendar import *
import tkinter.messagebox as tkMessageBox
import sqlite3
import tkinter.ttk as ttk

logs = Tk()
logs.title("test NOTe-veseliba")
# width = 1280
# height = 900
# screen_width = logs.winfo_screenwidth()
# screen_height = logs.winfo_screenheight()
# x = (screen_width / 2) - (width / 2)
# y = (screen_height / 2) - (height / 2)
# logs.geometry("%dx%d+%d+%d" % (width, height, x, y))
logs.resizable(0, 0)

# =======================================VARIKI=====================================

LIETOTV = StringVar()
PAROLE = StringVar()
PASTS = StringVar()
PacVards = StringVar()
PacUzvards = StringVar()
PacPersKods = StringVar()
Preize = StringVar()
Oreize = StringVar()


# =======================================FUNKCIJAS=======================================
def Datubaze():
    global conn, cursor
    conn = sqlite3.connect("db_liet.db")
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS `lietotaji` (mem_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT, password TEXT, mail TEXT)")
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS `pacienti` (mem_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, Vards TEXT, Uzvards TEXT, PersKods TEXT, Ireize DATE, IIreize DATE)")


# def Exit():
#     ex = tkMessageBox.askquestion('test kysfag v1', 'Vai tiešām vēlaties iziet?', icon="warning")
#     if ex == 'yes':
#         logs.destroy()
#         exit()

bilde1 = PhotoImage(file='user.png')
bilde2 = PhotoImage(file='password.png')
bilde3 = PhotoImage(file='email.png')
bilde4 = PhotoImage(file='health.png').subsample(6, 8)
bilde5 = PhotoImage(file='rsu.png').subsample(2, 3)


# =====================================LOGIN FORMAS LOGS================================

def LoginForm():
    global LoginFrame, lbl_result1
    LoginFrame = Frame(logs, bg='white')
    LoginFrame.pack()

    # bilde1 = PhotoImage(file='user.png')
    lbl_username = Label(LoginFrame, image=bilde1, bg='white')
    lbl_username.image = bilde1
    lbl_username.grid(row=2, sticky=W)

    # bilde2 = PhotoImage(file='password.png')
    lbl_password = Label(LoginFrame, image=bilde2, bg='white')
    lbl_password.image = bilde2
    lbl_password.grid(row=3, sticky=W)

    ### REZULTĀTS APAKŠĀ
    lbl_result1 = Label(LoginFrame, text="", font=('arial', 18), bg='white')
    lbl_result1.grid(row=4, columnspan=2)

    username = Entry(LoginFrame, font=('arial', 20), textvariable=LIETOTV, width=15)
    username.grid(row=2, column=0)

    password = Entry(LoginFrame, font=('arial', 20), textvariable=PAROLE, width=15, show="*")
    password.grid(row=3, column=0)

    btn_login = Button(LoginFrame, text="Pierakstīties", font=('arial bold', 18), command=Login, bg='#092552',
                       fg='white', activebackground="#D0DBEC", cursor='hand2')
    btn_login.grid(row=5, columnspan=2, ipadx='93p', ipady=5)

    btn_register = Button(LoginFrame, text="Reģistrācija", fg="#092552", bg='white', font=('arial bold', 12),
                          relief=FLAT, height=2, command=ToggleToRegister, cursor='hand2', activebackground="#D0DBEC")
    btn_register.grid(row=1, column=0)
    LIETOTV.set("")
    PAROLE.set("")

    lbl_login = Label(LoginFrame, text="Pierakstīšanās", fg="#092552", bg='white',
                      font=('arial bold', 12, 'underline')
                      , height=2, relief=FLAT)
    lbl_login.grid(row=1, sticky=W)

    lbl_autentif = Label(LoginFrame, text='Autentifikācija', font=('arial bold', 18), bg='white', fg='#092552')
    lbl_autentif.grid(row=0, ipady=25, ipadx='90p')


# =====================================REGISTER FORMAS LOGS================================

def RegisterForm():
    global RegLogs, lbl_result2
    RegLogs = Frame(logs, bg='white')
    RegLogs.pack()

    # bilde3=PhotoImage(file='user.png')
    lbl_username2 = Label(RegLogs, image=bilde1, bg='white')
    lbl_username2.image = bilde2
    lbl_username2.grid(row=2, sticky=W)

    # bilde4 = PhotoImage(file='password.png')
    lbl_password2 = Label(RegLogs, image=bilde2, bg='white')
    lbl_password2.image = bilde2
    lbl_password2.grid(row=3, sticky=W)

    # bilde5=PhotoImage(file='email.png')
    lbl_mail = Label(RegLogs, image=bilde3, bg='white')
    lbl_mail.image = bilde3
    lbl_mail.grid(row=4, sticky=W)

    lbl_result2 = Label(RegLogs, text="", font=('arial', 18), bg='white')
    lbl_result2.grid(row=5, columnspan=2)

    username = Entry(RegLogs, font=('arial', 20), textvariable=LIETOTV, width=15)
    username.grid(row=2, column=0)

    password = Entry(RegLogs, font=('arial', 20), textvariable=PAROLE, width=15, show="*")
    password.grid(row=3, column=0)

    mail = Entry(RegLogs, font=('arial', 20), textvariable=PASTS, width=15)
    mail.grid(row=4, column=0)

    btn_register = Button(RegLogs, text="Reģistrēties", font=('arial bold', 18), command=Register, bg='#092552',
                          fg='white', activebackground="#D0DBEC", cursor='hand2')
    btn_register.grid(row=6, columnspan=2, ipadx='93p', ipady=5)

    btn_login2 = Button(RegLogs, text="Pierakstīšanās", fg="#092552", bg='white',
                        font=('arial bold', 12)
                        , height=2, relief=FLAT, command=ToggleToLogin, cursor='hand2', activebackground="#D0DBEC")
    btn_login2.grid(row=1, sticky=W)
    LIETOTV.set("")
    PAROLE.set("")
    PASTS.set("")
    lbl_register3 = Label(RegLogs, text="Reģistrācija", fg="#092552", bg='white',
                          font=('arial bold', 12, 'underline'), relief=FLAT, height=2)
    lbl_register3.grid(row=1, column=0)

    lbl_register = Label(RegLogs, text='Reģistrācija', font=('arial bold', 18), bg='white', fg='#092552')
    lbl_register.grid(row=0, ipady=25, ipadx='90p')


def ToggleToLogin(event=None):
    RegLogs.destroy()
    LoginForm()


def ToggleToRegister(event=None):
    LoginFrame.destroy()
    RegisterForm()


def Register():
    Datubaze()
    if LIETOTV.get == "" or PAROLE.get() == "" or PASTS.get() == "":
        lbl_result2.config(text="Aizpildiet visus laukus!", fg="red", bg='white')
        LIETOTV.set("")
        PAROLE.set("")
        PASTS.set("")
    else:
        # USERCAPS = LIETOTV.get().upper()
        cursor.execute("SELECT * FROM lietotaji WHERE username LIKE ?", (LIETOTV.get(),))
        if cursor.fetchone() is not None:
            lbl_result2.config(text="Lietotājvārds ir aizņemts", fg="red", bg='white')
            LIETOTV.set("")
            PAROLE.set("")
            PASTS.set("")
        else:
            cursor.execute("SELECT * FROM lietotaji WHERE mail LIKE ?", (PASTS.get(),))
            if cursor.fetchone() is not None:
                lbl_result2.config(text="E-pasts ir aizņemts", fg="red", bg='white')
                LIETOTV.set("")
                PAROLE.set("")
                PASTS.set("")
            else:
                cursor.execute("INSERT INTO lietotaji (username, password, mail) VALUES(?, ?, ?)",
                            (str(LIETOTV.get()), str(PAROLE.get()), str(PASTS.get())))
                conn.commit()
                LIETOTV.set("")
                PAROLE.set("")
                PASTS.set("")
                lbl_result2.config(text="Konts veiksmīgi izveidots!", fg="black")

        cursor.close()
        conn.close()


def Login():
    Datubaze()
    if LIETOTV.get == "" or PAROLE.get() == "":
        lbl_result1.config(text="Nepareizs lietotājvārds vai parole!", fg="red", bg='white')
        LIETOTV.set("")
        PAROLE.set("")
    else:
        cursor.execute("SELECT * FROM lietotaji WHERE username = ? and password = ?",
                       (LIETOTV.get(), PAROLE.get()))
        if cursor.fetchone() is not None:
            lbl_result1.config(text="Veiskmīga pievienošanās", fg="blue")
            LoginFrame.destroy()
            Programma()
        else:
            lbl_result1.config(text="Nepareizs lietotājvārds vai parole!", fg="red", bg='white')
            LIETOTV.set("")
            PAROLE.set("")


def Programma():
    global ProgLogs, izvelne, rsu, autors
    ProgLogs = Frame(logs, bg='white', width=1400, height=800)
    ProgLogs.pack(expand=True, side='right')
    ProgLogs.grid_propagate(False)
    rsu = Label(ProgLogs, image=bilde5, bg='white')
    rsu.image = bilde5
    rsu.grid(padx=200, pady=150)
    autors = Label(ProgLogs, text='Izstrādāja Roberts Tumeļkāns, MF2020v2', font=("Arial", 20, "bold", "italic"),
                   bg='white')
    autors.grid(padx=150, pady=100)

    izvelne = Frame(logs, bg='#092552', width=200, height=800, borderwidth=2, relief='flat')
    izvelne.pack(expand=False, fill='y', side='left', anchor='w')

    lbl_logo = Label(izvelne, image=bilde4, bg='white')
    lbl_logo.image = bilde4
    lbl_logo.grid(row=0, sticky=NW, ipadx=12)

    btn_ievade = Button(izvelne, text="Pacienta datu ievade", font=('arial bold', 11), command=lambda: [Ievade()],
                        bg='#092552',
                        fg='white', activebackground="#D0DBEC", cursor='hand2', relief='flat')
    btn_ievade.grid(row=1, ipadx='25p', ipady=5, pady=(50, 0))

    btn_meklet = Button(izvelne, text="Vakcinēto dati", font=('arial bold', 11), command=lambda: [Meklet()],
                        bg='#092552',
                        fg='white', activebackground="#D0DBEC", cursor='hand2', relief='flat')
    btn_meklet.grid(row=2, ipadx='28p', ipady=5)

    btn_about = Button(izvelne, text="Par projektu", font=('arial bold', 11), command=about, bg='#092552',
                       fg='white', activebackground="#D0DBEC", cursor='hand2', relief='flat')
    btn_about.grid(row=3, ipadx='47p', ipady=5)

    btn_exit = Button(izvelne, text="Iziet", font=('arial bold', 11), command=Exit, bg='#092552',
                      fg='white', activebackground="#D0DBEC", cursor='hand2', relief='flat')
    btn_exit.grid(row=4, ipadx='69p', ipady=5)


def about():
    print("xd")


def Meklet():  # --->Atvērt datu bāzi
    global Label1, Label2, Label3, Label4, Label5, Label6, data, meklesana, logs2

    def configScroll(canvas):
        canvas.configure(scrollregion=canvas.bbox('all'))

    Datubaze()
    logs2 = Tk()
    logs2.title("test NOTe-veseliba")
    canvas = Canvas(logs2, borderwidth=0, bg='white', width=770, height=500)
    meklesana = Frame(canvas, bg='white')
    scroll = Scrollbar(logs2, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scroll.set)
    scroll.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)
    meklesana.bind("<Configure>", lambda event, canvas=canvas: configScroll(canvas))
    canvas.create_window((5, 5), window=meklesana, anchor="nw")

    # visidati = Frame(bg='white')
    # visidati.geometry('1200x600')
    # scroll= Scrollbar(visidati)
    # scroll.pack(side=RIGHT, fill=Y)
    Label1 = Label(meklesana, text="ID", bg='#092552', fg='white', width=10)
    Label1.grid(row=0, column=0)
    Label2 = Label(meklesana, text="Vārds", bg='#092552', fg='white', width=10)
    Label2.grid(row=0, column=1)
    Label3 = Label(meklesana, text="Uzvārds", bg='#092552', fg='white', width=10)
    Label3.grid(row=0, column=2)
    Label4 = Label(meklesana, text="Personas Kods", bg='#092552', fg='white', width=10)
    Label4.grid(row=0, column=3)
    Label5 = Label(meklesana, text="I vakc reize", bg='#092552', fg='white', width=10)
    Label5.grid(row=0, column=4)
    Label6 = Label(meklesana, text="II vakc reize", bg='#092552', fg='white', width=15)
    Label6.grid(row=0, column=5)

    sqliteConnection = sqlite3.connect('db_liet.db')
    cursor = sqliteConnection.cursor()
    yes = cursor.execute("SELECT * FROM `pacienti`")
    i = 2  # rindas
    for dati in yes:
        for k in range(len(dati)):
            data = Entry(meklesana, width=20, fg='blue', state='normal')
            data.grid(row=i, column=k)
            data.insert(END, dati[k])
            data.configure(state='readonly')
        i = i + 1
    logs2.mainloop()
    # Datubaze()

    # tabula = ttk.Treeview(ProgLogs, selectmode='browse')
    # tabula.grid(row=1, column=1, padx=20, pady=20)
    # tabula['columns'] = ('id', 'Vards', 'Uzvards', 'PersKods', 'Ireize', 'IIreize')
    # for col in tabula['columns']:
    #    tabula.column(col, width=100, anchor='w')
    #    tabula.heading(col, col)
    # tabula.heading('id', text='ID')
    # tabula.heading('Vards', text='Pacienta vards')
    # tabula.heading('Uzvards', text='Pacienta uzvards')
    # tabula.heading('PersKods', text='personas kods')


# tabula.heading('Ireize', text='1.vakc reize')
# tabula.heading('IIreize', text='2.vakc reize')
##cursor.execute("SELECT * FROM `pacienti`")
# nolasit = cursor.fetchall()
# for dati in nolasit:
# tabula.insert('', 'end', values=(dati[1], dati[2], dati[3], dati[4], dati[5], dati[6]))


# lbl_vards2 = Label(ProgLogs, text="Ievadiet pacienta vārdu", font=('arial', 11), bg='white')
# lbl_vards2.grid(row=1, padx=(50, 0), pady=(50, 0))

def remove1():  # NEIZMANTOT
    lbl_vards.grid_remove()
    vards.grid_remove()
    lbl_uzvards.grid_remove()
    uzvards.grid_remove()
    lbl_kods.grid_remove()
    kods.grid_remove()
    lbl_result3.grid_remove()
    lbl_Ireize.grid_remove()
    Ireize.grid_remove()
    lbl_IIreize.grid_remove()
    IIreize.grid_remove()
    btn_ievade.grid_remove()


def remove2():    # NEIZMANTOT
    Label1.grid_remove()
    Label2.grid_remove()
    Label3.grid_remove()
    Label4.grid_remove()
    Label5.grid_remove()
    Label6.grid_remove()
    data.grid_remove()


def Ievade():
    global lbl_vards, vards, lbl_uzvards, uzvards, lbl_kods, kods, lbl_result3, lbl_Ireize, Ireize, lbl_IIreize, IIreize, btn_ievade
    # PACIENTA DATU IEVADES LIETAS
    lbl_vards = Label(ProgLogs, text="Ievadiet pacienta vārdu", font=('arial', 11), bg='white')
    lbl_vards.grid(row=1, padx=(50, 0), pady=(50, 0))
    vards = Entry(ProgLogs, font=('arial', 10), textvariable=PacVards, width=50)
    vards.grid(row=1, column=1, pady=(50, 0))

    lbl_uzvards = Label(ProgLogs, text="Ievadiet pacienta uzvārdu", font=('arial', 11), bg='white')
    lbl_uzvards.grid(row=2, padx=(50, 0), pady=(50, 0))
    uzvards = Entry(ProgLogs, font=('arial', 10), textvariable=PacUzvards, width=50)
    uzvards.grid(row=2, column=1, pady=(50, 0))

    lbl_kods = Label(ProgLogs, text="Pacienta personas kods", font=('arial', 11), bg='white')
    lbl_kods.grid(row=3, padx=(50, 0), pady=(50, 0))
    kods = Entry(ProgLogs, font=('arial', 10), textvariable=PacPersKods, width=50)
    kods.grid(row=3, column=1, pady=(50, 0))

    lbl_Ireize = Label(ProgLogs, text="1. vakcinācijas datums", font=('arial', 11), bg='white')
    lbl_Ireize.grid(row=4, padx=(50, 0), pady=(50, 0))
    Ireize = DateEntry(ProgLogs, font=('arial', 10), width=50, date_pattern='dd-mm-yyy', textvariable=Preize)
    Ireize.grid(row=4, column=1, pady=(50, 0))

    lbl_IIreize = Label(ProgLogs, text="2. vakcinācijas datums", font=('arial', 11), bg='white')
    lbl_IIreize.grid(row=5, padx=(50, 0), pady=(50, 0))
    IIreize = DateEntry(ProgLogs, font=('arial', 10), width=50, date_pattern='dd-mm-yyy', textvariable=Oreize)
    IIreize.grid(row=5, column=1, pady=(50, 0))

    lbl_result3 = Label(ProgLogs, text="", font=('arial', 11), bg='white')
    lbl_result3.grid(row=6)

    btn_ievade = Button(ProgLogs, text="Ievadīt pacientu datubāzē", font=('arial bold', 11), command=PacIevade,
                        bg='#092552',
                        fg='white', activebackground="#D0DBEC", cursor='hand2')
    btn_ievade.grid(row=7)

    autors.grid_remove()
    rsu.grid_remove()


def PacIevade():
    Datubaze()
    if PacVards.get() == "" or PacUzvards.get() == "" or PacPersKods.get() == "":
        lbl_result3.config(text="Ievadiet visus pacienta datus!", fg="black")
    else:
        cursor.execute("SELECT * FROM pacienti WHERE PersKods LIKE ?", (PacPersKods.get(),))
        if cursor.fetchone() is not None:
            lbl_result3.config(text="Pacients jau eksistē datubāzē", fg="red", bg='white')
        else:
            cursor.execute("INSERT INTO pacienti (Vards, Uzvards, PersKods, Ireize, IIreize) VALUES(?, ?, ?, ?, ?)",
                           (str(PacVards.get()), str(PacUzvards.get()), str(PacPersKods.get()), Preize.get(),
                            Oreize.get()))
            conn.commit()
            # PacVards.set("")
            # PacUzvards.set("")
            # PacPersKods.set("")
            lbl_result3.config(text="Pacients ievadīts!", fg="black")
        cursor.close()
        conn.close()


def Exit():
    ex = tkMessageBox.askquestion('test NOTe-veseliba', 'Vai tiešām vēlaties iziet?', icon="warning")
    if ex == 'yes':
        ProgLogs.destroy()
        izvelne.destroy()
        LoginForm()
        # if 'normal' == logs2.state():
        logs2.destroy()
    else:
        pass


LoginForm()

# ========================================MENUBAR WIDGETS==================================
# menubar = Menu(logs)
# filemenu = Menu(menubar, tearoff=0)
# filemenu.add_command(label="Exit", command=Exit)
# menubar.add_cascade(label="File", menu=filemenu)
# logs.config(menu=menubar)

logs.mainloop()
