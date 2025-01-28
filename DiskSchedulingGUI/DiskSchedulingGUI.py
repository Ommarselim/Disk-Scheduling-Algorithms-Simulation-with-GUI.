from tkinter import *
import turtle
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import time
from copy import copy
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
# 4 40 11 35 7 14
# 82 170 43 140 24 16 190
####################################################################################################################################################


def FCFS(Request, Start):
    Sum = 0                     #initialize to 0
    position = Start            #set current position = start
    Order = []                  # creates empty list of name Order
    Order.append(Start)         #adds Start to end of list Order
    for i in Request:           # i is the current element in the list(first loop i = 95)
        Sum += abs(i-position)  # sum = sum + (distance of current position from next position)
        position = i            # set position new position (i)
        Order.append(i)         # Add i to the end of the list Order
    return Order, Sum


####################################################################################################################################################


def SSTF(Request,Start):
    templist = copy(Request)
    position = Start
    highest = max(templist)
    mindiff=abs(Start-highest)
    j=highest
    templist.sort()
    Order = []
    Order.append(Start)
    Sum = 0
    while len(templist) > 0:
        for i in templist:
                diff= abs(position-i)
                if diff<mindiff:
                    mindiff=diff
                    j=i
        Sum+= abs(position-j)
        position = j
        templist.remove(j)
        Order.append(j)
        mindiff=abs(position-highest)
        j=highest
    return Order, Sum



####################################################################################################################################################


def SCAN_LEFT(Request, Start):
    n = len(Request)
    Order = []
    Request_tmp=copy(Request)
    Request_tmp.sort()
    if Start != 0 and Start < Request_tmp[n-1]:
        Request_tmp.append (0)
    p = len(Request_tmp)

    i = Start - 1
    Order.append(Start)
    while i >= 0:
        for j in range(0,p):
            if(Request_tmp[j] == i):
                Order.append(i)
        i -= 1



    k = Start + 1
    while k < 200:
        for l in range(0,n):
            if(Request[l] == k):
                Order.append(k)
        k += 1

    Sum = 0
    for p in range(0,len(Order) - 1):
        Sum += abs(Order[p] - Order[p+1])
    return Order, Sum



####################################################################################################################################################


def SCAN_RIGHT(Request, Start):
    n = len(Request)
    Order = []
    Request_tmp=copy(Request)
    Request_tmp.sort()
    if Start != 0 and Start < Request_tmp[n-1]:
        Request_tmp.append (199)
    p = len(Request_tmp)

    i = Start + 1
    Order.append(Start)
    while i <= 200:
        for j in range(0,p):
            if(Request_tmp[j] == i):
                Order.append(i)
        i += 1



    k = Start - 1
    while k > 0:
        for l in range(0,n):
            if(Request[l] == k):
                Order.append(k)
        k -= 1

    Sum = 0
    for p in range(0,len(Order) - 1):
        Sum += abs(Order[p] - Order[p+1])
    return Order, Sum

####################################################################################################################################################


def C_SCAN_LEFT(Request, Start):
    n = len(Request)
    Order = []
    Request_tmp=copy(Request)
    Request_tmp.sort()
    if Start != 0 and Start < Request_tmp[n-1]:
        Request_tmp.append (0)
    p = len(Request_tmp)

    i = Start - 1
    Order.append(Start)
    while i >= 0:
        for j in range(0,p):
            if(Request_tmp[j] == i):
                Order.append(i)
        i -= 1

    k = 199
    while k > Start:
        if(k == 199):
            Order.append(k)
        for l in range(0,n):
            if(Request[l] == k):
                Order.append(k)
        k -= 1

    Sum = 0
    
    for p in range(0,len(Order) - 1):
            Sum += abs(Order[p] - Order[p+1])
    return Order, Sum



####################################################################################################################################################


#82 170 43 140 24 16 190  FOR TEST
def C_SCAN_RIGHT(Request, Start):
    n = len(Request)
    Order = []
    Request_tmp=copy(Request)
    Request_tmp.sort()
    if Start != 0 and Start < Request_tmp[n-1]:
        Request_tmp.append (199)
    p = len(Request_tmp)

    i = Start +1
    Order.append(Start)
    while i <= 199:
        for j in range(0,p):
            if(Request_tmp[j] == i):
                Order.append(i)
        i += 1

    k = 0
    while k < Start:
        if(k == 0):
            Order.append(k)
        for l in range(0,n):
            if(Request[l] == k):
                Order.append(k)
        k += 1

    Sum = 0
    
    for p in range(0,len(Order) - 1):
            Sum += abs(Order[p] - Order[p+1])
    return Order, Sum
