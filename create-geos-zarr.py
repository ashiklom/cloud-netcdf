#!/usr/bin/env python
import xarray as xr
from dask.diagnostics import ProgressBar

dat = xr.open_mfdataset("data/geos-fp/GEOS.fp.asm.tavg1_2d_flx_Nx.20230101_*.V01.nc4")
dat2 = dat.chunk({"time": 12, "lat": 200, "lon": 200})
with ProgressBar():
    dat2.to_zarr("data/geos-fp.zarr", mode="w")
with ProgressBar():
    dat2.to_zarr("data/geos-fp.zarr", mode="w",
                 )

# Test Zarr
dzarr = xr.open_zarr("data/geos-fp.zarr")
