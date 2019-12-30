#!/bin/bash
# https://how-to.fandom.com/wiki/How_to_wipe_a_hard_drive_clean_in_Linux
# Wiping the entire disk
# This will overwrite all partitions, master boot records, and data. Use the sudo command as well (sudo dd...)
    # Filling the disk with all zeros (This may take a while, as it is making every bit of data 0) :
    dd if=/dev/zero of=/dev/sdX bs=1M
# If you are wiping your hard drive for security, you should populate it with random data rather than zeros (This is going to take even longer than the first example.) :
    dd if=/dev/urandom of=/dev/sdX bs=1M