####################################################################################################################################################



def LOOK_LEFT(Request, Start):
    n = len(Request)                        # Number of Requests
    Order = []
    i = Start - 1
    Order.append(Start)
    while i > 0:                            # Diskhead moving outward from start
        for j in range(0,n):                    #position
            if(Request[j] == i):            # Request found
                Order.append(i)             # Request executed
        i -= 1

    k = Start + 1
    while k < 200:                          # Diskhead moving inward from
        for l in range(0,n):                    #previous position
            if(Request[l] == k):            # Request found
                Order.append(k)             # Request executed
        k += 1

    Sum = 0
    for p in range(0,len(Order) - 1):
        Sum += abs(Order[p] - Order[p+1])   # Calculates total movement
    return Order, Sum
####################################################################################################################################################


def LOOK_RIGHT(Request, Start):
    n = len(Request)                        # Number of Requests
    Order = []

    k = Start + 1
    Order.append(Start)

    while k < 200:                          # Diskhead moving inward from
        for l in range(0,n):                    #previous position
            if(Request[l] == k):            # Request found
                Order.append(k)             # Request executed
        k += 1

    
    i = Start - 1
    while i > 0:                            # Diskhead moving outward from start
        for j in range(0,n):                    #position
            if(Request[j] == i):            # Request found
                Order.append(i)             # Request executed
        i -= 1

    

    Sum = 0
    for p in range(0,len(Order) - 1):
        Sum += abs(Order[p] - Order[p+1])   # Calculates total movement
    return Order, Sum
####################################################################################################################################################




def CLOOK_LEFT(Request, Start):
    n = len(Request)                            # Number of requests
    Order = []
    i = Start - 1
    Order.append(Start)
    while i > 0:                                # Diskhead moving outward from
        for j in range(0,n):                        #start position
            if(Request[j] == i):                # Request found
                Order.append(i)                 # Request executed
        i -= 1

    k = 199
    while k > Start:                            # Diskhead moving inward from
        for l in range(0,n):                        #highest request position
            if(Request[l] == k):                # Request found
                Order.append(k)                 # Request executed
        k -= 1

    Sum = 0
    SortedReq = copy(Order)                     # Creates copy of job order
    SortedReq.sort()                            # Sorts job order from lowest to
    for p in range(0,len(Order) - 1):               #highest
        if (Order[p] != SortedReq[0]):          # Excludes the circular movement
            Sum += abs(Order[p] - Order[p+1])   # Calculates total movement
    return Order, Sum

####################################################################################################################################################



def CLOOK_RIGHT(Request, Start):
    n = len(Request)                            # Number of requests
    Order = []
    k = Start +1
    Order.append(Start)
    while k < 200:                          # Diskhead moving inward from
        for l in range(0,n):                    #previous position
            if(Request[l] == k):            # Request found
                Order.append(k)             # Request executed
        k += 1


    I = 1
    while I < Start:                            # Diskhead moving inward from
        for l in range(0,n):                        #highest request position
            if(Request[l] == I):                # Request found
                Order.append(I)                 # Request executed
        I += 1

    Sum = 0
    
    for p in range(0,len(Order) - 1):               #highest
               # Excludes the circular movement
            Sum += abs(Order[p] - Order[p+1])   # Calculates total movement
    return Order, Sum


####################################################################################################################################################





def graphy(request_arr, start):
    plot_list=[]
    algos=["FCFS","SSTF","SCAN-L","SCAN-R","C_SCAN-L","C_SCAN-R","LOOK-L","LOOK-R","CLOOK-L","CLOOK-R"]
    dummy=0
    request=list(request_arr.split(" "))
    request=[int(i) for i in request]
    _,dummy=FCFS(request,start)
    plot_list.append(dummy)
    _,dummy=SSTF(request,start)
    plot_list.append(dummy)
    _,dummy=SCAN_LEFT(request,start)
    plot_list.append(dummy)
    _,dummy=SCAN_RIGHT(request,start)
    plot_list.append(dummy)
    _,dummy=C_SCAN_LEFT(request,start)
    plot_list.append(dummy)
    _,dummy=C_SCAN_RIGHT(request,start)
    plot_list.append(dummy)
    _,dummy=LOOK_LEFT(request,start)
    plot_list.append(dummy)
    _,dummy=LOOK_RIGHT(request,start)
    plot_list.append(dummy)
    _,dummy=CLOOK_LEFT(request,start)
    plot_list.append(dummy)
    _,dummy=CLOOK_RIGHT(request,start)
    plot_list.append(dummy)
    fig = plt.figure()
    fig.suptitle('Total Head Movement Graph', fontsize=14)
    
    plt.bar(algos, plot_list)
    plt.show()

