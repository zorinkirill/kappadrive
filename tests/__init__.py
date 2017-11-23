import unittest
from .core import suite_core

__all__ = ["suite_all"]


def suite_all():
    loader: unittest.TestLoader = unittest.TestLoader()

    suite: unittest.TestSuite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromModule(suite_core()))

    return suite
