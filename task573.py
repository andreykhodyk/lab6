list1 = [int(x) for x in input().split()]
list2 = [int(x) for x in input().split()]

common = set(list1) & set(list2)

for num in sorted(common):
    print(num, end=' ')