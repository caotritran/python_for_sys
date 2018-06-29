import os

def PingCheck():
    ### Ham doc file
    with open("list_domain.txt", "r") as f:
        lines = f.readlines()
        for l in lines:
            check = os.system("ping -c 2 " + l.strip("\n") + " > /dev/null 2>&1")
            #check = os.system("ping -c 2 " + l.strip("\n"))

            if check == 0:
                print("ping " + l.strip("\n") + ": OK!")
            else:
                print("ping " + l.strip("\n") + ": NOT OK!")
                # print(check)
            #print(l.rstrip("\n"))
    ###
if __name__ == '__main__':
    PingCheck()
