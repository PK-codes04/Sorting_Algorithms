from string import printable
from numpy import save
from BubbleSort import bubble_sort
from HeapSort import heap_sort
from InsertionSort import insertion_sort
from MergeSort import merge_sort
from Quicksort_regular import quicksort_r
from Quicksort import quickSort
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
root.geometry("900x700")
# root.maxsize(1000, 1000)


frame1 = Frame(root, borderwidth=2, relief='ridge')
frame2 = Frame(root, borderwidth=2, relief='ridge')
frame3 = Frame(root, borderwidth=2, relief='ridge')
frame4 = Frame(root, borderwidth=2, relief='ridge')
frame5 = Frame(root, borderwidth=2, relief='ridge')
frame6 = Frame(root, borderwidth=2, relief='ridge')


frame1.grid(column=0, row=0, sticky="nsew", columnspan=2)
frame2.grid(column=0, row=1, sticky="nsew", columnspan=2)
frame3.grid(column=0, row=2, sticky="nsew", columnspan=2)
frame4.grid(column=0, row=3, sticky="nsew", columnspan=2)
frame5.grid(column=0, row=5, sticky="nsew", columnspan=2)
frame6.grid(column=0, row=4, sticky="nsew", columnspan=2)

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
    global arr

    a=entry1.get()
    print('value a: ',a)
    arr=[int(item) for item in a.split()][:int(size)]
    print(arr)
    #if(a=="" and var.get()=="0"):
    if(var.get()=="0"):
        rnd_list=random_fun(size)
        arr = rnd_list
        print("you are here",rnd_list)        
        print(a)
        a=""
        a=",".join([str(i) for i in rnd_list])
    output1= "Your input series is : " + a
    print(output1)
    fh = open("input.txt","w")
    for num in arr:
        fh.write(str(num)+"\n")
    myLabel1=Label(frame2,text="Input sequence saved in input.txt file",wraplength=1000, justify="left") 
    myLabel1.pack()
    """
    if int(size)<1500:
    # frame2.pack(expand=False, fill=BOTH) #.grid(row=0,column=0)
        canvas=Canvas(frame2,bg='#FFFFFF',width=700,height=700,scrollregion=(0,0,3000,3000))
        hbar=Scrollbar(frame2,orient=HORIZONTAL)
        hbar.pack(side=BOTTOM,fill=X)
        hbar.config(command=canvas.xview)
        vbar=Scrollbar(frame2,orient=VERTICAL)
        vbar.pack(side=RIGHT,fill=Y)
        vbar.config(command=canvas.yview)
        canvas.config(width=4000,height=4000)
        canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
        canvas.pack(side=LEFT,expand=True,fill=BOTH)    
    
        myLabel1=Label(canvas,text=output1,wraplength=1000, justify="left") 
        myLabel1.grid(row =6, column = 0)
        entry1.delete(0, END)
    """
    

myButton1=Button(frame2,text="Enter", command=myClick1)
myButton1.pack()#.grid(row =5, column = 0,padx=40)

#--------------------------------------------------------------------------------------------------

l3=Label(frame4, text='Select preferred sorting Algorithm:')
l3.pack()

v = IntVar()
v.set(1)  # initializing the choice, i.e. Create
def ShowChoice():
    print(v.get())
    
Radiobutton(frame4,text="Bubble Sort",padx = 20,variable=v,command=ShowChoice,value=1).pack()
Radiobutton(frame4,text="Heap Sort",padx = 20,variable=v,command=ShowChoice,value=2).pack()
Radiobutton(frame4,text="Insertion Sort",padx = 20,variable=v,command=ShowChoice,value=3).pack()
Radiobutton(frame4,text="Merge Sort",padx = 20,variable=v,command=ShowChoice,value=4).pack()
Radiobutton(frame4,text="Quick Sort",padx = 20,variable=v,command=ShowChoice,value=5).pack()
Radiobutton(frame4,text="Quick Sort Median",padx = 20,variable=v,command=ShowChoice,value=6).pack()
Radiobutton(frame4,text="Selection Sort",padx = 20,variable=v,command=ShowChoice,value=7).pack()
Radiobutton(frame4,text="All",padx = 20,variable=v,command=ShowChoice,value=8).pack()


