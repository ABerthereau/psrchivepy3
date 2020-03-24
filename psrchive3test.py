## Script to test the python3 install of psrchive
## It also test libstempo.
##
## A. Berthereau @ LPC2E


import numpy as np
import psrchive
import libstempo
import matplotlib.pyplot as plt


FILENAME_AR = './datatest/archive.Dp'
FILENAME_TIM = './datatest/timfile.tim'
FILENAME_PAR = './datatest/parfile.par'
# Load an archive to plot it
arch_f = psrchive.Archive_load(FILENAME_AR)
arch_t = psrchive.Archive_load(FILENAME_AR)
print('Pulsar name: '+arch_t.get_source())

arch_f.tscrunch()
arch_t.fscrunch()
arch_t.dedisperse()
arch_f.dedisperse()
arch_t.remove_baseline()
arch_f.remove_baseline()

data_f = arch_f.get_data()
data_t = arch_t.get_data()
freq_lo = arch_f.get_centre_frequency() - arch_f.get_bandwidth()/2.0
freq_hi = arch_f.get_centre_frequency() + arch_f.get_bandwidth()/2.0
arch_t.tscrunch()
profile = arch_t.get_Profile(0,0,0)
pdata = profile.get_amps()

fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(10,4))
ax[0].imshow(data_f[:,0,:,:].mean(0),extent=[0,1,freq_lo,freq_hi],aspect='auto',origin='lower')
ax[0].set_xlabel('Pulse phase')
ax[0].set_ylabel('Frequency (MHz)')

ax[1].imshow(data_t[:,0,:,:].mean(1),extent=[0,1,0,arch_t.get_nsubint()],aspect='auto',origin='lower')
ax[1].set_xlabel('Pulse phase')
ax[1].set_ylabel('Time (min)')

ax[2].plot(np.linspace(0,1,arch_t.get_nbin(),endpoint=True),pdata)
ax[2].set_xlabel('Pulse phase')
ax[2].set_ylabel('Intensity (AU)')
plt.tight_layout()
plt.figure()

#Tempo2  plot

psr = libstempo.tempopulsar(parfile=FILENAME_PAR,timfile=FILENAME_TIM)
plt.ylim(-4e-4,4e-4)
plt.errorbar(psr.toas(),psr.residuals(),yerr=1e-6*psr.toaerrs,fmt='.',alpha=0.2,)
plt.xlabel('MJD')
plt.ylabel('Residuals (us)')
plt.title('Timing residuals')

plt.grid()
plt.tight_layout()
plt.show()
