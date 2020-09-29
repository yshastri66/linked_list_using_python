#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 10:27:20 2020

@author: yashodhara
"""

#doubly linked list implimentation with Insert - Delete - Display - Search Functions

import os   # For only clearing screen after every operation.

######################### Class Block #################################

class Node:
    def __init__(self,val,llink=None,rlink=None):
        self.val = val
        self.llink = llink
        self.rlink = rlink
    ################################################
    
    def display(self):
        curr = self.rlink
        print()
        while curr:
            print(" <= ",curr.val," => ",end=" ")
            curr = curr.rlink
        print()
        return
        
    ################################################
    
    def length(self):
        curr = self.rlink
        cnt=0
        while curr:
            cnt+=1
            curr = curr.rlink
        return cnt    
    
    
    ################################################
    
    def insert(self,n):
        curr = self
        
        while curr.rlink:
            curr = curr.rlink
            
        for i in range(n):
            print("Enter value for Node {}: ".format(i+1),end=" ")
            val = int(input())
            new_node = Node(val)
            new_node.llink = curr
            curr.rlink = new_node
            curr = curr.rlink
        print(" Elements inserted successfullly...")
        return
            
    ###############################################
    
    def insert_pos(self,pos):
        curr = self
        cnt = 0
        l = curr.length()
        if pos == l+1:
            curr.insert(1)
            return
        if pos > l:
            print("-----------------Invalid position------------------")
            return
        val = int(input(" Enter Element to insert : "))
        while curr:
            if cnt+1 == pos:
                new_node = Node(val)
                new_node.rlink = curr.rlink
                curr.rlink.llink = new_node
                new_node.llink = curr
                curr.rlink = new_node                
                print("Element {} Inserted..".format(new_node.val))
                return
            else:
                curr = curr.rlink
                cnt+=1
        
    
    ##############################################
    
    def delete(self):
        curr = self
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
                 while curr:
                     if cnt+1 == pos:
                         dele = curr.rlink.val
                         del_nxt_node = curr.rlink.rlink
                         curr.rlink = del_nxt_node
                         if del_nxt_node:
                             del_nxt_node.llink = curr
                         print(" Element {} Deleted successfully...".format(dele))
                         return
                     else:
                         curr = curr.rlink
                         cnt+=1
    
    
    #############################################
    
    def search(self,key):
        curr =self.rlink
        cnt = 1
        while curr:
            if curr.val == key:
                print("Element {} found at '{}'th position..".format(key,cnt))
                return
            else:
                cnt+=1
                curr = curr.rlink
        print("-----------------Element not found in linked List-------------------")
        
    
    #############################################    
    
    def reverse_display(self):
        curr = self.rlink 
        while curr.rlink:
            curr = curr.rlink
            
        while curr.llink:
            print(" <= ",curr.val," => ",end = "")
            curr = curr.llink
        print()
        return
        
            
            
############################### Class Block Ends ########################################    
    
# To clear screen after every operation.
def clear():
    os.system('clear')
 
    
############################### Main block starts #######################################
def main():
    first = Node(0)
    print("--------------Doubly Linked List---------------")
    
    # Operation performing loop
    while(True):
        choice = int(input("Operations available  :\n  1.insert\n  2.Insert at Position\n  3.display\n  4.Display reverse\n  5.Delete\n  6.Search\n  7.Exit\nEnter Number to perform specified operation : "))
        if choice == 1:
            n = int(input("Enter number of nodes to insert : "))
            first.insert(n)
        elif choice == 2:
            pos = int(input("Enter position to insert : "))
            first.insert_pos(pos)
        elif choice == 3:
            first.display()
        elif choice == 4:
            first.reverse_display()
        elif choice == 5:
            first.delete()
        elif choice == 6:
            key = int(input(" Enter the key element to search : "))
            first.search(key)
        elif choice == 7:
            break
        else:
            print("-----------Invalid choice-----------")
        input()
        clear()

############################## Main block Ends ######################################
        

# Main block invoking...
if __name__ == '__main__':
    main()
    