Squirrel joke:

what is a sheep?

a sheep is a machine for turning grass into poop.

sheep joke:

what is a squirrel?

A squirrel is a machine for turning nuts into squirrels


let's make sheep:

def sheep(grass):
    print "munching", grass
    return 'poop'


let's make some poop:

sheep()

(arg error)

we need to feed it something!  

somegrass = "green luscious grass"

>>> sheep("some grass")

greengrass

It's still there!

Fine!  let's be more diligent.


def sheep(grass):
    print "munching", grass
    del grass
    return 'poop'


It's still not gone.

Think about sheep pens.


The function is *closed* around it's variables,a nd a makes are reference copy.

This is heavy stuff :)



