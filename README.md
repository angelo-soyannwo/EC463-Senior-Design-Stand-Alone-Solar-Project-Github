# Sol: An Alternative Off-grid Solar Configuration

## Quick-Start Info

### Structural Hardware

The hardware of our system consists of a frame with solar panels on either side, and a pair of reflectors in between. These reflectors slide diagonally up and down, and sideways along the rails of the frame, moved a stepper motor on either side and ball screws as the linear actuator. 3D printed components are used for interface between different parts, such as the stepper motor mount, sliding face plates, and ball screw rod attachers. Housing has also been developed for our PCBs, battery, and solar charge controller.

### Electronic Hardware

Most of our electronic pieces fit on a PCB. The light sensors and limit switches fit on the solar panels and rails of the frame respectively. The components on the PCB are: 2 Rpi Pico W's, a motor driver, buttons for Pico reset and manual motor control, 2 current sensors, and a temperature sensor. A Renogy solar charge controller is used externally to charge our battery with the solar panel, as well as power our system along with any other load.

### Control Pico Software

Our control software controls the movement of our reflectors through the stepper motors. The two stepper motors are connected in parallel to just one motor driver, so the code is made simple. Upon startup, the program moves the reflectors to their bottom-most position, where it will hit the bottom limit switch and begins tracking its position through step count. As of now, the position tracking is not an integral part of the system, since the program allows the reflectors to move upwards or downwards until they hit the limit switches; the position can be used for other purposes in the future. After startup and every ten seconds, the reflectors will check the light sensor readings, move a certain number of steps in a direction determined from the previous iteration, and check the light reading again. Based on the difference between the two readings, it will continue to move in the direction with more light or stop moving when the difference no longer passes a certain threshold. All of these parameters can be set in the software, including time between iterations and light difference threshold. Additionally, data from the light sensors are sent to our database on each iteration.

### Monitoring Pico Software

The monitoring software keeps track of charge and discharge current and voltage, and temperature of our system within the housing. It does so using two current/voltage sensor and one temperature sensor. The program first connects to WiFi, then begins the normal operation during which it sends data to our database every few seconds.

### Web Application

The web application uses a MERN stack (MongoDB, Express.js, React, Node.js). The web app takes data from our database on MongoDB, which in turn has data uploaded from our Pico servers. The user interface of the web app allows users to create an account, create arrays of our solar modules, and monitor solar panel output power, solar irradiation, and temperature across time. If any anomaly is detected, the user will receive an email such that they can check up on the system as soon as they can.