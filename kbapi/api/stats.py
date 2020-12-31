# -*- encoding: utf-8 -*-
# kb-api v0.1.0
# A REST API for kb - the minimalist knowledge base organizer
# Copyright © 2020, alshapton.
# See /LICENSE for licensing information.

"""
kb-api stats api module

:Copyright: © 2020, alshapton.
:License: GPLv3 (see /LICENSE).
"""

from typing import Dict

from flask import make_response

from kb.actions.kbinfo import kb_stats
from kbapi.api.constants import MIME_TYPE


def stats(config: Dict[str, str]):
    """
    Get statistics about the database

    Argument:
    config:         - a configuration dictionary containing at least
                      the following keys:
                      PATH_KB           - the main path of KB
    """

    stats_content = kb_stats(config)
    resp = make_response(stats_content, 200)
    resp.mimetype = MIME_TYPE['json']
    return(resp)
