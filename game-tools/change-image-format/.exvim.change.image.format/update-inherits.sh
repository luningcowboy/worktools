#!/bin/bash
export DEST="./.exvim.change.image.format"
export TOOLS="/Users/tu/.vim/tools/"
export TMP="${DEST}/_inherits"
export TARGET="${DEST}/inherits"
sh ${TOOLS}/shell/bash/update-inherits.sh
