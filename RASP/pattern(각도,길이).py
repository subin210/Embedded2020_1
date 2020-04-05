from tkinter import *
import tkinter.messagebox
import math
import collections

clWidth=500
clHeight=500

root=Tk()

Position=collections.namedtuple('pos',['x','y'])
Pattern=collections.namedtuple('ptrn',['deg','dist'])

mouseDownPos=Position(-1,-1)
mouseUpPos=Position(-1,-1)
inputPattern=[0,0]
nPattern=[0,0]
nofPattern=0
maxNofPattern=len(nPattern)

setPatternMode=False

def InitPatternArray(ptrn):
    i=0
    while i<maxNofPattern:
        ptrn[i]=0
        i+=1

def GetDegree(x,y):
    tx=ty=0
    nSet=[0,0,3,0,0,0,1,0,2]
    n=nSet[3*(1-(int)(math.fabs(x)/x))+(1-(int)(math.fabs(y)/y))]

    if n==1 or n==3:
        tx=y;ty=x
    else:
        tx=x;ty=y
    
    return (math.atan(math.fabs(ty)/math.fabs(tx))*(180.0/3.141592)+(90*n))

def GetPattern(dpos,upos):
    pattern=0
    dist=0.0
    vec=0.0
    degree=0.0
    
    tx=(float)(upos.x-dpos.x)
    ty=(float)(upos.y-dpos.y)
    print(dpos,upos)
    print(tx,ty)
    
    dist=math.sqrt((tx**2)+(ty**2))
    degree=GetDegree(tx,ty)
    pattern=Pattern(degree,dist)
    
    print(pattern)

    return pattern

def MouseClick(event):
    global mouseDownPos
    
    mouseDownPos=Position(event.x,event.y)

def MouseRelease(event):
    global mouseUpPos
    global inputPattern
    global nPattern
    global nofPattern
    global setPatternMode

    mouseUpPos=Position(event.x,event.y)
    print("release")
    #GetPattern(mouseDownPos,mouseUpPos,(sPattern if setPatternMode else pattern))
    if setPatternMode:
        nPattern[nofPattern]=GetPattern(mouseDownPos,mouseUpPos)
        
    else:
        inputPattern[nofPattern]=GetPattern(mouseDownPos,mouseUpPos)
    
    nofPattern+=1
    
    if nofPattern>=maxNofPattern:
        if setPatternMode:
            print("pattern set done",nPattern)
            setPatternMode=False
            nofPattern=0
        else:
            ComparePattern(inputPattern)
            nofPattern=0
            InitPatternArray(inputPattern)
        

def ComparePattern(ipttrn):
    i=0
    print("ipttrn",ipttrn)
    while i<maxNofPattern:
        if not(nPattern[i][0]-3.0<ipttrn[i][0]<nPattern[i][0]+3.0) and not (nPattern[i][1]-15.0<ipttrn[i][1]<nPattern[i][1]+15.0):
            print('fail')
            return
        i+=1
        
    print("sucess")

def ChangeInputMode():
    global setPatternMode
    global nPattern
    global inputPattern
    
    if not setPatternMode:
        print("pattern setting mode")
        InitPatternArray(inputPattern)
        InitPatternArray(nPattern)
        setPatternMode=True
    
frame=Frame(root,width=clWidth,height=clHeight)
frame.bind("<Button-1>",MouseClick)
frame.bind("<ButtonRelease-1>",MouseRelease)
setPatternBtn=Button(root,text='set pattern',command=ChangeInputMode)
setPatternBtn.pack()
frame.pack()

root.mainloop()
