'''
power_spectra.py

This file contains the necessary information to calculate the surface power spectra for a surface described by x, y, z
coordinates.  The power spectra is useful when characterizing pavement surfaces, and using this information to estimate
rubber friction coefficients.
'''

import numpy as np
import pandas as pd
import radialprofile

class PowerSpectra():

    def __init__(self, x, y, z):
        """
        Calculates the power spectra based on input arrays x, y, z.

        :param x: List (mx1) containing x values
        :param y: List (nx1) containing y values
        :param z: List (mxn) containing z values corresponding to x, y arrays.
        :return:
        """

        # Check sizing; make m, n even number
        x = np.array(x)
        y = np.array(y)
        z = np.array(z)
        # import pdb; pdb.set_trace()
        shape_x = np.shape(x)
        shape_y = np.shape(y)
        shape_z = np.shape(z)

        if (shape_x[0] != shape_z[0]) and (shape_y[0] != shape_z[1]):
            raise ValueError('The shape of x [mx1] and y [nx1] must be consistent with z[mxn]. With provided inputs'
                             'x=[{}], y={}, z={}'.format(shape_x, shape_y, shape_z))


        # Remove average tilt from the 'z' values


        # Apply windowing function to ensure periodicity at edges and reduce leakage.


        # Calculate normalization constant for 2d FFT


        # Calculate the 2d FFT and normalize based on input values


        # Take the radial average of FFT


        # Calculate wavevectors

    @classmethod
    def from_multiscale_file(cls, file_path):
        """
        Initializes a PowerSpectra object from a multiscale consulting file format
        (http://www.multiscaleconsulting.com/downloads/ROADTYPE.NX.NY.a.prefz.Height.data.1x.2y.3h)

        :param file_path:
        :return:
        """
        topo_df = pd.read_csv(file_path, skiprows=5, header=None, delim_whitespace=True, names=['x','y','z'])
        pivot = topo_df.pivot('y','x','z')
        F1 = np.fft.fft2(pivot.values)
        F2 = np.fft.fftshift(F1)

        # Calculate 2D power spectrum
        psd2D = np.abs(F2)**2

        # Calculate azimuthly averaged 1D power spectrum
        psd1D = radialprofile.azimuthalAverage(psd2D)
