import unittest
from pathlib import Path
from typing import Optional

from pynanto.common.bundle import bundle_definition, Item, default_item_filter

parent = Path(__file__).parent


class BundleTest(unittest.TestCase):

    def test_one_file(self):
        folder = parent / 'support_data/one_file'
        actual = set(bundle_definition(folder))
        expect = set([Item(folder / 'foo.py', 'foo.py')])
        self.assertEqual(expect, actual)

    def test_zero_file(self):
        folder = parent / 'support_data/zero_file'
        folder.mkdir(exist_ok=True)  # git does not commit empty folders
        actual = set(bundle_definition(folder))
        expect = set([])
        self.assertEqual(expect, actual)

    def test_selective(self):
        folder = parent / 'support_data/relative_to'
        actual = set(bundle_definition(folder / 'yes', relative_to=folder))
        expect = set([Item(folder / 'yes/yes.txt', 'yes/yes.txt')])
        self.assertEqual(expect, actual)

    def test_item_filter(self):
        folder = parent / 'support_data/item_filter'
        reject = folder / 'yes/reject'

        pycache = folder / 'yes/__pycache__'
        pycache.mkdir(exist_ok=True)
        (pycache / 'cache.txt').write_text('some cache')

        def item_filter(item: Item) -> Optional[Item]:
            if item.filepath == reject:
                return None
            return default_item_filter(item)

        actual = set(bundle_definition(folder, item_filter=item_filter))
        expect = set([Item(folder / 'yes/yes.txt', 'yes/yes.txt')])
        self.assertEqual(expect, actual)


if __name__ == '__main__':
    unittest.main()
