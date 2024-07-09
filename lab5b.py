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

def append_file_string(file_name, string_of_lines):
    f = open(file_name, 'a')
    f.write(string_of_lines)
    f.close()
    # Takes two strings, appends the string to the end of the file
    
def write_file_list(file_name, list_of_lines):
    f = open(file_name, 'w')
    for line in list_of_lines:
        f.write(line + '\n')
    f.close()
    # Takes a string and list, writes all items from list to file where each item is one line

def copy_file_add_line_numbers(file_name_read, file_name_write):
    f = open(file_name_read, 'r')
    read = f.readlines()
    f.close()
   
    f = open(file_name_write, 'w')
    num = 1
    for l in read:
        f.write(str(num) + ":" + l)
        num += 1
    f.close()
    # Takes two strings, reads data from first file, writes data to new file, adds line number to new file

if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']

    append_file_string(file1, string1)
    print(read_file_string(file1))
    write_file_list(file2, list1)
    print(read_file_string(file2))
    copy_file_add_line_numbers(file2, file3)
    print(read_file_string(file3))

