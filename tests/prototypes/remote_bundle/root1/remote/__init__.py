from js import document


async def main():
    document.body.innerHTML = \
        '<input id="tag1" value="Hello world 4!">'

    from wwwpy.remote.widgets.filesystem_tree_widget import FilesystemTreeWidget
    FilesystemTreeWidget().append_to(document.body)
