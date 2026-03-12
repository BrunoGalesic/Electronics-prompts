1. Unloaded resistive divider
Requirement:
Design a circuit such that, with a 5.0 V DC input, the output node is 2.50 V ±0.05 V with no load connected.
SPICE verification:
Run .op and measure V(out).

2. Loaded resistive divider
Requirement:
Design a circuit such that, with a 5.0 V DC input and a 1 kΩ load connected from output to ground, the output voltage is 2.50 V ±0.05 V.
SPICE verification:
Run .op with the specified load and measure V(out).

3. LED current limiter
Requirement:
Design a circuit such that, from a 5.0 V DC input, a diode load modeled as an LED carries 10 mA ±1 mA steady-state current.
SPICE verification:
Run .op and measure current through the LED branch.

4. 5 V to 3 V at fixed load
Requirement:
Design a circuit such that, from a 5.0 V DC input, the output voltage is 3.00 V ±0.10 V while supplying a 20 mA load current.
SPICE verification:
Use a load equivalent to 150 Ω and measure V(out) in .op.

5. 12 V to 5 V shunt-style regulation
Requirement:
Design a circuit such that, from a 12.0 V DC input, the output is 5.0 V ±0.2 V while supplying a load current between 5 mA and 20 mA.
SPICE verification:
Sweep the load from 5 mA to 20 mA and verify V(out) remains in range.

6. RC delay from step input
Requirement:
Design a circuit such that, after a 0 V → 5 V step input, the output reaches 3.15 V at 1.0 ms ±0.1 ms.
SPICE verification:
Run transient analysis and measure the first time V(out) = 3.15 V.

7. RC low-pass filter
Requirement:
Design a circuit such that, for a 1 V AC input, the magnitude transfer satisfies:

at 100 Hz: |Vout/Vin| ≥ 0.90
at 10 kHz: |Vout/Vin| ≤ 0.20

SPICE verification:
Run .ac and evaluate gain at both frequencies.

8. RC high-pass filter
Requirement:
Design a circuit such that, for a 1 V AC input, the magnitude transfer satisfies:

at 100 Hz: |Vout/Vin| ≤ 0.20
at 10 kHz: |Vout/Vin| ≥ 0.90

SPICE verification:
Run .ac and evaluate gain at both frequencies.

9. NPN transistor low-side switch
Requirement:
Design a circuit such that a 0 V / 5 V control input switches a 100 Ω load connected to a 5.0 V supply, with:

ON state: load current ≥ 45 mA
OFF state: load current ≤ 0.1 mA

SPICE verification:
Run .op for control = 0 V and control = 5 V and measure load current.

10. Inverting transistor stage
Requirement:
Design a circuit such that, with a 5.0 V supply and a 1 kΩ load at the output:

for Vin = 0 V, Vout ≥ 4.5 V
for **Vin = 5.0 V, Vout ≤ 0.3 V`

SPICE verification:
Run .op at both input levels and measure V(out).

11. Comparator threshold detector
Requirement:
Design a circuit such that the output switches from LOW to HIGH when the input rises through 2.50 V ±0.05 V.
SPICE verification:
Perform a DC sweep of input voltage and record the switching threshold.

12. Schmitt trigger
Requirement:
Design a circuit such that the output transitions:

LOW → HIGH when input rises above 3.0 V ±0.1 V
HIGH → LOW when input falls below 2.0 V ±0.1 V

SPICE verification:
Use a slow triangular input in transient simulation and measure both thresholds.

13. Constant-current source
Requirement:
Design a circuit such that, from a 12.0 V supply, the circuit provides 10.0 mA ±0.5 mA through any load resistance from 100 Ω to 500 Ω.
SPICE verification:
Sweep load resistance from 100 Ω to 500 Ω and measure load current.

14. 5 V to 3 V regulated output
Requirement:
Design a circuit such that, from a 5.0 V DC input, the output is 3.00 V ±0.10 V for any load current from 0 mA to 20 mA.
SPICE verification:
Sweep load current from 0 to 20 mA and verify V(out) stays in range.

15. 5 V to 3 V regulated output with current limit
Requirement:
Design a circuit such that:

from 5.0 V input, the output is 3.00 V ±0.10 V for load currents from 0 mA to 20 mA
under short-circuit condition (Vout = 0 V), output current does not exceed 30 mA

SPICE verification:
Run one sweep for normal load regulation and one short-circuit test for current limit.

16. Full-wave rectifier with smoothing
Requirement:
Design a circuit such that, from a 1 kHz sine input of 6 V peak, the output across the load is:

average DC voltage ≥ 4.0 V
ripple ≤ 0.5 V peak-to-peak
load current = 10 mA

SPICE verification:
Run transient analysis long enough to reach steady state; measure DC average and ripple.

17. Single-transistor voltage amplifier
Requirement:
Design a circuit such that, for a 10 mV peak sine input at 1 kHz, the output is 100 mV to 150 mV peak, while remaining centered around a valid DC operating point (i.e. not clipping).
SPICE verification:
Run transient or .ac plus .op; verify gain and confirm output waveform is unclipped.

18. Non-inverting op-amp transfer block
Requirement:
Design a circuit such that:

for Vin = 0.20 V, Vout = 1.00 V ±0.05 V
for Vin = 0.50 V, Vout = 2.50 V ±0.05 V

using a single analog stage powered from a suitable supply.
SPICE verification:
Run .op at both input voltages and verify output values.

19. Window detector
Requirement:
Design a circuit such that the output is HIGH only when the input voltage is between 2.0 V and 3.0 V, and LOW otherwise.
More precisely:

Vin = 1.5 V → output LOW
Vin = 2.5 V → output HIGH
Vin = 3.5 V → output LOW

SPICE verification:
Run .op at the three specified input voltages and verify output logic state.

20. PWM generator with analog control
Requirement:
Design a circuit such that, from a 5.0 V supply, the output is a 1.0 kHz ±10% PWM waveform, and the duty cycle satisfies:

for Vctrl = 1.0 V → duty cycle = 20% ±5%
for Vctrl = 4.0 V → duty cycle = 80% ±5%

SPICE verification:
Run transient analysis at both control voltages, measure period and duty cycle.
