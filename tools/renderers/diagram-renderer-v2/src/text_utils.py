import html


def escape_xml(
    value
):

    return html.escape(
        str(value),
        quote=True
    )
