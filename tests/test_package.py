from LATS import hotpot
from LATS import programming
from LATS import webshop


def test_package_modules_load():
    assert hotpot is not None
    assert programming is not None
    assert webshop is not None