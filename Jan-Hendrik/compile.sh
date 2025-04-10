#!/bin/sh
pdflatex -output-directory=./output Part_A.tex
zathura ./output/Part_A.pdf