# 82 170 43 140 24 16 190 for testing


def Visualise(option, request_arr, start):
    request=list(request_arr.split(" "))
    request=[int(i) for i in request]
    if option == "FCFS":                        # Select and run algorithm
        Order, Sum = FCFS(request, start)
    elif option =="SSTF":
        Order, Sum = SSTF(request, start)
    elif option =="SCAN(left)":
        Order, Sum = SCAN_LEFT(request, start)
    elif option =="SCAN(right)":
        Order, Sum = SCAN_RIGHT(request, start)
    elif option =="C_SCAN(left)":
        Order, Sum = C_SCAN_LEFT(request, start)
    elif option =="C_SCAN(right)":
        Order, Sum = C_SCAN_RIGHT(request, start)
    elif option =="LOOK_LEFT)":
        Order, Sum = LOOK_LEFT(request, start)
    elif option =="LOOK(right)":
        Order, Sum = LOOK_RIGHT(request, start)
    elif option =="CLOOK_LEFT)":
        Order, Sum = CLOOK_LEFT(request, start)
    elif option =="CLOOK(right)":
        Order, Sum = CLOOK_RIGHT(request, start)
    

    
    turtle.clearscreen()
    Disk = turtle.Screen()

    Disk.title(option)
    Disk.bgcolor("#F8FBFF")
    Disk.setworldcoordinates(-5, -20, 210, 10)  # Set turtle window boundaries
    head = turtle.Turtle()
    head.shape("circle")
    head.color("#114579")
    head.turtlesize(.6, .6, .6)
    head.speed(3)
    head.pensize(2)

    head2 = turtle.Turtle()
    head2.shape("square")
    head2.color("green")
    head2.turtlesize(.5, .1, 1)
    head2.speed(3)
    head2.pensize(2)


    # لرسم النظام الاحداثي من صفر الى 200
    n = len(Order)
    y = -1
    y2=0
    temp_order=[int(i*10) for i in range(0,20)]
    temp_order.append(199)
    for i in range(0,len(temp_order)):
        head2.goto(temp_order[i], y2)
        head2.stamp()
        head2.write(temp_order[i], False, align="right")

        # Draw the output grapgh from the algorithm 
    for i in range(0, n):
        if i == 0:      # No drawing while the diskhead reaches start position
            head.penup()
            head.goto(Order[i], y)
            head.pendown()
            head.stamp()
            head.write(Order[i], False, align="right")
        else:           # Diskhead draws its path to each request
            head.goto(Order[i], y-1)
            head.stamp()
            head.write(Order[i], False, align="right")
            y -= 1
    head.hideturtle()
    head.color("#D84843")

    head.speed(3)
    head.penup()
    head.goto(100, 5)


    message1 = "Disk Scheduling Algorithm: " + option
    message2 = "Total Head Movement: " + str(Sum)
    message3 ="Average number of track traveled: " + str(Sum/len(request))
   
    head.write(message1, False, align="center",font=("Constantia", 16) )    # Display algorithm used
    head.goto(100,4)
    head.write(message2, False, align="center",font=("Constantia", 16))     # Display total movement
    head.goto(100,3)
    head.write(message3, False, align="center",font=("Constantia", 16))     # Display total movement

  
    head.pendown
    # Disk.exitonclick()



