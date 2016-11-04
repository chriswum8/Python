#!/usr/bin/python
# -*- coding: UTF-8 -*-


def printinfo( arg1, *vartuple ):
   "打印任何传入的参数"
   print "输出: "
   print arg1
   for var in vartuple:
      arg1 = arg1 + var
   print arg1


print printinfo(1,2,3,4,5)


sum = lambda arg1, arg2: arg1 + arg2;

print sum(2,2)

