#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# Created : Sun 26 Aug 2018 07:07:27 PM EDT
# Modified: Sat 31 Aug 2024 04:14:29 PM EDT

import fileinput


def main():
    for line in fileinput.input():
        print("'" + line.rstrip() + "'")


if __name__ == "__main__":
    main()
