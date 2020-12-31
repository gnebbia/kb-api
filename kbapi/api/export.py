# -*- encoding: utf-8 -*-
# kb-api v0.1.0
# A REST API for kb - the minimalist knowledge base organizer
# Copyright © 2020, alshapton.
# See /LICENSE for licensing information.

"""
kb-api export api module

:Copyright: © 2020, alshapton.
:License: GPLv3 (see /LICENSE).
"""

from typing import Dict
import base64

from flask import make_response

from kb.actions.export import export_kb
from kbapi.api.constants import MIME_TYPE


def export(args: Dict[str, str], config: Dict[str, str]):
    """
    Export the entire kb knowledge base.

    Arguments:
    args:           - a dictionary containing the following fields:
                      file -> a string representing the wished output
                        filename
    config:         - a configuration dictionary containing at least
                      the following keys:
                      PATH_KB           - the main path of KB
    """
    fname = export_kb(args, config=config)

    with open(fname, "rb") as export_file:
        encoded_string = base64.b64encode(export_file.read())
    export_content = '{"Export":"' + str(encoded_string) + '"}'
    resp = make_response((export_content), 200)
    resp.mimetype = MIME_TYPE['utf8']
    return(resp)
