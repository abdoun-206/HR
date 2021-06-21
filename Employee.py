#Abdoulaye Ndiaye
#Python 310 HR Assgmt
#05/21/2021

"""
With your newly acquired Python skills you have been asked by a friend who runs a small business to develop
an application to keep track of her employees.There will be about 40-50 employees.
"""

import csv

with open('employee2.csv', 'w', newline='') as f:
    data = csv.writer(f, delimiter=',')
    employee = data.writerow(['First_name', 'Last_name', 'ID', 'Email', 'Start Date'])
    data.writerow(['John', 'Doe', '100', 'j.doe@ABC.com', '05/14/2021'])
    data.writerow(['Omar', 'Garcia', '101', 'o.garcia@ABC.com', '05/19/2021'])
    data.writerow(['Abdul', 'Ndiaye', '102', 'a.andiaye@ABC.com', '04/19/2021'])
    data.writerow(['Bill', 'Gates', '103', 'b.gates@ABC.com', '03/19/2021'])
    data.writerow(['Alan', 'Barry', '104', 'a.barry@ABC.com', '02/19/2021'])
    data.writerow(['Andy', 'Miles', '105', 'a.miles@ABC.com', '03/15/2021'])
    data.writerow(['Susan', 'Little', '106', 's.little@ABC.com', '03/14/2021'])
    data.writerow(['Muhammad', 'Diallo', '107', 'm.diallo@ABC.com', '04/19/2020'])
    data.writerow(['Mamadu', 'Barro', '108', 'm.barro@ABC.com', '03/10/2020'])
    data.writerow(['Eric', 'Domingo', '109', 'e.domingo@ABC.com', '03/19/2020'])
    data.writerow(['Sanjay', 'Gupta', '110', 's.gupta@ABC.com', '02/05/2020'])
    data.writerow(['Yao', 'Zao', '111', 'y.zao@ABC.com', '02/06/2020'])
    data.writerow(['Gary', 'Tou', '112', 'g.tou@ABC.com', '02/19/2020'])
    data.writerow(['Ellen', 'Johnson', '113', 'a.johnson@ABC.com', '01/17/2020'])
    data.writerow(['Alice', 'White', '114', 'a.white@ABC.com', '09/19/2020'])
    data.writerow(['Zach', 'Summer', '115', 'z.summer@ABC.com', '10/15/2020'])
    data.writerow(['Ali', 'Traore', '116', 'a.traore@ABC.com', '11/11/2020'])
    data.writerow(['George', 'Gilbert', '117', 'g.gilbert@ABC.com', '02/12/2020'])
    data.writerow(['Clinton', 'Fearon', '118', 'c.fearon@ABC.com', '08/19/2020'])
    data.writerow(['Mark', 'Zuckerburg', '119', 'm.zuckerberg@ABC.com', '04/19/2019'])
    data.writerow(['Jeff', 'Bezos', '120', 'j.bezos@ABC.com', '03/10/2019'])


