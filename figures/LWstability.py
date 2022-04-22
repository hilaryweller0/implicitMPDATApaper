from pylab import *

c = linspace(1,3,41)
theta = 1 - 1/c
chi2nd = 1 - 2*theta
chiStable = (2*c-1)/c**2
chiUsed = maximum(chi2nd, zeros_like(c))
oneByC = 1/c

plot(c, chi2nd, 'k-', linewidth=1, label="2nd order")
fill_between(c, zeros_like(c), chiStable, color='grey', label="stable")
plot(c, chiUsed, 'k:', linewidth=3, label="MPDATA")
#plot(c, oneByC, 'k--', label = "1/c")
legend()
xlim([1,3])
xlabel("Courant number")
ylabel(r'$\chi$')
axvline(2, ls=':', color="black", linewidth=0.5)
savefig("LWstability.pdf")