def Main():

    #List of colours
    mainbg="#F8FBFF"
    HeaderBG="Black"
    TextCol="#114579"
    eleBG="#F8FBFF"
    #List of Messages
    algo="Choose Algorithm:"
    vals="Enter the head path? (Tracks)"
    current="Enter the Current position of the head:"

    Menu = Tk()
    Menu.title("Disk scheduling algorithms")
    Menu.overrideredirect(False)
    Menu.geometry("811x700+0+0")
    Menu.state('zoomed')
    Menu.columnconfigure(0, weight =1 )

    Menu.resizable(False, False)
    Menu.configure(bg='white',relief=RIDGE)



    img3=Image.open(r"bgimg1.jpg")
    img3=img3.resize((Menu.winfo_screenwidth(),Menu.winfo_screenheight()),Image.Resampling.LANCZOS)
    photoimg3=ImageTk.PhotoImage(img3)

    bg_img=Label(Menu,image=photoimg3)
    bg_img.place(x=0,y=0,width=Menu.winfo_screenwidth(),height=Menu.winfo_screenheight())





    user_inp=Text(Menu,font=("arial", 16),width=20,height=1,bg="#aaf0d1",fg=TextCol,bd=1,padx=26)
    user_inp.grid(row=7, column=0,pady=(2,22))
    user_inp.config(highlightbackground = "Red",highlightcolor="Red")
    title=Label(Menu, pady=0).grid(row=0)

    title=Label(Menu, text="[Operating systems] Disk Scheduling GUI",anchor=CENTER, bd=5,padx=44, bg="#D84843", fg=mainbg, font=("Century Gothic", 28), pady=0).grid(row=0,pady=(6,2))



    # List of options in dropdown menu
    optionlist = ('FCFS', 'SSTF', 'SCAN(left)','SCAN(right)','C_SCAN(left)','C_SCAN(right)', 'LOOK_LEFT)','LOOK(right)', 'CLOOK_LEFT)','CLOOK(right)')
    Option = StringVar()
    Start = IntVar()
    Option.set("FCFS")
    L1 = Label(Menu, text = algo,font=("Constantia", 16),bg=mainbg,fg=HeaderBG,pady=2)                # Label 1
    L1.grid(row=2,column=0,pady=(10,1))
    OM = OptionMenu(Menu, Option, *optionlist)                  # Dropdown menu
    OM.grid(row=4, column=0,pady=(1,20))
    OM.configure(bd = 1,bg=eleBG,fg=TextCol,highlightthickness = 0,padx=12,pady=4,font=("Constantia", 14))


    
    L2 = Label(Menu, text = current,font=("Constantia", 16),bg=mainbg,fg=HeaderBG,pady=0,padx=10)            # Label 2
    L2.grid(row=12, column=0,pady=(10,1) )
    E1 = Entry(Menu, textvariable = Start, bd = 1,fg=TextCol, width = 8,bg="#aaf0d1",justify=CENTER,font=("arial", 16))   # Textbox
    E1.grid(row=13, column=0,pady=(1,14))
   










    #Visualize
    img1=Image.open(r"visualization-icon-3.jpg")
    img1=img1.resize((180,90),Image.Resampling.LANCZOS)
    photoimg1=ImageTk.PhotoImage(img1)
    B2=Button(Menu,image=photoimg1,cursor="hand2",command = lambda:Visualise(Option.get(), user_inp.get(1.0,END), Start.get()) )
    B2.grid(row=14, column=0)
    B1 = Button(Menu,borderwidth=0,padx=31,pady=0,bg=eleBG,fg=TextCol, text = "Simulate head movement",\
    command = lambda:Visualise(Option.get(), user_inp.get(1.0,END), Start.get()),font=("Constantia", 14))  # Button
    B1.grid(row=15, column=0,pady=(0,20))
    






    #Graph
    img4=Image.open(r"visualization-icon-9.jpg")
    img4=img4.resize((180,90),Image.Resampling.LANCZOS)
    photoimg4=ImageTk.PhotoImage(img4)
    B2=Button(Menu,image=photoimg4,cursor="hand2",command =  lambda:graphy(user_inp.get(1.0,END), Start.get()) )
    B2.grid(row=16, column=0)
    B2 = Button(Menu,borderwidth=0,padx=38,pady=0,bg=eleBG,fg=TextCol, text = " Make a Statistic Graph ",\
    command = lambda:graphy(user_inp.get(1.0,END), Start.get()),font=("Constantia", 14))  # Button
    B2.grid(row=17, column=0)


    
    L1 = Label(Menu, text = vals,font=("Constantia", 16),bg="#F8FBFF",fg=HeaderBG,pady=0,padx=10)                # Label 1
    L1.grid(row=5,column=0,pady=(10,0))

    L1 = Label(Menu, text = "Ex:  4 40 11 35 7 14  ",font=("Arial", 12),bg="#F8FBFF",fg=HeaderBG,pady=0,padx=70)                # Label 1
    L1.grid(row=6,column=0,pady=(0,2))



    Menu.mainloop()
Main()