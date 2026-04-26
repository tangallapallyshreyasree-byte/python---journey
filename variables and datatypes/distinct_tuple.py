" check whether the given tuple is distinct or not "
arr = tuple(map(int, input().split()))
distinct_list = []
for x in arr:
    if x not in distinct_list:
        distinct_list.append(x)

distinct_tuple = tuple(distinct_list)

if len(arr) == len(distinct_tuple):
  print("already distinct :", distinct_tuple)
else:
  print("not distinct")
  print(" the distinct tuple is : " , distinct_tuple)
  
