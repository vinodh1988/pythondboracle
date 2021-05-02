import cx_Oracle 
  
  
# Create a table in Oracle database
try:
    con = cx_Oracle.connect('hr/hr@localhost:1521/xe')
    # Now execute the sqlquery
    cursor = con.cursor()
    data=[
          (1,'Rahul',9000.34),
          (2,'Harry',9000.34),
          (3,'Johny',15000.34),
          (4,'Jimmy',18000.34),
          (5,'Kenny',9200.34)
          ]
    cursor.executemany("insert into student values(:1,:2,:3)",data)
    con.commit()
except Exception as e:
    print(e)