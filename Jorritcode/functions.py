# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 12:31:07 2016

@author: Jorrit
"""
import matplotlib.pyplot as plt
import initial_conditions as ic
import math

def calc_distance(xp, yp, xs, ys):
    distance = math.sqrt(xp**2 + yp**2) + math.sqrt (xs**2 + ys**2)   
    return distance

def euler(xp, yp, xs, ys, vpx, vpy, vsx, vsy, dt):
  
    f = open('test', 'w')
    plt.ion()    
        
    for i in range(ic.N):
        
        distance = calc_distance(xp, yp, xs, ys)     
        
        
        if (yp != 0):
              theta = math.atan(abs(xp / yp))
        else:
              theta = math.pi / 2
         
        accpx = ic.G * ic.ms / (distance**2) * math.sin(theta)
        accpy = ic.G * ic.ms / (distance**2) * math.cos(theta)
        
        if (xp > 0):
            accpx = -accpx
    
        if (yp > 0):
            accpy = -accpy

        accsx = ic.G * ic.mp / (distance**2) * math.sin(theta)
        accsy = ic.G * ic.mp / (distance**2) * math.cos(theta)
        
        if (xs > 0):
            accsx = -accsx
            
        if (ys > 0):
            accsy = -accsy
        
#        print "theta = %f" % theta
#        print "xp = %.4g,  yp = %.4g,  xs = %.4g,  ys = %.4g" % (xp, yp, xs, ys)
#        print "vpx = %.4g, vpy = %.4g, vsx = %.4g, vsy = %.4g" % (vpx, vpy, vsx, vsy)
#        print "accpx = %.4g, accpy = %.4g, accsx = %.4g, accsy = %.4g" % (accpx, accpy, accsx, accsy)
#        print "\n"        
        
        xp = xp + vpx * dt
        yp = yp + vpy * dt
        
        xs = xs + vsx * dt
        ys = ys + vsy * dt
        
        vpx = vpx + accpx * dt
        vpy = vpy + accpy * dt
        
        vsx = vsx + accsx * dt
        vsy = vsy + accsy * dt
        
        f.write("xp = %f, yp = %f, xs = %f, ys = %f, vpx = %f, vpy = %f, vsx = %f, vsy = %f \n" % (xp, yp, xs, ys, vpx, vpy, vsx, vsy))
    
        plt.scatter(xp, yp)
        plt.draw()    
    
    f.close()    
    
    return xp, yp, xs, ys, vpx, vpy, vsx, vsy
    

    
    
euler(ic.xp, ic.yp, ic.xs, ic.ys, ic.vpx, ic.vpy, ic.vsx, ic.vsy, ic.dt)