# pdf book me sy excesises ko screenshot jupyter notebook me dalna tha:
# 1:
alias si='xclip -selection clipboard -t image/png -o >'
# ab har dafa screenshoot lya, or phir number(sequence me) enter kya
read a; si image_$a.png
# ooper wali line sy user input mangy ga, to agar me <4> press karun ga to clipboard par mojud screen shot directory me image_4.png k name sy save ho jay ga.

#================================
# large file ko 1GB ka chunks me split karna tha, phir un ko pehly sy bany 1 folder me daal kar us folder ko move karna tha, phir speaker sy (notification k tor par) kuch awaz chalwani thi taky me bar bar usy hi na check karta rahun.:
split -C 1G --numeric-suffixes lfd_voice_og2.txt voice_og2_
mv voice_og2_* voice_og2/
mv voice_og2/ lfd_voice_og2.txt /media/amir/450GB/
say 'hay'
