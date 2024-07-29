grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
a=sum(grades [0])
b=sum(grades [1])
c=sum(grades [2])
d=sum(grades [3])
e=sum(grades [4])
a1=sum(grades [0])/len(grades [0])
b1=sum(grades [1])/len(grades [1])
c1=sum(grades [2])/len(grades [2])
d1=sum(grades [3])/len(grades [3])
e1=sum(grades [4])/len(grades [4])
bal=[a1,b1,c1,d1,e1]
print([a1,b1,c1,d1,e1])

Alfavit=sorted(students)
print(Alfavit)
new_dict=dict(zip(Alfavit,bal))
print(new_dict)






