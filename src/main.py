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
    
                new_line_chars = re.findall(f"\n" , line)
                
                #  IF line does not have a new line char , it is the the stream's end 
                if(new_line_chars.__len__() == 0):
                    data.append(line)
                    break    
                
                # ELSE it is a regular line in the stream , need to replace new line char for comma 
                holder = line.split()
                holder = "".join(holder) + ","     
                data.append(holder)    


    # create output file and append the modified input's content 
    with open(OUTPUT ,"a") as file :
         for line in data :
              file.write(line)
main()