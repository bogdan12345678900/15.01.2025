# with open("data.txt", 'a', encoding='utf-8') as file:
#     for i in range(2):
#         file.write(input("input: ")+'\n')
#
# with open("data.txt", 'r', encoding='utf-8') as file:
#     result = file.read()
#
#
# symbol = input('S: ')
# count = 0
# for elem in result.split():
#     if elem.startswith(symbol):
#         count += 1
# print(count)

# import datetime
#
# def loggin():
#     with open('log.txt', 'a') as f:
#         f.write(f'Error {datetime.datetime.now()}' + '\n')
#
# def division(a: int,b: int )-> float:
#     try:
#         return a/b
#     except ZeroDivisionError as zde:
#         loggin()
#
#
# print(division(4,6))
# print(division(4,0))


# with open("file_1.txt" ,'a', encoding='utf-8') as f:
#     f.write(input("D"))
#
# with open("file_1.txt",'r',encoding='utf-8') as f:
#     data = f.read()
#
# with open('file_2.txt', 'a', encoding='utf-8') as f:
#     print()
#     for word in data.split():
#         if len(word) >= 7:
#             f.write(word + '\n')

# with open('file_1.txt', 'r', encoding="utf-8") as f:
#     data = f.readlines()
# for i in data[::-1]:
#     with open('file_2.txt', 'a', encoding='utf-8') as v:
#         v.write(i + '\n')


from tkinter import *
from tkinter import messagebox
def is_register_user():
    global login
    global pass_1


def user_login():
    global root
    global login
    global pass_1
    root.destroy()
    root = Tk()
    root.title("Singer in")
    root.geometry("400x400")
    root.resizable(False, False)
    label = Label(root, text="signin", font=('Arial', 18, 'bold'))
    label.pack()
    login_label = Label(root, text="input login", font=('Arial', 18, 'bold'))
    login_label.pack()
    login = Entry(root, font=('Arial', 18), width=15)
    login.pack()
    pass1_label = Label(root, text="password", font=('Arial', 18, 'bold'))
    pass1_label.pack()
    pass_1 = Entry(root, font=('Arial', 18), width=15)
    pass_1.pack()
    btn_sign_in = Button(root, text="Register", font=('Arial', 18, 'bold'), height=2, width=15, command=is_register_user)
    btn_sign_in.pack(pady=45)
def is_user(log):
    new_lst = []
    with open("user.txt", "r") as file:
        data = file.readlines()
    for log in data:
        new_lst.append(log[:log.find("|")])
        if log in new_lst:
            messagebox.showwarning("Error!","логін зайнятий")
            return False
        else:
            return True
def write_data():
    log = login.get()
    password = pass_1.get()
    if len(log)>2 and password == pass_2.get() and is_user(log):
        with open("user.txt","a") as file:
            file.write(f"{log}|{password}\n")
        messagebox.showinfo("Ok","ви зарегані")
    else:
        messagebox.showerror("No!","Ввод не вірний")

def register():
    global root
    global login
    global pass_1, pass_2
    root.destroy()
    root = Tk()
    root.title("Login and password")
    root.geometry("400x400")
    root.resizable(False, False)
    label = Label(root, text="signup", font=('Arial', 18, 'bold'))
    label.pack()
    login_label = Label(root, text="input login", font=('Arial', 18, 'bold'))
    login_label.pack()
    login = Entry(root, font=('Arial',18), width=15)
    login.pack()
    pass1_label = Label(root, text="password", font=('Arial', 18, 'bold'))
    pass1_label.pack()
    pass_1 = Entry(root, font=('Arial',18), width=15)
    pass_1.pack()
    pass_2 = Entry(root, font=('Arial',18), width=15)
    pass_2.pack()
    btn_register = Button(root, text="Register", font=('Arial', 18, 'bold'), height=2, width=15, command=write_data)
    btn_register.pack(pady=45)


def setuo_root():
    root.title("Login and password")
    root.geometry("400x400")
    root.resizable(False, False)
    label = Label(root, text="select an action", font=('Arial', 18, 'bold'))
    label.pack()
    btn_register = Button(root, text="Register", font=('Arial', 18, 'bold'), height=2, width=15, command=register)
    btn_register.pack(pady=45)
    btn_login = Button(root, text="Login", font=('Arial', 18, 'bold'), height=2, width=15 , command=user_login)
    btn_login.pack()


if __name__ == "__main__":
    root = Tk()
    login, pass_1,pass_2 = "","",""
    setuo_root()

    mainloop()
