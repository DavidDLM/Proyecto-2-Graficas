# Mario de Leon 19019
# Graficos por computadora basado en lo escrito por Ing. Dennis Aldana / Ing. Carlos Alonso

import matMath as mt
from intersect import Intersect
import numpy as np

# Colores default
white = (1, 1, 1)
black = (0, 0, 0)


class Plane(object):
    def __init__(this, position, normal,  material):
        this.position = position
        this.normal = [n / mt.normL2(normal) for n in normal]
        this.material = material

    def ray_intersect(this, origin, direction):
        denom = mt.dotMatrix(direction, this.normal)

        if abs(denom) > 0.0001:
            num = mt.dotMatrix(mt.subtractVectors(
                this.position, origin), this.normal)
            t = num / denom

            if t > 0:
                # P = O + t*D
                P = mt.addVectors(origin, [t * d for d in direction])
                return Intersect(distance=t,
                                 point=P,
                                 normal=this.normal,
                                 texcoords=None,
                                 sceneObj=this)

        return None
