# Latest version. Defualt.
try:
    while True:
        print ("Gamemode Selection:")
        print ("(1) Classic")
        print ("(2) Wavebased")
        print ("(3) Interesting")
        e = input("")
        if e == "1":
          import ver_12
        elif e == "2":
          import ver_12_wavebased
        elif e == "3":
          import ver_12_interesting
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    print("if you get a 'no module named pygame' error, that means you dont have pygame. go get pygame. read the 'readme.md' file stupid.")
    print("if you get litteraly any other error DM me and i'll take a look at it.")
    try:
        input("")
    except Exception as e:
        print(f"An unexpected error occured: {e}")

# Made by Sandstorm / united2300
