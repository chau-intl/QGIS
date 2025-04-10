# The following has been generated automatically from src/core/qgsmaplayerserverproperties.h
QgsServerWmsDimensionProperties.PredefinedWmsDimensionName.baseClass = QgsServerWmsDimensionProperties
try:
    QgsServerMetadataUrlProperties.MetadataUrl.__attribute_docs__ = {'url': 'URL of the link', 'type': 'Link type. Suggested to use FGDC or TC211.', 'format': 'Format specification of online resource. It is strongly suggested to either use text/plain or text/xml.'}
    QgsServerMetadataUrlProperties.MetadataUrl.__annotations__ = {'url': str, 'type': str, 'format': str}
    QgsServerMetadataUrlProperties.MetadataUrl.__doc__ = """MetadataUrl structure.
MetadataUrl is a link to the detailed, standardized metadata about the data."""
except (NameError, AttributeError):
    pass
try:
    QgsServerWmsDimensionProperties.wmsDimensionDefaultDisplayLabels = staticmethod(QgsServerWmsDimensionProperties.wmsDimensionDefaultDisplayLabels)
except (NameError, AttributeError):
    pass
try:
    QgsMapLayerServerProperties.__overridden_methods__ = ['layer']
except (NameError, AttributeError):
    pass
try:
    QgsServerWmsDimensionProperties.WmsDimensionInfo.__doc__ = """Setting to define QGIS Server WMS Dimension.

.. versionadded:: 3.10"""
except (NameError, AttributeError):
    pass
