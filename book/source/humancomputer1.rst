.. humancomputer:

=====================
The Human Computer!
=====================

..  warning::

    IF YOU ARE A STUDENT **TURN BACK NOW**.  You will have more fun if you don't
    know all the solutions up-front!


Audience
---------

Introductory programming students, who have used computers, but may not
have any formal programming training or experience.

Introduction (for the facilitator)
------------------------------------

Programming is normally taught in one of two ways: lecture or self-study.  With this exercise,
we are hoping to add a kinesthetic component.  

In this exercise, players will build a HUMAN COMPUTER, where they will play-act functions,
variables, flow control constructs and the like. 


Setup and Materials
-----------------------

*   The facilitator should understand the example program, and possible variations.
    If you can't program FizzBuzz in your language of choice, spend some time
    learning that first!

*   You will need:

    *  a big white board, chalkboard or equivalent to represent the "screen",
       for the printer
    *  some small whiteboard (hand size).  5 or so should be sufficient.
    *  index cards for ``return`` values.  

Running The Exercise
-----------------------

Keep this "example of play" in mind during the rest of the notes:

    After designing their machine, Adele, Ben, Jes, and Siri are chosen to play
    four of the parts in the computation.
    Adele plays ``main`` (the controller). Ben plays ``loopindex``, an integer variable.
    Jes plays ``print``. Siri plays ``div2``, a function that takes ``int`` and 
    returns ``boolean``.

    After a few rounds of computation, ``loopindex`` has the value 3.

    Adele:  ``loopindex``, what is your value?
        
    Ben:  (shows the 2 on his small white board)

    Adele:  "Siri, what does ``div2`` say about 3?"

    Siri:  That's ``True`` because it is divisible by 2 evenly (*holds up a "True" card*).

    Adele:  Jes, since that is ``True``, ``print 3, "buzz"`` please.

    Jes:  Got it!  (*writes '3 buzz' on the board*)
    

#.  Read THE SPEC aloud to the classroom.  

#.  Write **PARTS LIST** on the board.  This is where you will name and list all the *code*.

#.  DESIGN THE PROGRAM TOGETHER.  

    The classroom is meant to simulate a virtual machine for a "high-level" language 
    (such as Python) with appropriate primtives,
    such as *variables* (string, Boolean, integers), *flow control*, and *functions*.  

    You are the referee for whether or not a particular primitive is too simple or too complex.
    Since this is a Python course, sticking to ones that map well into Python syntax
    is probably wise!  For example, suggest ``print`` to them, if they are focusing

    Let them work out some tools for how to meet the spec.  Prompt with hints as necessary.  
    The goal here is to get the class to realize the important concepts of STATE, SUBROUTINES,
    VARIABLES, and OUTPUT.  As they discover / design parts, put them in the **parts list**.

    
    Example of guided exploration:

        Would it be useful to have a part whose job is to know if a number is 
        divisible by 3?  *class agrees.*  What would be a good name for it?  *Someone suggests "div3"*.   
        (*write down ``div3`` in the **PARTS LIST**).  What kinds of responses can it give?  (look for 
        True/False or similar.  If the class says 1,0  explain that our machine knows about True/False).

    There is no need to slavishly stick to Python syntax or constructions.  Is they sponteneously
    discover recursion, or generators, let the players follow it!  If instead
    of a while loop, they suggest "we invent a thing that spits out one
    number at a time until it hits 15", let them have ``xrange``!  

    NOTE:  you might have to give them 'while' (or another looping construct) for free to get them 
    started.  Don't use too much time on the mechanics of this.  

#.  Review the **parts list**, and write a bit of "spec notation" on each, including types,
    inputs, outputs, what it does (docstring).

#.  PLAY OUT the computation.  Assign player for each part.    

    * Each VARIABLE should get a small dry-erase white board, and a marker.  At the top
      in one corner, the should write the name of their variable LABEL(s).
      As their value changes, they should update their value accordingly.

    * Each FUNCTION should get index cards to "return"
      values.  Those returning booleans should get (or make) stacks of "True" and 
      "False" cards.  

    * Have the compiler hand over control to ``main`` start the calculation.  ``main``
      is in charge of (in most designs):

      * assignments
      * calls to other functions
      * looping (in some designs)

    * eventually ``main`` will hand control back to the compiler, and the program will
      finish.  

    * take the first few rounds slowly.  It might be worthwhile to have an actual 
      "runner" to *physically carry* inputs and returns around.

#.  Throw in some curveballs.  Stop the calculation periodically to check for understanding.
    Some suggestions:

    *  ask for the value of variables that don't exist yet.  (in Python,
       these would raise ``NameError``.  In other languages students know,
       some other behaviour might happen! 
    *  ask ``div2`` for a judgement on ``"a"``.  Since ``div2`` should only accept
       integers, this is a good time to explain ``Exception`` and ``raise``, or
       their equivalents. 

#.  (Extra credit) Translate the code they made into Python.

Hints for Better Play
------------------------

* don't particular players to "hog the spotlight".  All the parts of the program are
  need to make the computation run!
* if the computation is taking too long, cut down the spec to ``n=10``.  
* Since there are 
  infinite variations about to implement FizzBuzz, the "player" list below 
  is merely a suggestion.  If you have *lots* of players, allow people
  to change roles partly through, or add more roles (suggest more parts to the program).    


.. thespec:

The Spec
~~~~~~~~~

A user out in userland has demanded some work.
You, the HUMAN COMPUTER, are going to implement it.  As a group,
you are going to carry out a computation consistent with this specification:

    For the numbers from 1 to 15 (inclusive), if the number is EVEN,
    then print the number and the word "FIZZ".  If the number is 
    DIVISIBLE BY 3 (exactly), then print the number and the word "BUZZ".

Rememeber, computers are dumb!  They exhibit apparent complexity by COMBINING
SIMPLE OPERATIONS.  


Possible Player Roles
----------------------

Players play 'parts' of the machine, including clauses, functions, and variables.
Some players that might be involved in modeling "A Possible Solution" below are: 

* the "compiler" (to enforce that all rules are followed)
* the "runner" (who brings values into, and returns from functions or the like)
* ``ii`` (a variable) 
* ``div2`` (a boolean function)
* ``div3`` (a boolean function)
* ``printer`` (a void function, that side effects printing to ``stdout``)
* ``main`` (a controller)
* ``True`` (a constant)
* ``while`` (a clause)


Learning Goals
----------------

* algorithmic thinking
* code as message passing
* variables and their values are different
* the global state
* ``while`` loops
* ``TypeError``


A Possible Solution
--------------------

::

    def div2(ii):
        return ii %2 == 0

    def div3(ii):
        return ii %3 == 0

    def main():
        ii = 1
        while ii <= 15:
            if div2(ii):
                print ii, "FIZZ"
            
            if div3(ii):
                print ii, "BUZZ"
        ii+=1

    main()  # start off the whole thing.

