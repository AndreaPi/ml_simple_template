
import sys, pytest
from pathlib import Path
p = Path(__file__).parents[0] \ 'src'
sys.path.append(p)


from myfunctions import myfunction

def test_upper():
    assert myfunction('foo').upper() == 'FOOFOO'