# Write a Python script to concatenate following dictionaries to create a new one
# Input
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Output
# {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

## Solution
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
final_dic={}

final_dic.update(dic1)
final_dic.update(dic2)
final_dic.update(dic3)

print(final_dic)

## Solution2

for i in (dic1, dic2, dic3):
    final_dic.update(i)
print(final_dic)