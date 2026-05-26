import sys


def configure_runtime_encoding():

    for stream in [
        sys.stdout,
        sys.stderr
    ]:

        reconfigure = getattr(
            stream,
            "reconfigure",
            None
        )

        if reconfigure:

            reconfigure(
                encoding="utf-8"
            )
