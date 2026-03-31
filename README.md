# Mapping Cosmological Constraints to Dark Matter Models

This repository contains two Python scripts that translate the 95% upper limits on dark matter–neutrino interactions (from Planck 2018 CMB data) into constraints on the parameter space of two different particle physics models.  
The analysis is based on the results of Paul et al., *JCAP 10 (2021) 017* [arXiv:2104.04760].

## Background

In the standard $\Lambda$CDM cosmology, dark matter (DM) is assumed to be collisionless and non‑interacting with neutrinos. However, many particle physics models predict DM interactions with neutrinos, which can affect the cosmic microwave background (CMB) and the matter power spectrum.  
The Planck 2018 dataset sets upper limits on two parameters that characterize such interactions:

- **$u$**: a dimensionless parameter related to the DM–neutrino elastic scattering cross‑section.  
- **$\langle \sigma v \rangle$**: the thermally averaged DM annihilation cross‑section into invisible species (sterile neutrinos or light mediators).

Using these limits, we map them to two well‑motivated DM models.

---

## Model 1: Neutrino Portal (Scalar Mediator)

### Lagrangian
\[
\mathcal{L} \supset y_\chi \bar{\chi} \chi \phi + y_\nu \bar{\nu} \nu \phi
\]
where  
- $\chi$ is a Dirac fermion DM particle,  
- $\nu$ is an active neutrino (treated as a single flavour),  
- $\phi$ is a scalar mediator.

### Cross‑sections (tree level, $M_\phi \ll M_\chi$)

- **Scattering** $\chi + \nu \to \chi + \nu$:
  \[
  \sigma_{\chi\nu} = \frac{y_\chi^2 y_\nu^2}{64\pi M_\chi^2} \quad (\text{natural units})
  \]

- **Annihilation** $\chi\bar{\chi} \to \nu\bar{\nu}$:
  \[
  \langle \sigma v \rangle = \frac{y_\chi^2 y_\nu^2}{64\pi M_\chi^2} \quad (\text{s-wave, non‑relativistic})
  \]

### Mapping

The dimensionless scattering parameter $u$ is defined as
\[
u = \frac{\sigma_{\chi\nu}}{\sigma_{\mathrm{Th}}} \frac{100\ \mathrm{GeV}}{M_\chi},
\]
where $\sigma_{\mathrm{Th}}$ is the Thomson cross‑section.

The Planck 95% limit $u < 10^{-3}$ translates to an upper bound on the effective coupling
\[
y_{\mathrm{eff}} \equiv (y_\chi^2 y_\nu^2)^{1/4}.
\]

The annihilation cross‑section limit $\langle\sigma v\rangle_{\mathrm{lim}}(M_\chi) = 2.91\times10^{-25}\,\mathrm{cm^3/s} \times (100\ \mathrm{GeV}/M_\chi)^2$ (from the paper) gives another bound on $y_{\mathrm{eff}}$.

### Code: `neutrino_portal.py`

The script computes $y_{\mathrm{eff}}$ from both scattering and annihilation and produces a log‑log plot showing the excluded regions.

**Run**
```bash
Mapping Cosmological Constraints to Dark Matter Models.py
