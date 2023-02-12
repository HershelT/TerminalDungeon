while True:
        os.system('cls')
        type = input("\nAre you running this on Command Prompt or similar?\n(Windows CMD or Mac OS)\nBreaks game if given incorrect answer!!!!\n->")
        mess = type.lower()
        if "y" == mess or "yes" in mess: inits = True; Call.inits = True; break
        elif "n" == mess or "no" in mess: inits = False; break
    if Call.inits == True: print("Running init")