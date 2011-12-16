.. _fizzbuzz-player:

Player Materials
============================

Problem Specification
---------------------------

For the numbers from 1 to 15 (inclusive), 
    if the number is EVEN,  
        then print the number and the word "FIZZ".  
    if the number is DIVISIBLE BY 3 (exactly), 
        then print the number and the word "BUZZ".


Parts of a Flowchart
-------------------------

* diamonds are **choices**.
* cylinders are **data storage**.
* boxes are **processing** steps, including all output.
* (small) circles are **termination** steps (start/stop).


Playing Your Part
----------------------

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

