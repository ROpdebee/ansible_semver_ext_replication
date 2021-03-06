import seaborn as sns; 
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
from matplotlib import gridspec
import scipy
import numpy as np
import time
from matplotlib.ticker import MultipleLocator
style.use('ggplot')
sns.set_style('ticks',{'legend.frameon':True} )
sns.set_palette('colorblind')
FIG_SIZE = (12, 3)
font = {'family' : 'Times New Roman',
        'weight' : 'bold',
        'size'   : 16}
plt.rc('font', **font)
plt.rcParams['text.usetex'] = True

Set1 = sns.color_palette('Set1', n_colors=12)

PALETTE_BASE = sns.color_palette('muted', n_colors=12)
blue=PALETTE_BASE[0]
green=PALETTE_BASE[1] 
red=PALETTE_BASE[2] 
purple=PALETTE_BASE[3]
flatui = [sns.xkcd_rgb["medium green"], "orange", sns.xkcd_rgb["medium purple"], "#e74c3c", "#34495e", "#2ecc71"]
colors = {'Alpine': 'green',
         'Debian': blue,
         'node': PALETTE_BASE[-4],
          'python': PALETTE_BASE[-1],
          'ruby': PALETTE_BASE[-6],
          'major': 'red',
          'minor': flatui[1],
          'patch': blue,
	  'up-to-date': flatui[0],
          'green':green,
         }
# Considered period for the analysis
first_date="2016-06-10"
last_date="2019-12-11"
date_period = pd.to_datetime(first_date), pd.to_datetime(last_date)

plt.rcParams['pdf.fonttype'] = plt.rcParams['ps.fonttype']
plt.rcParams['text.latex.preamble'] = [r'\usepackage{amsmath,amssymb,amsfonts} '
                                       +r'\newcommand{\func}[1]{\mathsf{#1}} '
                                       +r'\newcommand{\alphalag}[1]{\func{#1\text{-}lag}} '
                                       +r'\newcommand{\pkglag}{\alphalag{pkg}} '
                                       +r'\newcommand{\timelag}{\alphalag{time}} '
                                       +r'\newcommand{\versionlag}{\alphalag{vers}} '
                                       +r'\newcommand{\vulnlag}{\alphalag{vuln}} '
                                       +r'\newcommand{\buglag}{\alphalag{bug}} ']
