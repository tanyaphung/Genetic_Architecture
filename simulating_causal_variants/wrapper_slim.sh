#!/bin/bash

for i in `seq 1 10000`; do
slim -seed ${i} -d "simnum=${i}" slim_script.txt
done
