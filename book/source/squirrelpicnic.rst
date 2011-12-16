

Squirrel Picnic
====================

..  image:: _static/img/il_fullxfull.209403027.jpg
    :align: center
    :alt: "From http://img3.etsystatic.com/il_fullxfull.209403027.jpg"


(from http://www.etsy.com/listing/66210307/squirrel-picnic-2)


..  container::
    class:: question

    Is there anything better than a picnic with friends during the summer?


..  container::
    class:: answer

    No!


..  container::
    class:: question

    What are three nuts you like?


..  container::
    class:: answer

    If you were a squirrel, you might have chosen:

    * filbert
    * acorn
    * walnut


..  container::
    class:: question

    Tell Python your three favorite nuts.

..  container::
    class:: answer

    ::
    
        >>> nutsilike = ["filbert","acorn","walnut"]

    This is a new data type, the ``list``.  

..  container::
    class:: question

    #. How long is the list?
    #. What is the first element in the list?
    #. What is the last element of the list?

..  container::
    class:: answer

    #. The list ``nutslike`` has 3 items.
    #. The string ``"filbert"`` 
    #. The string ``"walnut"``


..  container::
    class:: question

    Ask Python:

    #. How long is the list?
    #. What is the first element in the list?
    #. What is the last element of the list?

..  container::
    class:: answer

    .. doctest::
        >>> nutsilike = ["filbert","acorn","walnut"]
        >>> len(nutsilike)
        3
        >>> nutsilike[0]
        'filbert'
        >>> nutsilike[2]
        'walnut'
        >>> nutsilike[-1]
        'walnut'
        >>> nutsilike[len(nutsilike)]
        Traceback (most recent call last):
            ...
        IndexError: list index out of range
    
    In Python, lists are **indexable**, and the index *starts with 0*.
    This might seem strange but there are Good Reasons for it.  

    Enjoy a nut while this sinks in.  





..  container::
    class:: question

    #. make some new lists of strings
    #. make a list of lists
    #.  


..  container::
    class:: answer

    .. doctest::

        >>> ['a','b','c']
        ['a', 'b', 'c']
        >>> [['a','b','c'],'a string',['another','list']]
        [['a', 'b', 'c'], 'a string', ['another', 'list']]


..  container::
    class:: question

    Is ``"walnut"`` one of my favorite nuts?  How about ``"grapenuts"``?

    Now ask Python that question!

..  container::
    class:: answer

    ..  doctest::

        >>> nutsilike = ['filbert','acorn',''walnut']
        >>>
        >>> "walnut" in nutsilike
        True
        >>> "grapenuts" in nutsilike
        False


..  container::
    class:: question

    Squirrel joke: is there *corn* in *acorn*?  


..  container::
    class:: answer

    ..  doctest::

        >>> 'corn' in 'acorn'
        True

..  container::
    class:: question

    Squirrel joke:  Why do walnuts make bad houses?


..  container::
    class:: answer

    *Because they don't have walls!*

    ..  doctest::

        >>> 'walls' in 'walnuts'
        False


..  container::
    class:: question

    Describe what ``in`` does in Python?

..  container::
    class:: answer

    #. ``in`` is an **operator** 
    #. ``x in iterable`` gives a **boolean** (``True`` or ``False``) value


    (loosely, **iterable** means that the object is a *container* for other
    things.  We will refine this definition later)



..  container::
    class:: question

    If this list ``['one','two','three']`` is an iterable of strings,
    what does ``"mayflower"`` contain?  

..  container::
    class:: answer

    #. Pilgrims
    #. ``"mayflower"`` also contains strings, each of which is one letter long.

..  container::
    class:: question

    Are there ``"nuts"`` in ``True``?

..  container::
    class:: answer

    .. doctest::

        >>> "nuts" in True
        Traceback (most recent call last):
            ...
        TypeError: argument of type 'bool' is not iterable

    ``True`` is not a container.


**back to the picnic**

You and your friend Bushytail have decided to plan a picnic.  Bushytail is very 
particular about what nuts they like!  



..  container::
    class:: question

    Python, what is my favorite nut?


..  container::
    class:: answer

    an answer


Tell Python three nuts you like

Final program:

::

    storenuts = ['filbert','pecan','walnut','acorn','pignola']
    bushytail_dislikes = ['filbert','brazil nut']
    nutsilike = ['filbert','acorn',''walnut']
    consensus = []
    for nut in storenuts:
        print "The store has:", nut
        if nut in nutsilike:
            print "... which I like"
            if nut not in bushytail_dislikes:
                print "... and Bushytail doesn't dislike"
                consensus.append(nut)
                print "... so let's get some!"
            else:
                print "... which Bushtail HATES"
                print "... so NONE OF THOSE!"
        else:
            print "... gross for me"
            print "... which makes them RIGHT OUT!"
    
    print "we are getting:", consensus



Lessons Learned
-------------------

* ``['this','is','a','list','of','strings']``
* ``if`` **branches** the program based on **boolean** result of a **clause**
* ``not`` for **negation**
* ``for x in y`` **iterates** over values.
*  ``(a in b)``  with *parentheses* is a **grouped** clause.



