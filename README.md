# Python期末報告
10924107 鄭裕憲
# 期末報告第2題
打開當前路徑下“作業.txt”，分別打出檔中前30個字元和前3行內容
# 程式碼
將輸入的成績以空格分割
並將值給予scores
```
scores  = [int(to_score) for to_score in input().split()]
```
符合成績大於60的to_score都會進入to_scoure
```
count = len([to_score for to_score in scores if(int(to_score) > 60)])
```
計算總平均
```
average = sum(scores) /len(scores)
```
輸出及格人數與輸入成績
```
print("及格人數:",count)
print("輸入的成績是:" , average)
```
# 實作截演示
![image](https://github.com/OHIMEOPP/py/blob/main/pycode.png)
