#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#
#  WALL TO WALL PROGRAM
#
#  This program moves the robot at a medium speed along
#  a wall until it hits a wall, then proceeds to the
#  next wall and stops. It is a modification of another
#  simpler program that had the robot continuing forever
#
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#  INITIALIZE
#
#  Establish connection and jump to logic loop
#
  rinit                       #initialize robot
  jmp    logic                #go to logic loop

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#  LOGIC
#
#  Control the movement of the robot by getting sensor
#  data and jumping to a suitable procedure should a
#  condition apply
#
logic:
  rsens                       #update sensor data
  jgt    R9,$300,easeRight    #ease away from wall
  jlt    R9,$12,keepWallLeft  #keep near wall on left
  jlt    RA,$25,moveFwd       #move forward when clear
  jmp    logic                #continue getting data

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#  EASE RIGHT
#
#  Keep robot from hitting the wall on the lefthand side
#  or running into a wall in front
#
easeRight:
  jgt    RB,$700,turnRight    #turn when wall in front
  rspeed $4,$1                #straighten next to wall
  jmp    logic                #continue getting data

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#  KEEP WALL LEFT
#
#  Ease robot left to find a wall on the lefthand side
#
keepWallLeft:
  rspeed $3,$4                #ease toward wall
  jmp    logic                #continue getting data

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#  MOVE FORWARD
#
#  Move robot forward when clear
#
moveFwd:
  rspeed $3,$3                #go straight
  jmp    logic                #continue getting data

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#  TURN RIGHT
#
#  Swivel robot right when encountering a barrier
#
turnRight:
  rspeed $2,$-2               #swivel right
  rsens                       #update sensor data
  jlt    RA,$70,logic2        #clear ahead; continue
  jeq    R0,$1,stopLoop       #second wall hit; stop
  jmp    turnRight            #keep turning in place

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#  LOGIC 2
#
#  Control the movement of the robot by getting sensor
#  data and jumping to a suitable procedure should a
#  condition apply; set R0 for wall encountered
#
logic2:
  ld     R0,$1                #encountered first wall
  rsens                       #update sensor data
  jgt    R9,$600,turnRight    #encountered wall ahead
  jlt    R9,$12,keepWallLeft  #drifted too far from wall
  jgt    R9,$300,easeRight    #drifted too close to wall
  jlt    RA,$25,moveFwd       #clear ahead; move forward
  jmp    logic2               #continue getting data

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#  STOP LOOP
#
#  Make sure stop condition is satisfied and jump to
#  exit to end
#
stopLoop:
  rspeed $0,$0                #stop robot
  jgt    R9,$900,exit         #robot at wall; exit
  jmp    logic2               #continue getting data

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#  EXIT
#
#  Loop to cease sending and receiving data
#
exit:
  jmp    exit                 #do forever
