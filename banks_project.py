# Code for ETL operations on Country-GDP data

# Importing the required libraries
from datetime import datetime as dt
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import sqlite3

def log_progress(message):
    ''' This function logs the mentioned message of a given stage of the
    code execution to a log file. Function returns nothing'''
    timestamp_format = '%Y-%h-%d-%H:%M:%S' # Year-Monthname-Day-Hour-Minute-Second 
    now = dt.now()
    timestamp = now.strftime(timestamp_format)
    with open('code_log.txt', "a") as f:
        f.write(f"{timestamp}: {message}")


def extract(url, table_attribs):
    ''' This function aims to extract the required
    information from the website and save it to a data frame. The
    function returns the data frame for further processing. '''
    page = requests.get(url).text
    data = BeautifulSoup(page, 'lxml')
    df = pd.DataFrame(columns=table_attribs)
    tables = data.find_all('tbody')
    rows = tables[0].find_all('tr')
    for row in rows:
        col = row.find_all('td')
        
        if len(col)!=0:
            if col[1].find('a') != -1 and '_' not in col[2]:
                print()
                data_dict = {"Bank_Name": col[1].find_all('a')[1].text.strip(),
                                "MC_USD_Billion": col[2].contents[0].rstrip('\n')}
                df1 = pd.DataFrame(data_dict, index=[0])
                df = pd.concat([df,df1], ignore_index=True)
    return df


def transform(df, csv_path):
    ''' This function accesses the CSV file for exchange rate
	information, and adds three columns to the data frame, each
	containing the transformed version of Market Cap column to
	respective currencies'''

    return df

def load_to_csv(df, output_path):
    ''' This function saves the final data frame as a CSV file in
	the provided path. Function returns nothing.'''

def load_to_db(df, sql_connection, table_name):
    ''' This function saves the final data frame to a database
	table with the provided name. Function returns nothing.'''

def run_query(query_statement, sql_connection):
    ''' This function runs the query on the database table and
    prints the output on the terminal. Function returns nothing. '''

''' Here, you define the required entities and call the relevant
functions in the correct order to complete the project. Note that this
portion is not inside any function.'''

url = (
    "https://web.archive.org/web/20230908091635/"
    "https://en.wikipedia.org/wiki/List_of_largest_banks"
)

table_attribs = ["Bank_Name", "MC_USD_Billion"]
table_attribs_final = [
    "Name",
    "MC_USD_Billion",
    "MC_GBP_Billion",
    "MC_EUR_Billion",
    "MC_INR_Billion",
]

output_csv_path = "./Largest_banks_data.csv"
db_name = "Banks.db"
table_name = "Largest_banks"
log_file = "code_log.txt"

log_progress('Preliminaries complete. Initiating ETL process')

#log extraction
log_progress('Data extraction complete. Initiating Transformation process')
print(extract(url, table_attribs))
# df = extract(url, table_attribs)
# print(df)
