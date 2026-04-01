
---

### README2.md


# Dark Photon Mediator Dark Matter Model: Constraints from Planck 2018

This Python script translates cosmological upper limits on dark matter (DM)–neutrino interactions into constraints on the parameter space of the **dark photon mediator model** (vector mediator). The analysis is based on the results of Paul et al., *JCAP 10 (2021) 017* ([arXiv:2104.04760](https://arxiv.org/abs/2104.04760)).

## Background

In the standard $\Lambda$CDM cosmology, dark matter is assumed to be collisionless and does not interact with neutrinos. However, many extensions of the Standard Model predict DM–neutrino interactions that can leave imprints on the cosmic microwave background (CMB) and the matter power spectrum.

Using Planck 2018 data, the authors placed 95% upper limits on two parameters:

- **$u$**: a dimensionless parameter related to the DM–neutrino elastic scattering cross‑section.
- **$\langle \sigma v \rangle$**: the thermally averaged DM annihilation cross‑section into invisible species.

These limits are used here to exclude regions of parameter space for the dark photon (light vector mediator) model.

---

## Model Description: Dark Photon Mediator (Vector / Light Mediator)

### Lagrangian
\[
\mathcal{L} \supset g_\chi \phi^* \phi A'_\mu + g_\nu \bar{\nu} \gamma^\mu \nu A'_\mu
\]
- $\phi$: complex scalar DM particle  
- $\nu$: active neutrino  
- $A'$: light dark photon mediator ($M_{A'} \ll M_\phi$)

### Cross‑sections (tree level, natural units)
- **Scattering** $\phi + \nu \to \phi + \nu$:
  \[
  \sigma_{\phi\nu} = \frac{g_\chi^2 g_\nu^2}{\pi M_\phi^2}
  \]
- **Annihilation** $\phi\phi^* \to \nu\bar{\nu}$ (s‑wave):
  \[
  \langle \sigma v \rangle = \frac{g_\chi^2 g_\nu^2}{8\pi M_\phi^2}
  \]

### Mapping
Using the same $u$ parameter and annihilation limit, we constrain the effective coupling
\[
g_{\mathrm{eff}} \equiv g_\chi g_\nu.
\]

---

### Requirements


- Python 3.6+
- NumPy
- Matplotlib

## Results

<img width="1137" height="849" alt="image" src="https://github.com/user-attachments/assets/0e504567-430b-4650-83e7-ad4c92406f12" />
