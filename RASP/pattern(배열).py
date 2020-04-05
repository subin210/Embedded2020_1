from tkinter import *
row=3
col=3
clWidth=500
clHeight=500
oldIndex=-1

cellSize=100
cellRectOrig={'l':(clWidth/3)/2-(cellSize/2),'t':(clHeight/3)/2-(cellSize/2),
          'r':(clWidth/3)/2+(cellSize/2),'b':(clHeight/3)/2+(cellSize/2)}
mClicked=0

root=Tk()

nPattern=[0,0,0,0,0,0,0,0,0]
inputPattern=[0,0,0,0,0,0,0,0,0]
pastCellNum=0
nofPatternCell=len(nPattern)

setPatternMode=False

def InitPatternArray(ptrn,initVar):
    global pastCellNum
    i=0

    if type(initVar)==int:
        while i<nofPatternCell:
            ptrn[i]=0
            i+=1
    else:
        while i<nofPatternCell:
            ptrn[i]=initVar[i]
            i+=1
            
    pastCellNum=0
    

def PointInRect(point,rect):
    if(((rect['l']<point['x'])and(rect['r']>point['x']))and
       ((rect['t']<point['y'])and(rect['b']>point['y']))):
        return True
    else:
        return False

def SetCellRect(index):
    cellColPos=(clWidth/3)*(index%col)
    cellRowPos=(clHeight/3)*(index//row)

    cellRect={'l':cellRectOrig['l']+cellColPos,
              't':cellRectOrig['t']+cellRowPos,
              'r':cellRectOrig['r']+cellColPos,
              'b':cellRectOrig['b']+cellRowPos}
    return cellRect

def DrawPattern(index,mpos):
    global inputPattern
    
    if oldIndex!=index:
        cellRect=SetCellRect(index)
        
    if PointInRect(mpos,cellRect):
        if not inputPattern[index]:
            global pastCellNum
            pastCellNum+=1
            inputPattern[index]=pastCellNum

def MouseMove(event):
    mPos={'x':event.x,'y':event.y}
    patternIndex=(int)((event.x//(clWidth/3))+(event.y//(clHeight/3)*col))
    DrawPattern(patternIndex,mPos)

def MouseRelease(event):
    global nPattern
    global inputPattern
    global setPatternMode
    
    if setPatternMode:
        print("pattern setting done")
        InitPatternArray(nPattern,inputPattern)
        setPatternMode=False
    else:
        ComparePattern(inputPattern)
    InitPatternArray(inputPattern,0)

def ComparePattern(ipttrn):
    i=0
    
    while i<nofPatternCell:
        if ipttrn[i]!=nPattern[i]:
            print("fail")
            return
        i+=1
    print("success")

def ChangeInputMode():
    global setPatternMode
    global nPattern
    global inputPattern
    
    if not setPatternMode:
        print("pattern setting mode")
        InitPatternArray(inputPattern,0)
        InitPatternArray(nPattern,0)
        setPatternMode=True

frame=Frame(root,width=clWidth,height=clHeight)
frame.bind("<B1-Motion>",MouseMove)
frame.bind("<ButtonRelease-1>",MouseRelease)
setPatternBtn=Button(root,text='set pattern',command=ChangeInputMode)
setPatternBtn.pack()
frame.pack()

root.mainloop()
