# Little Interactions Everywhere

## Prep
## Overview

The point of this lab is to introduce you to distributed interaction. We have included some Natural Language Processing (NLP) and Generation (NLG) but those are not really the emphasis. Feel free to dig into the examples and play around the code which you can integrate into your projects if wanted. However, we want to emphasize that the grading will focus on your ability to develop interesting uses for messaging across distributed devices. Here are the four sections of the lab activity:

A) [MQTT](#part-a)

B) [Send and Receive on your Pi](#part-b)

C) [Streaming a Sensor](#part-c)

D) [The One True ColorNet](#part-d)

E) [Make It Your Own](#part-)

## Part 1.

### Part A
### MQTT

MQTT is a lightweight messaging portal invented in 1999 for low bandwidth networks. It was later adopted as a defacto standard for a variety of [Internet of Things (IoT)](https://en.wikipedia.org/wiki/Internet_of_things) devices. 

#### The Bits
Once connected, you should be able to see all the messages under the IDD topic. , go to the **Publish** tab and try publish something! From the interface you can send and plot messages as well. Remember, you are limited to subtopics of `IDD`. That is, to publish or subcribe, the topics will start with `IDD/`.

![publish settings](imgs/mqtt_explorer_2.png?raw=true)


### Part B
### Send and Receive on your Pi
[sender.py](./sender.py) and and [reader.py](./reader.py) show you the basics of using the mqtt in python. Let's spend a few minutes running these and seeing how messages are transferred and shown up. Before working on your Pi, keep the connection of `farlab.infosci.cornell.edu/8883` with MQTT Explorer running on your laptop.
**Running Examples on Pi**

**\*\*\*Consider how you might use this messaging system on interactive devices, and draw/write down 5 ideas here.\*\*\***

### Part C
### Streaming a Sensor

**\*\*\*Include a picture of your setup here: what did you see on MQTT Explorer?\*\*\***

**\*\*\*Pick another part in your kit and try to implement the data streaming with it.\*\*\***

### Part D
### The One True ColorNet


**\*\*\*Can you set up the script that can read the color anyone else publish and display it on your screen?\*\*\***


### Part E
### Make it your own

**\*\*\*1. Explain your design\*\*\*** For example, if you made a remote controlled banana piano, explain why anyone would want such a thing.

**\*\*\*2. Diagram the architecture of the system.\*\*\*** Be clear to document where input, output and computation occur, and label all parts and connections. For example, where is the banana, who is the banana player, where does the sound get played, and who is listening to the banana music?

**\*\*\*3. Build a working prototype of the system.\*\*\*** Do think about the user interface: if someone encountered these bananas somewhere in the wild, would they know how to interact with them? Should they know what to expect?

**\*\*\*4. Document the working prototype in use.\*\*\*** It may be helpful to record a Zoom session where you should the input in one location clearly causing response in another location.

<!--**\*\*\*5. BONUS (Wendy didn't approve this so you should probably ignore it)\*\*\*** get the whole class to run your code and make your distributed system BIGGER.-->

