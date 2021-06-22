# Sensor Fusion of LiDAR and Camera

Finding suitable way to transform from one sensor space to another in real-time. ( Pixels and Points correspondence )

### LiDAR [ Light Detection and Ranging ]

- It emits laser rays  and maps the environment based on points that are reflected back from the sorrounding.
- LiDARs provide a $360^{\circ}$ horizontal Field of View ( FOV ) and limited Vertical FOV.
- They give very accurate depth values in comparison to the camera but the output is sparse( not as high-resolution as from camera )

### Camera

- It provides high resolution outputs.
- It has limited FOV and provides less accurate depth information.

Fusion them together overcomes their limitations when they are on their own. Fusion can either be done with the data from each sensor or the results( outputs ).

## Data Fusion

Overlapping the camera image and LiDAR point colud so we get depth information for the pixels in the camera. This Fusion requires finding the intersection of the FOV's of  both sensors and assigning remaining points in the point cloud to corresponding pixel in the image. 

## Output Fusion

After performing objection in the camera image and in the LiDAR point cloud separately,   the results are fused to increase the confidence. The results from sensors are processed separately and verified against each other. It helps increase the reliability of the system.

____

**Notes**

- Manual and automatic calibration of sensors.
- Upsampling Depth Image


**Questions**

1. Computing Device and Availability ( Local / Remote )
2. Devices Specifications [ e.g. Resolution, Model No., etc. ]
3. Number of Sensors and their Positioning ? Decided ?

## Interesting Literatures

1. [[ LiDAR-Camera Calibration using 3D-3D Point correspondences ](https://arxiv.org/pdf/1705.09785.pdf)]

2. 
