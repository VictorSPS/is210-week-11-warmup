#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Creating class"""

import time


class Snapshot(object):
    """Object stores the timestamps.
    """
    def __init__(self, created=None):
        """Constructor for Snapshot.
        Attribute:
           created(numeric): output for time
        """
        if created is None:
            created = int(time.time())
        self.created = created
