#!/usr/local/bin/python
# by Daniel Rosengren modified by e-satis

import sys, time
stdout = sys.stdout

BAILOUT = 16
MAX_ITERATIONS = 1000

class Iterator(object) :
    def __init__(self):
        print 'Rendering...'
        for y in xrange(-39, 39): 
            stdout.write('\n')
            for x in xrange(-39, 39):
                if self.mandelbrot(x/40.0, y/40.0) :
                    stdout.write(' ')
                else:
                    stdout.write('*')


    def mandelbrot(self, x, y):
        cr = y - 0.5
        ci = x
        zi = 0.0
        zr = 0.0

        for i in xrange(MAX_ITERATIONS) :
            temp = zr * zi
            zr2 = zr * zr
            zi2 = zi * zi
            zr = zr2 - zi2 + cr
            zi = temp + temp + ci

            if zi2 + zr2 > BAILOUT:
                 return i

        return 0

t = time.time()
Iterator() 
print '\nPython Elapsed %.02f' % (time.time() - t)

