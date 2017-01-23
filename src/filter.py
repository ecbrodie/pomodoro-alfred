#!/usr/bin/python
# encoding: utf-8

import sys

from workflow import Workflow, ICON_WARNING


def main(wf):
    query = None

    args = wf.args
    if len(wf.args):
        query = wf.args[0]

    items = all_items()
    if query:
        items = wf.filter(query, items, lambda item: item['arg'])

    if not items:
        wf.add_item('Unknown pomo command', icon=ICON_WARNING)

    for item in items:
        wf.add_item(item['title'], item['description'], arg=item['arg'])

    # Send output to Alfred. You can only call this once.
    wf.send_feedback()

def all_items():
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
