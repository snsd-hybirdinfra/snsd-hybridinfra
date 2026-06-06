from html import escape


def escape_xml(
    value
):

    return escape(
        str(
            value
        ),
        quote=True
    )


def truncate_text(
    value,
    max_length: int
):

    text = str(
        value
    )

    if len(
        text
    ) <= max_length:

        return text

    if max_length <= 0:

        return ""

    return text[:max_length]


def escape_truncated(
    value,
    max_length: int
):

    return escape_xml(
        truncate_text(
            value,
            max_length
        )
    )



