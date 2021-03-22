# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 10:52:39 2021

@author: Oranf_fjox16m
"""
from colorama import Fore, Style

def menu():
    
    comm_list = ['search', 'add', 'mod', 'quit']
    
    print('-----------------------')
    print('Python commands DB v. 0')
    print('-----------------------')
    print('')
    print('Welcome. To begin, enter a command')
    
    while True:
        
        print('\"search\": Search for a library or a command')
        print('\"add\": Add new library')
        print('\"mod\": Modify or add new commands to an existing library')
        print('\"quit\": Quit the program')
    
        comm = input()
        comm = comm.lower()
    
        if comm in comm_list:
            
            if  comm == 'search':
                print('search')
                break
            
            elif comm == 'add':
                print('add')
                break
            
            elif comm == 'mod':
                print('mod')
                break
                
            else:
                raise SystemExit
                
        else:
            print('')
            print(f'{Fore.RED}Invalid Command{Style.RESET_ALL}')
            print('')
        
        
menu()  
    
    
    