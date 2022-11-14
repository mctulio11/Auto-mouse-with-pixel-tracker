# AM v1.3

***What changed from version 1.0 to version 1.3***
1. The application did not report the current position of the mouse pointer, but the position before the new one. The app now
reports the precise position of the mouse and the entire pixel path it takes.
2. Added a new interface for ease of use of the application. There's only one button that says "Launch", you can't go wrong.

It is recommended that you are using the latest version of Python to avoid compatibility issues.
To learn more about versions, go to https://www.python.org/downloads/ and download the latest version.

***Project of an anti-inactivity application that moves the mouse by itself within a specific period of time.***

- By default, the application time is 0.5 seconds, with a duration of 0.5 seconds of animation (time that the mouse will take to move the pointer).
To change the duration time and the animation time, it is necessary to change some parameters within the code:

  
        pag.moveTo(x,y,.5) --> .5 is the animation time. Changes to a valid value of seconds are required.
        time.sleep(.5) --> Time the application waits until the next move. Time in seconds too.
        

The launcher.zip file is the executable version of the two applications in one, to save your pc from create too many windows.
The executable version has been added for better compatibility with all audiences, not everyone has python installed on their PC.


That's it! Good use. The pixel-tracker is to know precisely what area of ​​the screen the pointer is in, but it's just
for technical use, it has no other functionality.

Important note: It is not yet possible to change the time the pointer takes to go from one point to another, but I can work on a solution and launch
ASAP.


***mctulio11.
