# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Growing
                                 A QGIS plugin
 Imaging of the growing season with Modis data.
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2022-05-09
        copyright            : (C) 2022 by Damian Dybciak
        email                : da
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load Growing class from file Growing.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .Growing import Growing
    return Growing(iface)
