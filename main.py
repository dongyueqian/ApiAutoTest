#!/usr/bin/env python
import pytest
if __name__ == '__main__':
    command_line = ['-s', '-v', '${WORKSPACE}/dev/testcases', '--alluredir=${WORKSPACE}/dev/reports']
    pytest.main(command_line)
