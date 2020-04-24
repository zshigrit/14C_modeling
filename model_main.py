#%% import libraries
import numpy as np
import math
#
from model_paramters import *
from model_initial_conditions import *
from model_carbon_input import *
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
    Flb = Vlm * C_lmwc * C_mic / (C_mic + Klb) * St * Sw # * (CUEref - CUEt * (T - Tref)) (Flagged)
    # 0.3 is CUE subject to change
    # Equation 3: dC_agg/dt = Fma+Fpa-Fa
    Fma = Vma * C_maom /(Kma + C_maom) * (1 - C_agg/Amax) * St * Sw
    # Equation 4: dMAOM/dt = Flm+Fbm-Fma+Fa(1-pa)
    Fbm = Kmm * C_mic * St * Sw 
    Fam = Fagg * (1-pa) 
    # Equation 5: dMIC/dt = Flb-Fbm-Fmr
    Fmr = Kmic * C_mic * St * Sw 
    # newly added from Xu model description
    # Xu found this process is not important
    Fml = Vml * (C_maom - M_Lmin) / (Kml + C_maom - M_Lmin) * St * Sw
    # state variables 
    C_pom = C_pom + pi * Fi_day + Fap - Fpa - Fpl 
    C_lmwc = C_lmwc + (1-pi) * Fi_day + Fpl + Fml - Fl - Flm - Flb
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


#%% plotting figures note: horizontally and in year unit
import numpy as np
import matplotlib.pyplot as plt
import matplotlib 
#from model_main import years,C_pom_record,C_agg_record,\
#    C_lmwc_record,C_maom_record,C_mic_record,C_total
matplotlib.rcParams.update({'font.size': 18})
fig, axs = plt.subplots(2,3,figsize = (20,12))

x = np.arange(0,years,1/365)

axs[0,0].plot(x,C_pom_record)
axs[0,0].set_ylabel('C_pom (gC/m2)',fontsize = 18)
axs[0,0].set_xlabel('Time (years)')

axs[0,1].plot(x,C_agg_record)
axs[0,1].set_ylabel('C_agg (gC/m2)',fontsize = 18)
axs[0,1].set_xlabel('Time (years)')

axs[0,2].plot(x,C_lmwc_record)
axs[0,2].set_ylabel('C_lmwc (gC/m2)',fontsize = 18)
axs[0,2].set_xlabel('Time (years)')

axs[1,0].plot(x,C_maom_record)
axs[1,0].set_ylabel('C_maom (gC/m2)',fontsize = 18)
axs[1,0].set_xlabel('Time (years)')

axs[1,1].plot(x,C_mic_record)
axs[1,1].set_ylabel('C_mic (gC/m2)',fontsize = 18)
axs[1,1].set_xlabel('Time (years)')

axs[1,2].plot(x,C_total)
axs[1,2].set_ylabel('C_total (gC/m2)',fontsize = 18)
axs[1,2].set_xlabel('Time (years)')
#plt.show()
#st = plt.suptitle('initial condition AGG'+ '%d' %C_agg0)
#st.set_y(0.75)
#st.set_x(0.55)
plt.tight_layout()
plt.savefig('figure1_horizontal.png')

# %%
