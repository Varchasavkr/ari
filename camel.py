total=int(input('Enter no. of bananas at starting: '))
distance=int(input('Enter distance you want to cover: '))
load_capacity=int(input('Enter max load capacity of your camel: '))
lose=0
start=total
for i in range(distance):
    while start>0:
        start=start-load_capacity

        if start==1:
            lose=lose-1
        lose=lose+2

    lose=lose-1
    start=total-lose
    if start==0:
        break
print(start)

# Output
# Enter no. of bananas at starting: 3000
# Enter distance you want to cover: 1000
# Enter max load capacity of your camel: 1000
# 533

