import numpy as np

z = np.array([[3,6,7],[1,9,4]])

print z[0:,:2]

p = np.array([18,8,7,2,7,15])
print p[4]

#*args allows to take more arguments as a list39
def testArgs(arg1,*args):
    print "first argument:",arg1
    for arg in args:
        print "Next argument through *args:",arg


testArgs('Hello','Welcome','to',"Hello World")

#**kwargs allows to take more arguments as keyworded like dictionaries


def testKwargs(arg1,**kwar3):
    print "first argument:",arg1
    for k,v in kwargs.iteritems():
        print k

dictVar = {"name":"sravan","age":34}

testKwargs("hi",**dictVar)