#Abdoulaye Ndiaye
#Python 310 HR Assgmt
#05/21/2021

"""
With your newly acquired Python skills you have been asked by a friend who runs a small business to develop
an application to keep track of her employees.There will be about 40-50 employees.
"""

import csv

with open('employee.csv', 'w', newline='') as f:
    data = csv.writer(f, delimeter=',')
    employee = [['First_name', 'Last_name', 'ID']
                ['John', 'Doe', '100']
                ['Omar', 'Garcia', '101']
                ['Abdul', 'Ndiaye', '102']
                ['Bill', 'Gates', '103']
                ['Alan', 'Barry', '104']
                ['Andy', 'Miles', '105']
                ['Susan', 'Little', '106']
                ['Muhammad', 'Diallo', '107']
                ['Mamadu', 'Barro', '108']
                ['Eric', 'Domingo', '109']
                ['Sanjay', 'Gupta', '110']
                ['Yao', 'Zao', '111']
                ['Gay', 'Tou', '112']
                ['Ellen', 'Johnson', '113']
                ['Alice', 'White', '114']
                ['Zach', 'Summer', '115']
                ['Ali', 'Traore', '116']
                ['George', 'Gilbert', '117']
                ['Clinton', 'Fearon', '118']
                ['Mark', 'Zuckerburg', '119']
                ['Jeff', 'Bezos', '120']]
    data.writerow(employee)