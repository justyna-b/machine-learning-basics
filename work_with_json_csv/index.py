import json
import requests
import csv
import pandas

data = {
    'song': {
        'singer': 'Zbignie Wodecki',
        'title': 'Pszcolka Maja'
    }
}

with open("data_file.json", "w") as write_file:
    json.dump(data, write_file)

json_string = json.dumps(data)
json_string_indent = json.dumps(data, indent=1)
# print dictionary
print(type(data))
# print string
print(type(json_string))

# tuple
blackjack_hand = (8, "Q")
encoded_hand = json.dumps(blackjack_hand)
decoded_hand = json.loads(encoded_hand)
print(blackjack_hand == decoded_hand)
# tuple
print(type(blackjack_hand))
# list
print(type(decoded_hand))
print(blackjack_hand == tuple(decoded_hand))

print("///////////////////////////")
with open("data_file.json", "r") as read_file:
    data = json.load(read_file)
    print(type(data))
    print(data)

json_string = """
{
    "singer": {
        "name": "Beata Kozidrak",
        "genre": "pop-rock",
        "songs": [
            {
                "title": "Biala Armia",
                "date": "2008"
            }
        ]
    }
}
"""
data = json.loads(json_string)
print(type(data))

response = requests.get("https://jsonplaceholder.typicode.com/photos")
photos = json.loads(response.text)
print(photos == response.json())
print(photos[:10])


class Cat:
    def __init__(self, note, evaluation=None):
        self.note = note
        self.evaluation = {
            "furriness": 3, "weight": 5, "coat": 2,
            "age": 2, "tail_length": 25
        } if evaluation is None else evaluation


def encode_complex(z):
    if isinstance(z, complex):
        return (z.real, z.imag)
    else:
        type_name = z.__class__.__name__
        print(f"Object of type '{type_name}' is not JSON serializable (msg from function)")
norris = Cat(21)
print(json.dumps(norris, default=encode_complex))

# works, encoded
print(type(json.dumps(9 + 5j, default=encode_complex)))
# does not work
# print(json.dumps(norris, default=encode_complex))
# although it is not good idea to encode complex obj to a tuple


class ComplexEncoder(json.JSONEncoder):
    def default(self, z):
        if isinstance(z, complex):
            return (z.real, z.imag)
        else:
            return super().default(z)


print("with override default func in ComplexEncoder" +
      json.dumps(2 + 5j, cls=ComplexEncoder))

complex_json = json.dumps(4 + 17j, cls=ComplexEncoder)
print(json.loads(complex_json))

years = []
with open('hurricanes.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for col in csv_reader:
        print(
            f'In {col[0]} occures {col[1]} averrage hurricanes in years 2005 - 2015')

with open('hurricanes.txt', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        print(f'\tIn month {row["Month"]} hurricanes,  in years 2005 - 2015')
        line_count += 1
    print(f'Processed {line_count} lines.')


with open('hurricanes.csv', mode='w') as hurricane_file:
    hurricane_write = csv.writer(hurricane_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    hurricane_write.writerow(['test', 'test', 'test'])
    hurricane_write.writerow(['test', 'test', 'test', 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])

df = pandas.read_csv('players.csv')
print(df)
print(df['Name'][0])
print(type(df['Name'][0]))

df_names = pandas.read_csv('players.csv', index_col='Name')
print(df)

