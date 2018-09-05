#!/usr/bin/env python

import time
import sys
import os
import argparse

# parser = argparse.ArgumentParser(description='Command to copy files')
# parser.add_argument('--source', dest='source', help='Source File', required=True)
# parser.add_argument('--destination', dest='destination', help='Destination File', required=True)
# args = parser.parse_args()
# print args


def main():
    parser = argparse.ArgumentParser(description="Command to copy files")
    parser.add_argument('files', nargs=2, help='Specify the source file name and destination file name separated by comma')
    args = parser.parse_args()

    # Fetch the script start time
    start_time = time.time()

    try:
        # # Ensure that script name, source and destination are passed correctly.
        # if len(sys.argv) != 3:
        #      raise Exception(
        #         'ERROR: Arguments must be specified in correct order - <script to be run> <source> <destination>')

        # Fetch the source and destination passed from cli
        # source = sys.argv[1]
        # destination = sys.argv[2]
        source = args.files[0]
        destination = args.files[1]

        # Check if the user has specified current location as destination
        # If so, fetch the path to current location & file name from source
        #if sys.argv[2] == '.':
        if destination == '.':
            dest_path = os.getcwd()
            file_name = os.path.basename(source)
        else:

            # Case when destination location has been specified
            dest_path = os.path.dirname(destination)
            file_name = os.path.basename(destination)
            if not file_name:
                file_name = os.path.basename(source)

        # Create destination by joining path and filename
        destination = os.path.join(dest_path, file_name)

        # Display exception if destination directory doesn't exist
        if not os.path.exists(dest_path):
            raise Exception('ERROR: Destination doesnt exist!')

        # Display error if source file doesn't exist
        if not os.path.exists(source):
            raise Exception('ERROR: Source File doesnt exist!')

        # Open the source file and copy the contents to destination file
        with open(source) as fs:
            with open(destination, 'w') as fd:
                for line in fs:
                    fd.write(line)
    except Exception as e:
        print(e)
    else:

        # Fetch script end time
        end_time = time.time()
        print('###File Copied in {} seconds###'.format(end_time - start_time))

if __name__ == '__main__':
    main()
