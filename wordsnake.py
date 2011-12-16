print "\n\nWELCOME TO WORDSSSSSSSSSSSSSSSSSSSNAKE\n\n"

word = "exfoliant"
needed = set(list(word))
snake = ">--:OOOOooo~~~"
me = ":-)"   

right = list()
turns = 10
bad=list()
dead=False
won=False
whichturn = 0
while not (dead or won):
    whichturn = whichturn+1

    #import pdb
    #pdb.set_trace()
    print "\n\n=== TURN ", whichturn, "===\n\n"

    print me + " "*(turns-len(bad)) + snake 

    # print the word in progress
    print "word so far: ",
    for l in word:
        if l in right:
            print l,
        else:
            print "_", 

    print "\n"

    print "bad guesses: ", bad
    letter = raw_input("Guess a letter: ").strip().lower()
    if letter in word:
        print "\nGOOD GUESS!!", letter,  "is in the word!"
        if letter in needed:
            needed.remove(letter)
            right.append(letter)
        
        # all of the letters have been found
        if not needed:
            print "you win!  word is \n\n  :: ", word , ":: \n\n"
            won=True
    else:
        print "\nBZZZZT!  WRONG GUESS.  SNAKE GOT CLOSER"
        bad.append(letter)
        if len(bad) > turns: 
            print "You have died!"
            died = True
