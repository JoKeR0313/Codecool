print("The following doors are open:")

doors = [0] * 100  #Create a list, with 100 pcs of 0.

for x in range (1, 101):
    for status in range (100):
        if (status + 1) % x == 0:  #status+1 (0 is the first index)
            if doors[status] == 0: #0 means that the door is closed, 1 means the opened status.
               doors[status] = 1   
            else:
                doors[status] = 0

for status in range(100): #Counting the opened doors.
    if doors[status] == 1:
        print(status+1 ,end=" ")
