from random import uniform, randint, choice

def sign(number):
    if number == 0:
        return 0
    return (abs((number))/number)

def prod(x1, x2, w0, w1, w2):
    return (w0 + w1*x1 + w2*x2)

def adapt(w0, w1, w2, mnu, desired, x1, x2):
    error = mnu * (desired - sign(prod(x1, x2, w0, w1, w2)))
    return (w0 + error, w1 + error*x1, w2 + error*x2)


def neural(w0, w1, w2, class1x1, class1x2, class1y1, class1y2, 
class2x1, class2x2, class2y1, class2y2, mnu, it):
        if it == 0:
            return (w0, w1, w2)
        else:
            x = 0
            y = 0
            desired = int(choice([-1, 1]))
            if desired == -1:
                x = uniform(class1x1, class1x2)
                y = uniform(class1y1, class1y2)
            else:
                x = uniform(class2x1, class2x2)
                y = uniform(class2y1, class2y2)
            adap = adapt(w0, w1, w2, mnu, desired, x, y)
            return neural(adap[0], adap[1], adap[2], class1x1, 
        class1x2, class1y1, class1y2, class2x1, class2x2, class2y1, 
        class2y2, mnu, it - 1)

(w0, w1, w2) = neural(0, 0, 0, 1, 2, 1, 2, 3, 4, 0, 1, 0.01, 100)
