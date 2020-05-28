#An interactive COnsole DIcionary Application that fetches data from a db and inteeelligently returns responses to the users.
import mysql.connector
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches
import time



connection = mysql.connector.connect(
user = "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database"
)
cursor = connection.cursor()
query = cursor.execute("SELECT * FROM Dictionary")
results = cursor.fetchall()

user_query = input("Enter a word you wish to search:  \n")

def listTupleToDict(tup, Dict):
    Dict = dict(tup)
    return Dict

dictionary = {}
close_match = get_close_matches(user_query, (listTupleToDict(results, dictionary).keys()))

def CheckWord(user_query):
    user_query = user_query.lower()
    if user_query in results:
        return cursor.execute(f"SELECT * FROM Dictionary WHERE Expression = '{user_query}'")
    if user_query.title() in results:
        return cursor.execute("SELECT * FROM Dictionary WHERE Expression = '{}'").format(user_query.title())
    if user_query.upper() in results:
        return cursor.execute("SELECT * FROM Dictionary WHERE Expression = '{}'").format(user_query.upper())
    if len(close_match) > 0 :
        second_input = input(f"Did you mean {close_match[0]} instead ? \n Y if yes, N if No")
        if "Y" in second_input:
            return cursor.execute(f"SELECT * FROM Dictionary WHERE Expression = '{close_match[0]}'")
        elif "N" in second_input:
            return "Oh. Well I'm sorry but we cant find the word in the dicionary"
            time.sleep(1)
            exit()
        else:
            return "Please input one of the options"


Output = CheckWord(user_query)
 
if isinstance(Output, list):
    for out in Output:
        print(result[1])
else:
    print(Output)


