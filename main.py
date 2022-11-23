from gl import Raytracer, V3
import math
import conversions as conv
import struct
from disk import *
from box import *
from intersect import *
from lights import *
from material import *
from plane import *
from sphere import *
from collections import namedtuple
import matMath as mt
from textures import *
from obj import *
from math import cos, sin, tan, pi


width = 1280
height = 720

# Materiales a usar
glass = Material(diffuse=(0.9, 0.9, 0.9), spec=64,
                 ior=1.5, matType=TRANSPARENT)
lid = Material(texture=Texture("corcho.bmp"),
               spec=50, ior=1.5, matType=REFLECTIVE)
pot1 = Material(texture=Texture("pink.bmp"),
                spec=50, ior=1.5, matType=TRANSPARENT)
pot2 = Material(diffuse=(0.4, 0.4, 2.4),
                spec=64, ior=1.5, matType=REFLECTIVE)
pot3 = Material(texture=Texture("purple.bmp"),
                spec=64, ior=1.5, matType=TRANSPARENT)

rtc = Raytracer(width, height)

# Fondo
rtc.envMap = Texture("bck.bmp")

# Luces
rtc.lights.append(AmbientLight(intensity=0.1))
rtc.lights.append(DirectionalLight(direction=(0, 0, -1), intensity=0.1))
rtc.lights.append(DirectionalLight(direction=(0, 0, -5), intensity=0.1))

# Pocion 1
rtc.scene.append(Sphere(center=(0, 1, -10), radius=2, material=pot1))
rtc.scene.append(Sphere(center=(0, 3.7, -10), radius=0.7, material=glass))
rtc.scene.append(Disk(position=(0, 4.5, -10), radius=0.8,
                 normal=(0, 1, 0), material=lid))
rtc.scene.append(Box(position=(0, 4.9, -10), size=(2, 1, 1), material=lid))

# Pocion 2
rtc.scene.append(Sphere(center=(6, 1, -10), radius=0.7, material=glass))
rtc.scene.append(Sphere(center=(6, -1, -10), radius=2, material=pot2))
rtc.scene.append(Box(position=(5, 1, -10), size=(1, 2, 1), material=lid))
rtc.scene.append(Box(position=(7, 1, -10), size=(1, 2, 1), material=lid))

# Pocion 3
rtc.scene.append(Sphere(center=(-6, -1, -10), radius=2, material=pot3))
rtc.scene.append(Sphere(center=(-5, 1, -10), radius=0.7, material=glass))
rtc.scene.append(Sphere(center=(-4.6, 0.8, -10), radius=0.7, material=glass))
rtc.scene.append(Sphere(center=(-4.6, 1.4, -10), radius=0.7, material=glass))
rtc.scene.append(Sphere(center=(-4.6, 1.6, -10), radius=0.7, material=glass))
rtc.scene.append(Box(position=(-4.6, 2.3, -10), size=(1, 2, 1), material=lid))

rtc.glRender()
rtc.write("output.bmp")
