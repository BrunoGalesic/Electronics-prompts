import schemdraw
import schemdraw.elements as elm

with schemdraw.Drawing() as d:
    d += elm.Ground()
    d += elm.SourceSin().up().label('1 V AC')
    d += elm.Capacitor().right().label('C1\n10 nF')
    d += elm.Dot().label('VOUT')
    d.push()
    d += elm.Resistor().down().label('R1\n10 kΩ')
    d += elm.Ground()
    d.pop()
    d.draw()
