#%% model coefficients
St = 1 # for now; subject to change to functions
Sw = 1 
Qmax1 = 10**(c1 * math.log(clay_per,10) + c2)
Qmax = BulkD * Qmax1 * 10**(-3) # convert to gC/m2 (flagged)
# convert mg C kg-1 dry soil to gC/m2(flagged; not sure log10 or loge )
# note that I added  10**(-3) in the equation. The original is likely be wrong
