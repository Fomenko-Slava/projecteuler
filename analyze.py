import time


def check_time(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()

        #time_string = humanize_seconds(round(te - ts, 2))

        dif = round(te - ts, 10)

        print('Function %r, execution time = %s' % (method.__name__, dif))
        print("*******************************************************************")
        return result

    return timed
