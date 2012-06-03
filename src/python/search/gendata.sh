#!/bin/bash

tables="places availability ratings"

for table in ${tables}; do
    python gendata.py --table "${table}" > "data_${table}.txt"
done

