#!/bin/bash
export DEST="./.exvim.change.image.format"
export TOOLS="/Users/tu/.vim/tools/"
export TMP="${DEST}/_ID"
export TARGET="${DEST}/ID"
sh ${TOOLS}/shell/bash/update-idutils.sh
