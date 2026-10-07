# 1. structure : []
li = [10, 20, 30, 40]

print (type(li)) #<class 'list'>

#2. Type of data: Heterogeneous
li_1 = [10, 20, 30, 40,'abc']
print (type(li_1)) #<class 'list'>
print(li_1)#[10, 20, 30, 40, 'abc']

#3. Sequential: Ordered
print (li) #[10, 20, 30, 40]

#4. Changable: Mutable
li_2 = [10, 20, 30, 40,'abc']
print(id(li_2)) #2221150187264
li_2[0]=50
print(li_2) #[50, 20, 30, 40, 'abc']
print(id(li_2))#2221150187264
#5. Duplication: Allowed
