#! /bin/bash
# https://medium.com/@sankad_19852/shell-scripting-exercises-5eb7220c2252
# Exercise_5 - Write a shell script that displays “man”,”bear”,”pig”,”dog”,”cat”,and “sheep” on the screen with each appearing on a separate line. Try to do this in as few lines as possible.

# strings=(man bear pig dog cat sheep)
# for i in "${strings[@]}"; do
# 	echo $i
# done


strings="man bear pig dog cat sheep"
for string in strings; do
	echo $string
done