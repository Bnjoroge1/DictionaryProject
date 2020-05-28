import mysql.connector
import time
from difflib import get_close_matches
 
def db_conn():
    con = mysql.connector.connect(
    user = "ardit700_student",
    password="ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
    )
    return con
 
def db_search(word):
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM Dictionary WHERE Expression = '{word}'")
    results = cursor.fetchall()
    return results
 
def close_matches(word):
    cursor = conn.cursor()
    query = cursor.execute("SELECT * FROM Dictionary")
    all = cursor.fetchall()
    all_words = []
    for q in all:
        all_words.append(q[0])
    close_words = get_close_matches(word, all_words, n = 3, cutoff = 0.85)
    return close_words
 
def all_words():
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM Dictionary")
    results = cursor.fetchall()
    return results
 
 
def close_word_submission(word):
    all = []
    for v in local_result:
        all.append(v[1])
        return(all)
 
def posibilities(local_result, word):
    if local_result:
        all = []
        for v in local_result:
            all.append(v[1])
        return(all)
    else:
        all_dict = all_words()
        for all in all_dict:
            if word.upper() == all[0]:
                return all
            elif word.title() == all[0]:
                return all
            elif close_matches(word):
                close_word = close_matches(word)
                yn = input(f'Word not found. Did you mean {close_word[0]}? y/n > ')
                if yn == 'y':
                    new_all = []
                    for v in all_dict:
                        if v[0] == close_word[0]:
                            new_all.append(v[1])
                    print(f"new_all = {new_all} and type is {type(new_all)}")
                    return new_all
                else:
                    return 'Input not recognised'
            else:
                return 'Word not found'
 
conn = db_conn()
while True:
    word = input('Enter a word or enter "exit()" to close program > ').lower()
    if word == 'exit()':
        print('Thanks for using our app. Goodbye...')
        time.sleep(1)
        break
    else:
        local_result = db_search(word)
        output = (posibilities(local_result, word))
        if isinstance(output, list):
            for o in output:
                print(o)