#Writing structures to a file
#To write a structure such as a list or a dictionary to a file and read it subsequently, we use the Python module pickle.
#dump(): to convert a structure to byte stream and write it to a file
#load(): to read a byte stream from a file and convert it back to the original structure

import pickle
def brain_burst():
    f = open('D:/vn/log3.txt','wb')
    pickle.dump(['brain', 'burst'],f)
    pickle.dump({3:'three', 2:'two', 1:'one'},f)
    f.close()
    f = open('D:/vn/log3.txt','rb')
    value1 = pickle.load(f)
    value2 = pickle.load(f)
    print(value1, value2)
    print('Infinite burst on')
    f.close()
if __name__ == '__main__':
    brain_burst()
