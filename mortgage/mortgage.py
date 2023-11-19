"""
Description: A class meant to manage Mortgage options.
Author: {Student Name}
Date: {Date}
Usage: Create an instance of the Mortgage class to manage mortgage records and 
calculate payments.
"""
from mortgage.pixell_lookup import MortgageRate, PaymentFrequency, VALID_AMORTIZATION


class Mortgage:
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
    
    @property
    def loan_amount(self):
        return self._loan_amount
    
    @loan_amount.setter
    def loan_amount(self, value):
        if value > 0:
            self._loan_amount = float(value)
        else:
            raise ValueError("Loan Amount must be positive.")     
           
    @property
    def rate(self):
        return self._rate
    
    @rate.setter
    def rate(self, value):
        if isinstance(value,MortgageRate):
            self._rate = value
        else:
            raise ValueError("Rate provided is invalid.")        

    @property
    def frequency(self):
        return self._frequency
    
    @frequency.setter
    def frequency(self, value):
        if isinstance(value,PaymentFrequency):
            self._frequency = value
        else:
            raise ValueError("Frequency provided is invalid.")        

    @property
    def amortization(self):
        return self._amortization
    
    @amortization.setter
    def amortization(self, value):
        if value in VALID_AMORTIZATION:
            self._amortization = value
        else:
            raise ValueError("Amortization provided is invalid.")  
        
    def calculate_payment(self) -> float:
        r = self.rate.value/self.frequency.value
        n = self.amortization * self.frequency.value
        P = self.loan_amount * (r * (1 + r) ** n) / ((1 + r) ** n - 1)
        return round(P, 2)