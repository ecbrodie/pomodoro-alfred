#!/usr/bin/python
# encoding: utf-8

import sys

from workflow import Workflow


def main(wf):
    # Get args from Workflow, already in normalized Unicode
    args = wf.args

    wf.add_item(u'pomo-start', u'Start a pomodoro')
    wf.add_item(u'pomo-stop', u'Stop a pomodoro')
    wf.add_item(u'pomo-break', u'Start a break')

    # Send output to Alfred. You can only call this once.
    # Well, you *can* call it multiple times, but Alfred won't be listening
    # any more...
    wf.send_feedback()


if __name__ == '__main__':
    # Create a global `Workflow` object
    wf = Workflow()
    # Call your entry function via `Workflow.run()` to enable its helper
    # functions, like exception catching, ARGV normalization, magic
    # arguments etc.
    sys.exit(wf.run(main))
