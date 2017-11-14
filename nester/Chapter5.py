""" headfirst book chapter5 example """

import sys

def resovle_file():
    """ constructor:
    step1:read file
    step2:put the file to the list
    step3:print
    """

    james_list = read_file('hfpy_ch5_data\james.txt')
    print(sorted(james_list))
    julie_list = read_file('hfpy_ch5_data\julie.txt')
    print(sorted(julie_list))
    mikey_list = read_file('hfpy_ch5_data\mikey.txt')
    print(sorted(mikey_list))
    sarah_list = read_file('hfpy_ch5_data\sarah.txt')
    print(sorted(sarah_list))

def read_file(file_name):
    rtn_list = []
    try:
        with open(file_name) as ofile:
            for each_line in ofile:
                for each_item in each_line.strip().split(','):
                    rtn_list.append(sanitize(each_item))
        return rtn_list
    except IOError as io_err:
        print('File function error:' + str(io_err))

""" 使用列表推导功能 """
def read_file_new(file_name):
    try:
        with open(file_name) as ofile:
            for each_line in ofile:
                rtn_list = [sanitize(s) for s in each_line.strip().split(',')]
        return rtn_list
    except IOError as io_err:
        print('New File function error:' + str(io_err))

""" 转换时间字符串 """
def sanitize(time_string):
   if '-' in time_string:
       splitter = '-'
   elif ':' in time_string:
       splitter = ':'
   else:
       return (time_string)

   (mins,secs) = time_string.split(splitter)
   return(mins + '.' + secs)

resovle_file()