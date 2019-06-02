#!/usr/bin/env python3

# Copyright (C) 2017 Stefan Constantin
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
import hashlib
import os


def updateHashObjectWithFile(hashObject, file, ignoreHiddenFiles):
    if os.path.isdir(file):
        for fileInDir in sorted(os.listdir(file)):
            if not ignoreHiddenFiles or not fileInDir.startswith('.'):
                updateHashObjectWithFile(hashObject, os.path.join(file, fileInDir), ignoreHiddenFiles)
    else:
        print(file)
        with open(file, 'rb') as openedFile:
            hashObject.update(openedFile.read())


def calculateHash(files, ignoreHiddenFiles, hashAlgorithm):
    if len(files) >= 1:
        hashObject = hashlib.new(hashAlgorithm)

        for file in sorted(files):
            updateHashObjectWithFile(hashObject, file, ignoreHiddenFiles)

        checksum = hashObject.hexdigest()
        print(checksum)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Calculates one hash of multiple given files. '
        'The aggregated hash depends on the order of the files. '
        'The order of the files and the aggregated hash is printed on the standard output.')
    parser.add_argument('files', metavar='FILES', type=str, nargs='+',
                        help='the files to hash (the aggregated hash depends on the order, the files are sorted)')
    parser.add_argument('-i', '--ignoreHiddenFiles', action='store_true', help='ignore hidden files')
    parser.add_argument('-a', '--hashAlgorithm', metavar='HASH_ALGORITHM', type=str, default='sha512',
        help='the algorithm for calculating the hash (default is sha512, available on this system: ' +
        ', '.join(hashlib.algorithms_available)  + ')')
    args = parser.parse_args()

    calculateHash(args.files, args.ignoreHiddenFiles, args.hashAlgorithm)
