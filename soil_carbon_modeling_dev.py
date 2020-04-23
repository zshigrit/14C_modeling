#%% developing a soil carbon model to capture radiocarbon 14C on the basis of MILLENNIAL model
# Abramoff et al. 2018 Biogeochemistry
#%% soil carbon pools: C_pom (Particulate Organic Matter), C_maom (Minearl Assoicated Organic Matter)
# C_lmwc (Low Molecular Weight Carbon); C_agg (Aggregate carbon); C_mic: microbial biomass
#%% libraries
import math
import numpy as np
#%% model paramter values
Kagg = 0.0002 # kb in the paper (unitless)
Vpa = 0.002 # gC / (m2 day)
Kpa = 50 # gC/m2
Amax = 500 # gC/m2
Vpl = 10 # gC / (m2 day)
Vlm = 0.35 # gC / (m2 day)
Vma = 0.07
Kpl = 150 # gC/m2
Kpe = 12 # gC/m2
Kl = 0.0015 # gC / (m2 day)
Klm = 0.25 # gC/m2
Klb = 7.2 # gC/m2
Kma = 200
Kmm = 0.025 # unitless
Kmic = 0.036 # per day

BulkD = 1150 # kg soil /m3
clay_per = 40 # percentage
c1 = 0.4833 #0.297 default in Millennial
c2 = 2.3282 #3.355 default 

pi = 2./3.
pa = 1./3.
#%% initial conditions
C_agg = 500 # gC/m2
C_pom = 200
C_mic = 100
C_maom = 2000
C_lmwc = 100
#%% model coefficients
St = 1 # for now; subject to change to functions
Sw = 1 
Qmax1 = 10**(c1 * math.log(clay_per,10) + c2)
Qmax = BulkD * Qmax1 * 10**(-3) # convert to gC/m2 (flagged)
# convert mg C kg-1 dry soil to gC/m2(flagged; not sure log10 or loge )
# note that I added  10**(-3) in the equation. The original is likely be wrong
#%% carbon input into the system
Fi = 172. # gC/m2/yr
Fi_day = Fi/365.# gC/m2/day suject to change (flagged)
#%% pre-assign carbon pools
C_pom_record = []
C_agg_record = []
C_lmwc_record = []
C_maom_record = []
C_mic_record = []
#%% model processes
years = 100
for day in np.arange(years*365):
    # Equation 1: dC_pom/dt = piFi + paFa - Fpa - Fpl
    Fagg = Kagg * C_agg * St * Sw 
    Fpa = Vpa * (C_pom / (Kpa + C_pom)) * (1 - (C_agg/Amax)) * St * Sw 
    Fpl = Vpl * (C_pom/(Kpl+C_pom)) * (C_mic / (Kpe + C_mic)) * St * Sw # double Michaelis-Menten equation
    Fap = Fagg * pa 
    # Equation 2: dL/dt = Fi(1-pi)-Fl+Fpl-Flm-Flb # low molecular weight carbon
    Fl = Kl * C_lmwc * St * Sw 
    Flm = C_lmwc * (Klm * Qmax * C_lmwc/(1+(Klm * C_lmwc)) - C_maom ) / Qmax * St *Sw 
    Flb = Vlm * C_lmwc * C_mic / (C_mic + Klb) * St * Sw # * (CUEref - CUEt * (T - Tref))  (Flagged)
    # Equation 3: dC_agg/dt = Fma+Fpa-Fa
    Fma = Vma * C_maom /(Kma + C_maom) * (1 - C_agg/Amax) * St * Sw
    # Equation 4: dMAOM/dt = Flm+Fbm-Fma+Fa(1-pa)
    Fbm = Kmm * C_mic * St * Sw 
    Fam = Fagg * (1-pa) 
    # Equation 5: dMIC/dt = Flb-Fbm-Fmr
    Fmr = Kmic * C_mic * St * Sw 
    #
    #
    C_pom = C_pom + pi * Fi_day + Fap - Fpa - Fpl 
    C_lmwc = C_lmwc + (1-pi) * Fi_day + Fpl - Fl - Flm - Flb
    C_agg = C_agg + Fma + Fpa - Fagg
    C_maom = C_maom + Flm + Fbm + Fam - Fma
    C_mic = C_mic + Flb - Fbm - Fmr  
    #
    # 
    C_pom_record = np.append(C_pom_record,C_pom) 
    C_agg_record = np.append(C_agg_record,C_agg)
    C_lmwc_record = np.append(C_lmwc_record,C_lmwc)
    C_maom_record = np.append(C_maom_record,C_maom)  
    C_mic_record = np.append(C_mic_record,C_mic)
C_total = C_pom_record + C_agg_record + C_lmwc_record\
    + C_maom_record + C_mic_record
#%% plotting figures
import matplotlib.pyplot as plt

fig, axs = plt.subplots(3,2,figsize = (10,12))

axs[0,0].plot(np.arange(365*years),C_pom_record)
axs[0,0].set_ylabel('C_pom')
axs[0,0].set_xlabel('Time (days)')

axs[0,1].plot(np.arange(365*years),C_agg_record)
axs[0,1].set_ylabel('C_agg')
axs[0,1].set_xlabel('Time (days)')

axs[1,0].plot(np.arange(365*years),C_lmwc_record)
axs[1,0].set_ylabel('C_lmwc')
axs[1,0].set_xlabel('Time (days)')

axs[1,1].plot(np.arange(365*years),C_maom_record)
axs[1,1].set_ylabel('C_maom')
axs[1,1].set_xlabel('Time (days)')

axs[2,0].plot(np.arange(365*years),C_mic_record)
axs[2,0].set_ylabel('C_mic')
axs[2,0].set_xlabel('Time (days)')

axs[2,1].plot(np.arange(365*years),C_total)
axs[2,1].set_ylabel('C_total')
axs[2,1].set_xlabel('Time (days)')
#plt.show()
plt.savefig('figure2.png')
# %%
