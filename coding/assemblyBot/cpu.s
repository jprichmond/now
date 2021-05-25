#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#
#  SIMULATED CPU DEVICE: 16 32-bit registers, 64K memory
#
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

  .section .data

ip:
  .long  0

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#
#         simulated memory
#
smem:
        .byte  0x00,0x00
        .byte  0x05,0x60
        .long  0
        .byte  0x05,0x70
        .long  0
        .byte  0x1C,0x00
        .word  18
        .byte  0x02,0x67
        .byte  0x01,0x00
        .byte  0x21,0x90
        .word  90
        .long  700
        .byte  0x22,0x90
        .word  58
        .long  12
        .byte  0x22,0xA0
        .word  74
        .long  25
        .byte  0x21,0x90
        .word  90
        .long  500
        .byte  0x1C,0x00
        .word  18
        .byte  0x05,0x60
        .long  2
        .byte  0x05,0x70
        .long  4
        .byte  0x1C,0x00
        .word  18
        .byte  0x05,0x60
        .long  3
        .byte  0x05,0x70
        .long  3
        .byte  0x1C,0x00
        .word  18
        .byte  0x05,0x60
        .long  2
        .byte  0x05,0x70
        .long  -2
        .byte  0x1C,0x00
        .word  18
        .rept  65430
        .byte  0xFF
        .endr


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#
#         simulated registers
#
regs:
  .rept  16
  .long  0
  .endr

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#
#         table of opcodes
#
optbl:
#robot interface
  .long rinit                 #00
  .long rsens                 #01
  .long rspdr                 #02
  .long rspdi                 #03
#load register with value
  .long ldr                   #04
  .long ldi                   #05
  .long ldm                   #06
  .long ldx                   #07
  .long ldn                   #08
#store value from register
  .long stm                   #09
  .long stx                   #0A
  .long stn                   #0B
#bitwise AND values
  .long andr                  #0C
  .long andi                  #0D
  .long andm                  #0E
  .long andx                  #0F
  .long andn                  #10
#bitwise OR values
  .long orr                   #11
  .long ori                   #12
  .long orm                   #13
  .long orx                   #14
  .long orn                   #15
#bitwise XOR values
  .long xorr                  #16
  .long xori                  #17
  .long xorm                  #18
  .long xorx                  #19
  .long xorn                  #1A
#bitwise NOT value
  .long notr                  #1B
#jump to location
  .long jmps                  #1C
#jump if condition
  .long jgtr                  #1D
  .long jltr                  #1E
  .long jeqr                  #1F
  .long jezr                  #20
  .long jgti                  #21
  .long jlti                  #22
  .long jeqi                  #23
#call/return jumps
  .long jalm                  #24
  .long jmpn                  #25
#add values together
  .long andr                  #26
  .long andi                  #27
  .long andm                  #28
  .long andx                  #29
  .long andn                  #2A
#spare room
  .rept 8                     #repeat until shri
  .long skip                  #2B->32
  .endr                       #end repeat
#shift bits right
  .long shri                  #33
#spare room
  .rept 256-((.-optbl)/4)     #repeat to fill optbl
  .long skip                  #34->FF
  .endr                       #end repeat

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#
#         register/sensor variables
#
r0 = regs                     #regs[0]
r1 = regs + 4                 #regs[1]
r2 = regs + 8                 #regs[2]
r3 = regs + 12                #regs[3]
r4 = regs + 16                #regs[4]
r5 = regs + 20                #regs[5]
r6 = regs + 24                #regs[6]
r7 = regs + 28                #regs[7]
s0 = regs + 32                #regs[8]
s1 = regs + 36                #regs[9]
s2 = regs + 40                #regs[10]
s3 = regs + 44                #regs[11]
s4 = regs + 48                #regs[12]
s5 = regs + 52                #regs[13]
s6 = regs + 56                #regs[14]
s7 = regs + 60                #regs[15]

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#
#         command strings and buffer
#
bufstr:                      #buffer for the strings
  .space  80
strmov:                      #string for move values
  .string "D,%d,%d\n"
