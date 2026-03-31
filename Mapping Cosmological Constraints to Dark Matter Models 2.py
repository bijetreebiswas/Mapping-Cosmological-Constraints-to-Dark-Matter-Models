# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 07:21:00 2026

@author: bijet
"""

# -*- coding: utf-8 -*-
"""
Mapping Planck 2018 constraints to a scalar DM model with dark photon mediator.
DM: complex scalar phi
Mediator: dark photon A' (vector) with couplings g_chi and g_nu.
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
sigma_v_limit_100 = 2.91e-25  # ⟨σv⟩ limit (cm^3/s) at M=100 GeV (paper, Section 6)

def g_eff_from_scattering(M_GeV):
    """
    Returns the effective coupling g_eff = g_chi * g_nu that saturates
    the u_95 bound for a given DM mass M_GeV (in GeV).
    For vector mediator, σ_χν = (g_eff^2) / (π M_GeV^2) in natural units.
    """
    # σ_χν (natural units) = g_eff^2 / (π M_GeV^2)
    # σ_χν (cgs) = σ_χν (natural) * GeV2_to_cm2
    # u = (σ_χν / σ_Th) * (100 / M_GeV)
    # Solve: u_95 = ( (g_eff^2 / (π M^2)) * GeV2_to_cm2 / σ_Th ) * (100/M)
    # => g_eff^2 = u_95 * π M^3 * σ_Th / (GeV2_to_cm2 * 100)
    factor = u_95 * np.pi * M_GeV**3 * sigma_Th / (GeV2_to_cm2 * 100.0)
    return np.sqrt(factor)

def g_eff_from_annihilation(M_GeV):
    """
    Returns the effective coupling g_eff that saturates the ⟨σv⟩ limit,
    assuming s-wave annihilation DM+DM → ν+ν via vector mediator.
    ⟨σv⟩ (natural units) = g_eff^2 / (8π M_GeV^2) * (velocity factor ≈ 1).
    The limit at M=100 GeV is σv_limit_100, and we scale as 1/M^2.
    """
    # ⟨σv⟩ (cgs) = (g_eff^2 / (8π M^2)) * GeV2_to_cm3ps
    # limit at M: σv_limit_100 * (100/M)^2
    limit = sigma_v_limit_100 * (100.0 / M_GeV)**2
    # g_eff^2 = limit * 8π M^2 / GeV2_to_cm3ps
    factor = limit * 8 * np.pi * M_GeV**2 / GeV2_to_cm3ps
    return np.sqrt(factor)

# Mass range for plotting (0.01 GeV to 1 TeV)
M_GeV = np.logspace(-2, 3, 200)

# Compute the coupling bounds
g_scatter = g_eff_from_scattering(M_GeV)
g_annihilate = g_eff_from_annihilation(M_GeV)

# Plotting
plt.figure(figsize=(8,6))
plt.loglog(M_GeV, g_scatter, 'r-', linewidth=2, label='Scattering ($u=10^{-3}$)')
plt.loglog(M_GeV, g_annihilate, 'b--', linewidth=2, label='Annihilation ($\\langle\\sigma v\\rangle$ limit)')

# Fill excluded regions (above the curves)
plt.fill_between(M_GeV, g_scatter, 1, where=(g_scatter<1), color='red', alpha=0.2, label='Excluded by scattering')
plt.fill_between(M_GeV, g_annihilate, 1, where=(g_annihilate<1), color='blue', alpha=0.2, label='Excluded by annihilation')

plt.xlim(1e-2, 1e3)
plt.ylim(1e-8, 1e1)
plt.xlabel('DM Mass $M_\\phi$ [GeV]', fontsize=12)
plt.ylabel('Effective Coupling $g_{\\mathrm{eff}} = g_\\chi g_\\nu$', fontsize=12)
plt.title('Scalar DM + Dark Photon Mediator: Constraints from Planck 2018', fontsize=14)
plt.grid(True, which='both', alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()