#2302
#Author: Emmanuel Alvarez 80567137
#Instructor: Olac Fuentes
#Last Mofification date: 02-27-2019
#The purpose of this assignment is to create a linked list with integers and 
#sort them using different bubble sort, quick sort and merge sort



import random
from copy import copy,deepcopy
##############################################################################
class Node(object):
    # Constructor
    def __init__(self, item, next=None):  
        self.item = item
        self.next = next 
        
def PrintNodes(N):
    if N != None:
        print(N.item, end=' ')
        PrintNodes(N.next)
        
def PrintNodesReverse(N):
    if N != None:
        PrintNodesReverse(N.next)
        print(N.item, end=' ')
        
#List Functions
class List(object):   ########################################################
    # Constructor
    def __init__(self): 
        self.head = None
        self.tail = None
        
def IsEmpty(L):  
    return L.head == None     
        
def Append(L,x): 
    # Inserts x at end of list L
    if IsEmpty(L):
        L.head = Node(x)
        L.tail = L.head
    else:
        L.tail.next = Node(x)
        L.tail = L.tail.next
        
def Print(L):
    # Prints list L's items in order using a loop
    temp = L.head
    while temp is not None:
        print(temp.item, end=' ')
        temp = temp.next
    print()  # New line 

def PrintRec(L):
    # Prints list L's items in order using recursion
    PrintNodes(L.head)
    print() 
    
def Remove(L,x):
    # Removes x from list L
    # It does nothing if x is not in L
    if L.head==None:
        return
    if L.head.item == x:
        if L.head == L.tail: # x is the only element in list
            L.head = None
            L.tail = None
        else:
            L.head = L.head.next
    else:
         # Find x
         temp = L.head
         while temp.next != None and temp.next.item !=x:
             temp = temp.next
         if temp.next != None: # x was found
             if temp.next == L.tail: # x is the last node
                 L.tail = temp
                 L.tail.next = None
             else:
                 temp.next = temp.next.next
         
def PrintReverse(L):
    # Prints list L's items in reverse order
    PrintNodesReverse(L.head)
    print()     
    
def ElementAt(l,n,index):
    #print(getLength(l))
    temp = l
    if n == index:
        return -2#temp.item
    ElementAt(temp.next,n+1,index)
    return -1


def getLength(L):
    temp = L
    if L is not None:
        return 1 + getLength(temp.next)
    return 0 


    
############################################################################

    
def create_list(n): # Creates a linked list with random integers
    randomList = List()
    while n > 0:        
        Append(randomList,random.randint(0,100))
        n = n-1
    return randomList

#############################################################################
def bubbleSort(L):
    done = False    
    while done is not True:
        done = True
        temp = L.head
        while temp.next is not None:
            if(temp.item > temp.next.item):
                aux = temp.item
                temp.item = temp.next.item
                temp.next.item = aux
                done = False
            temp = temp.next
#############################################################################
def merge(L1,L2):
    if L1 is None:
        return L2
    if L2 is None:
        return L1
    if L1.head.item < L2.head.item:
        sortedList = L1
        sortedList.next = merge(L1.next,L2)
    else:
        sortedList = L2
        sortedList.next = merge(L1,L2.next)
    return sortedList
#############################################################################
#def mergeSort(L): 
    #half = getLength(L.head)//2
    #counter = 0
    #L1 = List()
    #while counter is not half-1:
       # Append(L1,L.head.item)
        
    #sortedList = List()
    #sortedList = merge(L1,L2)
    #sortedList2 = List()
    #Append(sortedList2,sortedList.head)
    #print(sortedList.head.item)
#############################################################################
def quickSort(L):
    temp = L.head
    if getLength(L.head) > 1:
        pivot = temp.item
        temp = temp.next
        L1 = List()
        L2 = List()
        while temp is not None:
            if temp.item < pivot:
                Append(L1,temp.item)
            else:
                Append(L2,temp.item)
        quickSort(L1)
        quickSort(L2)
    L = L1 + L2    
#############################################################################    
length = 8
randomList = List()
randomList = create_list(length)

randomList2 = create_list(length)
Print(randomList2)
print('Random list before sort it')
Print(randomList)
bubbleSort(randomList)
print('Random list after sort it using bubble sort')
Print(randomList)
median = ElementAt(randomList.head,0,length//2)
#quickSort(randomList2)
Print(randomList2)
#print(median)
#print(getLength(randomList.head))
#mergeSort(randomList2)



















