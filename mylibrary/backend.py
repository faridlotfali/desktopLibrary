import sqlite3


def connect():
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
    cur.execute(
        "Create Table If NOT EXISTS books (id INTEGER PRIMARY KEY, author text, title text ,year integer, isbn integer)")
    conn.commit()
    conn.close()


def insert(title, author, year, isbn):
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
    cur.execute("insert into books values (Null,?,?,?,?)",
                (author, title, year, isbn))
    conn.commit()
    conn.close()


def search(title= "" , author="", year="", isbn=""):
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
    cur.execute("Select * from books where title=? or author=? or year=? or isbn=?", (title, author, year, isbn))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
    cur.execute("delete from books where id=?",(id,))
    conn.commit()
    conn.close()

def update(id,title,author,year,isbn):
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
    cur.execute("update books set title=? , author=? , year=?, isbn=? where id=?",(title,author,year,isbn,id))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
    cur.execute("Select * from books")
    rows = cur.fetchall()
    conn.close()
    return rows


# insert('ml', 'faizi', '2016', '3465464')
# insert('romeo', 'shekspeer', '1950', '34524')
# update(1,"ml","farid","1998","54646")
# print(search("","ml"))
# print(view())

# i= 0
# while i < len(view()) :
#     print(view()[i])
#     i = i+1

# i= 0
# for i in range(len(view())) :
#     print(view()[i])
#     # i = i+1

# for x in view():
#     print(x)

# i= 0
# for i in range(len(view())-2,len(view())) :
#     print(view()[i])

# for x in view()[-2:]:
#     print(x)

# for i in range(1,5):
#     print('*'*i)

# for i in range(1,5):
#     for j in range(i):
#         print('*', end='')  
#     print("\n")

# delete(1)
# connect()
