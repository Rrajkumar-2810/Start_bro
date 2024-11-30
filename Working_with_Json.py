book = {}
book['tim'] = {
    'name': 'tim',
    'age': '36',
    'id': '45123'
}
book['jake'] = {
    'name': 'jake',
    'age': '45',
    'id': '78459'
}
import json
b =json.dumps(book)
print('Json Format:', b)
print(type(b))
c = json.loads(b)
print("Dictionary Format:", c)
print(type(c))
print(book)
print("Tim:",book['tim'])
print("Tim's age:",book['tim']['age'])

for people in book:
    print(book[people])
    