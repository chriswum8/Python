#!/usr/bin/python
# -*- coding: UTF-8 -*-


def printinfo( arg1, *vartuple ):
   "打印任何传入的参数"
   print "输出: "
   print arg1
   for var in vartuple:
      arg1 = arg1 + var
   print arg1

#test2

print printinfo(1,2,3,4,5)

