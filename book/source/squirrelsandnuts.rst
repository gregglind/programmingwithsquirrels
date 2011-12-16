.. programmingwithsquirrels



Squirrels and Nuts
======================

..  container::
    class:: question


    What is a squirrel?
    
    (click **answer** to the right for the answer)

..  container::
    class:: answer

    `Squirrels <http://en.wikipedia.org/wiki/Squirrel/>`_
    are rodents native to North America and other places.
    
    These are some squirrels:

    ..  image:: _static/img/Sciuridae.jpg
        :width: 200px
        :align: center
        :height: 200px
        :alt: Some squirrels, via Wikipedia. 


..  container::
    class:: question

    Is  ``"squirrel"`` a squirrel?


..  container::
    class:: answer

    >>> "squirrel"
    'squirrel'

    No.  ``"squirrel"`` is a ``string`` containing the letters ``"s"``, ``"q"``,
    ``"u"``, etc.


..  container::
    class:: question

    Is ``"abcde fgh ijklm"`` a squirrel?


..  container::
    class:: answer

    No, it is also a string.  


..  container::
    class:: question

    Does Python know what a ``"squirrel"`` is?

..  container::
    class:: answer

    No. ``"squirrel"`` is just a string, which Python treats like any
    other string.  

    Python can make strings on demand, but doesn't know what they mean.
    
    *Do you know what it means to be a squirrel?*

..  container::
    class:: question

    Is ``squirrel`` a string?

..  container::
    class:: answer

    No.  

    Let's ask Python:
    
    ..  doctest::

        >>> squirrel
        Traceback (most recent call last):
          ...
        NameError: name 'squirrel' is not defined

    What do you think a ``NameError`` implies?


..  container::
    class:: question

    What is the difference between ``squirrel`` and ``"squirrel"``?


..  container::
    class:: answer

    One has quotes around it, and doesn't.  This doesn't seem like it a Big Deal,
    but it is, which we explore next.  


..  container::
    class:: question

    Let's forget about squirrels and think about nuts.

    ::

        >>> print "nuts"
        >>> print "my favorite nut is", "walnut"
        >>> print "but I don't like", "filberts"

    
..  container::
    class:: answer

    ``print`` is a python ``statement`` (special construction) that prints
    things to the screen.

    .. doctest::

        >>> print "nuts"
        nuts
        >>> print "my favorite nut is", "walnut"
        my favorite nut is walnut
        >>> print "but I don't like", "filberts"
        but I don't like filberts


..  container::
    class:: question

    Aside:  what is the ``,`` for?  

    (Hint:  think about what it means in normal written text.)

..  container::
    class:: answer

    The ``,`` implies "multiple" things.  This is will come again later.

    .. doctest:

        >>> print "I", "print", "four", "strings"
        'I print four strings'

    *(We now return to your regularly scheduled nuts.)*


..  container::
    class:: question

    Python, what is my favorite nut?


..  container::
    class:: answer

    ..  doctest::

        >>> print "Tell me my", favorite_nut
        Tell me my
        Traceback (most recent call last):
          ...
        NameError: name 'favorite_nut' is not defined

    Python doesn't know what your favorite nut is.  


..  container::
    class:: question


    Tell Python your ``favorite_nut`` and your ``hated_nut``.

..  container::
    class:: answer

    ..  doctest::

        >>> favorite_nut = "walnut"
        >>> hated_nut = "filberts"

    Note that after each **assignment** there is no response from the  
    Python interpreter.  


..  container::
    class:: question

    Python, what is my favorite nut?


..  container::
    class:: answer

    ..  doctest::
        
        >>> print "My Favorite nut is", favorite_nut
        My Favorite nut is walnut


..  container::
    class:: question

    How is ``favorite_nut`` different than ``"favorite_nut"``?


..  container::
    class:: answer

    ``favorite_nut`` is a **label**;  ``"favorite_nut"`` is a string.  

    By labeling a particular object, you can tell Python that is is *important*
    and to keep track of it, so you can reuse it, modify it.

..  container::
    class:: question

    What is **value** for the label ``favorite_nut``?  

    (Make Python tell you the value of ``favorite_nut``)

..  container::
    class:: answer

    ::

        >>> favorite_nut
        'walnut'


..  container::
    class:: question

    What is a ``squirrel``?


..  container::
    class:: answer

    ``squirrel`` is a label (a **variable**) that doesn't refer to
    anything until you **assign** it.  


..  container::
    class:: question

    Now, go be a good squirrel and eat some nuts!


..  container::
    class:: answer

    ..  image:: _static/img/Hexagon_nuts.jpg
        :width: 240px
        :align: center
        :height: 180px
        :alt: Some nuts, via Wikipedia. 

    **BUT NOT THIS KIND OF NUT**


Lessons Learned
-----------------

* ``"string are written like this"``
* ``mylabel = someobject`` 
* there is a difference between the label, and the object to which it 
  refers
* you can type things at the Python interpreter








JUNK
==========================

..  container::
    class:: question

    Python, what is my favorite nut?



..  container::
    class:: answer

    a sample answer




single and double string?
why is it useful to assign this to a variable?
Do we *need to*   NO!

lists can be mixtures of object types
what si the first item in the list?  -> the list...


squirrels have limited imaginations


docs.python.org/reference/datamodel.html#object.__contains__
(tries ``__contains__``, then looking in the result of ``__iter__``

