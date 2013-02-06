#! /usr/bin/python
# -*- coding:utf-8 -*-

"""
Issue was when some friend of mine got new smart phone and transated its
contacts from the old cell phone she couldn't see contacts picture in address
book and when the contact was calling or she called a contact.
A have noticed tha she dosn't have the correct phone number on all of theres
contact. Contry code was (like +381) was missing on most of phone numbers.
It would be to annoing to change manulay all the contacts phone, so I decided to
help her and I wrote a small script that checks and changes if phone number was
incorrect in '.vcf' files.
"""

#import re
import os


def collect_file_names(directory):
    collection = []

    # Listing directory.
    for dirpath, dirnames, filenames in os.walk(directory):
        pass
    for filename in filenames:
        #collection.append(str(os.path.join(dirpath, filename)))
        collection.append(filename)
    #print collection
    return collection


def open_file(file_name):
    fp = open(file_name, 'r')
    content = fp.readlines()

    fp.close()

    return content


def find_change(content):
    new_content = []
    TCELL = 'TEL;CELL:'
    TEL = 'TEL:'
    INSERT_SR = '+381'

    for line in content:
        tmp_line = line

        if line.startswith(TCELL):
            line = TCELL

            if tmp_line[len(TCELL):len(TCELL) + 1] == '0':
                line += INSERT_SR
                line += tmp_line[len(TCELL) + 1:]

            else:
                line += tmp_line[len(TCELL):]  # If tel number is already correct.

        elif line.startswith(TEL):
            line = TEL

            if tmp_line[len(TEL):len(TEL) + 1] == '0':
                line += INSERT_SR
                line += tmp_line[len(TEL) + 1:]

            else:
                line += tmp_line[len(TEL):]  # If tel number is already correct.

        new_content.append(line)

    return new_content


def write_changes(file_name, new_content):
    #dir_path = os.path.abspath('.')
    #dir_path = os.path.join(dir_path, 'output')

    fp = open(file_name, 'w')
    fp.writelines(new_content)
    fp.close()


def main():
    """
    Create 'test' and 'output' directories.
    test dir is for testing. First copy there all your .vcf files,
    and work there first.
    """
    dir_path = os.path.abspath('.')
    dir_path_input = os.path.join(dir_path, 'test')
    dir_path_output = os.path.join(dir_path, 'output')

    file_names = collect_file_names(dir_path)

    for file_name in file_names:
        content = open_file(os.path.join(dir_path_input, file_name))

        new_content = find_change(content)  # This just changes the new string.

        # Write changes to the output directory
        write_changes(os.path.join(dir_path_output, file_name), new_content)

    return "Finished"

if __name__ == "__main__":
    main()

# vim: tw=79:
