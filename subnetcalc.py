# Part 1

import random
import sys

def subnet_calc():
    try:
        print "\n"
        
        #Checking IP address validity
        while True:
            # asking the user for IP address
            ip_address = raw_input("Enter an IP address: ")
            
            #Checking octets
            # return a list of users IP address            
            a = ip_address.split('.')
                        
            if (len(a) == 4) and (1 <= int(a[0]) <= 223) and (int(a[0]) != 127) and (int(a[0]) != 169 or int(a[1]) != 254) and (0 <= int(a[1]) <= 255 and 0 <= int(a[2]) <= 255 and 0 <= int(a[3]) <= 255):
                break
            else:
                print "\nThe IP address is INVALID! Please retry!\n"
                # redirect the user to the top of while loop
                continue
        
        masks = [255, 254, 252, 248, 240, 224, 192, 128, 0]
        
        #Checking Subnet Mask validity
        while True:
            subnet_mask = raw_input("Enter a subnet mask: ")
            
            #Checking octets            
            b = subnet_mask.split('.')
            
            if (len(b) == 4) and (int(b[0]) == 255) and (int(b[1]) in masks) and (int(b[2]) in masks) and (int(b[3]) in masks) and (int(b[0]) >= int(b[1]) >= int(b[2]) >= int(b[3])):
                break   
            else:
                print "\nThe subnet mask is INVALID! Please retry!\n"
                # redirect the user to the top of while loop
                continue
    
    except KeyboardInterrupt:
        print "\n\nProgram aborted by user. Exiting...\n"
        sys.exit()
        
#Calling the function
subnet_calc()