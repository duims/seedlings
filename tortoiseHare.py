"""Practising really understanding implementing algorithm concepts == actually implementing some algorithms
This algorithm was invented in the late 60's by Robert Floyd, a computer science professor at Stanford. 

The implementation of Linked Lists: Each node is a dict containing keys: data, the value in the node, and next, which points to the next node in the list.
Each node only points to 1 other node, or None.

"""
import random


def tortoiseHare(linkedList):
    if linkedList == None or linkedList['next'] == None or linkedList['next']['next'] == None:
        # short Circuitry at work! :)
        return False

    slow = linkedList
    fast = linkedList['next']['next']
    while id(slow)!= id(fast):
        if fast['next'] == None or fast['next']['next'] == None:
            return False
        else:
            fast = fast['next']['next']
        slow = slow['next']
    return True



def makeLinkedList(_list):
    
    linkedList = None
    
    #iterate backwards through the originallist and append values to the head of the linked list.
    #Useful because we only have unidirectional pointers.

    for i in range(len(_list) - 1, -1, -1):
        linkedList = insertHead(linkedList, _list[i])
    return linkedList


def insertAtEnd(linkedList, value):
    newNode = {}
    newNode['data'] = value
    newNode['next'] = None
    ptr = linkedList
    while ptr['next'] != None:
        ptr = ptr['next']
    ptr['next'] = newNode
    return linkedList


def insertHead(linkedList, value):
    newNode = {}
    newNode['data'] = value
    newNode['next'] = linkedList
    return newNode


def makeALoop(linkedList, ptMe):
    #ptMe is the "index" value of the element that starts the cycle.
    ptr = linkedList
    for i in range(ptMe - 1):
        ptr = ptr['next']
    end = linkedList
    while end['next'] != None:
        end = end['next']
    end['next'] = ptr
    return linkedList


def printLinkedList(linkedList):
    printThis = "["
    ptr = linkedList
    while ptr != None:
        printThis = printThis + str(ptr['data'])
        if ptr['next'] != None:
            printThis = printThis + ", "
        ptr = ptr['next']

    printThis = printThis + "]"
    print (printThis)
    return None
