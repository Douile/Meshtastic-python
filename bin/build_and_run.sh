#!/bin/sh

BINDIR=$(dirname "$0")

python3 -m pip install "$BINDIR/.."
"$BINDIR/run.sh" $@
