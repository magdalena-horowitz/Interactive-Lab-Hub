# Observant Systems
#### Magdalena Horowitz and Ethan Chang (Group XYZ on Canvas)


### Deliverables for this lab are:
1. Show pictures, videos of the "sense-making" algorithms you tried.
1. Show a video of how you embed one of these algorithms into your observant system.
1. Test, characterize your interactive device. Show faults in the detection and how the system handled it.

## Overview
#### Building upon the paper-airplane metaphor (we're understanding the material of machine learning for design), here are the four sections of the lab activity:
---
## Brainstorming Ideas for Our Version:

Our idea is to make zoom for teachers easier and important lecture materials readily available after the class. This would include, but not be limited to:

_Face Detection_

-    See if a student is paying attention based on face recognition and presence

_Gesture detection_

-   When a student raises his hand, a notification would pop up quietly on the teacher's end of the screen
-   When a student shrugs his shoulders, metrics are taken in during the 5-minute sequence and gathered. Both a notification is sent to the professor such as "10 students shrugged and are confused about this section" and a note is taken down the time sequence and topic currently being discussed so the teacher can make note of it later and post more slides and/or a discussion thread about the confusion later
-   When a student points his finger upward, it means the professor is going to slowly - a metric/alert that captures > 40% of students recording this could warn the teacher to slow down
-   Similarly, when a student points his finger downward, it means the lecture is too fast and the professor should slow down 
-   Keep reading Parts A - D for more details and to see the development of this idea


A) [Play](#part-a)

B) [Fold](#part-b)

C) [Flight test](#part-c)

D) [Reflect](#part-d)

### Part A
### Play with different sense-making algorithms.

#### OpenCV
**\*\*\*Try each of the following four examples in the `openCV-examples`, include screenshots of your use and write about one design for each example that might work based on the individual benefits to each algorithm.\*\*\***


#### 1. contours.py
<img src="https://user-images.githubusercontent.com/27168450/139714372-6763c569-8e16-44ee-b524-973b46219051.png" width="300" height="300">

##### Analysis for OUR project:

Contours would definitely be usef
#### 2. face-detection.py
<img src="https://user-images.githubusercontent.com/27168450/139714605-4881b038-34be-4aac-8d58-2a7c70229114.png" width="300" height="300">

#### 3. optical_flow.py
<img src="https://user-images.githubusercontent.com/27168450/139714984-400da6ee-b6b2-4622-9122-31f8daec0813.png" width="300" height="300">

#### 4. detect.py
<img src="https://user-images.githubusercontent.com/27168450/139715136-dc95631b-826e-4888-9016-da3a9ee1d8a8.png" width="300" height="300">


## Analysis of Sense-Making Algorithms:

###### 1. Contours can be used to detect certain objects in images. A design case using contours could be detecting how many wood blocks (or any object) are in an image. We can see how many contours connect into geometric shapes at any given time, count them, then display them to the user. This can be extended into more useful applications, such as quick counting inventory in warehouses.

###### 2. Face detection would be extremely useful for this design because the algorithm tracks when a person is present or if they've stepped away from their computer to get food, watch TV, or not attend the lecture. We can also use this to detect whether the student is closing their eyes, getting tired, or is distracted. Finally, we could use this for in-class "zoom" exams to see whether students are consulting other students. 

###### 3. Optical flows could work well in analyzing foot traffic in front of stores to see which window displays, signages, or shops are interesting to onlookers. An implementation could be to mount a camera in front of the store, measure and to measure the approximate speed of the people passing through. If there is a large enough to decrease in speed then one can assume that someone stopped to look into the shop; these people would be added as a data point in time series data.

###### 4. Object detection is great because it can tell whether a student is picking up their phone during zoom or any other distracting device. We can use this for minimizing distractions and setting filters for certain objects such as cellphones, food, etc. If a student is eating or texting during class, this can be noted and sent to the professor.

#### MediaPipe

**Try the two main features of this script: 1) pinching for percentage control, and 2) "[Quiet Coyote](https://www.youtube.com/watch?v=qsKlNVpY7zg)" for instant percentage setting. Notice how this example uses hardcoded positions and relates those positions with a desired set of events, in `hand_pose.py` lines 48-53. **

#### Testing it out :
**FUll gesture vs pinching half and pinging all the way
**
<img src="https://user-images.githubusercontent.com/27168450/139718977-2cbd4978-a480-4f64-86a4-259304f77672.png" width="300" height="300">
<img src="https://user-images.githubusercontent.com/27168450/139719031-9e12d553-53c0-48e7-898b-24d0170e9444.png" width="300" height="300">
<img src="https://user-images.githubusercontent.com/27168450/139719057-5f921421-b289-4463-90c1-ffa647e214fc.png" width="300" height="300">


**\*\*\*Consider how you might use this position based approach to create an interaction, and write how you might use it on either face, hand or body pose tracking.\*\*\***

