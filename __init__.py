# -*- coding: utf-8 -*-
"""
/***************************************************************************
 WKTLayer
                                 A QGIS plugin
 Inserir um wkt 
                             -------------------
        begin                : 2018-04-16
        copyright            : (C) 2018 by Tiago
        email                : tinorberto@yahoo.com.br
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
    """Load WKTLayer class from file WKTLayer.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .wktlayer import WKTLayer
    return WKTLayer(iface)
