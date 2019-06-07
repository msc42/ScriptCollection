#!/usr/bin/env python3

# Copyright (C) 2019 Stefan Constantin
#
# This file is part of msc42's ScriptCollection.
#
# ScriptCollection is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# ScriptCollection is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with ScriptCollection. If not, see <http://www.gnu.org/licenses/>.

import argparse
import codecs


def convert_encoding(encoded_string):
    print(codecs.encode(codecs.decode(encoded_string.encode('utf-8'), 'base64'), 'hex').decode())


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='base64 to hex converter')
    parser.add_argument('input_string', metavar='INPUT_STRING', type=str, help='the input string')
    args = parser.parse_args()

    convert_encoding(args.input_string)
