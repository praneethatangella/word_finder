import os
import sys
import pytest
import platform
script_path = os.path.realpath(__file__)
script_dir = os.path.dirname(script_path)
sys.path.insert(0, os.path.join(script_dir, '../modules/'))
import word_finder

@pytest.fixture(scope="session", autouse=True)
def make_unreadable_resource():
    print('Making file read only')
    os.chmod(os.path.join(script_dir, 'resources', 'unreadable_file.txt'), 0000)


class TestFileCheckers:

    def test_is_file_empty(self):
        'Positive Test Case'
        assert word_finder.is_empty_file(
            os.path.join(script_dir, 'resources', 'empty_file.txt')
        ) == True

    def test_is_not_file_empty(self):
        'Negative Test Case'
        assert word_finder.is_empty_file(
            os.path.join(script_dir, 'resources', 'testcase1.txt')
        ) == False


    def test_is_file_readable(self):
        'Positive Test Case'
        assert word_finder.is_file_readable(
            os.path.join(script_dir, 'resources', 'testcase1.txt')) == True

    @pytest.mark.skipif(platform.system().lower() == 'windows',
                        reason="requires mac/linux env")
    def test_is_file_not_readable(self):
        'Negative Test Case'

        assert word_finder.is_file_readable(
            os.path.join(script_dir, 'resources', 'unreadable_file.txt')) == False

    def test_file_checker_non_existant_file(self):
        'Negative Test Case'
        with pytest.raises(word_finder.FileNotFoundException):
            word_finder.file_checker(
            os.path.join(script_dir, 'resources', 'not_there.txt'))

    @pytest.mark.skipif(platform.system().lower() == 'windows',
                        reason="requires mac/linux env")
    def test_file_checker_unreadable_file(self):
        'Negative Test Case'
        with pytest.raises(word_finder.FileUnReadableException):
            word_finder.file_checker(
            os.path.join(script_dir, 'resources', 'unreadable_file.txt'))

    def test_file_checker_empty_file(self):
        'Negative Test Case'
        with pytest.raises(word_finder.FileEmptyException):
            word_finder.file_checker(
                os.path.join(script_dir, 'resources', 'empty_file.txt'))

    def test_file_checker_transpose_file_1(self):
        'Positive Test Case'
        longest_word, transpose_word = word_finder.word_finder(
             os.path.join(script_dir, 'resources', 'testcase1.txt'))
        assert longest_word == "abcde"
        assert transpose_word == "edcba"

    def test_file_checker_transpose_file_2(self):
        'Positive Test Case'
        longest_word, transpose_word = word_finder.word_finder(
             os.path.join(script_dir, 'resources', 'testcase2.txt'))
        assert longest_word == "137862146214972492713"
        assert transpose_word == "317294279412641268731"

    def test_file_checker_transpose_file_not_present(self):
        'Negative Test Case'
        with pytest.raises(word_finder.FileNotFoundException):
            longest_word, transpose_word = word_finder.word_finder(
                 os.path.join(script_dir, 'resources', 'not_there.txt'))

    def test_file_checker_transpose_file_empty(self):
        'Negative Test Case'
        with pytest.raises(word_finder.FileEmptyException):
            longest_word, transpose_word = word_finder.word_finder(
                 os.path.join(script_dir, 'resources', 'empty_file.txt'))

    @pytest.mark.skipif(platform.system().lower() == 'windows',
                        reason="requires mac/linux env")
    def test_file_checker_transpose_file_unreadable(self):
        'Negative Test Case'
        with pytest.raises(word_finder.FileUnReadableException):
            longest_word, transpose_word = word_finder.word_finder(
                 os.path.join(script_dir, 'resources', 'unreadable_file.txt'))
