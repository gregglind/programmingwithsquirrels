..  _humancomputer:

=====================
The Human Computer!
=====================

..  warning::

    IF YOU ARE A STUDENT **TURN BACK NOW**.  You will have more fun if you don't
    know all the solutions up-front!  (Or go on to :ref:`Player Materials <fizzbuzz-player>`).


Audience
---------------------

Introductory programming students, who have used computers, but may not
have any formal programming training or experience.  


Introduction (for the facilitator)
------------------------------------

Programming is normally taught in one of two ways: lecture or self-study.  With this exercise,
we are hoping to add a kinesthetic component.  

In this exercise, players will build a HUMAN COMPUTER, where they will play-act functions,
variables, flow control constructs and the like. 




Before the Exercise (Setup and Materials)
-----------------------------------------------

*   The facilitator should understand the example program, and possible variations.
    If you can't program FizzBuzz in your language of choice, spend some time
    learning that first!

*   You will need:

    *  a big white board, chalkboard or equivalent to represent the "screen",
       for the printer
    *  some small whiteboard (hand size).  5 or so should be sufficient.
    *  index cards for ``input`` and ``return`` values.  

*   Print some copies of the **Player Materials**


Running the Exercise
--------------------------

#.  You read and did the **Before The Exercise** above, right?

#.  Read players the spec.  

    As a group, you are going to design and carry out a computation 
    consistent with this specification:

        For the numbers from 1 to 15 (inclusive), 
            if the number is EVEN,  
                then print the number and the word "FIZZ".  
            if the number is DIVISIBLE BY 3 (exactly), 
                then print the number and the word "BUZZ".

#.  Design it! (Part 1: highlevel, flowchart).

    Instructor:

        Now, let's design the machine.  We are going to use flowcharts to make
        a first pass at modelling it...
    
    #.  give them flowchart ideas:  ``storage``, ``decisions``, ``processes``
        ``termination``.
        
        Write these on the board:

        * diamonds are **choices**.
        * cylinders are **data storage**.
        * boxes are **processing** steps, including all output.
        * (small) circles are **termination** steps (start/stop).

    #.  they should construct a flowchart from the 'English' in the spec.
    #.  start them off with 'loop' at 4, if they need it or get stuck
    #.  a correct answer includes all of:

        *  starting conditions
        *  ending condition 
        *  spec being met
        *  correct starting and finishing indices [1..15]

    ..  image:: _static/img/Visio-fizzbuzz2.png
        :width: 300px
        :align: center
        :alt: FizzBuzz Flow Diagram
        :target: _static/img/Visio-fizzbuzz.png


#.  Design it! (Part 2: low-level, stack-based, 'sequence diagram')

    Instructor text:

        So, lets look at what is going on inside one of those branch points!
        Let's pick on "is the number divisible by three".
        Remember, computers are pretty dumb.  

    *   introduce sequence diagram.  http://en.wikipedia.org/wiki/Sequence_diagram
    *   for the lanes, start with ``controller``, ``is divisible by 3``
    *   guide the class to invent/discover ``div3``.  
    *   The final answer might look like this:

        ..  image:: _static/img/fizzbuzz-sequence.png
            :width: 300px
            :align: center
            :alt: FizzBuzz Sequence Diagram.
            :target: _static/img/fizzbuzz-sequence.png

    *   Assign players to the roles in sequence diagram, and act out the sequence.
        This teaches players the rules.  [see 'Example of play' below]


#.  Act out the computation.  

    #.  Assign roles.  Generate a *parts list* from the flow diagram, 
        and write a bit of "spec notation" on each, 
        including types, inputs, outputs, what it does (docstring).

    #.  Issue props and get into position:

        * storage:  little whiteboard and marker
        * print process:  go to big whiteboard
        * controller, branch.  cards to issue message requests (with variables)
        * processes:  index cards to give return values, if any.  

    ``controller``

    * set, read, modify variables
    * ask branch points "where do I go next", and receive answers
    * call functions and statements
    * runs from 'top to bottom'.
    * programs begin and end with the controller.  

    ``decisions``

    * get asked by controllers "where next"
    * answers with a branch:  e.g., "go to branch 'yes'"
    * to get that answer, can do PROCESSING, including looking up variables,
      calling functions, etc.

    ``processors`` (functions)

    * get inputs (which are all values)
    * returns outputs.

    ``storage``

    * say their value, upon request
    * set / change their value, by order of the controller.  


    #.  Control starts with the controller, and passes around as previously
        described.  

    #.  Throw in some curveballs.  Stop the calculation periodically to check for understanding.
        Some suggestions:

        *  what if the ``div2`` and ``div3`` sections were reversed?  What would
           change?  (ans:  in round 6, the printing would go in reverse order)
        *  ask for the value of variables that don't exist yet.  (in Python,
           these would raise ``NameError``.  In other languages students know,
           some other behaviour might happen! 

