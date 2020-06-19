import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="AIMAOMAO980126",
    database="bighomework"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT DISTINCT case_type FROM userInfo")

caseType = mycursor.fetchall()

for x in caseType:
    #print(type(x[0]))
    #mycursor.execute("CREATE TABLE "+x[0]+" (id INT, type VARCHAR(10), user_id INT, final_score INT)")
    sql1 = "SELECT * FROM userInfo WHERE case_type ='" + x[0] + "'"
    mycursor.execute(sql1)
    result = mycursor.fetchall()
    sql = "INSERT INTO "+x[0]+" (id, type, user_id, final_score) VALUES (%s, %s, %s, %s)"
    val = []
    for y in result:
        val1 = (y[1], y[2], y[0], y[3])
        val.append(val1)
    mycursor.executemany(sql, val)
    mydb.commit()
