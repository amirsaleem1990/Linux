#!/bin/bash
read -p "Enter File size in GB: " file_size
read -p "Enter place to create a <zeros> file: " place
dd if=/dev/zero of=$place bs=512 count=$(expr $file_size \* 1024 \* 1024 \* 1024 / 512)
