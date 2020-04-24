import math
#%% model paramter values
Kagg = 0.0002 # kb in the paper (unitless; Should be gC/m2/day)
Amax = 500 # gC/m2
Vpa = 0.002 # gC / (m2 day)
Vpl = 10 # gC / (m2 day)
Vlm = 0.35 # gC / (m2 day)
Vml = 0.01
Vma = 0.07
Kpa = 50 # gC/m2
Kpl = 150 # gC/m2
Kpe = 12 # gC/m2
Kl = 0.0015 # gC / (m2 day)
Klm = 0.25 # gC/m2 flagged
Kml = 25
Klb = 7.2 # gC/m2
Kma = 200
Kmm = 0.025 # unitless
Kmic = 0.036 # per day
M_Lmin = 10

BulkD = 1150 # kg soil /m3
clay_per = 40 # percentage
c1 = 0.4833 #0.297 default in Millennial
c2 = 2.3282 #3.355 default 

pi = 2./3.
pa = 1./3.
#%% model coefficients
St = 1 # for now; subject to change to functions
Sw = 1 
Qmax1 = 10**(c1 * math.log(clay_per,10) + c2)
Qmax = BulkD * Qmax1 * 10**(-3) # convert to gC/m2 (flagged)
# convert mg C kg-1 dry soil to gC/m2(flagged; not sure log10 or loge )
# note that I added  10**(-3) in the equation. The original is likely be wrong
