"""Practising really understanding implementing algorithm concepts == actually implementing some algorithms
This algorithm was invented in the late 60's by Robert Floyd, a computer science professor at Stanford. 

implementation of Linked Lists: Each node is a dict containing key: data, the value in the node, and next, which points to the next node in the list.
"""

import random

def tortoiseHare(linkedList):
	if linkedList==None or linkedList['next']==None or linkedList['next']['next'] :
		#short Circuitry at work! :)
		return False
	slow=linkedList
	fast=linkedList['next']['next']
	while slow !=fast:
		if fast['next']['next']== None or fast['next']==None:
			return False
		else:
			fast=fast['next']['next']
			print("fast", fast['data'])
		slow=slow['next']
		print("slow", slow['data'])

	return True

def makeLinkedList(_list):
        linkedList = None
        for i in range(len(_list)-1 , -1, -1):
                linkedList = insertHead(linkedList, _list[i])
        return linkedList

def insertAtEnd(linkedList, value):
	newNode={}
	newNode['data'] = value
	newNode['next']=None
	ptr = linkedList
	while ptr['next'] != None:
		ptr=ptr['next']
	ptr['next']=newNode
	return linkedList
	
def insertHead(linkedList, value):
	newNode={}
	newNode['data']=value
	newNode['next']=linkedList
	return newNode

def makeALoop(linkedList, ptMe):
        ptr=linkedList
        for i in range(ptMe-1):
                ptr=ptr['next']
        end=linkedList
        while end['next'] != None:
                end=end['next']
        end['next']=ptr
        return linkedList
                
def printLinkedList(linkedList):
        printThis="["
        ptr=linkedList
        while ptr != None:
                printThis= printThis + str(ptr['data'])
                if ptr['next'] != None:
                        printThis=printThis + ", "
                ptr=ptr['next']
        
        printThis= printThis + "]"
        print (printThis)

def test():
        x=[3,34, 5, 6, 3, 2]
        y=[]
        z=[1]
        w=[2,3,4]
        xs=[4,5,6,2,3]

        x=makeLinkedList(x)
        y=makeLinkedList(y)
        z=makeLinkedList(z)
        w=makeLinkedList(w)
        xs=makeLinkedList(xs) 

        print ("x:")
        print(tortoiseHare(x))
        print("y:")
        print(tortoiseHare(y))
        print('z:')
        print(tortoiseHare(z))
        print("w")
        print(tortoiseHare(w))
        print('xs')
        print(tortoiseHare(xs))

	
	
test()
