#!/usr/bin/python
file_object = open('iplist.xml')
try:
    all_the_text = file_object.read( )
    print all_the_text
finally:
     file_object.close( )
