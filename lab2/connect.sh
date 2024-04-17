#/usr/bin/bash

# Usage: sh connect.sh <level>
# sh connect.sh 2 (connect to 2->3 level)

ssh -p 2220 "bandit$1@bandit.labs.overthewire.org"
