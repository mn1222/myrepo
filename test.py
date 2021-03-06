# SPECIFICATION:
#
# add8 emulates an 8-bit hardware adder.
# it takes 16 bits, representing two 8-bit
# numbers and a carry bit.
#
# TASK:
#
# Write test() such that it achieves 100% 
# statement coverage of the add8 function.

def add8(a0,a1,a2,a3,a4,a5,a6,a7,b0,b1,b2,b3,b4,b5,b6,b7,c0):
    s1 = False
    if (a0 != b0) != c0:
        s1 = True
    c1 = False
    if (a0 and b0) != (c0 and (a0 != b0)):
        c1 = True
    s2 = False
    if (a1 != b1) != c1:
        s2 = True
    c2 = False
    if (a1 and b1) != (c1 and (a1 != b1)):
        c2 = True
    s3 = False
    if (a2 != b2) != c2:
        s3 = True
    c3 = False
    if (a2 and b2) != (c2 and (a2 != b2)):
        c3 = True
    s4 = False
    if (a3 != b3) != c3:
        s4 = True
    c4 = False
    if (a3 and b3) != (c3 and (a3 != b3)):
        c4 = True
    s5 = False
    if (a4 != b4) != c4:
        s5 = True
    c5 = False
    if (a4 and b4) != (c4 and (a4 != b4)):
        c5 = True
    s6 = False
    if (a5 != b5) != c5:
        s6 = True
    c6 = False
    if (a5 and b5) != (c5 and (a5 != b5)):
        c6 = True
    s7 = False
    if (a6 != b6) != c6:
        s7 = True
    c7 = False
    if (a6 and b6) != (c6 and (a6 != b6)):
        c7 = True
    s8 = False
    if (a7 != b7) != c7:
        s8 = True
    c8 = False
    if (a7 and b7) != (c7 and (a7 != b7)):
        c8 = True
    return (s1,s2,s3,s4,s5,s6,s7,s8,c8)

def test():
    # Write test cases that achieve 100% 
    # Statement coverage of add8. You 
    # will need to call add8 multiple 
    # times in order to do this.
    ###Your code here.
    #print(add8(False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False))
    assert 0==helperFunction(0,0)
    assert 1==helperFunction(0,1)
    assert 2==helperFunction(1,1)

# Calls add8 with bit-representations of sum1 and sum2. Result of add8 is returned.
def helperFunction(sum1,sum2):	
	a0=sum1%2
	sum1=int(sum1/2)
	a1=sum1%2
	sum1=int(sum1/2)
	a2=sum1%2
	sum1=int(sum1/2)
	a3=sum1%2
	sum1=int(sum1/2)
	a4=sum1%2
	sum1=int(sum1/2)
	a5=sum1%2
	sum1=int(sum1/2)
	a6=sum1%2
	sum1=int(sum1/2)
	a7=sum1%2
	sum1=int(sum1/2)
	b0=sum2%2
	sum2=int(sum2/2)
	b1=sum2%2
	sum2=int(sum2/2)
	b2=sum2%2
	sum2=int(sum2/2)
	b3=sum2%2
	sum2=int(sum2/2)
	b4=sum2%2
	sum2=int(sum2/2)
	b5=sum2%2
	sum2=int(sum2/2)
	b6=sum2%2
	sum2=int(sum2/2)
	b7=sum2%2
	sum2=int(sum2/2)
	res = add8(a0,a1,a2,a3,a4,a5,a6,a7,b0,b1,b2,b3,b4,b5,b6,b7,0)
	#print((a0,a1,a2,a3,a4,a5,a6,a7))
	#print((b0,b1,b2,b3,b4,b5,b6,b7))
	#print(res)
	return int(res[0])+int(res[1])*2+int(res[2])*4+int(res[3])*8+int(res[4])*16+int(res[5])*32+int(res[6])*64+int(res[7])*128
	
test()
