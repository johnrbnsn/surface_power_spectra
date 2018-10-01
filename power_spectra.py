'''
power_spectra.py

This file contains the necessary information to calculate the surface power spectra for a surface described by x, y, z
coordinates.  The power spectra is useful when characterizing pavement surfaces, and using this information to estimate
rubber friction coefficients.
'''

import numpy as np
import pandas as pd
import radialprofile
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

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
        self.x = np.array(x)
        self.y = np.array(y)
        self.z = np.array(z)
        # import pdb; pdb.set_trace()
        shape_x = np.shape(self.x)
        shape_y = np.shape(self.y)
        shape_z = np.shape(self.z)

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
        Z_array = topo_df.pivot('y','x','z')
        # import pdb; pdb.set_trace()

        return cls(np.unique(topo_df['x']), np.unique(topo_df['y']), Z_array)
        # F1 = np.fft.fft2(Z_array.values)
        # F2 = np.fft.fftshift(F1)
        #
        # # Calculate 2D power spectrum
        # psd2D = np.abs(F2)**2
        #
        # # Calculate azimuthly averaged 1D power spectrum
        # psd1D = radialprofile.azimuthalAverage(psd2D)

    def plot_surface(self):
        """
        Plots the surface in 3D, using MatPlotLib
        :return:
        """
        X, Y = np.meshgrid(self.x, self.y)
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(X=X, Y=Y, Z=self.z)
        plt.show()

    def imshow_surface(self):
        """
        Plots a simple 2d image of the surface with the depth show as color using MatPlotLib imshow.
        :return:
        """
        plt.imshow(self.z)
        plt.colorbar()
        plt.show()
