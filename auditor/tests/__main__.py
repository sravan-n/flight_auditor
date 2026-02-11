"""
The entry point for unit test script

This file imports the tests and runs them all on execution.
"""
# To fix a Codio problem
import sys, os.path
workdir = os.path.abspath(__file__)
workdir = os.path.split(workdir)[0]
sys.path.insert(0,os.path.split(workdir)[0])

from test_all import test
test()
