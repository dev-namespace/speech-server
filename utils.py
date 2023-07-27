#!/usr/bin/env python

import os

input_folder = "input_files"

class TempFile():
    def __init__(self, input_file):
        self.input_file = input_file

    def __enter__(self):
        if not os.path.exists(input_folder):
            os.mkdir(input_foler)

        self.path = os.path.join("./input_files", self.input_file.filename)
        self.input_file.save(self.path)
        return self.path

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.remove(self.path)
