'''
Test file for power_spectra.py
'''

import unittest
import power_spectra

class PowerSpectraTests(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_initialize(self):
        power_spectra.PowerSpectra([0, 1], [0, 1], [[1, 0],[0,1]])

    # def test_input_size_consisentcy(self):
    #     """
    #     Checks that the input sizing is consistent, and if not an exception is raised.
    #
    #     x = [1xm]
    #     y = [1xn]
    #     z = [mxn]
    #     :return:
    #     """
    #     x1 = range(3)
    #     y1 = range(5)
    #     z1 = [range(len(x1)), range(len(y1))]
    #
    #     power_spectra.PowerSpectra(x1, y1, z1)

    def test_from_multiscale_file(self):
        """
        Uses a multiscale consulting file to determine surface roughness.
        :return:
        """
        ps = power_spectra.PowerSpectra.from_multiscale_file(
            'http://www.multiscaleconsulting.com/downloads/ROADTYPE.NX.NY.a.prefz.Height.data.1x.2y.3h')
        ps.plot_surface()
        ps.imshow_surface()
        assert True

if __name__ == "__main__":
    unittest.main()