#file = open("D:\\vn\\log1.txt",'w')

file = open("D:\\vn\\log1.txt",'r')
print(file.read())
file = open("D:\\vn\\log1.txt",'r')
print(file.read(5))
file = open("D:\\vn\\log1.txt",'r')
print(file.readline()) #line by line output
print(file.readlines()) #Read lines separately
print(file.readline(5)) #Read the paticular line only
file.flush() #Saving the contents of the file
file.close() #closing the file

file1 = open("D:\\vn\\log2.txt",'w')
print(file1.write('Failure is a part of success'))
file1 = open("D:\\vn\\log2.txt", 'r')
#print(file1.read())
#file1.close()

file1 = open("D:\\vn\\log2.txt", 'a')
file1.write('''
What are your views on it?
Care to share? 
When the moon's shining light is upon us
There comes the wolf among us.''')
file1 = open('D:/vn/log2.txt','r')
print(file1.read())
file1.flush()
file1.close()

