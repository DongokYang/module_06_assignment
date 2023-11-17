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
        amortization = 40

        Mortgage(loan_amount,rate,frequency,amortization)
        self.assertEqual(Mortgage.loan_amount, float(loan_amount))
        self.assertEqual(Mortgage.rate, rate)
        self.assertEqual(Mortgage.frequency, frequency)
        self.assertEqual(Mortgage.amortization, amortization)
    #amortization == invalid