#!/usr/bin/bash

# while getopts ":a:p:" opt; do
#   case $opt in
#     a) arg_1="$OPTARG"
#     ;;
#     p) p_out="$OPTARG"
#     ;;
#     \?) echo "Invalid option -$OPTARG" >&2
#     exit 1
#     ;;
#   esac

#   case $OPTARG in
#     -*) echo "Option $opt needs a valid argument"
#     exit 1
#     ;;
#   esac
# done

# printf "Argument p_out is %s\n" "$p_out"
# printf "Argument arg_1 is %s\n" "$arg_1"

##############################################

# while [ $# -gt 0 ]; do
#   case "$1" in
#     -p|--p_out)
#       p_out="$2"
#       ;;
#     -a|--arg_1)
#       arg_1="$2"
#       ;;
#     -h|--help)
#       echo -e "
#   Usage:

#   -p, --p_out ............. 1st argument
#   -a, --arg_1 ............. 2nd argument
#   -h, --help  ............. help page
#   "
#   exit
#       ;;
#     *)
#       echo -e "
#     ***************************
#     * Error: Invalid argument.*
#     ***************************
#       "
#       exit 1
#   esac
#   shift
#   shift
# done
# [[ -z $p_out ]] || [[ -z $arg_1 ]]
# if [[ $? -eq 0 ]]; then
#   echo -e "
#   Please provide all perameters
#   Aborting........
#   "
#   exit
# fi
