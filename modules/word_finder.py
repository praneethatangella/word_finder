# Word Finder Module File contains
# Exceptions / Functions for performing max word finding and transpose word finding
# PEP8 Clean
# PyLint Clean
import os


class FinderBaseException(Exception):
    exit_code = 50


class FileNotFoundException(FinderBaseException):
    exit_code = 51


class FileUnReadableException(FinderBaseException):
    exit_code = 52


class FileEmptyException(FinderBaseException):
    exit_code = 53


def is_empty_file(file_path: str) -> bool:
    '''
    Checks if file is empty
    :param file_path: Path to File
    :return: True or False
    '''
    return os.stat(file_path).st_size == 0


def is_file_readable(file_path: str) -> bool:
    '''
    Checks if file has read permission
    :param file_path: Path to File
    :return: True or False
    '''
    return os.access(file_path, os.R_OK)


def file_checker(file_path: str) -> bool:
    '''
    Checks if file is readable
    :param file_path: Path to File
    :return: True or False
    '''
    if not os.path.exists(file_path):
        raise FileNotFoundException(
            f'File at location "{file_path}" not found.')
    if not is_file_readable(file_path):
        raise FileUnReadableException(
            f'File at location "{file_path}" not readable.')
    if is_empty_file(file_path):
        raise FileEmptyException(
            'File at location "{file_path}" is empty.'
        )
    return True


def word_finder(file_path: str) -> str:
    '''

    :param file_path: Input File Path
    :return: longest_word, transposed_word
    '''
    longest_word = ''
    file_checker(file_path)
    with open(file_path) as file_obj:
        for line in file_obj:
            words = line.split()
            longest_word = max(words + [longest_word], key=len)
    return longest_word, longest_word[::-1]


if __name__ == "__main__":
    print(
        word_finder(
            '/Users/neetha/Documents/coding/QA_CodingChallenge'
            '/testing/resources/unreadable_file.txt'))
