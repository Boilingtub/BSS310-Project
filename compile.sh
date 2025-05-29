#!/bin/sh
if [ "$1" = "" ]; then
 lualatex -shell-escape main.tex
elif [ "$1" = "revJ" ]; then 
 lualatex -shell-escape main_revJ.tex
elif [ "$1" = "revD" ]; then 
 lualatex -shell-escape main_revD.tex
fi




