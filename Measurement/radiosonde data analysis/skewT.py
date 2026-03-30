from contextlib import ExitStack
from matplotlib.axes import Axes
import matplotlib.axis as maxis
from matplotlib.projections import register_projection
import matplotlib.spines as mspines
import matplotlib.transforms as transforms
import matplotlib.pyplot as plt
import numpy as np
import netCDF4 as nc
from io import StringIO
from matplotlib.ticker import (MultipleLocator, NullFormatter, ScalarFormatter)

class SkewXTick(maxis.XTick):
    def draw(self, renderer):
        with ExitStack() as stack:
            for artist in [self.gridline, self.tick1line, self.tick2line, self.label1, self.label2]:
                stack.callback(artist.set_visible, artist.get_visible())
            needs_lower = transforms.interval_contains(self.axes.lower_xlim, self.get_loc())
            needs_upper = transforms.interval_contains(self.axes.upper_xlim, self.get_loc())
            self.tick1line.set_visible(self.tick1line.get_visible() and needs_lower)
            self.label1.set_visible(self.label1.get_visible() and needs_lower)
            self.tick2line.set_visible(self.tick2line.get_visible() and needs_upper)
            self.label2.set_visible(self.label2.get_visible() and needs_upper)
            super().draw(renderer)

    def get_view_interval(self):
        return self.axes.xaxis.get_view_interval()
    
class SkewXAxis(maxis.XAxis):
    def _get_tick(self, major):
        return SkewXTick(self.axes, None, major=major)

    def get_view_interval(self):
        return self.axes.upper_xlim[0], self.axes.lower_xlim[1]
    
class SkewSpine(mspines.Spine):
    def _adjust_location(self):
        pts = self._path.vertices
        if self.spine_type == 'top':
            pts[:, 0] = self.axes.upper_xlim
        else:
            pts[:, 0] = self.axes.lower_xlim


class SkewXAxes(Axes):
    name = 'skewx'

    def _init_axis(self):
        super()._init_axis()
        self.xaxis = SkewXAxis(self)
        self.spines.top.register_axis(self.xaxis)
        self.spines.bottom.register_axis(self.xaxis)

    def _gen_axes_spines(self):
        spines = {'top': SkewSpine.linear_spine(self, 'top'),
                  'bottom': mspines.Spine.linear_spine(self, 'bottom'),
                  'left': mspines.Spine.linear_spine(self, 'left'),
                  'right': mspines.Spine.linear_spine(self, 'right')}
        return spines

    def _set_lim_and_transforms(self):
        super()._set_lim_and_transforms()
        rot = 30
        self.transDataToAxes = (self.transScale + self.transLimits + transforms.Affine2D().skew_deg(rot, 0))
        self.transData = self.transDataToAxes + self.transAxes
        self._xaxis_transform = (transforms.blended_transform_factory(
            self.transScale + self.transLimits, transforms.IdentityTransform()) + transforms.Affine2D().skew_deg(rot, 0) + self.transAxes)

    @property
    def lower_xlim(self):
        return self.axes.viewLim.intervalx

    @property
    def upper_xlim(self):
        pts = [[0., 1.], [1., 1.]]
        return self.transDataToAxes.inverted().transform(pts)[:, 0]

register_projection(SkewXAxes)

vvm = '/data3/cloud/WCD2023/taiwanvvm/'
case = 'tpe20050712cln'
path = vvm+case

th, p, pibar, qv = np.loadtxt(f'{path}/fort.98',skiprows=262,max_rows=70,usecols=(2,3,4,5),unpack=True)
z = np.loadtxt(f'{path}/fort.98',skiprows=188,usecols=1,max_rows=70)
T = th*pibar - 273.15
p = p/100

rootgrp = nc.Dataset(f'{path}/archive/exp.L.Dynamic-000000.nc')
u = rootgrp.variables['u'][0][:,0,0]
v = rootgrp.variables['v'][0][:,0,0]

R = 287.0
cp = 1004.0  
P0 = 1000.0  
epsilon = 0.622
Rv = 461
Lv = 2.5e6
e0 = 6.112
T_K = T + 273.15
es = e0*np.exp(Lv/Rv*(1/273.15-1/T_K))
qs = epsilon*es/(p-es*(1-epsilon))
rh = qv/qs
r = qv/(1-qv)
the = (T_K+(Lv/cp)*r) * (P0/p) ** (R/cp)
Td = 237.7*((17.27*T)/(237.7+T)+np.log(rh/100))/(17.27-((17.27*T)/(237.7+T)+np.log(rh/100)))

import matplotlib.gridspec as gridspec

gs = gridspec.GridSpec(5, 10)
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(gs[:, :-4], projection='skewx') 

ax.semilogy(T, p, color='C3')
ax.semilogy(Td, p, color='C2')

ax.yaxis.set_major_formatter(ScalarFormatter())
ax.yaxis.set_minor_formatter(NullFormatter())
ax.set_yticks(np.linspace(100, 1000, 10))
ax.set_ylim(1050, 100)

ax.xaxis.set_major_locator(MultipleLocator(10))
ax.set_xlim(-50, 50)
ax.set_ylabel('Pressure [hPa]')
ax.set_xlabel('Temperature [°C]')
plt.grid(True)
plt.title(f'{case}', loc = 'left')
plt.title('initial profile', loc = 'right')

ax2 = fig.add_subplot(gs[:,-3:-1],sharey=ax)
ax2.plot(th,p, label=r'$\theta$')
ax2.plot(the,p, label=r'$\theta_{e}$')

dthdz = np.gradient(th, z, axis=0)
BLH_qv = z[np.argmin(dthdz)]
ax.axhline(y=p[np.argmax(dthdz)], linestyle='--', label='BLH_th')

ax2.grid()
ax2.set_xlim(280,360)
ax2.set_xlabel(r'$\theta$ [K]')
ax2.set_xticks(np.arange(280,370,20),['280','300','320','340','360'])
ax2.yaxis.tick_right()
ax2.legend()

ax_barbs = fig.add_subplot(gs[:, -4:-3], sharey=ax)
ax_barbs.barbs(np.zeros_like(p)[::40], p[::40], u[::40], v[::40])
ax_barbs.axis('off')

left, width = .45, .12
bottom, height = .57, .27
right = left + width
top = bottom + height

fig.patches.extend([plt.Rectangle((left, bottom), width, height,
                                      facecolor='none',
                                      edgecolor='black',
                                      fill=True, 
                                      color='white', 
                                      alpha=0.5, 
                                      #zorder=1000,
                                      lw=1, 
                                      transform=fig.transFigure, figure=fig)])

plt.subplots_adjust(left=0.1, right=1, top=0.9, bottom=0.1)
plt.savefig(f'initial_profile_{case}.png',dpi=300,transparent=False, facecolor='white')
plt.show()



