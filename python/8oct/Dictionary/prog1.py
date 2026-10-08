student={
        101:{"name":"Aditi","scores":[78,98,45]},
        102:{"name":"shreya","scores":[86,92,67]},
        103:{"name":"sakshi","scores":[67,100,100]},
        104:{"name":"priya","scores":[57,82,74]},
        105:{"name":"sneha","scores":[79,87,70]}
    }

for sid,details in student.items():
           avg=sum(details["scores"])/len(details["scores"])
           details["average"]=avg
           details["passed"]=avg>=50

print("students who passed")
for sid ,details in student.items():
        if(details["passed"]):
                print(details["name"])