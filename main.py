"""
Description: A client program written to verify accuracy of and 
calculate payments for PiXELL River Mortgages.
Author: ACE Faculty
Edited By: Dongok Yang
Date: 11.17
"""

### REQUIREMENT
### ADD IMPORT STATEMENTS FOR THE MORTGAGE CLASS, THE 
### MORTGAGERATE AND MORTGAGEFREQUENCY ENUMERATIONS AND THE 
### VALID_AMORTIZATION LIST

from mortgage.mortgage import Mortgage
from mortgage.pixell_lookup import MortgageRate, PaymentFrequency, VALID_AMORTIZATION

### REQUIREMENT
### ENCLOSE THE FOLLOWING 'WITH OPEN' BLOCK IN A 'TRY-EXCEPT' BLOCK WHICH 
### WILL CATCH A 'FILENOTFOUNDERROR' EXCEPTION
try:
    with open ("data\\pixell_river_mortgages.txt","r") as input:
        print("**************************************************")
        
        for data in input:
            items = data.split(",")
            
                ### REQUIREMENT:
                ### INSTANTIATE A MORTGAGE OBJECT USING THE VALUES
                ### FOR AMOUNT, RATE, FREQUENCY AND AMORTIZATION ABOVE.
            try:
                amount = float(items[0])
                rate = MortgageRate[items[1]]
                amortization = int(items[2])
                frequency = PaymentFrequency[items[3]]
                mortgage = Mortgage(amount, rate, frequency, amortization)
                
                ### REQUIREMENT:
                ### PRINT THE MORTGAGE OBJECT
                print(mortgage)
            except ValueError as e:
                # This except block will catch Explicit exceptions: 
                # Those raised by the programmer in the Mortgage class.
                print(f"Data: {data.strip()} caused Exception: {e}")
            
            except Exception as e:
                # This except block will catch Implicit exceptions:  
                # Those raised through normal execution.
                print(f"Data: {data.strip()} caused Exception: {e}")
            finally:
                print("**************************************************")
except FileNotFoundError:
    print("The file was not found.")
#If file is not foujd, shows error 