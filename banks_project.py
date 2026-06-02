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

def extract(url, table_attribs):
    ''' This function aims to extract the required
    information from the website and save it to a data frame. The
    function returns the data frame for further processing. '''

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

data_url = (
    "https://web.archive.org/web/20230908091635/"
    "https://en.wikipedia.org/wiki/List_of_largest_banks"
)

table_attribs_extract = ["Name", "MC_USD_Billion"]
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
