import cx_Oracle 
from custom import customprint

# Create a table in Oracle database
try:
    con = cx_Oracle.connect('hr/hr@localhost:1521/xe')
    # Now execute the sqlquery
    cursor = con.cursor()
    result=cursor.execute("select * from student")
    customprint(cursor)

    cursor.close()
    cursor =con.cursor()
    result=cursor.execute("select * from jobs")
    customprint(cursor)

    #print(cursor.description)
    """
    print("sno      Name                   Fee")
    print("------------------------------------------------------------")
    for x in result:
        print("{:10d} {:20s} {:7.2f}".format(x[0],x[1],x[2]))"""
except Exception as x:
    print(x)
    