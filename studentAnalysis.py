import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="AIMAOMAO980126",
    database="bighomework"
)
mycursor = mydb.cursor()

nums = dict(图结构=12, 字符串=17, 查找算法=21, 树结构=28, 数组=44, 排序算法=11, 数字操作=35, 线性表=32)


def getUserInfo(id):
    sql = "SELECT *  FROM userInfo WHERE id = '" + id + "'"
    mycursor.execute(sql)
    totalInfo = mycursor.fetchall()
    str1 = "该生共有：" + str(len(totalInfo)) + "道题有提交记录,完成了" + str(len(totalInfo) / 2) + "%"
    fullScore = 0
    for f in totalInfo:
        if f[3] == 100:
            fullScore = fullScore + 1
    str10 = "满分的题有" + str(fullScore) + "道,占提交作业的" + str(round(fullScore / len(totalInfo) * 100, 2)) + "%"
    hisnums = [0, 0, 0, 0, 0, 0, 0, 0]
    for x in totalInfo:
        if x[2] == '图结构':
            hisnums[0] = hisnums[0] + 1
        elif x[2] == '字符串':
            hisnums[1] = hisnums[1] + 1
        elif x[2] == '查找算法':
            hisnums[2] = hisnums[2] + 1
        elif x[2] == '树结构':
            hisnums[3] = hisnums[3] + 1
        elif x[2] == '数组':
            hisnums[4] = hisnums[4] + 1
        elif x[2] == '排序算法':
            hisnums[5] = hisnums[5] + 1
        elif x[2] == '数字操作':
            hisnums[6] = hisnums[6] + 1
        else:
            hisnums[7] = hisnums[7] + 1
    str2 = "其中，图结构提交了" + str(hisnums[0]) + "道,占全部" + str(nums['图结构']) + "道题的" + str(
        round(hisnums[0] / nums['图结构'] * 100, 2)) + "%"
    str3 = "字符串提交了" + str(hisnums[1]) + "道,占全部" + str(nums['字符串']) + "道题的" + str(
        round(hisnums[1] / nums['字符串'] * 100, 2)) + "%"
    str4 = "查找算法提交了" + str(hisnums[2]) + "道,占全部" + str(nums['查找算法']) + "道题的" + str(
        round(hisnums[2] / nums['查找算法'] * 100, 2)) + "%"
    str5 = "树结构提交了" + str(hisnums[3]) + "道,占全部" + str(nums['树结构']) + "道题的" + str(
        round(hisnums[3] / nums['树结构'] * 100, 2)) + "%"
    str6 = "数组提交了" + str(hisnums[4]) + "道,占全部" + str(nums['数组']) + "道题的" + str(
        round(hisnums[4] / nums['数组'] * 100, 2)) + "%"
    str7 = "排序算法提交了" + str(hisnums[5]) + "道,占全部" + str(nums['排序算法']) + "道题的" + str(
        round(hisnums[5] / nums['排序算法'] * 100, 2)) + "%"
    str8 = "数字操作提交了" + str(hisnums[6]) + "道,占全部" + str(nums['数字操作']) + "道题的" + str(
        round(hisnums[6] / nums['数字操作'] * 100, 2)) + "%"
    str9 = "线性表提交了" + str(hisnums[7]) + "道,占全部" + str(nums['线性表']) + "道题的" + str(
        round(hisnums[7] / nums['线性表'] * 100, 2)) + "%"
    print(str1)
    print(str10)
    print(str2)
    print(str3)
    print(str4)
    print(str5)
    print(str6)
    print(str7)
    print(str8)
    print(str9)

    return totalInfo


def getDetail(kinds, totalInfo):
    fullKind = []
    for x in totalInfo:
        if x[2] == kinds:
            fullKind.append(x)
    if len(fullKind) != 0:
        # 题目完成率
        sql = "SELECT DISTINCT user_id, COUNT(*) as count FROM " + kinds + " GROUP BY user_id ORDER BY count DESC"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        stuNum = len(result)  # 学生人数
        hisNum = 0  # 该生的做题量排名
        for x in result:
            if x[1] == len(fullKind):
                break
            else:
                hisNum = hisNum + 1
        str1 = "该生在全部" + str(stuNum) + "名学生中中，做题量排名" + str(hisNum)
        print(str1)
        # 题目正确率
        rightNum = 0
        totalNum = 0
        for y in fullKind:
            if y[3] == 100:
                rightNum = rightNum + 1
            totalNum = totalNum + y[3]
        totalNum = round(totalNum / len(fullKind), 2)

        str2 = "该生已完成的" + str(len(fullKind)) + "道题中,全部正确的有" + str(rightNum) + "道,总正确率为" + str(totalNum) + "%"
        print(str2)
        if totalNum == 100:
            print("该生" + kinds + "类题目掌握度十分出色")
        else:
            # 最大似然估计求得该类题目的均值和方差
            sql = "SELECT DISTINCT user_id,COUNT(*) as count, SUM(final_score) as sum FROM " + kinds + " GROUP BY user_id "
            mycursor.execute(sql)
            result = mycursor.fetchall()
            arr = []
            for x in result:
                if x[1] != 0:
                    arr.append(float(float(x[-1]) / x[1]))
                else:
                    arr.append(0)
            #print(arr)
            mu = 0
            sigma = 0
            for z in arr:
                mu = mu + z
            mu = mu / stuNum
            for z in arr:
                sigma = sigma + (z - mu) ** 2
            sigma = sigma / stuNum
            if totalNum >= mu:
                print("该生" + kinds + "类题目掌握度较高")
            else:
                print("该生" + kinds + "类题目掌握度有待提高")
    else:
        print("该生未进行此类题目的练习，不予评定")


id = input("请输入学生id:")
totalInfo = getUserInfo(id)
kinds = input("请输入题型:")
getDetail(kinds, totalInfo)
