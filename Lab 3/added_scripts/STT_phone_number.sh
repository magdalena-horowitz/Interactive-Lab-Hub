# from https://elinux.org/RPi_Text_to_Speech_(Speech_Synthesis)



#Added Script 2 For Part 1: Magdalena Horowitz Lab 3
# SST - input your phone number
#uses the new file: input_STT.py to parse your phone number and save it and print it

espeak -ven+f2 -k5 -s150 --stdout  "Tell me your phone number" | aplay
 
arecord -D hw:2,0 -f cd -c1 -r 48000 -d 5 -t wav recorded_mono.wav
python3 input_STT.py recorded_mono.wav