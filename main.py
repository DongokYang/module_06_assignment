"""
Description: A client program written to verify accuracy of and 
calculate payments for PiXELL River Mortgages.
Author: ACE Faculty
Edited By: Dongok Yang
Date: 11.17
"""


from mortgage.mortgage import Mortgage
from mortgage.pixell_lookup import MortgageRate, PaymentFrequency, VALID_AMORTIZATION

try:
    with open ("data\\pixell_river_mortgages.txt","r") as input:
        print("**************************************************")
        
        for data in input:
            items = data.split(",")
            
            try:
                amount = float(items[0])
                rate = MortgageRate[items[1]]
                amortization = int(items[2])
                frequency = PaymentFrequency[items[3]]
                mortgage = Mortgage(amount, rate, frequency, amortization)
                print(mortgage)
                
            except ValueError as e:
                print(f"Data: {data.strip()} caused Exception: {e}")
            
            except Exception as e:
                print(f"Data: {data.strip()} caused Exception: {e}")
            finally:
                print("**************************************************")
except FileNotFoundError:
    print("The file was not found.")
#If file is not found, shows error 