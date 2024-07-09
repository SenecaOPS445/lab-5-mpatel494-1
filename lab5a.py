#!/usr/bin/env python3
# Author ID: mpatel494

def read_file_string(file_name):
    f = open(file_name, 'r')
    read_file = f.read()
    f.close()
    return read_file
    # Takes file_name as string for a file name, returns its entire contents as a string

def read_file_list(file_name):
    f = open(file_name, 'r')
    listing = f.readlines()
    f.close()
    return [line.rstrip('\n') for line in listing]
    # Takes a file_name as string for a file name, 
    # return its entire contents as a list of lines without new-line characters

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))

