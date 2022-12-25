import unittest
from pathlib import Path

parent = Path(__file__).parent


class Test_integration(unittest.TestCase):
    support_data = parent / 'support_data/bundle_definition'

    def test_one_file(self):
        script = Path(__file__).parent / 'browser.py'

        import pynanto.common as pn
        import pynanto.server as pns

        # remote = pn.Remote() \
        #     .set_routes(pn.Routes().add_root_index()) \
        #     .add_bundle(pn.Bundle().add_file(script)) \
        #     .set_main(script)

        remote = pn.Setup().add_bundle(pn.Bundle().add_file(script))
        # remote.attach_webserver(pns.webserver.flask())
        pns.webserver.flask().set_remote(remote).instance() \
            .run(host="0.0.0.0", port=5020, debug=False, use_reloader=True)


if __name__ == '__main__':
    unittest.main()
