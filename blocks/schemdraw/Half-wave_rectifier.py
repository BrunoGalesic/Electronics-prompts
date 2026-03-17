import schemdraw
import schemdraw.elements as elm

with schemdraw.Drawing() as d:
    d += elm.Ground()
    d += elm.SourceSin().up().label('6Vpk\n1kHz')
    d += elm.Dot().label('VIN')
    d += elm.Diode().right().label('1N4148')
    d += elm.Dot().label('VOUT')

    d.push()
    d += elm.Capacitor().down().label('22µF')
    d += elm.Ground()
    d.pop()

    d.push()
    d += elm.Line().right()
    d += elm.Resistor().down().label('510Ω')
    d += elm.Ground()
    d.pop()

    d.draw()
