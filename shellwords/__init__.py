#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Parse line as shell words."""

from __future__ import absolute_import, print_function, unicode_literals
import os
import re
from subprocess import PIPE, Popen
import sys

__title__ = 'shellwords'
__version__ = '0.1.0'
__author__ = 'mozillazg'
__license__ = 'MIT'
__copyright__ = 'Copyright (c) 2015 mozillazg'

encoding = sys.stdout.encoding
re_env = re.compile(r'\$({[a-zA-Z0-9_]+}|[a-zA-Z0-9_]+)')


def shell_run(command):
    p = Popen(command, shell=True, stdout=PIPE, stderr=PIPE)
    stdout, stderr = p.communicate()

    stdout = stdout.decode(encoding, 'replace')
    stderr = stderr.decode(encoding, 'replace')
    return stdout, stderr


def replace_env(string):
    def replace(m):
        s = m.group(0)
        s = s[1:]
        if s.startswith('{'):
            s = s[1: -1]
        return os.environ.get(s, '')
    return re_env.sub(replace, string)


class ShellWords(object):

    def __init__(self, parse_env=False, parse_backtick=False):
        self.parse_env = parse_env
        self.parse_backtick = parse_backtick

    def parse(self, line):
        line = line.strip()
        args = []
        buf = ''
        escaped = double_quoted = single_quoted = back_quote = False
        backtick = ''

        for r in line:
            if escaped:
                buf += r
                escaped = False
                continue

            if r == '\\':
                if single_quoted:
                    buf += r
                else:
                    escaped = True
                continue

            if not r.strip():
                if single_quoted or double_quoted or back_quote:
                    buf += r
                    backtick += r
                elif buf != '':
                    if self.parse_env:
                        buf = replace_env(buf)
                    args.append(buf)
                    buf = ''
                continue

            if r == '`':
                if not single_quoted and not double_quoted:
                    if self.parse_backtick:
                        if back_quote:
                            out, err = shell_run(backtick)
                            if err:
                                raise Exception(err)
                            buf = out.strip()
                        backtick = ""
                        back_quote = (not back_quote)
                        continue

                    backtick = ""
                    back_quote = (not back_quote)
            elif r == '"':
                if not single_quoted:
                    double_quoted = (not double_quoted)
                    continue
            elif r == '\'':
                if not double_quoted:
                    single_quoted = (not single_quoted)
                    continue

            buf += r
            if back_quote:
                backtick += r

        if buf != '':
            if self.parse_env:
                buf = replace_env(buf)
            args.append(buf)

        if escaped or single_quoted or double_quoted or back_quote:
            raise Exception("invalid command line string")

        return args
