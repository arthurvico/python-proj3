# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 10:45:21 2018

@author: arthu
"""


answer = input("Would you like to (D)ecrypt, (E)ncrypt or (Q)uit? ")
while answer.upper() != 'Q':
    while answer.upper() == 'E':
        keyword = input("Please enter a keyword: ")
        message = input("Enter your message: ")
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        new_alpha = ""
        new_alpha_2 = ""
        new_message = ""
        keyword = keyword.lower()
        message = message.lower()
        if keyword.isalpha() == False:
            print("There is an error in the keyword. It must be all letters and a maximum length of 26")
            continue
        if len(keyword) > 26:
            print("There is an error in the keyword. It must be all letters and a maximum length of 26")
            continue
        for ch in keyword:
            if ch not in new_alpha:
                new_alpha += ch
        for ch in alphabet:
            if ch not in new_alpha:
                new_alpha += ch
        for ch in new_alpha:
                index = new_alpha.index(ch)
                index = ((5*index)+8)%26
                new_alpha_2 += new_alpha[index]
        for ch in message:
            if ch.isalpha():
                index = alphabet.index(ch)
                new_message += new_alpha_2[index]
            else:
                new_message += ch
        print("your encoded message:  "+new_message)
        answer = input("Would you like to (D)ecrypt, (E)ncrypt or (Q)uit? ")
    while answer.upper() == 'D':
        keyword = input("Please enter a keyword: ")
        message = input("Enter your message: ")
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        new_alpha = ""
        new_alpha_2 = ""
        new_message = ""
        keyword = keyword.lower()
        message = message.lower()
        if keyword.isalpha() == False:
            print("There is an error in the keyword. It must be all letters and a maximum length of 26")
            continue
        if len(keyword) > 26:
            print("There is an error in the keyword. It must be all letters and a maximum length of 26")
            continue
        for ch in keyword:
            if ch not in new_alpha:
                new_alpha += ch
        for ch in alphabet:
            if ch not in new_alpha:
                new_alpha += ch
        for ch in new_alpha:
                index = new_alpha.index(ch)
                index = ((5*index)+8)%26
                new_alpha_2 += new_alpha[index]
        for ch in message:
             if ch.isalpha():
                 index = new_alpha_2.index(ch)
                 new_message += alphabet[index]
             else:
                 new_message += ch
         
            
            
        print ("your decoded message:  "+new_message)       
        answer = input("Would you like to (D)ecrypt, (E)ncrypt or (Q)uit? ")
print("See you again soon!")
    #print("Testing:", answer)
    #answer = input("Would you like to (D)ecrypt, (E)ncrypt or (Q)uit? ")