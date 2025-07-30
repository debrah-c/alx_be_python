size = int(input("Enter the size of the pattern:"))  #should be positive integer
i = 0
while i < size:
    for j in range(size):
        print("*", end=" ")
    print()
    i += 1
    
