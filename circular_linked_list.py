#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 18:17:01 2020

@author: yashodhara
"""

#circular linked list implimentation with Insert - Delete - Display - Search Functions

import os   # For only clearing screen after every operation.

######################### Class Block #################################

class Node:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next
        
    ################################################
    
    def display(self):
        curr = self.next
        first = self
        print()
        while curr != first:
            print(curr.val," => ",end=" ")
            curr = curr.next
        print()
        return
        
    ################################################
    
    def length(self):
        curr = self.next
        first = self
        cnt=0
        while curr != first:
            cnt+=1
            curr = curr.next
        return cnt    
    
    
    ################################################
    
    def insert(self,n):
        curr = self
        first = self
        while curr.next != first:
            curr = curr.next
            
        for i in range(n):
            print("Enter value for Node {}: ".format(i+1),end=" ")
            val = int(input())
            curr.next = Node(val)
            curr = curr.next
            curr.next = first
        return
            
    ###############################################
    
    def insert_pos(self,pos):
        curr = self.next
        first = self
        cnt = 0
        l = curr.length()
        if pos == l+1:
            first.insert(1)
            return
        if pos > l:
            print("-----------------Invalid position------------------")
            return
        val = int(input(" Enter Element to insert : "))
        while curr != first:
            n_node = curr.next
            if cnt+1 == pos:
                curr.next = Node(val)
                curr = curr.next
                curr.next = n_node
                print("Element {} Inserted..".format(curr.val))
                return
            else:
                curr = curr.next
                cnt+=1
        
    
    ##############################################
    
    def delete(self):
        curr = self.next
        first = self
        cnt = 0
        l = curr.length()
        if l == 0:
            print(" No nodes to delete")
        else:
             pos = int(input(" Enter position to delete : "))
             if pos > l:
                 print("--------------------Invalid position--------------------")
                 return
             else:
                 while curr != first:
                     if cnt+1 == pos:
                         dele = curr.next.val
                         n_node = curr.next.next
                         curr.next = n_node
                         print(" Element {} Deleted successfully...".format(dele))
                         return
                     else:
                         curr = curr.next
                         cnt+=1
    
    
    #############################################
    
    def search(self,key):
        curr =self.next
        first = self
        cnt = 1
        while curr != first:
            if curr.val == key:
                print("Element {} found at '{}'th position..".format(key,cnt))
                return
            else:
                cnt+=1
                curr = curr.next
        print("-----------------Element not found in linked List-------------------")
            
############################### Class Block Ends ########################################    
    
# To clear screen after every operation.
def clear():
    os.system('clear')
 
    
############################### Main block starts #######################################
def main():
    first = Node(0)
    first.next = first
    print("--------------Singly Linked List---------------")
    
    # Operation performing loop
    while(True):
        choice = int(input("Operations available  :\n  1.insert\n  2.Insert at Position\n  3.display\n  4.Delete\n  5.Search\n  6.Exit\nEnter Number to perform specified operation : "))
        if choice == 1:
            n = int(input("Enter number of nodes to insert : "))
            first.insert(n)
        elif choice == 2:
            pos = int(input("Enter position to insert : "))
            first.insert_pos(pos)
        elif choice == 3:
            first.display()
        elif choice == 4:
            first.delete()
        elif choice == 5:
            key = int(input(" Enter the key element to search : "))
            first.search(key)
        elif choice == 6:
            break
        else:
            print("-----------Invalid choice-----------")
        input()
        clear()

############################## Main block Ends ######################################
        

# Main block invoking...
if __name__ == '__main__':
    main()
    