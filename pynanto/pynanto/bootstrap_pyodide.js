if (typeof loadPyodide === 'undefined') {
    let script = document.createElement('script');
    script.src = 'https://cdn.jsdelivr.net/pyodide/v0.21.3/full/pyodide.js';
    script.onload = async () => (await loadPyodide()).runPythonAsync(`# python replace marker`);
    document.body.append(script)
}