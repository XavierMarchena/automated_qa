#!/usr/bin/env python
# coding: utf-8

# This project is hosted at: <>
# Copyright 2019 Xavier Marchena [xmarchena.xm at gmail dot com]
# License: GPL <http://www.gnu.org/copyleft/gpl.html>

import time


def send_keys_delay(controller, keys, delay=0.25):
    """
    From a set of keys send each key to a UI element and then delay
    :param controller:
    :param keys:
    :param delay:
    :return:
    """
    for key in keys:
        controller.send_keys(key)
        time.sleep(delay)
