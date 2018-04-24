dict1 = [{'name':'vaari' , 'point':100} , { 'name':'nidhi' ,'point' :110}]
l1 = map(lambda x:x['name'] , dict1)
print(list(l1))

#_________________________________________________________________________
l2 = map(lambda x:x['point'] , dict1)
print(list(l2))

#______________________________________________________________________
a =[1,2,3,4]
b=[1,1,1,1]
l3 = map(lambda x,y : x+y ,a,b)
print(list(l3))

f = filter(lambda x:x%2==0,a)
print(list(f))

