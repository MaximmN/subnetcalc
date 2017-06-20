	# Part 1.

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
	         
	# Part 2.
		 
        #Algorithm for subnet identification, based on IP and Subnet Mask
        
        #Convert mask to binary string
        mask_octets_padded = []
        mask_octets_decimal = subnet_mask.split(".") # list of mask "b"
        #print mask_octets_decimal
        
        for octet_index in range(0, len(mask_octets_decimal)):
            
            #print in binary value
            #print bin(int(mask_octets_decimal[octet_index]))
            
            #print 8 bits in 1st 3 octets and 1 bit in 4th
            binary_octet = bin(int(mask_octets_decimal[octet_index])).split("b")[1]
            #print binary_octet
            
            #print octets in a list with filled 0 to 8 numbers in 4th octet
            if len(binary_octet) == 8:
                mask_octets_padded.append(binary_octet)
            
            elif len(binary_octet) < 8:
            	#zfill fills octets with 0 until up to this length
                binary_octet_padded = binary_octet.zfill(8)
                mask_octets_padded.append(binary_octet_padded)
                
        #print mask_octets_padded
        

        decimal_mask = "".join(mask_octets_padded)
        #print decimal_mask   #Example: for 255.255.255.0 => 11111111111111111111111100000000
        


        #Counting host bits in the mask and calculating number of hosts/subnet
        no_of_zeros = decimal_mask.count("0")
        no_of_ones = 32 - no_of_zeros
        no_of_hosts = abs(2 ** no_of_zeros - 2) #return positive value for mask /32
        
        #print no_of_zeros
        #print no_of_ones
        #print no_of_hosts
        


        #Obtaining wildcard mask
        wildcard_octets = []
        for w_octet in mask_octets_decimal:
            wild_octet = 255 - int(w_octet)
            wildcard_octets.append(str(wild_octet))
        
        #Example: for 255.255.255.0 => ['0','0','0','255']    
        #print wildcard_octets
        
        wildcard_mask = ".".join(wildcard_octets)
        #Example: for 255.255.255.0 => 0.0.0.255
        #print wildcard_mask


    except KeyboardInterrupt:
        print "\n\nProgram aborted by user. Exiting...\n"
        sys.exit()
        
#Calling the function
subnet_calc()