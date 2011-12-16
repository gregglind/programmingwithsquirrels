
ans = raw_input("Choose:  rock, paper, scissors\n").strip()

import random
their = random.choice(['rock','paper','scissors'])

print "theirs is", their

if ans == 'rock':
    if their == 'scissors':
        print 'rock breaks scissors'
    if their == 'rock':
        print 'rock ties rock'
    if their == 'paper':
        print 'paper covers rock'

if ans == 'scissors':
    if their == 'scissors':
        print 'scissors ties scissors'
    if their == 'rock':
        print 'rock ties scissors'
    if their == 'paper':
        print 'scissors cuts paper'

if ans == 'paper':
    if their == 'scissors':
        print 'scissors cuts paper'
    if their == 'rock':
        print 'paper covers rock'
    if their == 'paper':
        print 'paper ties paper'


"""
So what stinks here?

* lots of repeated text
* if vs elif
* only plays once
"""

