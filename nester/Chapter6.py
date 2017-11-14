def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return (time_string)
    (mins,secs) = time_string.split(splitter)
    return (mins + '.' + secs)

def get_coach_data(filename):
    try:
        with open(filename) as fn:
            data = fn.readline()
            temp1 = data.strip().split(',')
            return (AthleteList(temp1.pop(0),temp1.pop(0),temp1))
    except IOError as ioerr:
        print('File function error')

class AthleteList(list):
    def __init__(self, a_name, a_dob = None, a_times = []):
        list.__init__([])
        self.name = a_name
        self.dob = a_dob
        #self.times = a_times
        self.extend(a_times)

    def top3(self):
        return (sorted(set([sanitize(t) for t in self]))[0:3])

james = get_coach_data('hfpy_ch5_data\james.txt')
print(james.name + '\'s fastest times are:' + str(james.top3()))