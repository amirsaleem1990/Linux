#!/bin/bash
### This program will take input/s from user and return the mean
array=()
if [[ $1 == "" ]]; then
  # Take values from user if values are not passed
  while IFS= read -r -p "Next item (end with an empty line): " line; do
      [[ $line ]] || break  # break if line is empty
      array+=("$line")
  done
else
  # if values passed
  if [[ $(echo $@ | grep -o "," | wc -w) -gt 0 ]] ; then
    # if values delimated by <,>
    IFS=',' read -r -a array <<< "$@"
  else
    # if values delimated by space
    array=("$@")
  fi
fi

SUM=0
for i in ${array[@]}; do
  let "SUM+=$i"
  # SUM=$(echo `expr $SUM + $i`)
done

LEN_OF_ARRAY=$(echo "${#array[@]}")

mean=$(echo "scale=3; $SUM/$LEN_OF_ARRAY" | bc)
echo $mean