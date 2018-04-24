a = [12,2, 3,45 ,78,7]
g = filter (lambda x:x%2==0 , a)
print(list(g))
### filter returns only the specific value satisfied by the func or the lambda
### but map returns all the lements of an iterable whether satisfed or not
