#!/bin/bash

#ctags -R package/SharepointBackup
find . -type f -name "*.py" -not -path "./package/build/*" | xargs ctags
