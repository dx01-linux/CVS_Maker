#!/usr/bin/env python3


import re
import pathlib

PATH = pathlib.Path("../").parent
INPUT = PATH.joinpath("input.txt")
OUTPUT = PATH.joinpath("output.txt")

def main():
    data = []
    # open a file in read mode 
    with open(f"{INPUT.absolute()}" ,"r") as file:

            for line in file :
                # IF new line char at the end convert string to array and replace it 
                new_line = re.findall(f"\n" , line)
                
                #  last line in the stream
                if(new_line.__len__() == 0):
                    data.append(line)
                    break    
                
                # regular line in the stream
                elif(new_line.__len__() > 0):
                    holder = line.split()
                    holder = "".join(holder) + ","     
                    data.append(holder)    



    with open(OUTPUT ,"a") as file :
         for line in data :
              file.write(line)
main()