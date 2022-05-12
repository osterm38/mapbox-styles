# mapbox-styles

This repo is meant to help me figure out how to:
- get kepler.gl maps rendering WMS/WMST tiles
  - this amounts to finding a url's WMS specs
  - then shoving this into a Mapbox GL spec json
  - then hosting this json
  - pointing kepler to this hosted file
- get kepler.gl to load locally served Mapbox GL spec json
  - this amounts to altering python's http.server to serve back a CORS-based header
  - running forever this server serving a directory with the desired file
  - pointing kepler to this hosted file
- get leafmap to render similar WMS/WMST tiles
  - leafmap.leafmap does fine
  - leafmap.kepler will now do this thanks to above solution
- get unfolded ai to do same as kepler (should by fact that kepler is backbone)
- show examples to pull from for each map type in jupyter notebooks