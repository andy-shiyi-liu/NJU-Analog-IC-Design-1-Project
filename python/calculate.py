import math

import parameters.model as model
import parameters.requirements as req
from functions.validate import *
from functions.print import *
import functions.mos as mos

# Additional parameters
Cl = 10e-12

# Design parameters
Cc = 0.3 * Cl
S1 = 1
S2 = S1
S3 = 1
S4 = 1
S5 = 1
# S6 = 1
# S7 = 1
V_bias = 1.5

# Restrain calculation
Cc_min = 0.22 * Cl

validate(Cc, Cc_min, ">", "C_c")

I5_min = req.SR_min* Cc
I5 = mos.Vgs2Id(Vgs=V_bias, Vth=model.V_THN, K=model.K_N, S=S5)
validate(I5, I5_min, ">", "I")

S3_max = 2 * (I5_min / 2) / (model.K_P * (req.Vdd - req.Vin_max - model.V_THP + model.V_THN))
validate(S3, S3_max, "<", "S3")

gm1_min = req.GB * Cc
gm2_min = gm1_min

gm1 = mos.Id2gm(Id=I5/2, K=model.K_N, S=S1)
gm2 = mos.Id2gm(Id=I5/2, K=model.K_N, S=S2)
validate(S1, (gm1_min ** 2) / model.K_N * I5)
validate(S2, (gm2_min ** 2) / model.K_N * I5)

Vds5_sat_max = req.Vin_min - req.Vss - mos.Id2Von(Id=I5/2, K = model.K_N, S = S1) - model.V_THN
S5_min  = (2*I5)/(model.K_N * (Vds5_sat_max ** 2))
validate(S5, S5_min, ">", "S5")

gm3 = mos.Id2gm(Id=I5/2, K=model.K_P)
gm4 = gm3

gm6 = 2.2 * gm2 * (Cl / Cc)
S6 = S4 * gm6 / gm4

I6 = (gm6**2) / (2 * model.K_P * S6)

S7 = (I6 / I5) * S5

Av = (2 * gm2 * gm6)/(I5 * I6 * ((model.Lambda_P)**2))
validate(Av, req.Ac_min, ">", "Av")

Power = (I5 + I6)*(req.Vdd + abs(req.Vss))