###### A position-based approach would be very useful when incorporating feedback about a zoom lecture and sending this information back to the professor. In simple mode, it could use the same pinching based percentage approach to give the teacher more precise feedback on how confident students are feeling about the lecture content. On a deeper level, it could even analyze face expressions such as furrowing one's brow (the distance between the person's eyebrows decreases), yawning (open mouth) indicates boredness/exhaustion, and relate them back to percentages of understanding. Finally, hand and body poses could be used to silently interact and provide continuous feedback and metrics about the students during the lecture either for immediate or post analysis. 


#### Teachable Machines

**\*\*\*Whether you make your own model or not, include screenshots of your use of Teachable Machines, and write how you might use this to create your own classifier. Include what different affordances this method brings, compared to the OpenCV or MediaPipe options.\*\*\***
![image](https://user-images.githubusercontent.com/27168450/139731886-0596f672-4eb1-4703-a51a-f72fdfd7a4bc.png)

#### Filtering, FFTs, and Time Series data. (optional)

**1. Set up threshold detection** Can you identify when a signal goes above certain fixed values?

**2. Set up averaging** Can you average your signal in N-sample blocks? N-sample running average?

**3. Set up peak detection** Can you identify when your signal reaches a peak and then goes down?

**\*\*\*Include links to your code here, and put the code for these in your repo--they will come in handy later.\*\*\***


### Part B
### Construct a simple interaction.

Pick one of the models you have tried, pick a class of objects, and experiment with prototyping an interaction.
This can be as simple as the boat detector earlier.
Try out different interaction outputs and inputs.

**\*\*\*Describe and detail the interaction, as well as your experimentation here.\*\*\***

To experiment with this interaction, we decided to test out object detection using the class of phones. If a face and a phone are detected in the same frame, this should trigger an alert and take note of the time-code and user. This is the first step toward detecting if the user is engaged during class hours and is paying attention to the material on the screen and staying active during the lecture. 

We will be testing this out using various different objects: Coffee Cup, banana, etc... Ideally, the alert should not be triggered if a user were to pick up a cup to drink some water during class. 
Additionally, thresholds such as picking up a phone for 1 second should not set an alarm, but should be recorded as a single "instance" as the phone may have shown a brief notification on the screen. After several "instances" or an extended period of time (i.e. greater than 3 minutes), the interaction can be recorded as a violation and a notification can be sent to the professor.

![image](https://user-images.githubusercontent.com/27168450/139728222-30d2f593-d3cd-46d1-9563-c0f07bd89da6.png)

<img src="https://user-images.githubusercontent.com/27168450/139729551-fc789fd2-3302-43b8-a921-3affa128354f.png" width="200" height="300"> Versus... <img src="https://user-images.githubusercontent.com/27168450/139729343-6ac23f54-88f0-42fe-804e-e79431a5e274.png" width="200" height="300">



### Part C
### Test the interaction prototype

Now flight test your interactive prototype and **note down your observations**:
For example:
1. When does it what it is supposed to do?
2. When does it fail?
3. When it fails, why does it fail?
4. Based on the behavior you have seen, what other scenarios could cause problems?

**\*\*\*Think about someone using the system. Describe how you think this will work.\*\*\***
1. Are they aware of the uncertainties in the system?

- There are several uncertainties that come into play when using this system. From the first basic interaction -- determining whether a user is paying attention based on whether they have a phone object in their hand or not -- may be misleading. If the model isn't trained correctly, other rectangular objects are mistaken for a phone, the user has pictures of phones on his wall, etc, could trigger a unecessary/invalid alert. Additionally, the user could be aware of these uncertainties and take advantage of them. For example they could turn off their video, find a digital background, or disguise the back of their phone with a case or hide it behind another object. 

2. How bad would they be impacted by a miss classification?

- Without some sort of verification system, a user could falsely be reported as not paying attention in class and get points taken off his grade. At further iterations, when we detect for confusion (knit eyebrows), feedback (too slow/too fast), exhaustion (yawning/sleeping), if there are misclassifications, then the professor will wrongfully adjust his lectures according to the feedback. This would result in a bad class experience for both the professors and the students.

3. How could change your interactive system to address this?

- Intensive training measures can be implemented with different scenes, varying models, and lots of variation.
- ...


4. Are there optimizations you can try to do on your sense-making algorithm.

- aksdjf;
- 

### Part D
### Characterize your own Observant system

Now that you have experimented with one or more of these sense-making systems **characterize their behavior**.
During the lecture, we mentioned questions to help characterize a material:
* What can you use X for?
* What is a good environment for X?
* What is a bad environment for X?
* When will X break?
* When it breaks how will X break?
* What are other properties/behaviors of X?
* How does X feel?

**\*\*\*Include a short video demonstrating the answers to these questions.\*\*\***

### Part 2.

Following exploration and reflection from Part 1, finish building your interactive system, and demonstrate it in use with a video.

**\*\*\*Include a short video demonstrating the finished result.\*\*\***
