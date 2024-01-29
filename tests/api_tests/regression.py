import sys

from testflows.core import *  # NOQA

append_path(sys.path, "..")

xfails = {}


@TestModule
@Name("API")
@XFails(xfails)
def regression(self):
    Feature(run=load("websocket_tests.websocket_scenarios", test="websocket_scenarios"))


if main():
    regression()
