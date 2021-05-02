

def customprint(cursor):
    length=len(cursor.description)
 
    for x in cursor.description:
        print(x[0],end="   ")
    print("\n------------------------------------------")
    for row in cursor:
        for y in range(0,length):
            print(row[y],end=" ")
        print()
    print("---------------------------------------------")