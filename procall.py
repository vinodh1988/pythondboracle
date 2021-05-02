import cx_Oracle 


# Create a table in Oracle database
try:
    con = cx_Oracle.connect('hr/hr@localhost:1521/xe')
    # Now execute the sqlquery
    cursor = con.cursor()
    outVal = cursor.var(str)
    cursor.callproc('getjobtitle', ['AD_PRES', outVal])
    print(outVal.getvalue())        # will print 246
except Exception as e:
    print(e)