from pasrser import *

alphabets = []
states = []
init_state = " "
final_state = []
Transitions = []
now_state = ""
string = ""


def __init__(st):
    global string, now_state, init_state
    now_state = init_state
    string = st
    return check_string()


def check_string():
    global string, now_state, Transitions, final_state, now_state, alphabets
    while string != "":
        letter = string[0]
        string = string[1:]
        flag = True
        if letter not in alphabets:
            return "alphabet error"
        for transition in Transitions:
            if transition[0] == now_state:
                if transition[2] == letter:
                    now_state = transition[1]
                    flag = False
                    break
        if flag:
            return False
    if string == "":
        return now_state in final_state


alphabets = find_alphabet()
states = find_states()
init_state = find_init_state()
final_state = find_final_states()
Transitions = find_transitions()