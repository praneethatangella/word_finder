# QA Software Testing Coding Challenge


## Code Dependencies
MacOS/Linux

Python 3.9.12

pytest 7.1.1

coverage 6.4.4

Tested on Windows. Few tests skipped in Windows.

## Code Organization

### 1. Executables
./bin/run_word_finder.py

1. Get Help ./bin/run_word_finder.py -h
2. Run Word Finder on File ./bin/run_word_finder.py -f <path_to_file>
3. path_to_file can be absolute or relative path

./bin/test_word_finder.sh

1. Runs the pytest unit tests on various functions

### 2. Functional Module
./modules/word_finder.py

1. Contains several methods to perform word computation.

### 3. Testing Resources
./testing/resources

1. Contains various file testcases 
2. Valid File with long word / Empty File / unreadable file

./ testing/test_word_finder.py

1. pytest unit tests which stress test the functions in word_finder.py


### 4. Coverage

>> coverage run -m pytest . --verbose && coverage report -m

Name                          Stmts   Miss  Cover   Missing
-----------------------------------------------------------
modules/word_finder.py           31      1    97%   77
testing/test_word_finder.py      50      0   100%
-----------------------------------------------------------
TOTAL                            81      1    99%

