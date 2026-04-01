# Mapping Cosmological Constraints to Dark Matter Models

# Constraining Dark Matter–Neutrino Interactions from Planck 2018

This repository contains Python scripts that translate cosmological upper limits on dark matter (DM)–neutrino interactions into constraints on the parameter space of two well‑motivated particle physics models. The analysis is based on the results of Paul et al., *JCAP 10 (2021) 017* ([arXiv:2104.04760](https://arxiv.org/abs/2104.04760)).

## Background

In the standard $\Lambda$CDM cosmology, dark matter is assumed to be collisionless and does not interact with neutrinos. However, many extensions of the Standard Model predict DM–neutrino interactions that can leave imprints on the cosmic microwave background (CMB) and the matter power spectrum.

Using Planck 2018 data, the authors placed 95% upper limits on two parameters:

- **$u$**: a dimensionless parameter related to the DM–neutrino elastic scattering cross‑section.
- **$\langle \sigma v \rangle$**: the thermally averaged DM annihilation cross‑section into invisible species.

These limits are used here to exclude regions of parameter space for two different DM models.

---

## Model 1: Neutrino Portal (Scalar Mediator)

### Lagrangian
\[
\mathcal{L} \supset y_\chi \bar{\chi} \chi \phi + y_\nu \bar{\nu} \nu \phi
\]
- $\chi$: Dirac fermion DM particle  
- $\nu$: active neutrino (single flavour)  
- $\phi$: scalar mediator (light, $M_\phi \ll M_\chi$)

### Cross‑sections (tree level, natural units)
- **Scattering** $\chi + \nu \to \chi + \nu$:
  \[
  \sigma_{\chi\nu} = \frac{y_\chi^2 y_\nu^2}{64\pi M_\chi^2}
  \]
- **Annihilation** $\chi\bar{\chi} \to \nu\bar{\nu}$ (s‑wave, non‑relativistic):
  \[
  \langle \sigma v \rangle = \frac{y_\chi^2 y_\nu^2}{64\pi M_\chi^2}
  \]

### Mapping to cosmological parameters
The dimensionless scattering parameter $u$ is defined as
\[
u = \frac{\sigma_{\chi\nu}}{\sigma_{\mathrm{Th}}} \frac{100\ \mathrm{GeV}}{M_\chi},
\]
where $\sigma_{\mathrm{Th}}$ is the Thomson cross‑section.  
From $u < 10^{-3}$ (95% CL), we obtain a bound on the effective coupling
\[
y_{\mathrm{eff}} \equiv (y_\chi^2 y_\nu^2)^{1/4}.
\]

The annihilation cross‑section limit is taken as
\[
\langle\sigma v\rangle_{\mathrm{lim}}(M_\chi) = 2.91\times10^{-25}\,\mathrm{cm^3/s} \times \left(\frac{100\ \mathrm{GeV}}{M_\chi}\right)^{\!2}
\]

## Results

<img width="1137" height="849" alt="image" src="https://github.com/user-attachments/assets/916b02ea-2641-4d1f-a9c0-0749a3feedb5" />

(consistent with the scaling of an s‑wave process). This gives a second bound on $y_{\mathrm{eff}}$.

