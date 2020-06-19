import imp
import json
import sys
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="AIMAOMAO980126",
    database="bighomework"
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE TABLE userInfo (id Integer, case_id Integer, case_type Varchar(10), final_score Integer, "
#                 "nums Integer)")
imp.reload(sys)

f = open('test_data.json', encoding="UTF-8")
res = f.read()
data = json.loads(res)

users = []


def getUserInfo(data):  # 获取学生成绩数据，主键为学生id,其他数据有题号case_id,题目类型case_type,最终成绩final_score,提交次数nums
    for value in data.values():
        user_id = value['user_id']
        for case in value['cases']:
            userInfo = (user_id, case['case_id'], case['case_type'], case['final_score'], len(case['upload_records']))
            users.append(userInfo)
    return 0


getUserInfo(data)
sql = "INSERT INTO userInfo (id, case_id, case_type, final_score, nums) VALUES (%s, %s, %s, %s, %s)"

mycursor.executemany(sql, users)

mydb.commit()