ret=-1
return_index=''
def myClick2():
    global myLabel3
    global arr
    global print_arr_string
    print("Numbers to be sorted:",arr)
    save_file = "\n"
    if v.get()==1:
        st_time = time.time()       
        ret_arr=bubble_sort(arr)
        end_time = time.time()
        total_time = str(end_time-st_time)+" seconds"
        print_arr_string = '\n'.join(str(x) for x in ret_arr)
        print_text += "Sorted List of Numbers using Bubble Sort:\n"+print_arr_string+"\n"+total_time+"\n"
        save_file += print_text
        #myLabel3=Label(frame5,text=print_text)
        #myLabel3.pack()
    elif v.get()==2:
        st_time = time.time()       
        ret_arr=heap_sort(arr)
        end_time = time.time()
        total_time = str(end_time-st_time)+" seconds"
        print_arr_string = '\n'.join(str(x) for x in ret_arr)
        print_text += "Sorted List of Numbers using Heap Sort:\n"+print_arr_string+"\n"+total_time+"\n"
        save_file += print_text
        #myLabel3=Label(frame5,text=print_text)
        #myLabel3.pack()
    elif v.get()==3:
        st_time = time.time()       
        ret_arr=insertion_sort(arr)
        end_time = time.time()
        total_time = str(end_time-st_time)+" seconds"
        print_arr_string = '\n'.join(str(x) for x in ret_arr)
        print_text = "Sorted List of Numbers using Insertion Sort:\n"+print_arr_string+"\n"+total_time+"\n"
        save_file += print_text
        #myLabel3=Label(frame5,text=print_text)
        #myLabel3.pack()
    elif v.get()==4:
        st_time = time.time()       
        ret_arr=merge_sort(arr)
        end_time = time.time()
        total_time = str(end_time-st_time)+" seconds"
        print_arr_string = '\n'.join(str(x) for x in ret_arr)
        print_text = "Sorted List of Numbers using Merge Sort:\n"+print_arr_string+"\n"+total_time+"\n"
        save_file += print_text
        #myLabel3=Label(frame5,text=print_text)
        #myLabel3.pack()
    elif v.get()==5:
        st_time = time.time()       
        ret_arr=quicksort_r(arr, 0, len(arr)-1)
        end_time = time.time()
        total_time = str(end_time-st_time)+" seconds"
        print_arr_string = '\n'.join(str(x) for x in ret_arr)
        print_text = "Sorted List of Numbers using Quick Sort:\n"+print_arr_string+"\n"+total_time+"\n"
        save_file += print_text
        #myLabel3=Label(frame5,text=print_text)
        #myLabel3.pack()
    elif v.get()==6:
        st_time = time.time()       
        ret_arr=quickSort(arr, 0, len(arr)-1)
        end_time = time.time()
        total_time = str(end_time-st_time)+" seconds"
        print_arr_string = '\n'.join(str(x) for x in ret_arr)
        print_text = "Sorted List of Numbers using Quick Sort Median:\n"+print_arr_string+"\n"+total_time+"\n"
        save_file += print_text
        #myLabel3=Label(frame5,text=print_text)
        #myLabel3.pack()
    elif v.get()==7:
        st_time = time.time()       
        ret_arr=selection_sort(arr)
        end_time = time.time()
        total_time = str(end_time-st_time)+" seconds"
        print_arr_string = '\n'.join(str(x) for x in ret_arr)
        print_text = "Sorted List of Numbers using Selection Sort:\n"+print_arr_string+"\n"+total_time+"\n"
        save_file += print_text
        #myLabel3=Label(frame5,text=print_text)
        #myLabel3.pack()
    elif v.get()==8:
        st_time = time.time()       
        ret_arr=bubble_sort(arr)
        end_time = time.time()
        total_time = str(end_time-st_time)+" seconds"
        print_arr_string = '\n'.join(str(x) for x in ret_arr)
        save_file += "Sorted List of Numbers using Bubble Sort:\n"+print_arr_string+"\n"+total_time+"\n"
        #myLabel3=Label(frame5,text="Sorted List of Numbers using Bubble Sort:"+print_arr_string+"\n"+total_time+"\n")
        #myLabel3.pack()

        st_time = time.time()       
        ret_arr=heap_sort(arr)
        end_time = time.time()
        total_time = str(end_time-st_time)+" seconds"
        print_arr_string = '\n'.join(str(x) for x in ret_arr)
        save_file += "Sorted List of Numbers using Heap Sort:\n"+print_arr_string+"\n"+total_time+"\n"
        #myLabel3=Label(frame5,text="Sorted List of Numbers using Heap Sort:"+print_arr_string+"\n"+total_time+"\n")
        #myLabel3.pack()

        st_time = time.time()       
        ret_arr=insertion_sort(arr)
        end_time = time.time()
        total_time = str(end_time-st_time)+" seconds"
        print_arr_string = '\n'.join(str(x) for x in ret_arr)
        save_file += "Sorted List of Numbers using Insertion Sort:\n"+print_arr_string+"\n"+total_time+"\n"
        #myLabel3=Label(frame5,text="Sorted List of Numbers using Insertion Sort:"+print_arr_string+"\n"+total_time+"\n")
        #myLabel3.pack()

        st_time = time.time()       
        ret_arr=merge_sort(arr)
        end_time = time.time()
        total_time = str(end_time-st_time)+" seconds"
        print_arr_string = '\n'.join(str(x) for x in ret_arr)
        save_file += "Sorted List of Numbers using Merge Sort:\n"+print_arr_string+"\n"+total_time+"\n"
        #myLabel3=Label(frame5,text="Sorted List of Numbers using Merge Sort:"+print_arr_string+"\n"+total_time+"\n")
        #myLabel3.pack() 

        st_time = time.time()       
        ret_arr=quicksort_r(arr, 0, len(arr)-1)
        end_time = time.time()
        total_time = str(end_time-st_time)+" seconds"
        print_arr_string = '\n'.join(str(x) for x in ret_arr)
        save_file += "Sorted List of Numbers using Quick Sort:\n"+print_arr_string+"\n"+total_time+"\n"
        #myLabel3=Label(frame5,text="Sorted List of Numbers using Quick Sort:"+print_arr_string+"\n"+total_time+"\n")
        #myLabel3.pack()   

        st_time = time.time()       
        ret_arr=quickSort(arr, 0, len(arr)-1)
        end_time = time.time()
        total_time = str(end_time-st_time)+" seconds"
        print_arr_string = '\n'.join(str(x) for x in ret_arr)
        save_file += "Sorted List of Numbers using Quick Sort Median:\n"+print_arr_string+"\n"+total_time+"\n"
        #myLabel3=Label(frame5,text="Sorted List of Numbers using Quick Sort Median:"+print_arr_string+"\n"+total_time+"\n")
        #myLabel3.pack()       

        st_time = time.time()       
        ret_arr=selection_sort(arr)
        end_time = time.time()
        total_time = str(end_time-st_time)+" seconds"
        print_arr_string = '\n'.join(str(x) for x in ret_arr)
        save_file += "Sorted List of Numbers using Selection Sort:\n"+print_arr_string+"\n"+total_time+"\n"
        #myLabel3=Label(frame5,text="Sorted List of Numbers using Selection Sort:"+print_arr_string+"\n"+total_time+"\n")
        #myLabel3.pack()
    print(v)
    fh = open("results.txt","w")
    fh.write(save_file)


myButton2=Button(frame6,text="Sort and Save to file", command=myClick2,padx=40)
myButton2.pack()


def myClick3():
    if output0!='':
        myLabel0.destroy()
    if output1!='':
        myLabel1.destroy()
    #myLabel3.destroy()
    frame5.grid_forget()
    


myButton3=Button(frame6,text="Clear All", command=myClick3,padx=40)
myButton3.pack()

#--------------------------------------------------------------------------------------------------


root.mainloop()
