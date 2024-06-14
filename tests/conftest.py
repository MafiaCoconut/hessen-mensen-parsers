import sys
import os

print('----------')
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))


from tests.fixtures.entities_fixtures import *
from tests.fixtures.repositories_fixtures import *
from tests.fixtures.services_fixtures import *
from tests.fixtures.interfaces_fixtures import *