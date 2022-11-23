# Mario de Leon 19019
# Graficos por computadora basado en lo escrito por Ing. Dennis Aldana / Ing. Carlos Alonso

import matMath as mt
from intersect import Intersect
from plane import Plane
import numpy as np

# Colores default
white = (1, 1, 1)
black = (0, 0, 0)


class Disk(object):
    def __init__(this, position, radius, normal,  material):
        this.plane = Plane(position, normal, material)
        this.material = material
        this.radius = radius

    def ray_intersect(this, orig, dir):

        intersect = this.plane.ray_intersect(orig, dir)

        if intersect is None:
            return None

        contact = mt.subtractVectors(intersect.point, this.plane.position)
        contact = mt.normL2(contact)

        if contact > this.radius:
            return None

        return Intersect(distance=intersect.distance,
                         point=intersect.point,
                         normal=this.plane.normal,
                         texcoords=None,
                         sceneObj=this)
