# create a file called data.txt
# add a few lines of text in it 
# write a python function that opens, reads, abd prints out cleanly

def read_file():
    with open("data.txt", "r") as file:
        for index, line in enumerate(file, start=1):
            print(f"{index}. {line.strip()}")


read_file() # remember to call the function