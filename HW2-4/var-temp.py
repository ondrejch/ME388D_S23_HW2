#!/usr/bin/env python3

import os
import numpy as np


enr = 2.0
for temp in np.linspace(300, 600, 31):
    print(f"temp = {temp}")
    deckpath = f'temp{temp:04.0f}'
    if not os.path.isdir(deckpath):
        os.mkdir(deckpath)
    os.chdir(deckpath)
    fout = open('2_4','w')
    fout.write(f'''=t-newt
SCALE Materials HW2 problem 4
v7-252
read comp
    uo2       1                                  0.10        {temp} 92235 {enr} 92238 {100-enr} end
    h2o       1 den=0.7561                       0.8999      {temp} end
    atomboh3  1     1.44 3  5000 1 8000 3 1000 3 0.0001      {temp} 5010 70 5011 30 end
end comp
read model
read parm
  prtflux=yes inners=1000  cmfd=no epsilon=1e-6 sn=2 epsinner=1e-8
end parm
read materials
  mix=1 end
end materials
read geometry
    global unit 1
    cuboid    1  0.1 -0.1 0.1 -0.1
    media 1 1 1
    boundary 1  1 1
end geometry
read bounds
    all=refl
end bounds
end model
end
''')
    os.system('qsub ../scalerun.sh')
    os.chdir("..")

