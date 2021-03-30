#!/usr/bin/python3

def main():

    fileloc = input("Where is the file to open? ")

    with open(fileloc, "a") as myfile:
        myfile.write("We added this line to the bottom of the file\n")
    
    # old way of opening a file (you'll still see this)
    myfile = open(fileloc,"r")


    print(myfile.read())
    myfile.close()
 

if __name__ == "__main__":
    main()
