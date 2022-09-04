List = ['123', 'root', 'GO', 'Job23', 'Global', 'INT', 'Intfo', 'Foo']
NewList = []

for i in List:
    if len(i) <= 3: 
        print(i)
        NewList.append(i)       

print(NewList)