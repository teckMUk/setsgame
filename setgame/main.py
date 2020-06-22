import argparse

FUNCTION_MAP = {"setsgame":set_finder , "drawcards": draw_12_card}


def set_prase() -> ArgumentParser:
    parser = argparse.ArgumentParser(description="This file runs the game called sets game")

    parser.add_argument("-s", "--setgame", dest="func", choices=FUNCTION_MAP.keys())
    parser. add_argument("-c","--cards", dest = "id", required =True , ngars = 3)  

def find_my_card(id_number):
    myquery = {"_id" : id_number}
    for card in mycol.find(myquery):
        return card



def draw_12_card():
    for number in range(1,13):
        x = random.randint(1,81)
        print(find_my_card(x))

def set_finder(id):
    
    card_1 = find_my_card(id[0])
    card_2 = find_my_card(id[1])
    card_3 = find_my_card(id[2])
    set_or_not = True
    if card_1['color'] == card_2['color'] and card_1['color'] != card_3['color']:
        set_or_not = False
    elif card_1['color'] != card_2['color'] and card_1['color'] == card_3['color']:
        set_or_not = False
    if card_1['shape'] == card_2['shape']  and card_1['shape'] != card_3['shape']:
        set_or_not = False
    elif card_1['shape'] != card_2['shape']  and card_1['shape'] == card_3['shape']:
        set_or_not = False
    if card_1['fill_type'] == card_2['fill_type']  and card_1['fill_type'] != card_3['fill_type']:
        set_or_not = False
    elif card_1['fill_type'] != card_2['fill_type']  and card_1['fill_type'] == card_3['fill_type']:
        set_or_not = False
    if card_1['Number of shapes'] == card_2['Number of shapes']  and card_1['Number of shapes'] != card_3['Number of shapes']:
        set_or_not = False
    elif card_1['Number of shapes'] != card_2['Number of shapes']  and card_1['Number of shapes'] == card_3['Number of shapes']:
        set_or_not = False    
    if set_or_not == True:
        print("Yes")
    else:
        print("No")   



def main():
     parser = set_prase()
     args: Namespace = parser.parse_args()
     call_func = FUNCTION_MAP[func]
     call_func()
     set_finder(id.args)                   