import unittest
from pathlib import Path

parent = Path(__file__).parent


class Test_integration(unittest.TestCase):
    support_data = parent / 'support_data/bundle_definition'

    def test_one_file(self):
        script = Path(__file__).parent / 'browser.py'

        import pynanto as pn
        remote = pn.Remote() \
            .set_bootstrap(pn.Bootstrap().set_index('/')) \
            .add_bundle(pn.Bundle().add_file(script)) \
            .set_main(script)


if __name__ == '__main__':
    unittest.main()
