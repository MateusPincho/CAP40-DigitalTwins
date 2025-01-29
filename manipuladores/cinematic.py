#!/usr/bin/env python3
import roboticstoolbox as rtb

# import the UR10 model from the toolbox
UR10 = rtb.models.URDF.UR5()

UR10.fkine(UR10.qr).printline()

UR10.plot(UR10.qr)