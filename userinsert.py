import cx_Oracle 
  
  
# Create a table in Oracle database
try:
    con = cx_Oracle.connect('hr/hr@localhost:1521/xe')
    # Now execute the sqlquery
    cursor = con.cursor()
    sno=input("enter sno->")
    name=input("enter name->")
    fee=input("enter fee->")
    cursor.execute("insert into student values(:1,:2,:3)",(sno,name,fee))
    con.commit()
except Exception as e:
    print(e)