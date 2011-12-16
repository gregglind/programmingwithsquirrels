
Interlude: Same Name, Different Squirrel
==========================================


..  container::
    class:: question

    How are you feeling today??

..  container::
    class:: answer

    (It should involve "squirrels" or "nuts")

..  container::
    class:: question

    What is the value of ``squirrel`` after this statement?

    ::
    
        >>> squirrel = 'a'


..  container:: 
    class:: answer

    ..  doctest::

        >>> squirrel = 'a'
        >>> squirrel
        'a'


..  container::
    class:: question

    ::

        squirrel = 'a'
        squirrel = 'b'

    What about now?


..  container:: 
    class:: answer
    
    ..  doctest::

        >>> squirrel = 'a'
        >>> squirrel = 'b'
        >>> squirrel
        'b'

    The label ``squirrel`` is assigned to the string ``'a'``, then *reassigned*
    to the string ``'b'``

    The actions are *sequential*.  After reassignment, the ``'a'`` string
    is gone.  



Lessons Learned
-------------------

* assigning a label to a new value is possible
* sequential reassignment 'loses' the old value.


