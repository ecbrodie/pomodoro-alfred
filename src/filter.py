#!/usr/bin/python
# encoding: utf-8

import sys

from workflow import Workflow


def main(wf):
    # Get args from Workflow, already in normalized Unicode
    args = wf.args

    for item in items():
        wf.add_item(item['title'], item['description'], arg=item['arg'])

    # Send output to Alfred. You can only call this once.
    # Well, you *can* call it multiple times, but Alfred won't be listening
    # any more...
    wf.send_feedback()

def items():
    return [
        dict(title='pomo-start', description='Start a pomodoro', arg='start'),
        dict(title='pomo-stop', description='Stop a pomodoro', arg='stop'),
        dict(title='pomo-break', description='Start a break', arg='break'),
    ]

if __name__ == '__main__':
    # Create a global `Workflow` object
    wf = Workflow()
    # Call your entry function via `Workflow.run()` to enable its helper
    # functions, like exception catching, ARGV normalization, magic
    # arguments etc.
    sys.exit(wf.run(main))
