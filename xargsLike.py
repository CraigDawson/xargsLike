#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# Created : Sun 26 Aug 2018 07:07:27 PM EDT
# Modified: Fri 31 Aug 2018 01:21:33 PM EDT

import better_exceptions  # noqa


def main():
    import fileinput
    for line in fileinput.input():
        print("'" + line.rstrip() + "'")


if __name__ == '__main__':
    main()
