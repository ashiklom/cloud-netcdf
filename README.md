# Exploring NetCDF files in the cloud

## Building the library

First, install Spack.

```bash
# Create and activate a spack environment for this
spack env create cloud-netcdf
spack env activate cloud-netcdf

# Install NetCDF with the right flags (+hdf4, +dap). This step takes a *while*
spack install --add netcdf-c+hdf4+dap
```

## Try reading a remote NetCDF file

**All of the tests below fail so far when trying to do `ncdump`**.
Usually, the error is `Malformed URL` or `No such file or directory`.

NetCDF tests:

```
# From `netcdf-c source: nc_test/test_byterange.sh`
# THREDDS:
"https://thredds-test.unidata.ucar.edu/thredds/fileServer/pointData/cf_dsg/example/point.nc#mode=bytes"
"https://thredds-test.unidata.ucar.edu/thredds/fileServer/irma/metar/files/METAR_20170910_0000.nc#bytes"

# S3
"https://s3.us-east-1.amazonaws.com/noaa-goes16/ABI-L1b-RadC/2017/059/03/OR_ABI-L1b-RadC-M3C13_G16_s20170590337505_e20170590340289_c20170590340316.nc#mode=bytes"
"s3://noaa-goes16/ABI-L1b-RadC/2017/059/03/OR_ABI-L1b-RadC-M3C13_G16_s20170590337505_e20170590340289_c20170590340316.nc#mode=bytes"
# Requires auth
"s3://unidata-zarr-test-data/byterangefiles/upload3.nc#bytes"
# Requires auth
"s3://unidata-zarr-test-data/byterangefiles/upload4.nc#bytes&aws.profile=unidata"
# Test alternate URL with no specified region
"http://noaa-goes16.s3.amazonaws.com/ABI-L1b-RadF/2022/001/18/OR_ABI-L1b-RadF-M6C01_G16_s20220011800205_e20220011809513_c20220011809562.nc#mode=bytes,s3"
```

GOES ABI 17:

```
s3://noaa-goes17/ABI-L2-FDCC/2023/003/10/OR_ABI-L2-FDCC-M6_G17_s20230031056176_e20230031058549_c20230031059158.nc
```

## Try reading a remote Zarr file

The command below hangs while using a large amount of RAM (>19 GB).
This suggests that it "works", but tries to pull the entire dataset, which defeats the point.

```
ncdump -s -h https://ncsa.osn.xsede.org/Pangeo/pangeo-forge/WOA_1degree_monthly-feedstock/woa18-1deg-monthly.zarr#mode=zarr
```

## Try reading a local Zarr file

1. `download-geos-netcdf.sh` -- Download some GEOS-FP data for testing (~1.7 GB)
2. `create-geos-zarr.py` -- Convert to Zarr for testing (1.9 GB)


