#!/usr/bin/env python2.7
# -*- coding:UTF-8 -*-

import unittest
import modules


class ModuleCase(unittest.TestCase):

    # @unittest.skip('nope')
    def test_1_module_operating_at_stc(self):
        '''
        Task 1: Create a (python) module with functions that describe a
        (solar) module. Load the module coefficients for the Trina TSM PA05
        from the CSV.

        This test will pass when you calculate voltage and current matching the
        correct numerical values along the (solar) module's I/V curve.
        '''

        current = modules.calculate_module_current('TSM PA05', 1000, 5)
        self.assertAlmostEquals(current, 8.345847070106313)

        current = modules.calculate_module_current('TSM PA05', 1000, 25)
        self.assertAlmostEquals(current, 8.276615347828452)

        current = modules.calculate_module_current('TSM PA05', 1000, 30)
        self.assertAlmostEquals(current, 7.981905356152154)

        current = modules.calculate_module_current('TSM PA05', 1000, 35)
        self.assertAlmostEquals(current, 3.9434722231704042)

    def test_2_optimize_module_power(self):
        '''
        Task 2:  Usually, we don't just need to understand what the potential
        output of a solar module is (e.g. the I/V curve), we want to find out
        what voltage and current the module should be operating at in order to
        produce the most power.

        Write a function that determines the voltage and current along a
        modules I/V curve that maximizes power.
        '''
        (voltage, current) = modules.calculate_max_power_point('TSM PA05', 1000)

        # numerically check that this is optimal
        v_high = voltage + 1e-5
        v_low = voltage - 1e-5

        i_high = modules.calculate_module_current('TSM PA05', 1000, v_high)
        i_low = modules.calculate_module_current('TSM PA05', 1000, v_low)

        self.assertGreater(voltage * current, v_high * i_high)
        self.assertGreater(voltage * current, v_low * i_low)


if __name__ == "__main__":
    unittest.main()
