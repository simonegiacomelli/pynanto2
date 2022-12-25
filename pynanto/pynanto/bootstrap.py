from pathlib import Path


class Bootstrap:
    def __init__(self):
        self.remote_python = 'from js import document\n' + \
                             'document.body.innerHTML = "<h1>bootstrap done. No remote python specified</h1>"'

    def set_python(self, remote_python: str) -> 'Bootstrap':
        self.remote_python = remote_python
        return self

    def get_javascript(self) -> str:
        parent = Path(__file__).parent
        js = parent / 'bootstrap_pyodide.js'
        return js.read_text().replace('# python replace marker', self.remote_python)
