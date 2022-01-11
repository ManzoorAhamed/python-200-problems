# Sum all the items in a dictionary
# Input {'data1':100,'data2':-54,'data3':247}
# Output 293

## Solution 1

d = {'data1':100,'data2':-54,'data3':247}
sum1 = int(0)
for key,value in d.items():
    sum1 += value

print("outptu",sum1)

## Solution 2
my_dict = {'data1':100,'data2':-54,'data3':247}
print(sum(my_dict.values()))