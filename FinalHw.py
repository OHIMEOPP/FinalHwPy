# 统计学生平均成绩与及格人数
#描述
#编写程序，计算学生们的平均成绩，并统计及格（成绩不低于60分）的人数。题目保证输入与输出均在整型范围内。

#输入格式
#在一行中给出n个非负整数，即这n位学生的成绩，其间以空格分隔。

#输出格式
#按照以下格式输出：

#average = 成绩均值
#count = 及格人数

scores  = [int(to_score) for to_score in input().split()]
#符合if>60的to_score都會進入to_scoure
count = len([to_score for to_score in scores if(int(to_score) > 60)])
        
average = sum(scores) /len(scores)

print("及格人數:",count)
print("輸入的成績是:" , average)
