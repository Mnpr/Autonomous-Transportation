# Environment Representation [ Maps ]

**Localization of a vehicle in the environment**

- Localization point cloud or feature map

- Collects continuous sets ( if LiDAR )

- The difference between LiDAR maps is used to calculate the movement of the vehicle.

**Collision avoidance with static objects**

- Occupancy grid map ( likelihood that the grid is occupied by obstacles over time )

- Used to create collision free paths (  for local planning )

- Discretized fine grain grid map ( 2D | 3D )

- Occupancy by a static object ( trees , buildings etc. )

- Curbs and other non drivable surfaces ( dynamic object identified by perception steps are removed )

**Path planning**

- Detailed road map

- Represents information regarding traffic regulations , lane/ route boundaries

- Creation
  
  - Fully Online ( static objects mapping )
  
  - Fully Offline ( collected and labelled using static objects perception and human labeling  ) [ unable to react on changing environment ]
  
  - Created Offline and updated online with new relavant information
