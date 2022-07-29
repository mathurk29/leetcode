# create your own custom range function

def my_range(start, stop=None, step=1):
    '''
      mimic inbuilt range func
    '''

    if stop == None:
        stop = start
        start = 0

    result = []

    i = start

    while (i < stop):
        yield i
        i += step

    return result
