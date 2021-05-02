import cx_Oracle 


# Create a table in Oracle database
try:
    con = cx_Oracle.connect('hr/hr@localhost:1521/xe')
    # Now execute the sq
    cursor = con.cursor()
    returnVal = cursor.callfunc("greet", str, ["Ganesh"])
    print(returnVal)    
except Exception as e:
    print(e)


    #sql alchemy is an orm solution