strsen:                      #string for sensor values
  .string "N\n"

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#
#         CODE
#
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

  .globl _start
  .section .text

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#
#         begin program
#
_start:
  movl  $0, %edi              #start ip at 0

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#
#         fetch, decode, execute
#
#  This is the central processing loop which fetches the
#  opcode the instruction pointer ip is pointing to, de-
#  codes it using the optbl, points ip to the next byte
#  in memory, then calls the operation before looping
#  back again indefinitely.
#
fetch:                        #get the next opcode to run
  andl  $0xffff, %edi         #keep ip in array bounds
  movb  smem(,%edi,1), %al    #move Rf to low byte al
  andl  $0xff, %eax           #zero out the higher bytes
  movl  optbl(,%eax, 4), %eax #get opname from table
  incl  %edi                  #point ip to Rf
  andl  $0xffff, %edi         #keep ip in array bounds
  call  *%eax                 #call operation
  jmp   fetch                 #loop back to get next op


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#
#         OPCODE instructions
#
#  Rf signifies the register field. It is the byte
#  immediately following the opcode that holds the
#  register number with the value the operation is
#  being run on in the high nybble (designated as the
#  register destination Rd) and the register number
#  with the value, index offset, or memory address the
#  operation is run with in the low nybble (designated
#  as the register source Rs). The fetch loop will
#  always set the instruction pointer to this field
#  before calling the operation.
#
#  Opcodes use the following naming conventions:
#    r-  'robot' : Codes beginning with 'r' control
#        interfacing with the robot.
#    -r  'register/register' : Codes ending with 'r'
#        mean operation is run on Rd with Rs (or just
#        Rd for unary operations).
#    -i  'register/immediate' : Codes ending with 'i'
#        mean operation is run on Rd with an immediate
#        value.
#    -m  'register/memory address' : Codes ending with
#        'm' mean operation is run on Rd with a value
#        at a given memory address.
#    -x  'register/memory[index]' : Codes ending with
#        'x' mean operation is run on Rd with a value
#        at a given memory address with an index offset.
#    -n  'register/indirect register' : Codes ending
#        with 'n' mean operation is run on Rd with a
#        value at the memory address in Rs (or just a
#        memory address in Rd).
#    -s  'sans registers' : Codes ending with 's' do not
#        access the register field at all.
#
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#
#         robot instructions
#
#  This set of operations interfaces with the robot,
#  controling its initialization along with receiving
#  data from the sensors and sending velocities to the
#  wheels.
#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#  initialize robot
#
rinit:
  movl  %edi, ip              #save current ip value
  call  open_pipes            #establish connection
  movl  ip, %edi              #restore ip value
  addl  $1, %edi              #point to next opcode
  ret                         #return to fetch

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#  get robot sensor data
#
rsens:
  movl  %edi, ip              #save current ip value
  pushl $strsen               #push cmd format string
  pushl $s0                   #push regs[8] for data
  call  sndRcv_0              #interface with robot
  addl  $8, %esp              #reset stack pointer
  movl  ip, %edi              #restore ip value
  addl  $1, %edi              #point to next opcode
  ret                         #return to fetch

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#  set wheel speeds to Rd and Rs
#
rspdr:
  movb  smem(,%edi,1), %al    #move Rf to low byte al
  movl  %eax, %ebx            #copy eax to ebx
  sarl  $4, %eax              #shift eax to isolate Rd
  andl  $0xf, %eax            #isolate nybble Rd
  andl  $0xf, %ebx            #isolate nybble Rs
  movl  %edi, ip              #save current ip value
  pushl regs(,%ebx,4)         #push Rs[left wheel]
  pushl regs(,%eax,4)         #push Rd[right wheel]
  pushl $strmov               #push move format string
  pushl $bufstr               #push string buffer size
  call  sprintf               #format move values
  pushl $s0                   #values start at regs[8]
  call  sndRcv_0              #interface with robot
  addl  $20, %esp             #reset stack pointer
  movl  ip, %edi              #restore ip value
  addl  $1, %edi              #point to next opcode
  ret                         #return to fetch

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#  set wheel speeds to immediate values
#
rspdi:
  movl  %edi, ip              #save current ip value
  pushl smem+5(,%edi,1)       #push $i left wheel speed
  pushl smem+1(,%edi,1)       #push $i right wheel speed
  pushl $strmov               #push move format string
  pushl $bufstr               #push string buffer size
  call  sprintf               #format move values
  pushl $s0                   #values start at regs[8]
  call  sndRcv_0              #interface with robot
  addl  $20, %esp             #reset stack pointer
  movl  ip, %edi              #restore ip value
  addl  $9, %edi              #point to next opcode
  ret                         #return to fetch

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#
#         load Rd with value
#
#  This set of operations loads the register destination
#  with a value from a given location.
#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#  load Rd with value in Rs
#
ldr:
  movb  smem(,%edi,1), %al    #move Rf to low byte al
  movl  %eax, %ebx            #copy eax to ebx
  sarl  $4, %eax              #shift eax to isolate Rd
  andl  $0xf, %eax            #isolate nybble Rd
  andl  $0xf, %ebx            #isolate nybble Rs
  movl  regs(,%ebx,4), %ebx   #get Rs contents
  movl  %ebx, regs(,%eax,4)   #load contents into Rd
  addl  $1, %edi              #point to next opcode
  ret                         #return to fetch

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#  load Rd with immediate value
#
ldi:
  movb  smem(,%edi,1), %al    #move Rf to low byte al
  sarl  $4, %eax              #shift eax to isolate Rd
  andl  $0xf, %eax            #isolate nybble Rd
  movl  smem+1(,%edi,1), %ebx #get immediate value
  movl  %ebx, regs(,%eax,4)   #load immediate into Rd
  addl  $5, %edi              #point to next opcode
  ret                         #return to fetch

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#  load Rd with value at memory address
#
ldm:
  movb  smem(,%edi,1), %al    #move Rf to low byte al
  sarl  $4, %eax              #shift eax to isolate Rd
  andl  $0xf, %eax            #isolate nybble Rd
  movw  smem+1(,%edi,1), %bx  #move memory& to word bx
  andl  $0xffff, %ebx         #isolate memory&
  movl  smem(,%ebx,1), %ebx   #get memory contents
  movl  %ebx, regs(,%eax,4)   #load contents into Rd
  addl  $3, %edi              #point to next opcode
  ret                         #return to fetch

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#  load Rd with value at memory address offset by Rs
#
ldx:
  movb  smem(,%edi,1), %al    #move Rf to low byte al
  movl  %eax, %ebx            #copy eax to ebx
  sarl  $4, %eax              #shift eax to isolate Rd
  andl  $0xf, %eax            #isolate nybble Rd
  andl  $0xf, %ebx            #isolate nybble Rs
  movl  regs(,%ebx,4), %ebx   #get index value
  movw  smem+1(,%edi,1), %cx  #move memory& to word cx
  addl  %ebx, %ecx            #add index offset to &
  andl  $0xffff, %ecx         #isolate memory&
  movl  smem(,%ecx,1), %ecx   #get memory contents
  movl  %ecx, regs(,%eax,4)   #load contents into Rd
  addl  $3, %edi              #point to next opcode
  ret                         #return to fetch

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#  load Rd with value at memory address in Rs
#
ldn:
  movb  smem(,%edi,1), %al    #move Rf to low byte al
  movl  %eax, %ebx            #copy eax to ebx
  sarl  $4, %eax              #shift eax to isolate Rd
  andl  $0xf, %eax            #isolate nybble Rd
  andl  $0xf, %ebx            #isolate nybble Rs
  movl  regs(,%ebx,4), %ebx   #get indirect Rs value
  andl  $0xffff, %ebx         #isolate memory&
  movl  smem(,%ebx,1), %ebx   #get contents pointed to
  movl  %ebx, regs(,%eax,4)   #load contents into Rd
  addl  $1, %edi              #point to next opcode
  ret                         #return to fetch

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#
#         store Rd to location
#
#  This set of operations stores the value in the
#  register destination to a given memory location.
#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#  store value in Rd to memory address
#
stm:
  movb  smem(,%edi,1), %al    #move Rf to low byte al
  sarl  $4, %eax              #shift eax to isolate Rd
  andl  $0xf, %eax            #isolate nybble Rd
  movw  smem+1(,%edi,1), %bx  #move memory& to word bx
  andl  $0xffff, %ebx         #isolate memory&
  movl  regs(,%eax,4), %eax   #get register contents
  movl  %eax, smem(,%ebx,1)   #store contents in mem
  addl  $3, %edi              #point to next opcode
  ret                         #return to fetch

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#  store value in Rd to memory address offset by Rs
#
stx:
  movb  smem(,%edi,1), %al    #move Rf to low byte al
  movl  %eax, %ebx            #copy eax to ebx
  sarl  $4, %eax              #shift eax to isolate Rd
  andl  $0xf, %eax            #isolate nybble Rd
  andl  $0xf, %ebx            #isolate nybble Rs
  movl  regs(,%ebx,4), %ebx   #get index value
  movw  smem+1(,%edi,1), %cx  #move memory& to word cx
  addl  %ebx, %ecx            #add index offset to &
  andl  $0xffff, %ecx         #isolate memory&
  movl  regs(,%eax,4), %eax   #get register contents
  movl  %eax, smem(,%ecx,1)   #store contents in mem
  addl  $3, %edi              #point to next opcode
  ret                         #return to fetch

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#  store value in Rd to memory address in Rs
#
stn:
  movb  smem(,%edi,1), %al    #move Rf to low byte al
  movl  %eax, %ebx            #copy eax to ebx
  sarl  $4, %eax              #shift eax to isolate Rd
  andl  $0xf, %eax            #isolate nybble Rd
  andl  $0xf, %ebx            #isolate nybble Rs
  movl  regs(,%ebx,4), %ebx   #get indirect Rs value
  andl  $0xffff, %ebx         #isolate memory&
  movl  regs(,%eax,4), %eax   #get register contents
  movl  %eax, smem(,%ebx,1)   #store contents in mem
  addl  $1, %edi              #point to next opcode
  ret                         #return to fetch

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#
#         AND Rd with value
#
#  This set of operations performs a bitwise AND on the
#  value in the register destination with a value from
#  a given location.
#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#  AND Rd with value in Rs
#
andr:
  movb  smem(,%edi,1), %al    #move Rf to low byte al
  movl  %eax, %ebx            #copy eax to ebx
  sarl  $4, %eax              #shift eax to isolate Rd
  andl  $0xf, %eax            #isolate nybble Rd
  andl  $0xf, %ebx            #isolate nybble Rs
  movl  regs(,%ebx,4), %ebx   #get Rs contents
  andl  %ebx, regs(,%eax,4)   #and contents with Rd
  addl  $1, %edi              #point to next opcode
  ret                         #return to fetch

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#  AND Rd with immediate value
#
andi:
  movb  smem(,%edi,1), %al    #move Rf to low byte al
  sarl  $4, %eax              #shift eax to isolate Rd
  andl  $0xf, %eax            #isolate nybble Rd
  movl  smem+1(,%edi,1), %ebx #get immediate value
  andl  %ebx, regs(,%eax,4)   #and immediate with Rd
  addl  $5, %edi              #point to next opcode
  ret                         #return to fetch

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#  AND Rd with value at memory address
#
andm:
  movb  smem(,%edi,1), %al    #move Rf to low byte al
  sarl  $4, %eax              #shift eax to isolate Rd
  andl  $0xf, %eax            #isolate nybble Rd
  movw  smem+1(,%edi,1), %bx  #move memory& to word bx
  andl  $0xffff, %ebx         #isolate memory&
  movl  smem(,%ebx,1), %ebx   #get memory contents
  andl  %ebx, regs(,%eax,4)   #and contents with Rd
  addl  $3, %edi              #point to next opcode
  ret                         #return to fetch

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#  AND Rd with value at memory address offset by Rs
#
andx:
  movb  smem(,%edi,1), %al    #move Rf to low byte al
  movl  %eax, %ebx            #copy eax to ebx
  sarl  $4, %eax              #shift eax to isolate Rd
  andl  $0xf, %eax            #isolate nybble Rd
  andl  $0xf, %ebx            #isolate nybble Rs
  movl  regs(,%ebx,4), %ebx   #get index value
  movw  smem+1(,%edi,1), %cx  #move memory& to word cx
  addl  %ebx, %ecx            #add index offset to &
  andl  $0xffff, %ecx         #isolate memory&
  movl  smem(,%ecx,1), %ecx   #get memory contents
  andl  %ecx, regs(,%eax,4)   #and contents with Rd
  addl  $3, %edi              #point to next opcode
  ret                         #return to fetch

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#  AND Rd with value at memory address in Rs
#
andn:
  movb  smem(,%edi,1), %al    #move Rf to low byte al
  movl  %eax, %ebx            #copy eax to ebx
  sarl  $4, %eax              #shift eax to isolate Rd
  andl  $0xf, %eax            #isolate nybble Rd
  andl  $0xf, %ebx            #isolate nybble Rs
  movl  regs(,%ebx,4), %ebx   #get indirect Rs value
  andl  $0xffff, %ebx         #isolate memory&
  movl  smem(,%ebx,1), %ebx   #get contents pointed to
  andl  %ebx, regs(,%eax,4)   #and contents with Rd
  addl  $1, %edi              #point to next opcode
  ret                         #return to fetch


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#
#         OR Rd with value
#
#  This set of operations performs a bitwise OR on the
#  value in the register destination with a value from
#  a given location.
#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#  OR Rd with value in Rs
#
orr:
  movb  smem(,%edi,1), %al    #move Rf to low byte al
  movl  %eax, %ebx            #copy eax to ebx
  sarl  $4, %eax              #shift eax to isolate Rd
  andl  $0xf, %eax            #isolate nybble Rd
  andl  $0xf, %ebx            #isolate nybble Rs
  movl  regs(,%ebx,4), %ebx   #get Rs contents
  orl   %ebx, regs(,%eax,4)   #or contents with Rd
  addl  $1, %edi              #point to next opcode
  ret                         #return to fetch

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#  OR Rd with immediate value
#
ori:
  movb  smem(,%edi,1), %al    #move Rf to low byte al
  sarl  $4, %eax              #shift eax to isolate Rd
  andl  $0xf, %eax            #isolate nybble Rd
  movl  smem+1(,%edi,1), %ebx #get immediate value
  orl   %ebx, regs(,%eax,4)   #or immediate with Rd
  addl  $5, %edi              #point to next opcode
  ret                         #return to fetch

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#  OR Rd with value at memory address
#
orm:
  movb  smem(,%edi,1), %al    #move Rf to low byte al
  sarl  $4, %eax              #shift eax to isolate Rd
  andl  $0xf, %eax            #isolate nybble Rd
  movw  smem+1(,%edi,1), %bx  #move memory& to word bx
  andl  $0xffff, %ebx         #isolate memory&
  movl  smem(,%ebx,1), %ebx   #get memory contents
  orl   %ebx, regs(,%eax,4)   #or contents with Rd
  addl  $3, %edi              #point to next opcode
  ret                         #return to fetch

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#  OR Rd with value at memory address offset by Rs
#
orx:
  movb  smem(,%edi,1), %al    #move Rf to low byte al
  movl  %eax, %ebx            #copy eax to ebx
  sarl  $4, %eax              #shift eax to isolate Rd
  andl  $0xf, %eax            #isolate nybble Rd
  andl  $0xf, %ebx            #isolate nybble Rs
  movl  regs(,%ebx,4), %ebx   #get index value
  movw  smem+1(,%edi,1), %cx  #move memory& to word cx
  addl  %ebx, %ecx            #add index offset to &
  andl  $0xffff, %ecx         #isolate memory&
  movl  smem(,%ecx,1), %ecx   #get memory contents
  orl   %ecx, regs(,%eax,4)   #or contents with Rd
  addl  $3, %edi              #point to next opcode
  ret                         #return to fetch

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#  OR Rd with value at memory address in Rs
#
orn:
  movb  smem(,%edi,1), %al    #move Rf to low byte al
  movl  %eax, %ebx            #copy eax to ebx
  sarl  $4, %eax              #shift eax to isolate Rd
  andl  $0xf, %eax            #isolate nybble Rd
  andl  $0xf, %ebx            #isolate nybble Rs
  movl  regs(,%ebx,4), %ebx   #get indirect Rs value
  andl  $0xffff, %ebx         #isolate memory&
  movl  smem(,%ebx,1), %ebx   #get contents pointed to
  orl   %ebx, regs(,%eax,4)   #or contents with Rd
  addl  $1, %edi              #point to next opcode
  ret                         #return to fetch

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#
#         XOR Rd with value
#
#  This set of operations performs a bitwise XOR on the
#  value in the register destination with a value from
#  a given location.
#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#  XOR Rd with value in Rs
#
xorr:
  movb  smem(,%edi,1), %al    #move Rf to low byte al
  movl  %eax, %ebx            #copy eax to ebx
  sarl  $4, %eax              #shift eax to isolate Rd
  andl  $0xf, %eax            #isolate nybble Rd
  andl  $0xf, %ebx            #isolate nybble Rs
  movl  regs(,%ebx,4), %ebx   #get Rs contents
  xorl  %ebx, regs(,%eax,4)   #xor contents with Rd
  addl  $1, %edi              #point to next opcode
  ret                         #return to fetch

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#  XOR Rd with immediate value
#
xori:
  movb  smem(,%edi,1), %al    #move Rf to low byte al
  sarl  $4, %eax              #shift eax to isolate Rd
  andl  $0xf, %eax            #isolate nybble Rd
  movl  smem+1(,%edi,1), %ebx #get immediate value
  xorl  %ebx, regs(,%eax,4)   #xor immediate with Rd
  addl  $5, %edi              #point to next opcode
  ret                         #return to fetch

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#  XOR Rd with value at memory address
#
xorm:
  movb  smem(,%edi,1), %al    #move Rf to low byte al
  sarl  $4, %eax              #shift eax to isolate Rd
  andl  $0xf, %eax            #isolate nybble Rd
  movw  smem+1(,%edi,1), %bx  #move memory& to word bx
  andl  $0xffff, %ebx         #isolate memory&
  movl  smem(,%ebx,1), %ebx   #get memory contents
  xorl  %ebx, regs(,%eax,4)   #xor contents with Rd
  addl  $3, %edi              #point to next opcode
  ret                         #return to fetch

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#  XOR Rd with value at memory address offset by Rs
#
xorx:
  movb  smem(,%edi,1), %al    #move Rf to low byte al
  movl  %eax, %ebx            #copy eax to ebx
  sarl  $4, %eax              #shift eax to isolate Rd
  andl  $0xf, %eax            #isolate nybble Rd
  andl  $0xf, %ebx            #isolate nybble Rs
  movl  regs(,%ebx,4), %ebx   #get index value
  movw  smem+1(,%edi,1), %cx  #move memory& to word cx
  addl  %ebx, %ecx            #add index offset to &
  andl  $0xffff, %ecx         #isolate memory&
  movl  smem(,%ecx,1), %ecx   #get memory contents
  xorl  %ecx, regs(,%eax,4)   #xor contents with Rd
  addl  $3, %edi              #point to next opcode
  ret                         #return to fetch

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#  XOR Rd with value at memory address in Rs
#
xorn:
  movb  smem(,%edi,1), %al    #move Rf to low byte al
  movl  %eax, %ebx            #copy eax to ebx
  sarl  $4, %eax              #shift eax to isolate Rd
  andl  $0xf, %eax            #isolate nybble Rd
  andl  $0xf, %ebx            #isolate nybble Rs
  movl  regs(,%ebx,4), %ebx   #get indirect Rs value
  andl  $0xffff, %ebx         #isolate memory&
  movl  smem(,%ebx,1), %ebx   #get contents pointed to
  xorl  %ebx, regs(,%eax,4)   #xor contents with Rd
  addl  $1, %edi              #point to next opcode
  ret                         #return to fetch

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#
#         NOT Rd
#
#  This operation performs a bitwise NOT on the value
#  in the register destination.
#
notr:
  movb  smem(,%edi,1), %al    #move Rf to low byte al
  sarl  $4, %eax              #shift eax to isolate Rd
  andl  $0xf, %eax            #isolate nybble Rd
  notl  regs(,%eax,4)         #not contents at Rd
  addl  $1, %edi              #point to next opcode
  ret                         #return to fetch

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#
#         jump to location
#
#  This operation jumps directly to a given memory ad-
#  dress with no preamble by loading the address into
#  the instruction pointer. It is used in all of the
#  following jump conditionals.
#
jmps:
  movw  smem+1(,%edi,1), %ax  #move memory& to word ax
  andl  $0xffff, %eax         #isolate memory&
  movl  %eax, %edi            #load edi with memory&
  ret                         #return to fetch with loc

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#
#         jump conditionals
#
#  This set of operations compares the magnitude of a
#  given value with the value in the register destina-
#  tion, jumping to a location if true. Each operation
#  uses 'jmps' if the condition is satisfied, returns
#  to 'fetch' if not.
#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#  jump if Rd is greater than Rs
#
jgtr:
  movb  smem(,%edi,1), %al    #move Rf to low byte al
  movl  %eax, %ebx            #copy eax to ebx
  sarl  $4, %eax              #shift eax to isolate Rd
  andl  $0xf, %eax            #isolate nybble Rd
  andl  $0xf, %ebx            #isolate nybble Rs
  movl  regs(,%eax,4), %eax   #get Rd contents
  movl  regs(,%ebx,4), %ebx   #get Rs contents
  cmpl  %ebx, %eax            #compare Rd[] with Rs[]
  jg    jmps                  #jump if eax > ebx to jmps
  addl  $3, %edi              #else point to next opcode
  ret                         #return to fetch

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#  jump if Rd is less than Rs
#
jltr:
  movb  smem(,%edi,1), %al    #move Rf to low byte al
  movl  %eax, %ebx            #copy eax to ebx
  sarl  $4, %eax              #shift eax to isolate Rd
  andl  $0xf, %eax            #isolate nybble Rd
  andl  $0xf, %ebx            #isolate nybble Rs
  movl  regs(,%eax,4), %eax   #get Rd contents
  movl  regs(,%ebx,4), %ebx   #get Rs contents
  cmpl  %ebx, %eax            #compare Rd[] with Rs[]
  jl    jmps                  #jump if eax < ebx to jmps
  addl  $3, %edi              #else point to next opcode
  ret                         #return to fetch

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#  jump if Rd is equal to Rs
#
jeqr:
  movb  smem(,%edi,1), %al    #move Rf to low byte al
  movl  %eax, %ebx            #copy eax to ebx
  sarl  $4, %eax              #shift eax to isolate Rd
  andl  $0xf, %eax            #isolate nybble Rd
  andl  $0xf, %ebx            #isolate nybble Rs
  movl  regs(,%eax,4), %eax   #get Rd contents
  movl  regs(,%ebx,4), %ebx   #get Rs contents
  cmpl  %ebx, %eax            #compare Rd[] with Rs[]
  je    jmps                  #jump if equal to jmps
  addl  $3, %edi              #else point to next opcode
  ret                         #return to fetch

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#  jump if Rd is equal to zero
#
jezr:
  movb  smem(,%edi,1), %al    #move Rf to low byte al
  sarl  $4, %eax              #shift eax to isolate Rd
  andl  $0xf, %eax            #isolate nybble Rd
  movl  regs(,%eax,4), %eax   #get Rd contents
  cmpl  $0, %eax              #compare Rd[] with 0
  je    jmps                  #jump if equal to jmps
  addl  $3, %edi              #else point to next opcode
  ret                         #return to fetch

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#  jump if Rd is greater than immediate value
#
jgti:
  movb  smem(,%edi,1), %al    #move Rf to low byte al
  sarl  $4, %eax              #shift eax to isolate Rd
  andl  $0xf, %eax            #isolate nybble Rd
  movl  regs(,%eax,4),%eax    #get Rd value
  movl  smem+3(,%edi,1), %ebx #get immediate value
  cmpl  %ebx, %eax            #compare Rd[] with $i
  jg    jmps                  #jump if eax > ebx to jmps
  addl  $7, %edi              #point to next opcode
  ret

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#  jump if Rd is less than immediate value
#
jlti:
  movb  smem(,%edi,1), %al    #move Rf to low byte al
  sarl  $4, %eax              #shift eax to isolate Rd
  andl  $0xf, %eax            #isolate nybble Rd
  movl  regs(,%eax,4),%eax    #get Rd value
  movl  smem+3(,%edi,1), %ebx #get immediate value
  cmpl  %ebx, %eax            #compare Rd[] with $i
  jl    jmps                  #jump if eax < ebx to jmps
  addl  $7, %edi              #point to next opcode
  ret

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#  jump if Rd is equal to immediate value
#
jeqi:
  movb  smem(,%edi,1), %al    #move Rf to low byte al
  sarl  $4, %eax              #shift eax to isolate Rd
  andl  $0xf, %eax            #isolate nybble Rd
  movl  regs(,%eax,4),%eax    #get Rd value
  movl  smem+3(,%edi,1), %ebx #get immediate value
  cmpl  %ebx, %eax            #compare Rd[] with $i
  je    jmps                  #jump if equal to jmps
  addl  $7, %edi              #point to next opcode
  ret

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#
#         jump call and return
#
#  These operations emulate the call and return func-
#  tions of other instructions: jump and link memory
#  'jalm' sets the register destionation with the in-
#  struction pointer to the next opcode in memory and
#  loads ip with another memory address to go to first,
#  like a call; jump indirect 'jmpn' gets the memory ad-
#  dress in the register destination and loads it into
#  the instruction pointer, like a return.
#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#  jump to memory address with ip linked to register
#
jalm:
  movb  smem(,%edi,1), %al    #move Rf to low byte al
  sarl  $4, %eax              #shift eax to isolate Rd
  andl  $0xf, %eax            #isolate nybble Rd
  movl  %edi, regs(,%eax,4)   #save ip to Rd
  addl  $3, regs(,%eax,4)     #increment ip
  jmp   jmps

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#  jump to memory address in Rd
#
jmpn:
  movb  smem(,%edi,1), %al    #move Rf to low byte al
  sarl  $4, %eax              #shift eax to isolate Rd
  andl  $0xf, %eax            #isolate nybble Rd
  movl  regs(,%eax,4), %eax   #get indirect Rd value
  andl  $0xffff, %eax         #isolate memory&
  movl  %eax, %edi            #load ip with memory&
  ret                         #return to fetch with ip

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#
#         add
#
#  This set of operations performs addition on the value
#  in the register destination with a value from a given
#  location.
#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#  add value in Rs to Rd
#
addr:
  movb  smem(,%edi,1), %al    #move Rf to low byte al
  movl  %eax, %ebx            #copy eax to ebx
  sarl  $4, %eax              #shift eax to isolate Rd
  andl  $0xf, %eax            #isolate nybble Rd
  andl  $0xf, %ebx            #isolate nybble Rs
  movl  regs(,%ebx,4), %ebx   #get Rs contents
  addl  %ebx, regs(,%eax,4)   #add contents to Rd
  addl  $1, %edi              #point to next opcode
  ret                         #return to fetch with ip

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#  add immediate value to Rd
#
addi:
  movb  smem(,%edi,1), %al    #move Rf to low byte al
  sarl  $4, %eax              #shift eax to isolate Rd
  andl  $0xf, %eax            #isolate nybble Rd
  movl  smem+1(,%edi,1), %ebx #get immediate value
  addl  %ebx, regs(,%eax,4)   #add immediate to Rd
  addl  $5, %edi              #point to next opcode
  ret                         #return to fetch with ip

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#  add value at memory address to Rd
#
addm:
  movb  smem(,%edi,1), %al    #move Rf to low byte al
  sarl  $4, %eax              #shift eax to isolate Rd
  andl  $0xf, %eax            #isolate nybble Rd
  movw  smem+1(,%edi,1), %bx  #move memory& to word bx
  andl  $0xffff, %ebx         #isolate memory&
  movl  smem(,%ebx,1), %ebx   #get memory contents
  addl  %ebx, regs(,%eax,4)   #add contents to Rd
  addl  $3, %edi              #point to next opcode
  ret                         #return to fetch with ip

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#  add value at memory address offset by Rs to Rd
#
addx:
  movb  smem(,%edi,1), %al    #move Rf to low byte al
  movl  %eax, %ebx            #copy eax to ebx
  sarl  $4, %eax              #shift eax to isolate Rd
  andl  $0xf, %eax            #isolate nybble Rd
  andl  $0xf, %ebx            #isolate nybble Rs
  movl  regs(,%ebx,4), %ebx   #get index value
  movw  smem+1(,%edi,1), %cx  #move memory& to word cx
  addl  %ebx, %ecx            #add index offset to &
  andl  $0xffff, %ecx         #isolate memory&
  movl  smem(,%ecx,1), %ecx   #get memory contents
  addl  %ecx, regs(,%eax,4)   #add contents to Rd
  addl  $3, %edi              #point to next opcode
  ret                         #return to fetch with ip

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#  add value at memory address in Rs to Rd
#
addn:
  movb  smem(,%edi,1), %al    #move Rf to low byte al
  movl  %eax, %ebx            #copy eax to ebx
  sarl  $4, %eax              #shift eax to isolate Rd
  andl  $0xf, %eax            #isolate nybble Rd
  andl  $0xf, %ebx            #isolate nybble Rs
  movl  regs(,%ebx,4), %ebx   #get indirect Rs value
  andl  $0xffff, %ebx         #isolate memory&
  movl  smem(,%ebx,1), %ebx   #get contents pointed to
  addl  %ebx, regs(,%eax,4)   #add contents to Rd
  addl  $1, %edi              #point to next opcode
  ret                         #return to fetch with ip

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#
#         shift bits right
#
#  This operation shifts the value in Rd to the right
#  by an immediate value.
#
shri:
  movb  smem(,%edi,1), %al    #move Rf to low byte al
  sarl  $4, %eax              #shift eax to isolate Rd
  andl  $0xf, %eax            #isolate nybble Rd
  movl  smem+1(,%edi,1), %ecx #get immediate value
  sarl  %cl, regs(,%eax,4)    #shift Rd $i bits right
  addl  $5, %edi              #point to next opcode
  ret

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#
#         skip
#
#  This operation does nothing but increment the in-
#  struction pointer.
#
skip:
  addl  $1, %edi              #point to next opcode
  ret                         #return to fetch

