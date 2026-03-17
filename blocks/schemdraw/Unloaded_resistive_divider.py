import schemdraw
import schemdraw.elements as elm

with schemdraw.Drawing() as d:
    d += elm.Ground()
    d += elm.SourceV().up().label('5V')
    d += elm.Resistor().right().label('R1\n10 kΩ')
    d += elm.Dot().label('VOUT')
    d.push()
    d += elm.Resistor().down().label('R2\n10 kΩ')
    d += elm.Ground()
    d.pop()
    d.draw()
