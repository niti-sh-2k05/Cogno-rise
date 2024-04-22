import time

def timer(inp_time):

    print("Your coundown starts...")

    while(inp_time>0):

        print(inp_time)

    time.sleep(1)

    inp_time=1

    print("Time up!")

def main():

 inp_time=int(input("Enter the time to be counted:"))

if(inp_time>0):
    return timer(inp_time);  

else:

         print("Please enter a valid Time to be counted.")

main()