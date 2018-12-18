#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 10:24:00 2018

@author: ep9k
"""

class Employee:
    
    num_of_emps = 0
    raise_amount = 1.04     #this is a class variable. applies to all instances of the class
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{first}.{last}@company.com'
        
        Employee.num_of_emps += 1

    def fullname(self):
        return(f'{self.first} {self.last}')
        
    def full_info(self):
        print("Full information about employee:")
        print(f"First Name: {self.first}")
        print(f"Last Name: {self.last}")
        print(f"Pay: {self.pay}")
        print(f"Email: {self.email}")
        
    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)    #I like this better because this is clear to me that raise_amount is a class variable
        
    @classmethod
    def set_raise_amt(cls, amount):
        pass


emp1 = Employee('Corey', 'Schafer', 50000)
emp2 = Employee('Test', 'User', 60000)

employee_list = [emp1, emp2]



#print(Employee.fullname(emp1))
#
#for employee in employee_list:
#    Employee.full_info(employee)
#    print()

print(Employee.num_of_emps)
        