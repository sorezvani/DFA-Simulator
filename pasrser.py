from bs4 import BeautifulSoup

with open('dfasample.xml', 'r') as f:
    data = f.read()
Bs_data = BeautifulSoup(data, features="xml")


def find_alphabet():
    final = []
    alphabet = Bs_data.find("Alphabets")
    num = int(alphabet.get("numberOfAlphabets"))
    alphabet = alphabet.find("alphabet")
    final.append(alphabet.get("letter"))
    for i in range(num - 1):
        alphabet = alphabet.find_next_sibling("alphabet")
        final.append(alphabet.get("letter"))
    return final


def find_states():
    final = []
    states = Bs_data.find("States")
    num = int(states.get("numberOfStates"))
    states = states.find("state")
    final.append(states.get("name"))
    for i in range(num - 1):
        states = states.find_next_sibling("state")
        final.append(states.get("name"))
    return final


def find_init_state():
    init_state = Bs_data.find("States")
    init_state = init_state.find("initialState")
    return init_state.get("name")


def find_final_states():
    final = []
    final_states = Bs_data.find("FinalStates")
    num = int(final_states.get("numberOfFinalStates"))
    final_states = final_states.find("finalState")
    final.append(final_states.get("name"))
    for i in range(num - 1):
        final_states = final_states.find_next_sibling("finalState")
        final.append(final_states.get("name"))
    return final


def find_transitions():
    final = []
    transition = Bs_data.find("Transitions")
    num = int(transition.get("numberOfTrans"))
    transition = transition.find("transition")
    final.append((transition.get("source"), transition.get("destination"), transition.get("label")))
    for i in range(num - 1):
        transition = transition.find_next_sibling("transition")
        final.append((transition.get("source"), transition.get("destination"), transition.get("label")))
    return final
