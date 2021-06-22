# Kalman filter and Extended Kalman Filter

**Purpose**

- Detection and ranging sensors combined to estimate the position, velocity and trajectory of the objects in the environment
- Redundant sensors for reliability and overcoming limitation( weather condition ) of sensors in different ODD

The algorithm used for sensor fusion have to deal with temporal, noisy input and generate probabilistically sound estimate of kinematic state. one of most common algorithm used for position and tracking estimation is `Kalman Filter` and it's variation `Extended Kalman Filter`.

## Kalman filter - ( with LiDAR )

This filter uses a series of state prediction and measurement using sensory information to update the state of tracked object. This filter assumes the location variables are gausian ( i.e. can be completely parameterized by mean and the covariance $X \sim N(\mu, {\sigma}^2)$.

### State-Space Models

State-space models are models that use state variables to describe a system by a set of first-order differential or difference equations, rather than by one or more nth-order differential or difference equations. State variables x(t) can be reconstructed from the measured input-output data, but are not themselves measured during an experiment [@](https://uk.mathworks.com/help/ident/ug/what-are-state-space-models.html)

The linear state of a system at time $t$ can be estimated from state at time $t-1$ given by following equation

$$
x_t = F_{t} x_{t-1} + B_{t}u_{t} + w_t
$$

where
-  $x_t$ : state vector ( position and velocity ) at time $t$
-  $u_t$ : motion vector representing stimulus ( steering angle, throttle )
-  $F_t$ : state transition matrix
-  $B_t$ : control input
-  $w_t$ : noise term for the state vector with zero mean and covariance $Q_t$

## Extended Kalman filter - ( with RaDAR )
