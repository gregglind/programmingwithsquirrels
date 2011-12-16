

is this is list of squirrels?

['Bushytail', "brenda", 'Ashti']


is this is list of squirrels?

"Bushytail Brenda, Ashti"



squirrels[1]

squirrels



as we saw before ``mydata[]`` implies *get the thing at location x*


bushytail in sqirrels...






for squirrel in squirrels:
    print squirrel, "is parading!"



Function, dict, closure, object

Here is a Mytree:

Mytree = {"total nuts": 0}

def storenut(tree):
    tree['total nuts'] += 1 

def getnut(tree):
    tree['total nuts'] += 1
    return "a nut"

def nutcount(tree):
    return tree['total nuts']

remember that functions are machines for doing things to data.


let's store a nut, then get a nut:

print storenut(tree)
print tree['total nuts]
print nutcount(Tree)
print getnut(tree)


This is all well and good, but the functions should go along with the Tree itself.

Mytree = {
    "total nuts" = 0,
    def storenut(tree):
        tree['total nuts'] += 1 
    
    def getnut(tree):
        tree['total nuts'] += 1
        return "a nut"
    
    def nutcount(tree):
        return tree['total nuts']


def Mytree():
    totalnuts"=0
    def storenut(tree):
        tree['total nuts'] += 1 
    
    def getnut(tree):
        tree['total nuts'] += 1
        return "a nut"
    
    def nutcount(tree):
        return tree['total nuts']


Note that all of the functions take the 'tree' as their first argument,

Let's *enclose" all that 


x = "mystring"

``someobject.somemethod()`` (syntatic sugar) for 

"x".upper() ->   ``upper("x")`` where ``upper`` is defined on all string objects.

In [4]: str.upper
Out[4]: <method 'upper' of 'str' objects>

In [5]: str.upper("here")
Out[5]: 'HERE'


In [8]: list.index(['a','b','c'],'b')
Out[8]: 1

In [9]: list.index(['a','b','c'],'a')
Out[9]: 0


In [11]: type("m")
Out[11]: <type 'str'>

In [12]: type("m").upper("string")
Out[12]: 'STRING'





We will show how these work when we talk about closures and objects later on.


Packing your own lunch...

def Tree():
    data = {
        nuts = []
    }
    def storenut(nut):
        data['nuts'].append(nut)
    
    def getnut(tree):
        return data['nuts'].pop()
    
    def nutcount(tree):
        return len(data['nuts'])

    return {
        'data': data,
        'store': storenut,
        'get': getnut,
        'size': nutcount'
    }


mytree = Tree()
dir(mytree)
mytree['data']
mytree['storenut']





people are 'variables' with whiteboard, and the class is the global state.

fizzbuzz


def div5(n):
    return (ii %  5 == 0)



ii = 0
while ii < 100:
    if div5(ii):
        print 'buzz'



(error)
bool div5 
bool div3
"while"
controller (flow logic, output/display)
ii: state
printer (at white board).  




rock
fizzbuzz action



rock paper (live)
rock paper (code) 
    * input, output, branching
    * they always throw paper
    * copy to all cases (cut + paste)
live fizzbuzz (state, while loops)
    * functions, state....?? 
    * cards with true, false, error
last together is:  design wordsnake on whiteboard
    * setup, win condition, turns, state = general for games
    * ????? break into groups, and hack.....
Badges


Lots of small whiteboards



class FizzBuzz(object):
    
    def do(self,n=100):
        


outputter = {
    3:  lambda: print('fizz'),
    5:  lambda: print('buzz')
}


for ii in range(100):
    for k in [2, 3,5]:
        if divisible(ii,k):
            print(ii)
            outputter[k]()  # because outputter[k] is callable




Address buzzer

