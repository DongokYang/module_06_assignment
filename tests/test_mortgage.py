"""
Description: A class used to test the Mortgage class.
Author: {Student Name}
Date: {Date}
Usage: Use the tests encapsulated within this class to test the MortgagePayment class.
"""

from unittest import TestCase
from mortgage.mortgage import Mortgage
from mortgage.pixell_lookup import MortgageRate, PaymentFrequency, VALID_AMORTIZATION

class MortgageTests(TestCase):

    def test_invalid_loan_amount(self):
        #arrange
        loan_amount = -100
        rate = MortgageRate.FIXED_5
        frequency = PaymentFrequency.MONTHLY
        amortization = 30

        #assemble 
        with self.assertRaises(ValueError) as context:
            Mortgage(loan_amount,rate,frequency,amortization)

        #act
        self.assertEqual(str(context.exception), "Loan Amount must be positive.")

    def test_invalid_rate(self):
        #arrange
        loan_amount = 10000
        rate = "invalid_rate"
        frequency = PaymentFrequency.MONTHLY
        amortization = 30

        #assemble 
        with self.assertRaises(ValueError) as context:
            Mortgage(loan_amount,rate,frequency,amortization)

        #act
        self.assertEqual(str(context.exception), "Rate provided is invalid.")

    def test_invalid_frequency(self):
        #arrange
        loan_amount = 10000
        rate = MortgageRate.FIXED_5
        frequency = "invalid_frequency"
        amortization = 30

        #assemble 
        with self.assertRaises(ValueError) as context:
            Mortgage(loan_amount,rate,frequency,amortization)

        #act
        self.assertEqual(str(context.exception), "Frequency provided is invalid")

    def test_invalid_amortization(self):
        #arrange
        loan_amount = 10000
        rate = MortgageRate.FIXED_5
        frequency = PaymentFrequency.MONTHLY
        amortization = 40

        #assemble 
        with self.assertRaises(ValueError) as context:
            Mortgage(loan_amount,rate,frequency,amortization)

        #act
        self.assertEqual(str(context.exception), "Amortization provided is invalid.")

    def test_valid_inputs(self):
        #arrange
        loan_amount = 10000
        rate = MortgageRate.FIXED_5
        frequency = PaymentFrequency.MONTHLY
        amortization = 30

        mortgage = Mortgage(loan_amount,rate,frequency,amortization)
        self.assertEqual(mortgage.loan_amount, float(loan_amount))
        self.assertEqual(mortgage.rate, rate)
        self.assertEqual(mortgage.frequency, frequency)
        self.assertEqual(mortgage.amortization, amortization)

    def test_loan_amount_mutator_negative_value(self):
        mortgage = Mortgage(10000,MortgageRate.FIXED_5,PaymentFrequency.MONTHLY,30) 

        with self.assertRaises(ValueError):
            mortgage.loan_amount = -1     

    def test_loan_amount_mutator_zero_value(self):
        mortgage = Mortgage(10000,MortgageRate.FIXED_5,PaymentFrequency.MONTHLY,30) 

        with self.assertRaises(ValueError):
            mortgage.loan_amount = 0  

    def test_loan_amount_mutator_positive_value(self):
        mortgage = Mortgage(10000,MortgageRate.FIXED_5,PaymentFrequency.MONTHLY,30) 

        mortgage.loan_amount =20000
        self.assertEqual(mortgage.loan_amount,20000) 

    def test_valid_rate(self):
        mortgage = Mortgage(10000,MortgageRate.FIXED_5,PaymentFrequency.MONTHLY,30) 
        mortgage.rate = MortgageRate.FIXED_3
        self.assertEqual(mortgage.rate,MortgageRate.FIXED_3) 

    def test_invalid_rate(self):
        mortgage = Mortgage(10000,MortgageRate.FIXED_5,PaymentFrequency.MONTHLY,30) 
        with self.assertRaises(ValueError):
            mortgage.rate = 2323

    def test_invalid_frequency(self):
        mortgage = Mortgage(10000,MortgageRate.FIXED_5,PaymentFrequency.MONTHLY,30) 
        with self.assertRaises(ValueError):
            mortgage.frequency = 2323 

    def test_valid_frequency(self):
        mortgage = Mortgage(10000,MortgageRate.FIXED_5,PaymentFrequency.MONTHLY,30) 
        mortgage.frequency = PaymentFrequency.WEEKLY
        self.assertEqual(mortgage.frequency,PaymentFrequency.WEEKLY) 

    def test_invalid_amortization(self):
        mortgage = Mortgage(10000,MortgageRate.FIXED_5,PaymentFrequency.MONTHLY,30) 
        with self.assertRaises(ValueError):
            mortgage.amortization = 2323

    def test_valid_amortization(self):
        mortgage = Mortgage(10000,MortgageRate.FIXED_5,PaymentFrequency.MONTHLY,30) 
        mortgage.amortization = 15
        self.assertEqual(mortgage.amortization,15) 

#python -m unittest -v tests/test_mortgage.py