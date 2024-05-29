import Dfa

while True:
    s = input()
    if s == "exit":
        break
    x = Dfa.__init__(s)
    if x == "alphabet error":
        print("alphabet is not in list")
    elif x:
        print("The input string is accepted.")
    else:
        print("The input string is not accepted.")
