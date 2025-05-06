#!/bin/sh
if [ "$1" = "" ]; then
 lualatex -shell-escape main.tex
elif [ "$1" = "A2" ]; then 
 lualatex -output-directory=./output -shell-escape JH_Part_A_2.tex
elif [ "$1" = "A3" ]; then 
 lualatex -output-directory=./output -shell-escape JH_Part_A_3.tex
fi




