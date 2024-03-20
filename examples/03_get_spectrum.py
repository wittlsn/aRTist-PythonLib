from artistlib import API
import numpy as np
from matplotlib import pyplot as plt
from xraydb import mu_elam
import re

# Install xraydb: pip install xraydb

def scrap_spectrum(artist_spectrum: str):
    spectrum_dict = artist_spectrum.split('# [degrees]} ')[1].split('{# Avg:')[0]
    spectrum_dict = spectrum_dict.replace('{', '')
    spectrum_dict = spectrum_dict.replace('}', '')
    spectrum_dict = spectrum_dict.replace('\t', ' ')
    spectrum_dict = spectrum_dict.split(' ')[:-1]
    spectrum = np.array(spectrum_dict, np.float32)
    return spectrum.reshape((-1, 2))


def get_current_artist_spcectrum(api: API) -> np.ndarray:
    return scrap_spectrum(api.rc.send('[Engine::GetSpectrum]'))


def main():
    api = API()
    current_spectrum = get_current_artist_spcectrum(api)
    energy_keV = current_spectrum[:, 0]
    photons_n = current_spectrum[:, 1]

    plt.plot(energy_keV, photons_n)
    plt.show()

    energy = np.arange(500, 120000, 10)  # energy in eV
      
    for elem in ('C', 'Cu', 'Au'):
        mu = mu_elam(elem, energy)
        plt.plot(energy, mu)
    
    plt.title('X-ray mass attenuation')
    plt.xlabel('Energy (eV)')
    plt.ylabel(r'$\mu/\rho \rm\, (cm^2/gr)$')
    plt.legend()
    plt.yscale('log')
    plt.xscale('log')
    plt.show()

if __name__ == '__main__':
    main()