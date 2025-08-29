#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
main.py: Main program for the Python Vehicle Simulator, which can be used
    to simulate and test guidance, navigation and control (GNC) systems.

Reference: T. I. Fossen (2021). Handbook of Marine Craft Hydrodynamics and
Motion Control. 2nd edition, John Wiley & Sons, Chichester, UK. 
URL: https://www.fossen.biz/wiley  
    
Author:     Thor I. Fossen
"""
import os
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from python_vehicle_simulator.vehicles import *
from python_vehicle_simulator.lib import *

# Simulation parameters: 
sampleTime = 0.1                # sample time [seconds]
N = 6000                  # number of samples

# 3D plot and animation parameters where bindexser = {firefox,chrome,safari,etc.}
numDataPoints = 50                  # number of 3D data points
FPS = 10                            # frames per second (animated GIF)
filename = '3D_animation.gif'       # data file for animated GIF

###############################################################################
# Vehicle constructors
###############################################################################
printSimInfo() 
"""
Call constructors without arguments to test step inputs, e.g. DSRV(), otter(), etc. 
"""
time_profile = pd.read_csv('Last_Profile.csv')
# 0.1397 is diameter of propeller in meters
# 42.95 is the constant value to find relation between rpm and speed in knots\
# val = time_profile.iloc[0,7]
# rpm_value = (42.95 * val ) / 0.1397
# rpm_value = round(rpm_value)
rpm_value = time_profile.iloc[0,2]
vehicle = remus100('depthHeadingAutopilot',time_profile.iloc[0,0],time_profile.iloc[0,1],rpm_value,time_profile.iloc[0,3],time_profile.iloc[0,4])
# vehicle = remus100('depthHeadingAutopilot',time_profile.iloc[0,0],time_profile.iloc[0,1],time_profile.iloc[0,2],time_profile.iloc[0,3],time_profile.iloc[0,4])
printVehicleinfo(vehicle, sampleTime, N)
[simTime, simData] = simulate(N, sampleTime, vehicle)

def leg(depth,yaw,legTime,calc_rpm):
    N_samples = legTime / sampleTime
    N_samples = round(N_samples)
    # speed_in_m_per_s = speed_in_knots * 0.51444  
    global simData,simTime
    vehicle.ref_z = depth
    if(abs(vehicle.ref_psi - yaw) > 180):
        vehicle.ref_psi = yaw + 360
    else:
        vehicle.ref_psi = yaw
    vehicle.ref_n = calc_rpm
    initial_state =np.array([simData[-1,0],simData[-1,1],simData[-1,2],simData[-1,3],simData[-1,4],simData[-1,5]])
    vehicle.nu = np.array([simData[-1,6],simData[-1,7],simData[-1,8],simData[-1,9],simData[-1,10],simData[-1,11]])
    vehicle.u_actual = np.array([simData[-1,15],simData[-1,16],simData[-1,17]])
    [simTime1, simData1] = simulate(N_samples, sampleTime, vehicle, simTime[-1], initial_state)
    simData =np.vstack((simData, simData1))
    simTime = np.vstack((simTime , simTime1))
###############################################################################
# Main simulation loop 
###############################################################################
def main():
    time_profile = pd.read_csv('Last_Profile.csv')
    for i in range(1,len(time_profile)):
        print(time_profile.iloc[i,8])
        # calc_rpm = (42.95 * time_profile.iloc[i,7]) / 0.1397
        # calc_rpm = round(calc_rpm)
        calc_rpm = time_profile.iloc[i,2]
        leg(time_profile.iloc[i,0],time_profile.iloc[i,1],time_profile.iloc[i,8],calc_rpm)

    final_data = np.hstack((simTime,simData))
    df = pd.DataFrame(final_data)
    # downsampled_df = df.iloc[::5]
    df.columns = ['Time(sec)', 'Position(x(m))', 'Position(y(m))', 'Position(z(m))', 'Roll(deg)', 'Pitch(deg)', 'Yaw(deg)', 'Surge_Velocity(m/s)', 'Sway_Velocity(m/s)', 'Heave_Velocity(m/s)', 'Roll_Rate(m/s)', 'Pitch_Rate(m/s)', 'Yaw_Rate(m/s)', 'Rud_angle_demand(deg)', 'Ster_angle_demand(deg)', 'RPM', 'Actu_Rud_ang(deg)', 'Act_Ster_ang(deg)', 'Act_RPM']
    df.to_csv("Trial_output.csv",index=False,mode="w")
    print("Trial_output.csv saved successfully")
    # downsampled_df.to_csv("DownSampled_LegData.csv",index=False)

    plotVehicleStates(simTime, simData, 1)
    plotControls(simTime, simData, vehicle, 2)
    plot3D(simData, numDataPoints, FPS, filename, 3)    

    plt.show()
    plt.close()
    # sys.exit(1)
main()
