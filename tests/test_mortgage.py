"""
Description: A class used to test the Mortgage class.
Edited By: Dongok Yang
Date: 11.17
Usage: Use the tests encapsulated within this class to test the MortgagePayment class.
"""
import unittest
from unittest import TestCase
from mortgage.mortgage import Mortgage
from mortgage.pixell_lookup import MortgageRate, PaymentFrequency, VALID_AMORTIZATION

class MortgageTests(TestCase):
    #created Mortgagtests to test each functions.
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
        # test whether input is valid amount or not  

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
        # test whether input is invalid rate or not

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
        # test whether input is invalid frequency or not

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
        # test whether input is invalid amortization or not

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
        # test whether 4 inputs are valid or not

    def test_loan_amount_mutator_negative_value(self):
        mortgage = Mortgage(10000,MortgageRate.FIXED_5,PaymentFrequency.MONTHLY,30) 

        with self.assertRaises(ValueError):
            mortgage.loan_amount = -1     
        # test to validate when negative input is given, it shows error    

    def test_loan_amount_mutator_zero_value(self):
        mortgage = Mortgage(10000,MortgageRate.FIXED_5,PaymentFrequency.MONTHLY,30) 

        with self.assertRaises(ValueError):
            mortgage.loan_amount = 0  
        # test to validate when zero input is given, it shows error

    def test_loan_amount_mutator_positive_value(self):
        mortgage = Mortgage(10000,MortgageRate.FIXED_5,PaymentFrequency.MONTHLY,30) 

        mortgage.loan_amount =20000
        self.assertEqual(mortgage.loan_amount,20000) 
        # test to validate when positive input is given, it changes value

    def test_valid_rate(self):
        mortgage = Mortgage(10000,MortgageRate.FIXED_5,PaymentFrequency.MONTHLY,30) 
        mortgage.rate = MortgageRate.FIXED_3
        self.assertEqual(mortgage.rate,MortgageRate.FIXED_3) 
        # test to validate when valid input is given, it doesn't show error

    def test_invalid_rate(self):
        mortgage = Mortgage(10000,MortgageRate.FIXED_5,PaymentFrequency.MONTHLY,30) 
        with self.assertRaises(ValueError):
            mortgage.rate = 2323
        # test to validate when invalid input is given, it shows error

    def test_invalid_frequency(self):
        mortgage = Mortgage(10000,MortgageRate.FIXED_5,PaymentFrequency.MONTHLY,30) 
        with self.assertRaises(ValueError):
            mortgage.frequency = 2323 
        # test to validate when invalid input is given, it shows error

    def test_valid_frequency(self):
        mortgage = Mortgage(10000,MortgageRate.FIXED_5,PaymentFrequency.MONTHLY,30) 
        mortgage.frequency = PaymentFrequency.WEEKLY
        self.assertEqual(mortgage.frequency,PaymentFrequency.WEEKLY) 
        # test to validate when valid input is given, it doesn't show error

    def test_invalid_amortization(self):
        mortgage = Mortgage(10000,MortgageRate.FIXED_5,PaymentFrequency.MONTHLY,30) 
        with self.assertRaises(ValueError):
            mortgage.amortization = 2323
        # test to validate when invalid input is given, it shows error

    def test_valid_amortization(self):
        mortgage = Mortgage(10000,MortgageRate.FIXED_5,PaymentFrequency.MONTHLY,30) 
        mortgage.amortization = 15
        self.assertEqual(mortgage.amortization,15) 
        # test to validate when valid input is given, it doesn't show error
    
    def test_calculate_payment_monthly(self):
        mortgage = Mortgage(682912.43, MortgageRate.FIXED_1, PaymentFrequency.MONTHLY, 30)
        calculated_payment = mortgage.calculate_payment()
        self.assertAlmostEqual(calculated_payment, 4046.23, places=2)
        # test whether calculate_payment can calculate monthly payment 

    def test_calculate_payment_weekly(self):
        mortgage = Mortgage(682912.43, MortgageRate.FIXED_1, PaymentFrequency.WEEKLY, 30)
        calculated_payment = mortgage.calculate_payment()
        self.assertAlmostEqual(calculated_payment, 933.11, places=2)
        # test whether calculate_payment can calculate weekly payment 

    def test_calculate_payment_biweekly(self):
        mortgage = Mortgage(682912.43, MortgageRate.FIXED_1, PaymentFrequency.BI_WEEKLY, 30)
        calculated_payment = mortgage.calculate_payment()
        self.assertAlmostEqual(calculated_payment, 1866.6, places=2)
        # test whether calculate_payment can calculate biweekly payment 

    def test_str_monthly(self):
        mortgage = Mortgage(682912.43, MortgageRate.FIXED_5, PaymentFrequency.MONTHLY, 30)
        expected = (
            f"Mortgage Amount: $682,912.43\n"
            f"Rate: 5.00%\n"
            f"Amortization: 30\n"
            f"Frequency: MONTHLY -- Calculated Payment: ${mortgage.calculate_payment():,.2f}"
        )
        self.assertEqual(str(mortgage), expected)
        # test whether __str__ can show desired output
        
    def test_str_biweekly(self):
        mortgage = Mortgage(682912.43, MortgageRate.FIXED_5, PaymentFrequency.BI_WEEKLY, 30)
        expected = (
            f"Mortgage Amount: $682,912.43\n"
            f"Rate: 5.00%\n"
            f"Amortization: 30\n"
            f"Frequency: BI_WEEKLY -- Calculated Payment: ${mortgage.calculate_payment():,.2f}"
        )
        self.assertEqual(str(mortgage), expected)
        # test whether __str__ can show desired output

    def test_str_weekly(self):
        mortgage = Mortgage(682912.43, MortgageRate.FIXED_5, PaymentFrequency.WEEKLY, 30)
        expected = (
            f"Mortgage Amount: $682,912.43\n"
            f"Rate: 5.00%\n"
            f"Amortization: 30\n"
            f"Frequency: WEEKLY -- Calculated Payment: ${mortgage.calculate_payment():,.2f}"
        )
        self.assertEqual(str(mortgage), expected)
        # test whether __str__ can show desired output

    def test__repr__representation(self):
        mortgage = Mortgage(682912.43, MortgageRate.FIXED_5, PaymentFrequency.WEEKLY, 30)
        expected_repr = f"[{mortgage._loan_amount}, {mortgage._rate.value}, {mortgage._amortization}, {mortgage._frequency.value}]"
        self.assertEqual(repr(mortgage), expected_repr)
        # test whether __repr__ can show desired output
if __name__ == '__main__':
    unittest.main()

#python -m unittest -v tests/test_mortgage.py