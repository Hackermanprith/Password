import string
import random
import pyodbc
if __name__ == "__main__":
    s1 = string.ascii_lowercase
   # print(s1)
    s2 = string.ascii_uppercase
    # print(s2)
    s3 = string.digits
    # print(s3)
    s4 = string.punctuation
    # print(s4)
    plen = int(input("Enter password length\n"))
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    # print(s)
    random.shuffle(s)
    # print(s)
    print("Your password is:")
    print("".join(s[0:plen]))
    conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Prithwish Mukherjee\Documents\Paswworddb.accdb;')
cursor = conn.cursor()
name = input('Name:\t')
pas = input('Password:\t')
app = input('App/Website for which app is generated:\t')
cursor.execute("INSERT INTO password_table (Name, Password,App) VALUES(?,?,?);",name, pas,app)
conn.commit()
   

    