#%% plotting figures
import numpy as np
import matplotlib.pyplot as plt
#from model_main import years,C_pom_record,C_agg_record,\
#    C_lmwc_record,C_maom_record,C_mic_record,C_total

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
plt.savefig('figure1.png')

# %%
#%% plotting figures note: horizontally
import numpy as np
import matplotlib.pyplot as plt
#from model_main import years,C_pom_record,C_agg_record,\
#    C_lmwc_record,C_maom_record,C_mic_record,C_total

fig, axs = plt.subplots(2,3,figsize = (12,10))

axs[0,0].plot(np.arange(365*years),C_pom_record)
axs[0,0].set_ylabel('C_pom')
axs[0,0].set_xlabel('Time (days)')

axs[0,1].plot(np.arange(365*years),C_agg_record)
axs[0,1].set_ylabel('C_agg')
axs[0,1].set_xlabel('Time (days)')

axs[0,2].plot(np.arange(365*years),C_lmwc_record)
axs[0,2].set_ylabel('C_lmwc')
axs[0,2].set_xlabel('Time (days)')

axs[1,0].plot(np.arange(365*years),C_maom_record)
axs[1,0].set_ylabel('C_maom')
axs[1,0].set_xlabel('Time (days)')

axs[1,1].plot(np.arange(365*years),C_mic_record)
axs[1,1].set_ylabel('C_mic')
axs[1,1].set_xlabel('Time (days)')

axs[1,2].plot(np.arange(365*years),C_total)
axs[1,2].set_ylabel('C_total')
axs[1,2].set_xlabel('Time (days)')
#plt.show()
plt.tight_layout()
plt.savefig('figure1_horizontal.png')

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
st = plt.suptitle('initial condition AGG'+ '%d' %C_agg0)
st.set_y(0.75)
st.set_x(0.55)
plt.tight_layout()
plt.savefig('figure1_horizontal.png')