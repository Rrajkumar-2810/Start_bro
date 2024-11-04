#Using For Loop
cubes =[]
n = 10
for i in range(1, n+1):
    cubes.append(i**3)
print("Cubes: ",cubes)

#Using List Comprehension
cube = [x**3 for x in range(1, n+1)]
print("Cube: ",cube)
#print(dir(cube))

#List as Arguments
def Updatedlist(a, i, value): #a-list, i-index, value-updated value
    a[i] = value
def main():
    lst = [10,20,30,40,[50,60]]
    print("Original List: ", lst)
    Updatedlist(lst, 2, 75)
    print("Updated List: ", lst)
if __name__ == '__main__':
    main()

square = lambda a: a**2
print("Square:",square(4))

SumofTwoCubes = lambda b,c: b**3 + c**3
#print("SumofTwoCubes:", SumofTwoCubes(int(input()), int(input())))
print("SumofTwoCubes:", SumofTwoCubes(3,5))
