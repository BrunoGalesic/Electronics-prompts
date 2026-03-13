Circuit: 5.0V to 2.50V No-Load Divider
Source: Designed solution

[Components]
R1 = 10 kΩ ±1%, Package=0603, Function=Upper divider resistor
R2 = 10 kΩ ±1%, Package=0603, Function=Lower divider resistor

[Nets]
+5V
VOUT
GND

[Component Connectivity]
R1
 Pin1(Pin1) -> +5V
 Pin2(Pin2) -> VOUT
R2
 Pin1(Pin1) -> VOUT
 Pin2(Pin2) -> GND

[Hierarchy]
Sheet main: R1, R2

[Notes]
- R1 and R2 form a 1:1 resistive divider from +5V to GND; VOUT is the junction(R1,R2).
- Nominal output with a 5.0 V DC input is 2.50 V with no load connected.
- Using equal ±1% resistors, worst-case no-load output is approximately 2.475 V to 2.525 V, which meets the requirement of 2.50 V ±0.05 V.
- This solution is valid only for the stated no-load condition; if any load is connected to VOUT, the divider ratio will shift unless the node is buffered.