#.  Questions for Further Reflection

    #  ask ``div2`` for a judgement on ``"a"``.  Since ``div2`` should only accept
       integers, this is a good time to explain ``Exception`` and ``raise``, or
       their equivalents. 

#.  Show off the actual Python code.  Connect it to their 'roles'.  



Example of Play (turn 4)
-----------------------------


After designing their machine, Adele, Ben, Jes, and Siri are chosen to play
four of the parts in the computation.  They simulate the section represented 
in the sequence diagram above.  

* Adele plays ``main`` (the controller). 
* Ben plays ``loop``, an integer variable.
* Jes plays ``print``, a process that takes arguments and prints them to the board
* Siri plays ``div2``, a process that takes ``int`` and returns ``boolean``.  
* Micah plays ``choice "is divisible by 2"``, a branch point.


After a few rounds of computation, ``loop`` has the value 4.

Adele:  "Micah, I am at your branch point, where do I go next?"

Micah:  "I need to do some work to find out!  ``loop``, what is your value?"
    
Ben:  (shows the 4 on his small white board)

Micah:  [Writes down ``4`` on an index card]. "What does ``div2`` say about this?"
[hands Siri the card].

Siri:  That's ``True`` because it is divisible by 2 evenly.  [sends back a "True" card*].

Micah:  "[to Adele], main controller, you should down my 'yes' path."

Adele:  "Got it.  [to Jes], ``print``, handle these for me."  [gives cards with '4', 'Fizz' to Jes].

Jes:  Got it!  (*writes ``4 Fizz`` on the board*)

[play continues on through the loop.]




Hints for Better Play
------------------------

* don't allow particular players to "hog the spotlight".  All the parts of the program are
  need to make the computation run!
* if the computation is taking too long, cut down the spec to ``n=10``.  
* Since there are 
  infinite variations about to implement FizzBuzz, the "player" list below 
  is merely a suggestion.  If you have *lots* of players, allow people
  to change roles partly through, or add more roles (suggest more parts to the program).    


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
* the various 'branch points'


Learning Goals
----------------

* algorithmic thinking
* code as message passing
* variables and their values are different
* the global state
* ``while`` loops
* ``TypeError``


A Possible Solution (Python Code)
---------------------------------

..  sourcecode:: python

    def div2(ii):
        return (ii % 2) == 0
    
    def div3(ii):
        return (ii % 3) == 0
    
    def main():
        ii = 1
        while ii <= 15:
            if div2(ii):
                print ii, "FIZZ"
            
            if div3(ii):
                print ii, "BUZZ"
        ii = ii + 1
    
    main()  # start off the whole thing.



Gory Gross Bits
---------------------------

In Flow diagrams, the decision and the machinery that makes the decision are conflated.  THAT IS OKAY.
We use a 'Sequence diagram' to expand part of it, and show off the handoffs / stack.

This exercise gets deep into theory of computation, pass-by-<something> semantics,
and the like if you look at it too hard.  Dodge all such questions.







..
    [old text I liked, and am not quite ready to abandon, so it's in comment]

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


    #.  PLAY OUT the computation.  Assign player for each part.    

        * Each VARIABLE should get a small dry-erase white board, and a marker.  At the top
          in one corner, the should write the name of their variable LABEL(s).
          As their value changes, they should update their value accordingly.

        * Each FUNCTION should get index cards to "return"
          values.  Those returning booleans should get (or make) stacks of "True" and 
          "False" cards.  

        * take the first few rounds slowly.  It might be worthwhile to have an actual 
          "runner" to *physically carry* inputs and returns around.



