#!/usr/bin/python
# -*- coding:utf-8 -*-
import cgi
import cgitb
cgitb.enable()
##############other imports
import basic
############obligatory file topping
print ("Content-Type:text/html; charset=utf-8")
print("")
print ("<html><body>")
#############################################getting form data
request = cgi.FieldStorage()# got the form info, if any
#############################################################
#if 


##############################################################
if "copy" in request and "dir1" in request and "dir2"in request:
    basic.framer1 (request["dir1".value], request["dir2".value]) 
    print (''' Done!''')
##############################################################
else:
    print ("List of Extensions:")
    print ('''<form method="get">''')
##############################################################
#printing True's from the list of extensions
    formatsTrue = basic.accessFormats ()
    for i in formats:
        output_line = \
        '''<input type="checkbox" name={0}, value ={0} checked>{0}<br/>''' 
        output_line = output_line.format(i)
        print (output_line)
##############################################################
#printing False's from the list of extensions
    formatsFalse = basic.accessFormats (False) 
    output_line = '''<input type="checkbox" name={0}, value ={0}>{0}<br/>''' 
    output_line = output_line.format(i)
    print (output_line)
##############################################################
#printing fields for source and target directories
    print ('''
    <input type = "text" name = "dir1"/><br/>
    <input type = "text" name = "dir2"/><br/>
    <input type="submit" name = "copy" value = "copy"/><br/>

##############################################################
#printing other options
#printing fields for source and target directories
    <input type ="submit" name = "newList" value = "New List"/><br/>
    <input type ="submit" name = "default" value="Default List"/><br/>
    <input type "submit" name = "add" value = "Add Item"/><br/>
    <input type "submit" name = "delete" value = "Delete Item"/><br/>
    </form>''')
    

print ("</body></html>")
