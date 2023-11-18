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
        self._validate_loan_amount(value)

    def _validate_loan_amount(self, loan_amount):
        if loan_amount > 0:
            self._loan_amount = float(loan_amount)
        else:
            raise ValueError("Loan Amount must be greater than 0.")