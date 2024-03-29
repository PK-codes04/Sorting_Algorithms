from SelectionSort import selection_sort
from tkinter import ttk
from tkinter import *
import random
import time

randomlist = []
max_limit=1000000

def random_fun(size):
    #randomlist=[]
    # for i in range(0,int(size)):
    while len(randomlist)<int(size):
        r=random.randint(1,max_limit)          
        if r not in randomlist: randomlist.append(r)
    print(randomlist)
    return(randomlist)


root = Tk()
root.title('Sorting Algorithms')
root.geometry("600x700")
root.minsize(620, 750)
# root.maxsize(1000, 1000)


frame1 = Frame(root, borderwidth=2, relief='ridge')
frame2 = Frame(root, borderwidth=2, relief='ridge')
frame3 = Frame(root, borderwidth=2, relief='ridge')
frame4 = Frame(root, borderwidth=2, relief='ridge')
frame5 = Frame(root, borderwidth=2, relief='ridge')

frame1.grid(column=0, row=0, sticky="nsew", columnspan=2)
frame2.grid(column=0, row=1, sticky="nsew", columnspan=2)
frame3.grid(column=0, row=2, sticky="nsew", columnspan=2)
frame4.grid(column=0, row=3, sticky="nsew", columnspan=2)
frame5.grid(column=0, row=4, sticky="nsew", columnspan=2)

l0=Label(frame1, text='Enter Array size: ')
l0.pack()
entry0 = Entry(frame1, width=10,borderwidth=4)
entry0.pack()
entry0.insert(0,'')

def myClick0():
    global size
    global myLabel0
    global output0
    size=entry0.get()
    print(size)
    output0= "Entered Array size: " + entry0.get()
    myLabel0=Label(frame1,text=output0)
    myLabel0.pack()
    entry0.delete(0, END)
    
myButton0=Button(frame1,text="Enter", command=myClick0,padx=30 )
myButton0.pack()

#--------------------------------------------------------------------------------------------------

l1=Label(frame2, text='Would you like to create sequence/randomly?')
l1.pack()#grid(row = 1, column = 0)

rnd=IntVar()
#callbacks
def enableEntry():
    #
    entry1.configure(state="normal")
    entry1.update()
    entry1.delete(0, END)
    rnd=0
    print("rnd: ",rnd)

def disableEntry():
    entry1.delete(0, END)
    entry1.configure(state="disabled")
    entry1.update()
    
    rnd=1
    print("rnd: ",rnd)

var = StringVar()
var.set(1)
disableEntryRadioButton = Radiobutton(frame2, text="Create Random Series", variable=var, value="0", command=disableEntry)
disableEntryRadioButton.pack()#.grid(row = 2, column = 0)#(anchor=W)
enableEntryRadioButton = Radiobutton(frame2, text="Enter Series(separated by spaces)", variable=var, value="1", command=enableEntry)
enableEntryRadioButton.pack()#.grid(row = 3, column = 0)#.pack(anchor=W)

#GUI widgets
entry1 = Entry(frame2, width=100,borderwidth=4)
entry1.pack()#grid(row =4, column = 0)
entry1.insert(0,'')


def myClick1():
    global myLabel1
    global output1
    global randomlist
    a=entry1.get()
    print('value a: ',a)
    randomlist=[int(item) for item in a.split()][:int(size)]
    print(randomlist)
    #if(a=="" and var.get()=="0"):
    if(var.get()=="0"):
        rnd_list=random_fun(size)
        print("you are here",rnd_list)        
        print(a)
        a=""
        a=",".join([str(i) for i in rnd_list])
    output1= "Your input series is : " + a
    print(output1)
    if int(size)<50:
    # frame2.pack(expand=False, fill=BOTH) #.grid(row=0,column=0)
        canvas=Canvas(frame2,bg='#FFFFFF',width=70,height=70,scrollregion=(0,0,500,500))
        hbar=Scrollbar(frame2,orient=HORIZONTAL)
        hbar.pack(side=BOTTOM,fill=X)
        hbar.config(command=canvas.xview)
        vbar=Scrollbar(frame2,orient=VERTICAL)
        vbar.pack(side=RIGHT,fill=Y)
        vbar.config(command=canvas.yview)
        canvas.config(width=100,height=100)
        canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
        canvas.pack(side=LEFT,expand=True,fill=BOTH)    
    
        myLabel1=Label(canvas,text=output1,wraplength=1000, justify="left") 
        myLabel1.grid(row =6, column = 0)
        entry1.delete(0, END)

myButton1=Button(frame2,text="Enter", command=myClick1)
myButton1.pack()#.grid(row =5, column = 0,padx=40)


#--------------------------------------------------------------------------------------------------
"""
l2=Label(frame3, text='Enter the number to be searched:')
l2.pack()
entry2 = Entry(frame3, width=40,borderwidth=4)
entry2.pack()
entry2.insert(0,'')


def myClick2():
    global myLabel2
    global output2
    global num
    num_str=entry2.get()
    num=int(num_str)
    output2= "Number to be searched is  : " + num_str
    myLabel2=Label(frame3,text=output2)
    myLabel2.pack()
    entry0.delete(0, END)
    entry1.delete(0, END)
    entry2.delete(0, END)
    
myButton2=Button(frame3,text="Enter", command=myClick2,padx=40)
myButton2.pack()#

"""
#--------------------------------------------------------------------------------------------------

