# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 10:52:39 2021

@author: Oranf_fjox16m
"""
from colorama import Fore, Style
import json

def menu():
    
    comm_list = ['search', 'add', 'mod', 'quit']
    
    print('-----------------------')
    print('Python commands DB v. 0.1')
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
                
            input('Add new library: ')
        
        #print(f'{Fore.RED}Library already in archive{Style.RESET_ALL}')
        
        
def check_existence(pass_library):
    
    with open('F:/Archivio/Python/prova.json', 'r') as archive:
            file_check = json.load(archive)
            for x in file_check:
                if pass_library in file_check:
                    return True
                else:
                    return False
    

def add():
    
    lib = input('New library: ')
    check = check_existence(lib)
    
    if check == True:
        print('True')
    else:
        print(f'Adding {lib} as new library.')
        print()
        desc = input('insert description: ')
        comm = input('insert commands: ')
        #qui ci sarà il dizionario da salvare sul file
        
        
            
        
            
   
        
add()  

    
    