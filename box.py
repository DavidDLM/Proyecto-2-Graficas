# Mario de Leon 19019
# Graficos por computadora basado en lo escrito por Ing. Dennis Aldana / Ing. Carlos Alonso

import matMath as mt
from intersect import Intersect
from plane import Plane
import numpy as np

# Colores default
white = (1, 1, 1)
black = (0, 0, 0)


class Box(object):
    def __init__(this, position, size, material):
        this.position = position
        this.size = size
        this.material = material

        this.planes = []

        halfSizes = [0, 0, 0]

        halfSizes[0] = size[0] / 3
        halfSizes[1] = size[1] / 3
        halfSizes[2] = size[2] / 3

        # Sides
        this.planes.append(
            Plane(mt.addVectors(position, (halfSizes[0], 0, 0)), (1, 0, 0), material))
        this.planes.append(
            Plane(mt.addVectors(position, (-halfSizes[0], 0, 0)), (-1, 0, 0), material))

        # Up and Down
        this.planes.append(
            Plane(mt.addVectors(position, (0, halfSizes[1], 0)), (0, 1, 0), material))
        this.planes.append(
            Plane(mt.addVectors(position, (0, -halfSizes[1], 0)), (0, -1, 0), material))

        # Front and back
        this.planes.append(
            Plane(mt.addVectors(position, (0, 0, halfSizes[2])), (0, 0, 1), material))
        this.planes.append(
            Plane(mt.addVectors(position, (0, 0, -halfSizes[2])), (0, 0, -1), material))

        # Bounds
        this.boundsMin = [0, 0, 0]
        this.boundsMax = [0, 0, 0]

        epsilon = 0.001

        for i in range(3):
            this.boundsMin[i] = this.position[i] - (epsilon + halfSizes[i])
            this.boundsMax[i] = this.position[i] + (epsilon + halfSizes[i])

    def ray_intersect(this, orig, dir):
        intersect = None
        t = float('inf')

        for plane in this.planes:
            planeInter = plane.ray_intersect(orig, dir)
            if planeInter is not None:

                planePoint = planeInter.point

                if this.boundsMin[0] <= planePoint[0] <= this.boundsMax[0]:
                    if this.boundsMin[1] <= planePoint[1] <= this.boundsMax[1]:
                        if this.boundsMin[2] <= planePoint[2] <= this.boundsMax[2]:

                            if planeInter.distance < t:
                                t = planeInter.distance
                                intersect = planeInter

                                # Tex Coords

                                u, v = 0, 0

                                # Las uvs de las caras de los lados
                                if abs(plane.normal[0]) > 0:
                                    # Mapear uvs para el eje x, usando las coordenadas de Y y Z
                                    u = (
                                        planeInter.point[1] - this.boundsMin[1]) / this.size[1]
                                    v = (
                                        planeInter.point[2] - this.boundsMin[2]) / this.size[2]

                                elif abs(plane.normal[1] > 0):
                                    # Mapear uvs para el eje y, usando las coordenadas de X y Z
                                    u = (
                                        planeInter.point[0] - this.boundsMin[0]) / this.size[0]
                                    v = (
                                        planeInter.point[2] - this.boundsMin[2]) / this.size[2]

                                elif abs(plane.normal[2] > 0):
                                    # Mapear uvs para el eje z, usando las coordenadas de X y Y
                                    u = (
                                        planeInter.point[0] - this.boundsMin[0]) / this.size[0]
                                    v = (
                                        planeInter.point[1] - this.boundsMin[1]) / this.size[1]

        if intersect is None:
            return None

        return Intersect(distance=t,
                         point=intersect.point,
                         normal=intersect.normal,
                         texcoords=(u, v),
                         sceneObj=this)
