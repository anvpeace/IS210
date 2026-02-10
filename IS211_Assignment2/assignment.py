import urllib.request
import argparse
import csv
from datetime import datetime
import io

# Write a function called downloadData, which takes in a string called url. The purpose of this function is
# to download the contents located at the url and return it to the caller. You should use urllib2 for this. Do not
# catch any exceptions here, as this will be done later.

url = "https://s3.amazonaws.com/cuny-is211-spring2015/birthdays100.csv"

def downloadData(url):
    with urllib.request.urlopen(url) as response:
        response = response.read().decode('utf-8')

    return response

# Write a function called processData, which takes the contents of the file as the first parameter, processes
# the file line by line, and returns a dictionary that maps a person’s ID to a tuple of the form (name, birthday).
# The birthday needs to be a Datetime object, not a string. You will have to process the birthday, which has a
# format of dd/mm/yyyy, and convert it into a Datetime object (NOTE: the time portion of the Datetime object
# will be 0, since we are not setting a time, just a date; you can use the Date object instead, if you feel
# comfortable doing so)

def processData(fileData):
    people = {}

    file = io.StringIO(fileData)
    reader = csv.reader(file)
    
    for row_num, row in enumerate(reader, start=1):

        if not row:
            continue
        
        name = row[0].strip()
        birthday = row[1].strip()
        person_id = int(row[2].strip())

        datetime_birthday = datetime.strptime(birthday, "%d/%m/%Y")

        people[person_id] = (name, datetime_birthday)
    
    return people