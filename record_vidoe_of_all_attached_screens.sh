# >>> xrandr --listmonitors
# Monitors: 3
#  0: +*DP-1 1920/521x1080/293+1920+0  DP-1
#  1: +eDP-1 1920/344x1080/194+1019+1080  eDP-1
#  2: +HDMI-1 1920/476x1080/268+0+0  HDMI-1

# Given the output of your xrandr --listmonitors command, you have three monitors:
# 
#     DP-1: 1920x1080 at position +1920+0
#     eDP-1: 1920x1080 at position +1019+1080
#     HDMI-1: 1920x1080 at position +0+0
# 
# To record all three screens, we need to determine the total resolution and positions. Here’s a breakdown:
# 
#     The width is the sum of the widths of DP-1 and HDMI-1: 1920 + 1920 = 3840 (we won't include eDP-1 in width as it is stacked vertically).
#     The height is the sum of the height of eDP-1: 1080 (for DP-1 and HDMI-1) + 1080 (for eDP-1) = 2160.
# 
# Calculate total resolution:
# 
# Width: 3840
# Height: 2160


ffmpeg -video_size 3840x2160 -framerate 25 -f x11grab -i :0.0+0,0 output.mp4