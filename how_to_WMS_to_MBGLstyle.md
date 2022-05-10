# HOW TO set up WMS in Mapbox GL style #

1. figure out what base url might have a WMS service
  - https://img.nj.gov
  
2. scour that site for a WMS url
  - https://img.nj.gov/imagerywms/Natural2015

3. grab that WMS url's capabilities as xml (could start with this and work back to 1 and 2 to gauge other metadata?)
  - https://img.nj.gov/imagerywms/Natural2015?VERSION=1.1.1&REQUEST=GetCapabilities&SERVICE=WMS&

4. set up full url query for style json source
  - tiles: https://img.nj.gov/imagerywms/Natural2015?bbox={bbox-epsg-3857}&format=image/png&service=WMS&version=1.1.1&request=GetMap&srs=EPSG:3857&transparent=true&width=256&height=256&layers=Natural2015
    - might have to be array
  - type: raster
  - tileSize: 256

5. set up layer
  - id: uuidx
  - type: raster
  - paint: {}
  - source: above uuidx of source

6. test with leafmap
  - pip install leafmap oswlib?
  - layer = leafmap.get_wms_layers(url)[i]
  - leafmap.Map().add_wms_layer(name='?', url=url, layers=layer, format='image/png', transparent=True, attribution='?')


https://mesonet.agron.iastate.edu/cgi-bin/wms/nexrad/n0r.cgi?VERSION=1.1.1&REQUEST=GetCapabilities&SERVICE=WMS&

