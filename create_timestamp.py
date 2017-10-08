#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 Takuma Yagi <tyagi@iis.u-tokyo.ac.jp>
#
# Distributed under terms of the MIT license.

from __future__ import print_function

import os
import sys
import glob

if __name__ == "__main__":
    indir = sys.argv[1]
    fps = int(sys.argv[2])
    imdir_name = sys.argv[3]

    image_list = sorted(glob.glob(os.path.join(indir, imdir_name, "*.jpg")))
    out_fn = os.path.join(indir, "rgb.txt")

    f = open(out_fn, "w")
    for idx, impath in enumerate(image_list):
        timestamp = float(idx) / fps
        f.write("{:.6f} {}\n".format(timestamp, os.path.join(imdir_name, os.path.basename(impath))))

    f.close()
    print("Done.")
