import os
import sys
import argparse
import traceback

script_path = os.path.realpath(__file__)
script_dir = os.path.dirname(script_path)
sys.path.insert(0, os.path.join(script_dir, '../modules/'))
import word_finder

def parse_args():
    '''
    Argument Parser for run_word_finder.py
    :return: arguments
    '''
    parser = argparse.ArgumentParser(
        description='Finds longest word in a file with transposed word')
    parser.add_argument(
        '-f', '--file_path',
        dest='file_path',
        help='Path to File',
        type=os.path.abspath)
    args = parser.parse_args()
    return args

def create_error_file():
    '''
    Captures the trace into a trace.rpt file
    :return:
    '''
    file_path = os.path.join(os.getcwd(), 'trace.rpt')
    print(f'Please check error in file {file_path}')
    exc_type, exc_value, exc_tb = sys.exc_info()
    with open(file_path, 'w') as fileobj:
        fileobj.write(''.join(
            traceback.format_exception(exc_type, exc_value, exc_tb)))


if __name__ == "__main__":
    args = parse_args()
    try:
        longest_word, transpose_word = word_finder.word_finder(args.file_path)
        print(f'Longest Word: {longest_word}')
        print(f'Transpose Word: {transpose_word}')
    except word_finder.FinderBaseException as e:
        print('\n'.join(e.args))
        create_error_file()