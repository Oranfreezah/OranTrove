# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 10:52:39 2021

@author: Oranf_fjox16m
"""
from colorama import Fore, Style
import csv

def menu():
    filecheck()
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
    
    with open('F:/Archivio/Python/prova.csv', 'r') as archive:
            file_check = csv.reader(archive)
            for x in file_check:
                if pass_library in file_check:
                    return True
                else:
                    return False
    

def command_list():
    comm_dict = {}
    while True:
        comm = input('New command. Input q to stop: ')
        if comm == 'q':
            break
        else:
            comm_fun = input('Insert command description: ')
            comm_dict.update({comm:comm_fun})
            print(comm_dict)
    
    return comm_dict
            
            
def filecheck():
    try:
        f = open('F:/Archivio/Python/prova.csv')   
    except IOError:
        print('File not found. Creating new file')
        open('F:/Archivio/Python/prova.csv', 'w')
                 
            
        

def add():
    
    lib = input('New library: ')
    check = check_existence(lib)
    
    
    if check == True:
        print('True')
    else:
        desc = input('insert description: ')
        comm_list = command_list()
        
        
    new_library = {"Name": lib,
                   "Use": desc,
                   "Commands": comm_list}
    with open('F:/Archivio/Python/prova.csv', 'w', newline="") as archive:
        fields = ["Name", "Use", "Commands"]
        writer = csv.DictWriter(archive, fieldnames=fields)
        writer.writeheader()
        writer.writerow(new_library)
    
    with open('F:/Archivio/Python/prova.csv', 'r') as archive:
        reader = csv.reader(archive)
        line_count = 0
        for row in reader:
            print(row)
        

add()  

    
    