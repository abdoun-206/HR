#Abdoulaye Ndiaye
#Python 310 HR Assgmt
#05/21/2021

"""
With your newly acquired Python skills you have been asked by a friend who runs a small business to develop
an application to keep track of her employees.There will be about 40-50 employees.
"""

import csv

with open('employee.csv', 'w', newline='') as f:
    data = csv.writer(f, delimiter=',')
    employee = data.writerow(['First_name', 'Last_name', 'ID'])
    data.writerow(['John', 'Doe', '100'])
    data.writerow(['Omar', 'Garcia', '101'])
    data.writerow(['Abdul', 'Ndiaye', '102'])
    data.writerow(['Bill', 'Gates', '103'])
    data.writerow(['Alan', 'Barry', '104'])
    data.writerow(['Andy', 'Miles', '105'])
    data.writerow(['Susan', 'Little', '106'])
    data.writerow(['Muhammad', 'Diallo', '107'])
    data.writerow(['Mamadu', 'Barro', '108'])
    data.writerow(['Eric', 'Domingo', '109'])
    data.writerow(['Sanjay', 'Gupta', '110'])
    data.writerow(['Yao', 'Zao', '111'])
    data.writerow(['Gay', 'Tou', '112'])
    data.writerow(['Ellen', 'Johnson', '113'])
    data.writerow(['Alice', 'White', '114'])
    data.writerow(['Zach', 'Summer', '115'])
    data.writerow(['Ali', 'Traore', '116'])
    data.writerow(['George', 'Gilbert', '117'])
    data.writerow(['Clinton', 'Fearon', '118'])
    data.writerow(['Mark', 'Zuckerburg', '119'])
    data.writerow(['Jeff', 'Bezos', '120'])
