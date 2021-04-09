import os
import tempfile
import csv
class File:
    def __init__(self, path):
        self.path = path
        if not os.path.exists(path):
            with open(path, 'w') as f:
                f.write('')
    def read(self):
        with open(self.path, 'r') as f:
            rr = f.read()
        return rr
    def write(self, text):
        with open(self.path, 'w') as f:
            f.write(text)
    def __str__(self):
        return self.path
    def __add__(self, obj):
        new_file = tempfile.NamedTemporaryFile(mode='w+t')
        new_obj = File(new_file.name + '.txt')
        new_obj.write(self.read() + obj.read())
        return new_obj
    def __iter__(self):
        self._curr = 0
        with open(self.path, "r") as f:
            self.lines = f.readlines()
        self.current = 0
        return self
    def __next__(self):
        if self.current >= len(self.lines):
            raise StopIteration
        result = self.lines[self.current]
        self.current += 1
        return result
