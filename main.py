#!/usr/bin/env python
import pytest
if __name__ == '__main__':
    command_line = ['-s', '-v', 'testcases', '--alluredir=reports']
    pytest.main(command_line)
