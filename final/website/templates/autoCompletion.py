import time
import keyboard
import sqlite3

def search_strs():
    search_str = ""
    while True:
        time.sleep(0.1)
        key_press = keyboard.read_key()
        if key_press == "backspace" and search_str:
            search_str = search_str[:-1]
        elif len(key_press) == 1 and ('a' <= key_press <= 'z'):
            search_str += keyboard.read_key()
        else:
            continue
        yield search_str

def inputValue(givenValue):
    return givenValue
	

def init(request):
    givenValue = request.POST['country']
    words = []
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT Country FROM Uni_Programs_Requ")
    data = c.fetchall()
    for row in data:
        for word in row:
            words.append(word.strip().lower())
            
    for search_str in inputValue(givenValue):
        for word in words:
            if word[:len(search_str)] == search_str:
                print(word)
                result += word
                return result
                
if __name__ == '__main__':
    result = init()