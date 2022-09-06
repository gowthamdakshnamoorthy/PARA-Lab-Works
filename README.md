# Pipeline Inspection Robot
It is a project done for [U.S. DOT Pipeline and Hazardous Materials Safety Administration](https://www.phmsa.dot.gov/). I would like to thank [Professor Yongming Liu](https://search.asu.edu/profile/436365), founder of [PARA Lab, ASU](https://paralab.engineering.asu.edu/people/) for giving me an opportunity to work in this project.

The primary objective of this project is to determine the uncertainty of the gas pipelines with respect to the defects of the inner wall of the pipeline using a computer vision enabled depth camera. But it was imperative that the camera should be able to scan for the entire length of the pipeline. So there was a requirement of a robot to augment the following process.

The robot should be capable of doing the following activities: -
* It should be capable of moving inside the pipe.
* It should house the depth camera and allow it to rotate 360<sup>0</sup> in different speeds and both direction.
* It should be capable of wireless control when the robot is inside the pipeline.
* It should house its own power supply.
* It should be able to adjust the altitude of the camera with respect to the diameter of the pipe.

This is an image of the robot frame designed by [Mr.Rohit Kalyan](https://www.linkedin.com/in/rohith-kalyan-kavadapu/)

<img src='imgs/Screenshot 2022-08-27 220944.png'  width=500>

The robot consists of following elements: -


The frame is extracted from [Yahboom G1 Tank Robot](https://category.yahboom.net/products/g1tank) as it has enough space to house the circuitry of the robot.

Firstly [Arduino Mega 2560T](https://store-usa.arduino.cc/products/arduino-mega-2560-rev3?selectedStore=us) microcontroller was used to control the elements of the robot

