"""
    Based on these 2 paragrahs 
    * [Writing CSV Files With csv](https://realpython.com/python-csv/#writing-csv-files-with-csv) and 
    * [Writing CSV File From a Dictionary With csv](https://realpython.com/python-csv/#writing-csv-file-from-a-dictionary-with-csv)
    Create a dictionary and write the content into a csv file
"""
import csv

with open('employee_file2.csv', mode='w') as csv_file:
    fieldnames = ['Name','Age','Cpr']
    writer = csv.DictWriter(csv_file, fieldnames = fieldnames)

    writer.writeheader()
    writer.writerow({'Name':'Marcus','Age':'22','Cpr':'1234567890'})
    writer.writerow({'Name':'John','Age':'32','Cpr':'0402747345'})