"""
Description: A class meant to manage Mortgage options.
Edited By: Dongok Yang
Date: 11.17
Usage: Create an instance of the Mortgage class to manage mortgage records and 
calculate payments.
"""
from mortgage.pixell_lookup import MortgageRate, PaymentFrequency, VALID_AMORTIZATION
#import pixell_lookup to utilize MortgageRate, PaymentFrequency, VALID_AMORTIZATION

class Mortgage:
    """
    A class used to calculate the amount of payment and verify input is correct.
    Attributes
    loan_amount(float) : The amount of loan
    rate(MortgageRate) : The interest rate
    frequency(PaymentFrequency) : The frequency of payment
    amortization(int) : amortization of mortgage

    method
    __init__ : initialize loan_amount,rate,frequency,amortization
    calculate_payment : calculate the desired amount of payment 

    return 
    __str__ : return mortgage amount, rate, amortization, frequency in a user-friendly way
    __repr__ : return mortgage amount, rate, amortization, frequency in a developer-friendly way

    """
    def __init__(self,loan_amount,rate,frequency,amortization):
        if loan_amount > 0:
            self._loan_amount = float(loan_amount)
        else:
            raise ValueError("Loan Amount must be positive.")
        
        if not isinstance (rate,MortgageRate):
            raise ValueError("Rate provided is invalid.")
        self.rate = rate

        if not isinstance (frequency,PaymentFrequency):
            raise ValueError("Frequency provided is invalid")
        self.frequency = frequency
        
        if amortization not in VALID_AMORTIZATION:
            raise ValueError("Amortization provided is invalid.")
        self.amortization = amortization
    # setup mortgage class to calculate payment of loan 

    @property
    def loan_amount(self):
        return self._loan_amount
    
    @loan_amount.setter
    def loan_amount(self, value):
        if value > 0:
            self._loan_amount = float(value)
        else:
            raise ValueError("Loan Amount must be positive.")     
    #mutator and Accessor were created to return and change the value of Loan amount
           
    @property
    def rate(self):
        return self._rate
    
    @rate.setter
    def rate(self, value):
        if isinstance(value,MortgageRate):
            self._rate = value
        else:
            raise ValueError("Rate provided is invalid.")    
    #mutator and Accessor were created to return and change the value of rate  

    @property
    def frequency(self):
        return self._frequency
    
    @frequency.setter
    def frequency(self, value):
        if isinstance(value,PaymentFrequency):
            self._frequency = value
        else:
            raise ValueError("Frequency provided is invalid.")   
    #mutator and Accessor were created to return and change the value of Frequency     

    @property
    def amortization(self):
        return self._amortization
    
    @amortization.setter
    def amortization(self, value):
        if value in VALID_AMORTIZATION:
            self._amortization = value
        else:
            raise ValueError("Amortization provided is invalid.")  
    #mutator and Accessor were created to return and change the value of Amortization
        
    def calculate_payment(self) -> float:
        """
        calculated desired payment per month by using following formula
        M = P(i(1+i)^n)/(1+i)^n -1)
        M : calculated payment
        P : principal loan amount
        i : monthly interest rate(annual rate / frequency)
        n : number of payments (amortization * frequency)
        
        """
        i = self.rate.value/self.frequency.value
        n = self.amortization * self.frequency.value
        P = self.loan_amount * (i * (1 + i) ** n) / ((1 + i) ** n - 1)
        return round(P, 2)
    #calculator desired payment per month 
    
    
    def __str__(self):
        return (
            f"Mortgage Amount: ${self._loan_amount:,.2f}\n"
            f"Rate: {self._rate.value * 100:.2f}%\n"
            f"Amortization: {self._amortization}\n"
            f"Frequency: {self._frequency.name} -- Calculated Payment: ${self.calculate_payment():,.2f}"
        )
    # return the value of mortgage amount, rate, amortization, and frequency in desired, user-friendly format

    def __repr__(self):
        return f"[{self._loan_amount}, {self._rate.value}, {self._amortization}, {self._frequency.value}]"
    # return the value of mortgage amount, rate, amortization, and frequency in desired, developer-friendly format