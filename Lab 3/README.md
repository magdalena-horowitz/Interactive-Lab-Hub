# Chatterboxes
[![Watch the video](https://user-images.githubusercontent.com/1128669/135009222-111fe522-e6ba-46ad-b6dc-d1633d21129c.png)](https://www.youtube.com/embed/Q8FWzLMobx0?start=19)

In this lab, we want you to design interaction with a speech-enabled device--something that listens and talks to you. This device can do anything *but* control lights (since we already did that in Lab 1).  First, we want you first to storyboard what you imagine the conversational interaction to be like. Then, you will use wizarding techniques to elicit examples of what people might say, ask, or respond.  We then want you to use the examples collected from at least two other people to inform the redesign of the device.

We will focus on **audio** as the main modality for interaction to start; these general techniques can be extended to **video**, **haptics** or other interactive mechanisms in the second part of the Lab.

## Prep for Part 1: Get the Latest Content and Pick up Additional Parts 

### Pick up Additional Parts

As mentioned during the class, we ordered additional mini microphone for Lab 3. Also, a new part that has finally arrived is encoder! Please remember to pick them up from the TA.

### Get the Latest Content

As always, pull updates from the class Interactive-Lab-Hub to both your Pi and your own GitHub repo. As we discussed in the class, there are 2 ways you can do so:

**\[recommended\]**Option 1: On the Pi, `cd` to your `Interactive-Lab-Hub`, pull the updates from upstream (class lab-hub) and push the updates back to your own GitHub repo. You will need the *personal access token* for this.

```
pi@ixe00:~$ cd Interactive-Lab-Hub
pi@ixe00:~/Interactive-Lab-Hub $ git pull upstream Fall2021
pi@ixe00:~/Interactive-Lab-Hub $ git add .
pi@ixe00:~/Interactive-Lab-Hub $ git commit -m "get lab3 updates"
pi@ixe00:~/Interactive-Lab-Hub $ git push
```

Option 2: On your your own GitHub repo, [create pull request](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2021Fall/readings/Submitting%20Labs.md) to get updates from the class Interactive-Lab-Hub. After you have latest updates online, go on your Pi, `cd` to your `Interactive-Lab-Hub` and use `git pull` to get updates from your own GitHub repo.

## Part 1.
### Text to Speech 

In this part of lab, we are going to start peeking into the world of audio on your Pi! 

We will be using a USB microphone, and the speaker on your webcamera. (Originally we intended to use the microphone on the web camera, but it does not seem to work on Linux.) In the home directory of your Pi, there is a folder called `text2speech` containing several shell scripts. `cd` to the folder and list out all the files by `ls`:

```
pi@ixe00:~/text2speech $ ls
Download        festival_demo.sh  GoogleTTS_demo.sh  pico2text_demo.sh
espeak_demo.sh  flite_demo.sh     lookdave.wav
```

You can run these shell files by typing `./filename`, for example, typing `./espeak_demo.sh` and see what happens. Take some time to look at each script and see how it works. You can see a script by typing `cat filename`. For instance:

```
pi@ixe00:~/text2speech $ cat festival_demo.sh 
#from: https://elinux.org/RPi_Text_to_Speech_(Speech_Synthesis)#Festival_Text_to_Speech

echo "Just what do you think you're doing, Dave?" | festival --tts
```

Now, you might wonder what exactly is a `.sh` file? Typically, a `.sh` file is a shell script which you can execute in a terminal. The example files we offer here are for you to figure out the ways to play with audio on your Pi!

You can also play audio files directly with `aplay filename`. Try typing `aplay lookdave.wav`.

\*\***Write your own shell file to use your favorite of these TTS engines to have your Pi greet you by name.**\*\*
(This shell file should be saved to your own repo for this lab.)


###### Find added script in: Lab3/added_scripts/greet_by_your_name.sh
![image](https://user-images.githubusercontent.com/27168450/136399715-61117952-1a6c-4e3d-ad1b-22b270e4d5db.png)


Bonus: If this topic is very exciting to you, you can try out this new TTS system we recently learned about: https://github.com/rhasspy/larynx

### Speech to Text

Now examine the `speech2text` folder. We are using a speech recognition engine, [Vosk](https://alphacephei.com/vosk/), which is made by researchers at Carnegie Mellon University. Vosk is amazing because it is an offline speech recognition engine; that is, all the processing for the speech recognition is happening onboard the Raspberry Pi. 

In particular, look at `test_words.py` and make sure you understand how the vocab is defined. Then try `./vosk_demo_mic.sh`

One thing you might need to pay attention to is the audio input setting of Pi. Since you are plugging the USB cable of your webcam to your Pi at the same time to act as speaker, the default input might be set to the webcam microphone, which will not be working for recording.

\*\***Write your own shell file that verbally asks for a numerical based input (such as a phone number, zipcode, number of pets, etc) and records the answer the respondent provides.**\*\*

###### Find added script in: Lab3/added_scripts/STT_phone.number.sh --> uses the new file: input_STT.py 

![image](https://user-images.githubusercontent.com/27168450/136400262-11f02d48-bbd6-4972-b5d0-cc599abd7b29.png)


Bonus Activity:

If you are really excited about Speech to Text, you can try out [Mozilla DeepSpeech](https://github.com/mozilla/DeepSpeech) and [voice2json](http://voice2json.org/install.html)
There is an included [dspeech](./dspeech) demo  on the Pi. If you're interested in trying it out, we suggest you create a seperarate virutal environment for it . Create a new Python virtual environment by typing the following commands.

```
pi@ixe00:~ $ virtualenv dspeechexercise
pi@ixe00:~ $ source dspeechexercise/bin/activate
(dspeechexercise) pi@ixe00:~ $ 
```

### Serving Pages

In Lab 1, we served a webpage with flask. In this lab, you may find it useful to serve a webpage for the controller on a remote device. Here is a simple example of a webserver.

```
pi@ixe00:~/Interactive-Lab-Hub/Lab 3 $ python server.py
 * Serving Flask app "server" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 162-573-883
```
From a remote browser on the same network, check to make sure your webserver is working by going to `http://<YourPiIPAddress>:5000`. You should be able to see "Hello World" on the webpage.

### Storyboard

Storyboard and/or use a Verplank diagram to design a speech-enabled device. (Stuck? Make a device that talks for dogs. If that is too stupid, find an application that is better than that.) 

\*\***Post your storyboard and diagram here.**\*\*

![Note Oct 3, 2021 11_18_47 PM](https://user-images.githubusercontent.com/27168450/135790062-860f1c3c-fe92-42e7-850d-618ef3b2eedb.jpg)

Write out what you imagine the dialogue to be. Use cards, post-its, or whatever method helps you develop alternatives or group responses. 


#### _Dialog_

"Hi I'm Planty, your new plant! Thanks for bringing me home. Just a reminder, that since I'm a succulent, I only need to be watered once every couple of weeks once my soil gets very dry and I love a lot of sunlight!"

...

"Hi Maggie... I'm feeling kind of thirsty. Can you give me some water? Don't overhydrate me though, just enough to dampen my soil, thanks!"


"Great!! No longer thirsty, see you tomorrow Maggie. Going to sleep now..."

...

"Hi Maggie, I'm feeling kind of moody. Can I get some more sunlight so I can boost my mood and be happier? Try moving me closer to the window or another natural light source!"

"That's great! Since yesterday I'm so much happier! Please keep me by this new spot. Talk to you soon! Thanks for taking care of me :) "



\*\***Please describe and document your process.**\*\*

##### Just like children and pets, plants need proper attention to thrive and grow: 

 Talky Plant would come in the form of a digital plant pot that would have light sensors, water sensors, and sound sensors. If the plant was unahappy or under not ideal conditions, it would strike up a conversation with its owner to ensure it gets the proper care it needs. 
 
 Talky Plant could also intake user speech and understand if the user said it just watered the plant or gave it more light to remind it to recheck its sensors and engage with the user.
 
 
### Acting out the dialogue

Find a partner, and *without sharing the script with your partner* try out the dialogue you've designed, where you (as the device designer) act as the device you are designing.  Please record this interaction (for example, using Zoom's record feature).


https://user-images.githubusercontent.com/27168450/135868186-1a5c1274-6714-44d5-867c-eaa8541afb54.mp4


\*\***Describe if the dialogue seemed different than what you imagined when it was acted out, and how.**\*\*
\*\***Describe if the dialogue seemed different than what you imagined, or when acted out, when it was wizarded, and how.**\*\*
Once we acted out the dialog, I realized that the device would actually need more than just a speaker and microphone to listen to input. It would also need various other motion sensors to detect when a user was nearby or if there was movement in the room so it could know when to call out to the user.

Also, in the scripted dialogue I didn't take into account volume settings, and sensor placement. Depending on where the plant pot would be placed in the house, maybe the pot would need adjustable sensors. This way, if the pot is on a high shelf, the sensors could still point downward to locate the user.

Acting this out really helped clarify what else would need to go into the logistics of planning Planty

### Wizarding with the Pi (optional)
In the [demo directory](./demo), you will find an example Wizard of Oz project. In that project, you can see how audio and sensor data is streamed from the Pi to a wizard controller that runs in the browser.  You may use this demo code as a template. By running the `app.py` script, you can see how audio and sensor data (Adafruit MPU-6050 6-DoF Accel and Gyro Sensor) is streamed from the Pi to a wizard controller that runs in the browser `http://<YouPiIPAddress>:5000`. You can control what the system says from the controller as well!



# Lab 3 Part 2

For Part 2, you will redesign the interaction with the speech-enabled device using the data collected, as well as feedback from part 1.

#### Feedback from Part 1:
Mayowa Olatoye
I loved you uploaded a video! Very cool interaction. An idea, would it be possible to show a visual display of the feedback from the plant also? This way you can share the experience of the plant with other participants in the home remotely.

Rohan Reddy
This is a really cool idea! I'm always forgetting about my plants so giving them a voice to talk about their needs is a great idea.
One possible suggestion could be to think about other sensors that you could use.
Maybe you could use light to convey when the plant is thirsty. Or you could use the press of a button to simulate petting the plant?
Cool idea though, and good luck with the rest of the lab!

Jenny Li
Hi Magdalena! I really really love your design! It is just so cool and I wish that I can be as creative! It is really important to check the status of the plant because they are really like babies that cannot talk and therefore may get hurt easily without detailed care. In this case, I found your design having a huge market in the real world if actual built. Besides, I think that your storyboard looks so cute and so clear, and your discussion about improving the design so that it can detect whether the person is around is also very constructive. Overall really great job! -- Jenny


## Prep for Part 2

_1. What are concrete things that could use improvement in the design of your device? For example: wording, timing, anticipation of misunderstandings..._


 The visuals of the design of the device can definitely be improved. While the device is a voice-activated plant that personifies your plant to treat it as a pet, there are currently only incoming signals that it reads: ie. motion, voice, and touch. It currently doesn't output a lot of signals other than sound (voice). 
 
 The second part of the lab now uses buttons to indicate that the plant is ready for care and is ready to say something. This will incorporate light, a display screen with audio --> text display for those who are hard of hearing or deaf, and the option to google the care instructions for your plant, its history, family tree, and any more information. 

_2. What are other modes of interaction _beyond speech_ that you might also use to clarify how to interact?_


For part 2, the plant will be able to be pet by pressing a button, watered for the correct amount of time (timed through 3-5 seconds through a blinking light), and the audio output will also be displayed on the screen. Finally, the option to integrate the device with a google search for your specific plant will be given so you can get more detailed instructions about the history, details, and care instructions for your plant.

_3. Make a new storyboard, diagram and/or script based on these reflections._

**_Script: _**

** Yellow light sensor is on: Plant needs care **

** Maggie sees the yellow light and walks closer toward the plant. As Maggie draws near, the camera and a motion detector collectively sense Maggie's presence and Planty begins to talk **

Planty: "Hi Maggie, Good morning! Thanks for noticing I need a bit of care today."

Maggie: "Hi Planty -- what do you need right now?"

Planty: "I need to be watered for 4 seconds and pet for some care!"

_Maggie waters plant -- *countdown shows up on screen*_

Planty: "Thanks for watering me for 4 seconds! Now pet me!"

_Maggie presses button and Planty speaks again_

Planty: "I need more pets, not enough!"

_Maggie presses button again and this time Planty shows a smiley face on the screen


Planty: "I am happy now, thanks! For more information, scan the QR code to learn more about me!"

_Maggie walks away and Planty can sense this with his motion detector_

Planty: "Bye Maggie! 

## Prototype your system

The system should:
###### use the Raspberry Pi:
- Display Smiley Face on the Screen
- Displays Visual Representation of Spoken text by Planty on the screen for those who are hard of hearing
- Use of Light: Yellow Light when Planty Needs Water, Blue Light when Planty is OK
- Allows button presses to pet/cuddle Planty



###### use one or more sensors

- Microphone
- Camera 
- Motion sensor
- Touch Sensor (for watering and petting actions)


###### require participants to speak to it:


- Maggie can speak to Planty
- Planty can listen, respond, and understand

*Document how the system works*

1. User walks toward Planty
2. Planty's motion sensors pick up movement and Planty emits a glowing light: Blue or yellow depending on its current conditions
3. Planty speaks to the user as it approaches and also displays its spoken text on the screen
4. User takes care of Planty: Waters for a certain amount of time until Planty's hydration sensor kicks in and is full
5. User pets Planty: Planty can tell how long the button is pressed and if it's not enough asks for more pets

*Include videos *

### Video Included Here: 

#### Put Audio all the way up for detailed narration and demo 

https://user-images.githubusercontent.com/27168450/137241312-e3cd97ba-963d-47c2-8ff6-cbf8aa566f54.mp4


## Test the system
Try to get at least two people to interact with your system. (Ideally, you would inform them that there is a wizard _after_ the interaction, but we recognize that can be hard.)

Answer the following:
### What worked well about the system and what didn't?
\*\**your answer here*\*\*

- Bad

-  Overactive Motion Sensor: 
Once people were interacting with the system, they realized that even if they came near the plant, it would talk to them and nudge them for care. 

- Strong speech:
Users realized they needed to speak relatively forcefully for Planty to pick up their speech accurately. 
One solution to this would be placing more microphones around the device. 

- Users really liked the light emanating from Planty but it wasn't as bright during the day


- Good
- Back and Forth conversation was very stimulating, users really liked that they could ask Planty if they were giving it enough care. They also liked that Planty validated them when it was enough or asked for more if Planty needed more care. 
- Incentive and personification
Users liked that Planty has a pet-like personality and was very cute. 


### What worked well about the controller and what didn't?

Petting planty with the touch of a button was not as sensitive as it could be, and voice controlling the interaction with Planty could use more accuracy. Adding additional sensors for surround sound, speaker integration, and a more personable voice would all allow the control of the device to be more customizable and cuter.

### What lessons can you take away from the WoZ interactions for designing a more autonomous version of the system?

When wizarding Planty, I realized that there are so many stimulating senses that are occuring all at once: sound, movement, response, and more! When designing a more autonomous version of the system, one thing to think about would be using AI to predict how the user is going to interact with Planty next. Planty could learn the users behavior and even wake up the user in the morning by talking to them. 


### How could you use your system to create a dataset of interaction? What other sensing modalities would make sense to capture?

Planty could record and collect common patterns, speech patterns, and habits of the user. Not only would the user look after the plant as a pet, but the pet would look after the owner. If any abnormalities or speech patterns change, or if there's silence or lack of activity in the house, Planty could alert the authorities and keep an eye on any safety concerns. 

Planty could also sense opening doors, change in natural vs. artificial light, other pets around the house, babies crying, and learn to stay silent when work-from-home meetings would take place.
