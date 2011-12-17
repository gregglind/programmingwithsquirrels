.. _fizzbuzz-player:

Player Materials
============================

Problem Specification: FizzBuzz
------------------------------------

For the numbers from 1 to 15 (inclusive),
    if the number is DIVISIBLE BY 2,
        then print the number and the word "FIZZ".
    if the number is DIVISIBLE BY 3,
        then print the number and the word "BUZZ".


Parts of a Flowchart
----------------------------

* Diamonds are **choices**.
* Cylinders are **data storage** or **variables**.
* Boxes are **processes**, including all output.
* Circles are **termination** steps (start/stop).

Together, let's draw out the steps.

Playing Your Part
----------------------

    #.  Take your props and read what you can do:

    	``variables``
			* say their value, upon request
			* set/change their value, by order of the controller
		``processes`` (functions)
			* get inputs (which are values)
			* returns outputs
		``choices``
			* get asked by controllers "where next"
			* answers with a branch:  e.g., "follow branch 'yes'"
			* to get that answer, can do **processing**, including looking up variables,
			  calling functions, etc.
		``controller``
			* set, read, modify variables
			* ask branch points "where do I go next" and receive answers
			* call functions and statements
			* runs from top to bottom
			* programs begin and end with the controller
			
        * ``variables``:  little whiteboard and marker
        * ``print process``:  big whiteboard and marker
        * ``processes``:  cards to give return values
        * ``choices``: cards to issue message requests (with variables)
        * ``controller``: cards to issue message requests (with variables)

    #.  Control starts with the controller, and passes around as described by the flowchart we created.

Example of Play (turn 4)
-----------------------------

After designing their machine, Adele, Ben, Jes, Siri and Micah are chosen to play
parts in the computation.  They simulate the section represented
in the sequence diagram above.

* Adele plays ``main`` (the controller).
* Ben plays ``turn``, an integer variable.
* Jes plays ``print``, a process that takes arguments and prints them to the board
* Siri plays ``div2``, a process that takes ``int`` and returns ``boolean``.
* Micah plays ``choice "is divisible by 2"``, a branch point.


After a few rounds of computation, ``turn`` has the value 4.

**Adele:**  "Micah, I'm at your branch point. Where do I go next?"

**Micah:**  "I need to do some work to find out!  ``turn``, what is your value?"

**Ben:**  [Shows the 4 on his small whiteboard.]

**Micah:**  [Writes down ``4`` on an index card.] "What does ``div2`` say about this?"
[Hands Siri the card.]

**Siri:**  "That's ``True`` because it is divisible by 2."  [Sends back a ``True`` card.]

**Micah:**  [to Adele] "Main controller, you should follow my ``True`` path."

**Adele:**  "Got it."  [to Jes:] "``print``, handle these for me."  [Gives cards with '4', 'Fizz' to Jes.]

**Jes:**  "Okay!"  [Writes ``4 Fizz`` on the board.]

Play continues on through the loop.