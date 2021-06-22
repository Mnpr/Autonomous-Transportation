# Sensors and Computing Hardware

- Sensors for perception

- Self-driving computing hardware

- Design of hardware configuration

- Software architecture, decomposition 

- Environment representation for self-driving

# Sensors

Device that measures or detects a property of the environment, or changes to a property

**Categories**

*exteroceptive* : extero = sorrounding

- Camera

- LiDAR

- RADAR

- SONAR [ Ultrasonics ]

*proprioceptive* : proprio = internal

- GNSS / IMU

## Camera

Properties : [ Resolution, Field of View, Dynamic Range, etc. ]

- Single Camera

- STERO Camera 
  
  - Combination of cameras with overlaping FOV
  
  - Enables depth estimation

## LiDAR [ Light Detection and Ranging ]

Spreading light beams in the environment and measuring the reflected return. By measuring Time of Flight and amount of light, both range and intensity of sorrounding objects is detected.

Properties :  [ Number of beams( 8, 16, 32 ,.. ), Points per second, Rotation rate, Field of View, etc.  ]

- Detailed 3D scene geometry from LiDAR point cloud

- Spinning Stacked light sources for 3D point cloud map

- Not affected by light conditions as Cameras.

- Solid-State LiDARs

## RADAR [ Radio Detection and Ranging ]

Properties : [ detection range, FOV, positon and speed accuracy ]

- either `WideFOV, short range` or `NarrowFOV, long range`

- Robust object detection and relative speed estimation

- Lesson 4 Environment Representation | CourseraEffective in adverse weather conditions.

## SONAR [ Sound Navigation and Ranging ]

Properties : [ Range, FOV, Cost ]

- Short-range all-weather distance measurement

- Ideal for low cost parking solutions

- Unaffected by lighting, precipitation

## GNSS/ IMU

These are combined to estimate the 3D orientation of the vehicle

Global Navigation Satellite Systems ( GPS, Galileo, etc. )

- Used to measure ego vehicle position, velocity ( RTK, PPP, DGPS )

Inertial Measurement Units

- Used to measure angular rotation rate, acceleration, etc.
