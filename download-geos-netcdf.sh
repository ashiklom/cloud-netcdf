#!/usr/bin/env bash

TO_DIR="data/geos-fp"
mkdir -p "$TO_DIR"
for s in $(seq -f '%02.0f' 0 23); do
  FNAME='https://portal.nccs.nasa.gov/datashare/gmao/geos-fp/das/Y2023/M01/D01/GEOS.fp.asm.tavg1_2d_flx_Nx.20230101_'"$s"'30.V01.nc4'
  wget --directory-prefix="$TO_DIR" "$FNAME"
done
