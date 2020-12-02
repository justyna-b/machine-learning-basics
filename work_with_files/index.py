import os

reader = open('Brzezinska.txt', 'r')
try:
    print(reader.readline(10))
    print(reader.readline(10))
    print(reader.readline(10))
    print(reader.read())
        # Read and print the entire file line by line
    line = reader.readline()
    while line != '':  # The EOF char is an empty string
        print(line, end='')
        line = reader.readline()
finally:
    reader.close()

f = open('Brzezinska.txt')
(f.readlines())  # Returns a list object
print(list(f))
f.close()

with open('Brzezinska.txt', 'r') as reader:
    # Read and print the entire file line by line
    line = reader.readline()
    while line != '':  # The EOF char is an empty string
        print(line, end='')
        line = reader.readline()

with open('Brzezinska.txt', 'r') as reader:
    for line in reader.readlines():
        print(line, end='')

with open('Brzezinska.txt', 'r') as reader:
    # Read and print the entire file line by line
    for line in reader:
        print(line, end='')

with open('Brzezinska.txt', 'r') as reader:
    dog_breeds = reader.readlines()

with open('Brzezinska_reversed.txt', 'w') as writer:
    for breed in reversed(dog_breeds):
        writer.write(breed)

with open('Brzezinska.txt', 'rb') as reader:
    print(reader.readline())

with open('Brzezinska.png', 'rb') as byte_reader:
    print(byte_reader.read(1))
    print(byte_reader.read(3))
    print(byte_reader.read(2))
    print(byte_reader.read(1))
    print(byte_reader.read(1))


class my_file_reader():
    def __init__(self, file_path):
        self.__path = file_path
        self.__file_object = None

    def __enter__(self):
        self.__file_object = open(self.__path)
        return self

    def __exit__(self, type, val, tb):
        self.__file_object.close()


with my_file_reader('Brzezinska.txt') as reader:
    # Perform custom class operations
    pass


class PngReader():
    _expected_magic = b'\x89PNG\r\n\x1a\n'

    def __init__(self, file_path):
        if not file_path.endswith('.png'):
            raise NameError("File must be a '.png' extension")
        self.__path = file_path
        self.__file_object = None

    def __enter__(self):
        self.__file_object = open(self.__path, 'rb')

        magic = self.__file_object.read(8)
        if magic != self._expected_magic:
            raise TypeError("The File is not a properly formatted .png file!")

        return self

    def __exit__(self, type, val, tb):
        self.__file_object.close()

    def __iter__(self):
        return self

    def __next__(self):
        initial_data = self.__file_object.read(4)
        if self.__file_object is None or initial_data == b'':
            raise StopIteration
        else:
            chunk_len = int.from_bytes(initial_data, byteorder='big')
            chunk_type = self.__file_object.read(4)
            chunk_data = self.__file_object.read(chunk_len)
            chunk_crc = self.__file_object.read(4)
            return chunk_len, chunk_type, chunk_data, chunk_crc



with PngReader('Brzezinska.png') as reader:
  for l, t, d, c in reader:
    print(f"{l:05}, {t}, {c}")
