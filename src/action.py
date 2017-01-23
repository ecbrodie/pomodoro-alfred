#!/usr/bin/python
# encoding: utf-8

import sys
from subprocess import call

from workflow import Workflow, notify
from args import *

def main(wf):
    args = wf.args

    actions = {
        START_ARG: start_action,
        STOP_ARG: stop_action,
        BREAK_ARG: break_action
    }
    action = args[0]
    actions[action]()

def start_action():
    notify.notify('Starting a pomodoro')
    run_script('src/applescript/startPomo.scpt')

def stop_action():
    notify.notify('Stopping a pomodoro/break')
    run_script('src/applescript/stopPomo.scpt')

def break_action():
    notify.notify('Starting a break')
    run_script('src/applescript/startBreak.scpt')

def run_script(filename):
    call(['osascript', filename])

if __name__ == '__main__':
    # Create a global `Workflow` object
    wf = Workflow()
    # Call your entry function via `Workflow.run()` to enable its helper
    # functions, like exception catching, ARGV normalization, magic
    # arguments etc.
    sys.exit(wf.run(main))
