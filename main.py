# Student Performance Analytics System

import pandas as pd

record = {
    "name":["Kranti","Ritesh","Samarth","Aditya","Omkar","Sumit","Lakhan","Ajinkya","Pratik","Mayur","Anshul","Pranav","Shreyash","Yash","Mahesh"],
    "ID" :[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],
    "DEPT":["AIDS","AIDS","AIDS","AIDS","AIDS","CS","IT","ENTC","AIML","CS","IT","IT","ENTC","AIDS","ENTC"],
    "ATDN":[87,87,98,78,67,67,87,98,56,78,65,78,65,78,98],
    "age":[21,21,23,21,19,21,23,22,21,20,23,21,23,24,25],
    "DS" :[45,65,76,87,80,90,95,78,87,34,64,65,54,34,64],
    "AI" :[45,64,65,54,34,64,64,65,54,34,64,67,90,89,64],
    "ML" :[53,67,86,56,64,65,54,34,64,6,56,87,89,90,43],
    "DL" :[98,56,55,43,7,90,64,65,54,34,64,89,43,53,34]
}

df = pd.DataFrame(record)
# print(df)

df.to_csv("student.csv",index=False)

k = pd.read_csv("student.csv")
# print(k)

Subjects = ["DS","AI","ML","DL"]

k["Average"]=k[Subjects].mean(axis=1)

def assign_grade(avg):
    if avg >= 95:
        return "A+"
    elif avg >= 85:
        return "A"
    elif avg >= 75:
        return "B+"
    elif avg >= 65:
        return "B"
    elif avg >= 45:
        return "C"
    else:
        return "D"

def check_result(avg):
    for subject in Subjects:
        if avg[subject] < 40:
            return "Fail"
    return "Pass"

k["Grade"]=k["Average"].apply(assign_grade)
k["Result"]=k.apply(check_result,axis=1)
k.loc[k["Result"] == "Fail", "Grade"] = "F"

# print(k[["name","Average","Grade","Result"]])

k["Total Marks"] = k[Subjects].sum(axis=1)

# print("Information of Table")

# k.info()

print("\n-----------STUDENT PERFORMANCE REPORT----------------")
print(k[["ID", "name", "DEPT", "ATDN","Total Marks", "Average", "Grade", "Result"]].to_string(index=False))
highest = k["Average"].max()
lowest  = k["Average"].min()
average = k["Average"].mean()

print(f"\nThe Highest Performing student {k[k['Average']==highest]['name'].iloc[0]} is {highest:.2f}")
print(f"\nThe Lowest Perfroming student {k[k['Average']==lowest]['name'].iloc[0]} is {lowest:.2f}")
print(f"\nThe Average of Entire class is : {average:.2f}")
print(f"Average Attendance: {k['ATDN'].mean():.2f}%")

print("\n-------------SUBJECT WISE ANALYSIS ---------------")
for subject in Subjects:
    print(f"\nSubject : {subject}")
    print(f"Average : {k[subject].mean():.2f}")
    print(f"Highest : {k[subject].max()}")
    print(f"Lowest : {k[subject].min()}")

top_performers = k.sort_values(
    by="Average",ascending=False
).head(3)

print("\n---------------TOP 3 PERFORMERS --------------------")
print(top_performers[["ID", "name", "Total Marks","Average", "Grade", "Result"]].to_string(index=False))

print("\n---------------Pass/Fail Statistics------------------------")
print(f"Students Passed : {(k['Result']=='Pass').sum()} ")
print(f"Students Failed : {(k['Result']=='Fail').sum()} ")

