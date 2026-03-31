# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 07:16:15 2026

@author: bijet
"""

# -*- coding: utf-8 -*-
"""
Mapping Planck 2018 constraints (u and <σv>) to a neutrino portal DM model.
Author: Adapted from the paper by Paul et al. (2021)
"""

import numpy as np
import matplotlib.pyplot as plt

# Physical constants (cgs)
sigma_Th = 6.65e-25            # Thomson cross-section (cm^2)
c = 2.998e10                   # speed of light (cm/s)
hbar_c_cm = 1.97327e-14        # ħc in cm (1 GeV^-1 = ħc = 1.973e-14 cm)
GeV2_to_cm2 = (hbar_c_cm)**2   # 1/GeV^2 -> cm^2
GeV2_to_cm3ps = GeV2_to_cm2 * c  # 1/GeV^2 -> cm^3/s (for σv)

# 95% upper limits from the paper (Table 1 and Fig. 4)
u_95 = 1e-3                   # dimensionless upper limit on u
sigma_v_limit_100 = 2.91e-25  # ⟨σv⟩ limit (cm^3/s) at M=100 GeV (from paper, Section 6)

def y_eff_from_scattering(M_GeV):
    """
    Returns the effective coupling y_eff = (y_chi^2 y_nu^2)^(1/4) that saturates
    the u_95 bound for a given DM mass M_GeV (in GeV).
    """
    # u = (σ_χν / σ_Th) * (100 GeV / M_GeV)
    # σ_χν = (y_eff^4 / (64π M_GeV^2)) * GeV2_to_cm2
    # Solve for y_eff:
    # y_eff^4 = u_95 * σ_Th * 64π M_GeV^2 / (GeV2_to_cm2 * (100 / M_GeV))
    #         = u_95 * σ_Th * 64π M_GeV^3 / (GeV2_to_cm2 * 100)
    factor = u_95 * sigma_Th * 64 * np.pi * M_GeV**3 / (GeV2_to_cm2 * 100.0)
    return factor ** 0.25

def y_eff_from_annihilation(M_GeV):
    """
    Returns the effective coupling y_eff that saturates the ⟨σv⟩ limit,
    assuming s-wave annihilation with ⟨σv⟩ ∝ 1/M^2.
    The limit at M=100 GeV is σv_limit_100.
    """
    # ⟨σv⟩ (cgs) = (y_eff^4 / (64π M_GeV^2)) * GeV2_to_cm3ps
    # For a given M, the limit scales as (100/M)^2:
    limit = sigma_v_limit_100 * (100.0 / M_GeV)**2
    # Solve for y_eff:
    # y_eff^4 = limit * 64π M_GeV^2 / GeV2_to_cm3ps
    factor = limit * 64 * np.pi * M_GeV**2 / GeV2_to_cm3ps
    return factor ** 0.25

# Mass range for plotting (0.01 GeV to 1 TeV)
M_GeV = np.logspace(-2, 3, 200)

# Compute the coupling bounds
y_scatter = y_eff_from_scattering(M_GeV)
y_annihilate = y_eff_from_annihilation(M_GeV)

# Plotting
plt.figure(figsize=(8,6))
plt.loglog(M_GeV, y_scatter, 'r-', linewidth=2, label='Scattering ($u=10^{-3}$)')
plt.loglog(M_GeV, y_annihilate, 'b--', linewidth=2, label='Annihilation ($\\langle\\sigma v\\rangle$ limit)')

# Fill excluded regions (above the curves)
plt.fill_between(M_GeV, y_scatter, 1, where=(y_scatter<1), color='red', alpha=0.2, label='Excluded by scattering')
plt.fill_between(M_GeV, y_annihilate, 1, where=(y_annihilate<1), color='blue', alpha=0.2, label='Excluded by annihilation')

plt.xlim(1e-2, 1e3)
plt.ylim(1e-8, 1e1)
plt.xlabel('DM Mass $M_\\chi$ [GeV]', fontsize=12)
plt.ylabel('Effective Coupling $y_{\\mathrm{eff}} = (y_\\chi^2 y_\\nu^2)^{1/4}$', fontsize=12)
plt.title('Neutrino Portal DM: Constraints from Planck 2018', fontsize=14)
plt.grid(True, which='both', alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()