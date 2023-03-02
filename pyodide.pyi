from typing_extensions import TYPE_CHECKING

import pyodide_http

if TYPE_CHECKING:
    print(pyodide_http)

http = pyodide_http
