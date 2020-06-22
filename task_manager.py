from tkinter import *
import sqlite3 as sqlite
root = Tk()
root.title("Task Manager")
root.geometry("257x400")

conn = sqlite.connect("tasks.db")
c = conn.cursor()

done = 0

def add_task(event):
    global done
    conn = sqlite.connect("tasks.db")
    c = conn.cursor()

    c.execute("INSERT INTO tasks VALUES (:task)",

              {
                  "task": add_task_e.get()
              })

    conn.commit()
    conn.close()

    add_task_e.delete(0, END)

def delete():

    conn = sqlite.connect("tasks.db")
    c = conn.cursor()

    c.execute("DELETE from tasks WHERE oid=" + delete_e.get())

    conn.commit()
    conn.close()

def show_tasks():
    conn = sqlite.connect("tasks.db")
    c = conn.cursor()
    query_lbl = Label(root, text="")
    query_lbl.grid(row=6, column=0, columnspan=2)

    c.execute("SELECT *, oid FROM tasks")
    records = c.fetchall()
    # print(records)
    print_records = ""

    for record in records:
        print_records += str(record[0]) + " ID: " + str(record[1]) + "\n"

    query_lbl.config(text=print_records)

    conn.commit()
    conn.close()

def create_table():
    c.execute("CREATE TABLE tasks (task text)")

add_table_lbl = Label(root, text="PS. only press button on first visit").grid(row=0, column=0, columnspan=2)

add_table_btn = Button(root, text="Create Table", command=create_table).grid(row=1, column=0, columnspan=2)

add_task_e = Entry(root, width=37)
add_task_e.grid(row=2, column=1, pady=(10, 0))

add_task_lbl = Label(root, text="task")
add_task_lbl.grid(row=2, column=0, pady=(10, 0))

add_task_e.bind("<Return>", add_task)

show_tasks_btn = Button(root, text="show tasks", command=show_tasks)
show_tasks_btn.grid(row=3, column=0, columnspan=2, ipadx=105, pady=10)

delete_e = Entry(root, width=37)
delete_e.grid(row=4, column=1, pady=10)

delete_lbl = Label(root, text="Delete ID")
delete_lbl.grid(row=4, column=0, pady=10)

delete_btn = Button(root, text="Delete", command=delete)
delete_btn.grid(row=5, column=0, pady=10, columnspan=2, ipadx=117)

conn.commit()
conn.close()

root.mainloop()