***

**Status**
Documentation ( Main Tasks )
- [ ] [[ Perception ]](https://github.com/Mnpr/Autonomous-Transportation/tree/master/perception)
- [ ] [[ Sensor Fusion ]](https://github.com/Mnpr/Autonomous-Transportation/tree/master/sensor_fusion)
- [ ] [[ Motion Planning ]](https://github.com/Mnpr/Autonomous-Transportation/tree/master/motion_planning)
- [ ] Vehicle Control
- [ ] [[ Hardware and Software Info ]](https://github.com/Mnpr/Autonomous-Transportation/tree/master/hard_soft_ware)

Implementation

- [x] [Implement simple object deteciton [ Yolov4 + darknet_backend ]](https://github.com/Mnpr/Autonomous-Transportation/tree/master/implementation/perception/object_detection)
- [ ] Kalman and Extended Kalman Filters for sensor fusion
- [ ] A case-study of Operational Design Domain [ operating condition and environment ]

***

# Autonomous Transportation

Autonomous Transportation can be seen as composition of following domains.

- Perception of the Environment
- Motion Planning [ A -2-> B ]
- Vehicle Control
- Operational Design Domain( ODD ) 

## Tasks for Autonomous Driving

- Lateral Control [ <- steering -> ]
- Longitudinal Control [ braking, acceleration ]
- Object and Event Detection and Response( OEDR ) [ Detection & Reaction ]
  - Automatic emergency response
  - Driver Supervision ?
- Motion Planning [ Long | Short term ]
- Miscellaneous [ Indicators and Signals ]

## Levels of Autonomy [1.]

0. `Level 0` No Automation

1. `Level 1` Driving Assistance [ Either Lateral or Logitudinal Control ]
   
   - e.g. Adaptive Cruise Control [ speed control with supervised steering ]
   - e.g. Lane Keeping Assistance( Cars. ) [ lateral centering with lane detection ]

2. `Level 2` Partial Driving Automation  [ Both Lateral & Longitudinal Control ]
   
   - e.g. GM Super Cruise, Nissan ProPilot Assist

3. `Level 3` Conditional Driving Automation [ Level2 + some degree of OEDR ] ( unsupervised by driver only in conditional scenarios ) 

4. `Level 4` High Driving Automation [ Level3 + automatic emergency response ] ( limited ODD )

5. `Level 5` High Driving Automation [ Level4 + Unlimited ODD ]

## References

1. [Taxonomy and Definitions for Terms Related to Driving Automation Systems for On-Road Motor Vehicles ](https://www.sae.org/standards/content/j3016_202104/)
2. [KITTI-360 : The KITTI Vision Benchmark Suite ](http://www.cvlibs.net/datasets/kitti/)
3. [[PDF] DARPA Urban Challenge Technical Paper | Semantic Scholar](https://www.semanticscholar.org/paper/DARPA-Urban-Challenge-Technical-Paper-Reinholtz-Alberi/c10acd8c64790f7d040ea6f01d7b26b1d9a442db?p2df)
4. [Lanelets: Efficient map representation for autonomous driving | IEEE Conference Publication | IEEE Xplore](https://ieeexplore.ieee.org/abstract/document/6856487)
5. [MODS - A USV-oriented object detection and obstacle segmentation benchmark](https://arxiv.org/pdf/2105.02359.pdf)