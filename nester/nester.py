import sys
#数据腌制
import pickle

def print_lol(the_list,level=0,indent = False,fh = sys.stdout):
    for each_item in the_list:
        if isinstance(each_item,list):
            print_lol(each_item,level + 1,indent,fh)
        else:
            if indent :
                for tab_stop in range(level):
                    print("\t", end='',file=fh)
            #for stage is print ("\t" * 8,end = '')
            print(each_item,file=fh)

def file_io():
    try:
        with open('man_data.txt','r') as man_file,open('out_data.txt','w') as out_file:
            print_lol(man_file,fh=out_file)
    except IOError as err:
        print("file error:" + str(err))

file_io()
print_lol(["迪斯尼","1997",["主演","tom"]],0,True)
print_lol(["迪斯尼","1997",["主演","tom"]])