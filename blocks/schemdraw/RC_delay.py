import schemdraw
import schemdraw.elements as elm

with schemdraw.Drawing() as d:
    d += elm.Ground()
    d += elm.SourceV().up().label('0 V to 5 V step')
    d += elm.Resistor().right().label('R1\n10 kΩ')
    d += elm.Dot().label('VOUT_DELAY')
    d.push()
    d += elm.Capacitor().down().label('C1\n100 nF')
    d += elm.Ground()
    d.pop()
    d.draw()
