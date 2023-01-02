from js import document


async def main():
    # res = await multiply(7, 6)
    res = 42
    document.body.innerHTML = str(res)
