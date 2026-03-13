import sys
import os
sys.path.append(os.path.abspath("../packages"))
from maths import *
from subpackages.mult import *
print(addition(3,4))
print(sub(3,4))
print(mul(2,3))