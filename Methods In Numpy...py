import pandas as pd
mydata={'Students':["Jayesh","Bhavesh","Abhishek","Rishikesh"],
        'Percentage':[90,99,85,85]}
myresult=pd.DataFrame(mydata)
print(myresult)

li1=[10,20,30,0,50]
myele=pd.Series(li1)
print(myele)


li2=[100,200,300,400,500]
myele=pd.Series(li2,index=["A","B","C","D","E"])
print(myele)

calories={"Day1":420,"Day2":380,"Day3":400,"Day4":500,"Day5":350}
myele=pd.Series(calories)
print(myele)