l2=Label(frame4, text='Select preferred sorting Algorithm:')
l2.pack()

v = IntVar()
v.set(1)  # initializing the choice, i.e. Create
def ShowChoice():
    print(v.get())
    
Radiobutton(frame4,text="selection sort",padx = 20,variable=v,command=ShowChoice,value=1).pack()
Radiobutton(frame4,text="Binary Search",padx = 20,variable=v,command=ShowChoice,value=2).pack()
Radiobutton(frame4,text="Binary Search Tree",padx = 20,variable=v,command=ShowChoice,value=3).pack()
Radiobutton(frame4,text="Red Black Tree",padx = 20,variable=v,command=ShowChoice,value=4).pack()
Radiobutton(frame4,text="Runtime Comparision",padx = 20,variable=v,command=ShowChoice,value=5).pack()


ret=-1
return_index=''
def myClick2():
    global myLabel2
    #print("number value is -----------------",num)
    print("random list is",randomlist)
    if v.get()==1:
        # Linear Search        
        t1=selection_sort(randomlist)
        print(randomlist)
    """         
        return_index1=str(ret1)
        if ret1!=-1:
            myLabel3=Label(frame5,text="Linear Search: Found at index -> " + return_index1 +" \n and runtime for linear search algorithm is "+t1,font=("Ariel 11 bold"))
        else:
            myLabel3=Label(frame5,text="Linear Search: Key not found in Array \nand runtime for linear search algorithm is "+t1,font=("Ariel 11 bold"))
    elif v.get()==2:
        # Binary Search        
        ret2,sorted_arr,t2=binary_search(randomlist,num)
        
        print(ret2)
        return_index2=str(ret2)
        if ret2!=-1:
            myLabel3=Label(frame5,text="Binary Search: For Sorted array: "+str(sorted_arr)+" \nFound at index -> " + return_index2+" \nand runtime for binary search algorithm is "+t2,font=("Ariel 11 bold"))
        else:
            myLabel3=Label(frame5,text="Binary Search: Key not found in Array: "+str(sorted_arr)+" \n and runtime for binary search algorithm is "+t2,font=("Ariel 11 bold"))
    elif v.get()==3:
        # Binary Search Tree
        ret3,t3=binary_search_tree(randomlist,num)
        
        if ret3!=-1:
            myLabel3=Label(frame5,text="Binary Search Tree: Key Found \nand runtime for binary search algorithm is "+t3,font=("Ariel 11 bold"))
        else:
            myLabel3=Label(frame5,text="Binary Search Tree: Key not found in Tree \nand runtime for binary search algorithm is "+t3,font=("Ariel 11 bold"))
        
        # img()
    elif v.get()==4:
        # Red Black Tree        
        ret4,t4=red_black_tree(randomlist,num)
        
        if ret4!=-1:
            myLabel3=Label(frame5,text="Red Black Tree: Key Found \nand runtime for binary search algorithm is "+t4,font=("Ariel 11 bold"))
        else:
            myLabel3=Label(frame5,text="Red Black Tree: Key not found in Tree \nand runtime for binary search algorithm is "+t4,font=("Ariel 11 bold"))
    else:
        ret1,t1=linear_search(randomlist,num)
        return_index1=str(ret1)

        ret2,sorted_arr,t2=binary_search(randomlist,num)
        return_index2=str(ret2)

        ret3,t3=binary_search_tree(randomlist,num)

        ret4,t4=red_black_tree(randomlist,num)

        if ret1!=-1 and ret2!=-1 and ret3!=-1 and ret3!=-1 and ret4!=-1:
            text1="Linear Search: Found at index -> " + return_index1 +" \n and runtime for linear search algorithm is "+t1 +"\n Binary Search: Found at index -> " + return_index2+" \n and runtime for binary search algorithm is "+t2+"\n Binary Search Tree: Key Found \n and runtime for binary search algorithm is "+t3+"\n Red Black Tree: Key Found \n and runtime for binary search algorithm is "+t4

            myLabel3=Label(frame5,text=text1,font=("Ariel 11 bold"))
        else:
            text2="Binary Search: Key not found in Array \n and runtime for binary search algorithm is "+t2+"\n Binary Search: Key not found in Array \n and runtime for binary search algorithm is "+t2+"\n Binary Search Tree: Key not found in Tree \n and runtime for binary search algorithm is "+t3+"\n Red Black Tree: Key not found in Tree \n and runtime for binary search algorithm is "+t4
            myLabel3=Label(frame5,text=text2,font=("Ariel 11 bold"))
        print("Linear Search " + t1 + "\n Binary Search " + t2 + "\n Binary Seach Tree " + t3 + "\n Red Black Tree " + t4)
    print(v)
    """
    #myLabel=Label(root,text="Found")
    myLabel2.pack()
    entry0.delete(0, END)
    entry1.delete(0, END)

myButton2=Button(frame5,text="Search", command=myClick2,padx=40)
myButton2.pack()
"""
def myClick3():
    if output0!='':
        myLabel0.destroy()
    if output1!='':
        myLabel1.destroy()
    if output2!='':
        myLabel2.destroy()
    myLabel3.destroy()
"""
"""
myButton3=Button(frame5,text="Clear All", command=myClick3,padx=40)
myButton3.pack()
"""

#--------------------------------------------------------------------------------------------------


root.mainloop()
