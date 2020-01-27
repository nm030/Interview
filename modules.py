#!/usr/bin/env python2.7
# -*- coding:UTF-8 -*-

from __future__ import division
import csv


def calculate_module_current(name, irradiance, voltage):
    raise NotImplementedError('populate this function')
    return -1  # should return a calculated value for current


def calculate_max_power_point(name, irradiance, tolerance=1e-5):
    raise NotImplementedError('populate this function')
    voltage, current = (-1, -1)
    return (voltage, current)


def read_csv(filename, field_names):
    """load a structured csv file

    Arguments:
        filename {str} -- the path to the file to be loaded
        field_names {List} -- an array of field names in the order of the
                              columns in the csv
    Returns:
        [type] -- [description]
    """
    rtn = []
    with open(filename) as f:
        reader = csv.DictReader(f, fieldnames=field_names)
        reader.next()
        for row in reader:
            rtn.append(row)

    return rtn


def convert_entry_to_float(val):
    try:
        return float(val)
    except ValueError:
        return val


def remap_parameters(params):
    """ simplify parameters for interview

    remove temperature dependence (fix at 25ºC)
    simplify  parameter names
    """

    # Solar Constants
    Q = 1.60217657e-19
    K = 1.3806488e-23
    ZERO_CELSIUS = 273.

    return {
        'name': params['name'],
        'manufacturer': params['manufacturer'],
        'i_sc': params['i_sc'],
        'a': params['i0'],
        'b': (Q / (K * (ZERO_CELSIUS + 25) * params['gamma'])),
        'r_series': params['r_series'],
        'r_parallel': params['r_parallel'],
    }


def get_parameters(name):
    """get the parameters for a solar module

    Arguments:
        name {str} -- the name of the module you'd like to load
    Returns:
        [dictionary] -- the parameters of the modules
    """
    field_names = ['manufacturer', 'name', 'power', 'i_sc', 'gamma', 'i0',
                   'r_series', 'r_parallel', 'tau']

    all_parameters = read_csv('data.csv', field_names)
    panel = next(x for x in all_parameters if x['name'] == name)

    return remap_parameters({
        key: convert_entry_to_float(val) for key, val in panel.items()
    })


if __name__ == '__main__':
    import pprint
    pprint.pprint(get_parameters('SF 150'))
