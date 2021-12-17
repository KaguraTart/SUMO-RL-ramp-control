from tqdm import tqdm
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import math
from dateutil.relativedelta import relativedelta
from datetime import datetime, date
import os, sys
import  time#绘图图式
plt.rcParams['figure.figsize']=(30,10)
# plt.style.use('ggplot')
from sumolib import checkBinary
# import xml2csv

0
'''
traci提供实时交互接口
'''
if 'SUMO_HOME' in os.environ:
     tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
     sys.path.append(tools)
else:
     sys.exit("please declare environment variable 'SUMO_HOME'")
sys.path.append(r"F:/software two/sumo-1.8.0/tools/xml")
import traci

gui = True
if gui == True: 
    sumoBinary = r"F:\software two\sumo-1.8.0\bin/sumo-gui"
else:
    sumoBinary = r"F:\software two\sumo-1.8.0\bin/sumo"
sumoCmd = [sumoBinary, "-c", 
        r"F:/大学/MTFwiki\SUMO-Q_learning\SUMO-RL-ramp-control/Q-learning-control/test1.sumo.cfg",'--tripinfo-output',
        r'F:\software two\sumo-1.8.0/file1/tripinfo2.xml','--duration-log.statistics']

#全局变量
simulation_time =1200
H_0_meanspeed_list =[]
H_1_meanspeed_list =[]
H_2_meanspeed_list =[]
H_3_meanspeed_list =[]
H_4_meanspeed_list =[]
get_OOC0_list = []
get_OOC1_list = []
get_OOC2_list = []
get_OOC3_list = []
get_OOC4_list = []
get_OOCall_list = []
H_0_car_speed = 0
H_1_car_speed = 0
H_2_car_speed = 0
H_3_car_speed = 0
H_4_car_speed = 0
Actions_move =['r','G']
def build_qq_table(step, actions):
    table = pd.DataFrame(
        np.zeros((step, len(actions))),   # q_table initial values
        columns=actions,    # actions's name
    )
    return table
qq_table = build_qq_table(simulation_time,Actions_move)

def RedYellowGreen_control():
    pass

def trafficlight_control(time):
    if time % 20 > 0 and time % 20 < 10:
        ramp = 'r'  #r means red light

    else:
        ramp = 'G'  #G means green light
    return ramp

def trafficlight_control2(time):
    H_12_car_mean_speed = (H_1_meanspeed_list[time]+H_2_meanspeed_list[time])/2

    if H_12_car_mean_speed < 33:
        ramp = 'r'
        qq_table.iloc[time,0] = 1
    else:
        ramp = 'G'
        qq_table.iloc[time,1] = 1
    return ramp

T1 = 'Lane car mean speed for limit speed '
T2 = 'car mean speed of H_1 and H_2 for limit speed '
T3 = 'Lane car OCC for limit speed'
T4 = 'Lane car OCC_mean for limit speed'

control_way = 'g'
def print_lane_speed():#输出0 1 道路的平均速度
    pass
def output_lane_speed():   #输出01234道路的平均速度
    car_simple1 = []
    car_simple2 = []
    car_simple3 = []
    car_simple4 = []
    car_simple5 = []
    car_simple_1_2_mean = []
    car_index   = []
    car_speed = {'H_0':H_0_meanspeed_list,
        'H_1':H_1_meanspeed_list,'H_2':H_2_meanspeed_list,
        'H_3':H_3_meanspeed_list,'H_4':H_4_meanspeed_list}
    car_speed = pd.DataFrame(data=car_speed)

    for i in range(0,car_speed.count()[0]):
        if i % 20 == 0:
            car_simple1.append(car_speed['H_0'][i])
            car_simple2.append(car_speed['H_1'][i])
            car_simple3.append(car_speed['H_2'][i])
            car_simple4.append(car_speed['H_3'][i])
            car_simple5.append(car_speed['H_4'][i])
            car_simple_1_2_mean.append((car_speed['H_1'][i]+car_speed['H_2'][i])/2)
            car_index.append(i/60)
    car_simple_speed = {'H_0':car_simple1,'H_1':car_simple2,'H_2':car_simple3,'H_3':car_simple4,'H_4':car_simple5 }
    car_simple_speed = pd.DataFrame(data = car_simple_speed,index = car_index)
    car_simple_speed.to_csv(r'F:/大学/MTFwiki\SUMO-Q_learning\SUMO-RL-ramp-control/Q-learning-control/csv/'+T1+'.csv')
    ax = car_simple_speed[['H_0', 'H_1','H_2','H_3','H_4']].plot(fontsize =30)
    plt.title(T1,fontsize = 30)
    fig = ax.get_figure()
    plt.xlabel('time /min',fontsize = 30)
    plt.ylabel('speed km/h',fontsize = 30)
    plt.legend(fontsize = 20)
    plt.show()
    fig.savefig(r'F:/大学/MTFwiki\SUMO-Q_learning\SUMO-RL-ramp-control/Q-learning-control/img/'   + T1+'.png')
    
    bplot1 = car_simple_speed[['H_0', 'H_1','H_2','H_3','H_4']].boxplot(fontsize=30)
    
    # colors = ['pink', 'lightblue', 'lightgreen','red']
    # for patch, color in zip(bplot1['boxes'], colors):
    #     patch.set_facecolor(color)
    plt.grid(True)
    plt.xlabel('Lane name',fontsize = 30)
    plt.ylabel('speed distribution(km/h)',fontsize = 30)
    plt.title('the Lanes speed box plots for limit speed',fontsize = 35)
    plt.show()
    fig.savefig(r'F:/大学/MTFwiki\SUMO-Q_learning\SUMO-RL-ramp-control/Q-learning-control/img/'   + T1+'_box.png')
    
    car_mean_speed = {'H_1_2_mean':car_simple_1_2_mean}
    car_mean_speed = pd.DataFrame(data = car_mean_speed,index = car_index)
    ax= car_mean_speed[['H_1_2_mean']].plot(fontsize =30)
    plt.title(T2,fontsize = 30)
    fig = ax.get_figure()
    plt.xlabel('time /min',fontsize = 30)
    plt.ylabel('speed km/h',fontsize = 30)
    plt.legend(fontsize = 20)
    plt.show()
    fig.savefig(r'F:/大学/MTFwiki\SUMO-Q_learning\SUMO-RL-ramp-control/Q-learning-control/img/'   + T2+'.png')

def output_lane_OOC(): #画图
    get_OOC = {'H_0':get_OOC0_list,
        'H_1':get_OOC1_list,'H_2':get_OOC2_list,
        'H_3':get_OOC3_list,'H_4':get_OOC4_list,'H_all':get_OOCall_list}
    get_OOC = pd.DataFrame(data=get_OOC)
    car_OOC_simple1 =[]
    car_OOC_simple2 =[]
    car_OOC_simple3 =[]
    car_OOC_simple4 =[]
    car_OOC_simple5 =[]
    car_OOC_simpleall =[]
    car_OOC_index   =[]
    for i in range(0,get_OOC.count()[0]):
        if i % 20 == 0:
            car_OOC_simple1.append(get_OOC['H_0'][i])
            car_OOC_simple2.append(get_OOC['H_1'][i])
            car_OOC_simple3.append(get_OOC['H_2'][i])
            car_OOC_simple4.append(get_OOC['H_3'][i])
            car_OOC_simple5.append(get_OOC['H_4'][i])
            car_OOC_simpleall.append((get_OOC['H_0'][i]+get_OOC['H_1'][i]+get_OOC['H_2'][i])/3)
            car_OOC_index.append(i/60)
    car_simple_OOC = {'H_0':car_OOC_simple1,'H_1':car_OOC_simple2,'H_2':car_OOC_simple3,'H_3':car_OOC_simple4,'H_4':car_OOC_simple5 ,'H_all':car_OOC_simpleall}
    car_simple_OOC = pd.DataFrame(data = car_simple_OOC,index = car_OOC_index)
    car_simple_OOC.to_csv(r'F:/大学/MTFwiki\SUMO-Q_learning\SUMO-RL-ramp-control/Q-learning-control/csv/'+T3+'.csv')
    ax = car_simple_OOC[['H_0', 'H_1','H_2','H_3','H_4']].plot(fontsize =30)
    car_simple_OOC[['H_0', 'H_1','H_2','H_3','H_4']].to_csv()
    plt.title(T3,fontsize = 30)
    fig = ax.get_figure()
    plt.xlabel('time /min',fontsize = 30)
    plt.ylabel('%',fontsize = 30)
    plt.legend(fontsize = 20)
    plt.show()
    fig.savefig(r'F:/大学/MTFwiki\SUMO-Q_learning\SUMO-RL-ramp-control/Q-learning-control/img/'   +T3+ '.png')
    
    
    
    
    
    
    boxpl2= car_simple_OOC[['H_0', 'H_1','H_2','H_3','H_4']].boxplot()
    plt.grid(True)
    plt.xlabel('Lane name',fontsize = 30)
    plt.ylabel('speed distribution(km/h)',fontsize = 30)
    plt.title('the Lanes OCC box plots for limit speed',fontsize = 35)
    plt.show()
    fig.savefig(r'F:/大学/MTFwiki\SUMO-Q_learning\SUMO-RL-ramp-control/Q-learning-control/img/'   + T3+'_box.png')

    ax = car_simple_OOC[['H_all']].plot(fontsize =30)
    plt.title(T4,fontsize = 30)
    fig = ax.get_figure()
    plt.xlabel('time /min',fontsize = 30)
    plt.ylabel('%',fontsize = 30)
    plt.legend(fontsize = 20)
    plt.show()
    fig.savefig(r'F:/大学/MTFwiki\SUMO-Q_learning\SUMO-RL-ramp-control/Q-learning-control/img/'   + T4+'.png')

#traci控制
def traci_control(step_time):
    for i in range(0,5):
        traci.lane.setMaxSpeed('H_'+str(i),27.78)
    traci.lane.setMaxSpeed('C1_0',8)
    traci.lane.setMaxSpeed('C1_1',8)
    # traci.lane.setMaxSpeed('H_2',15)
    # traci.lane.setMaxSpeed('H_3',15)
    # traci.lane.setMaxSpeed('H_4',15)
    for step in range(0,step_time):
        
        H_0_meanspeed_list.append(traci.lane.getLastStepMeanSpeed('H_0')*3.6)
        H_1_meanspeed_list.append(traci.lane.getLastStepMeanSpeed('H_1')*3.6)
        H_2_meanspeed_list.append(traci.lane.getLastStepMeanSpeed('H_2')*3.6)
        H_3_meanspeed_list.append(traci.lane.getLastStepMeanSpeed('H_3')*3.6)
        H_4_meanspeed_list.append(traci.lane.getLastStepMeanSpeed('H_4')*3.6)
        get_OOC0_list.append(traci.lane.getLastStepOccupancy('H_0')*100)
        get_OOC1_list.append(traci.lane.getLastStepOccupancy('H_1')*100)
        get_OOC2_list.append(traci.lane.getLastStepOccupancy('H_2')*100)
        get_OOC3_list.append(traci.lane.getLastStepOccupancy('H_3')*100)
        get_OOC4_list.append(traci.lane.getLastStepOccupancy('H_4')*100)
        get_OOCall_list.append((traci.lane.getLastStepOccupancy('H_0')+traci.lane.getLastStepOccupancy('H_1')+
        traci.lane.getLastStepOccupancy('H_2')+traci.lane.getLastStepOccupancy('H_3')+traci.lane.getLastStepOccupancy('H_4'))/4*100)

        #仿真延迟
        # time.sleep(0.2)

        #交通信号灯控制
        traci.trafficlight.setRedYellowGreenState(traci.trafficlight.getIDList()[0], 'g'+'G')  #trafficlight_control(step)  trafficlight_control2(step)

        #步长控制
        traci.simulationStep(step +1)

        # simulation_current_time = traci.simulation.getTime()

        #目前时间
        # print('simulation time is:',simulation_current_time)

        #获取车辆ID
        all_vehicle_id = traci.vehicle.getIDList()
        #获取车辆位置
        # all_vehicle_position = traci.vehicle.getPosition(step)
        #获取车辆是否经过车线

        try :# 获取截屏方法
            pass
            # 获取截屏
            # traci.gui.screenshot('View #0',r'F:\software two\sumo-1.8.0/file1/img/img{}.jpg'.format(step),-1,-1)
            # try:
            #     if traci.inductionloop.getLastStepVehicleNumber() > 0:
            #         traci.trafficlight.setRedYellowGreenState("0", "GGGGG")
            # except:
            #     traci.close()
            #     break
        except :
            pass


        # print(H_0_meanspeed)
    traci.close(wait=True)



'''
trafficlight_ID_list = traci.trafficlight.getIDList()
RedYellowGreenState = traci.trafficlight.getRedYellowGreenState(trafficlight_ID_list[0])
# print(trafficlight_ID_list[0],RedYellowGreenState)

# Lane_car_ID = traci.lanearea.getIDList()
# print(Lane_car_ID)

lane_ID = traci.lane.getIDList()
'''

'''
主函数
'''

if __name__ == "__main__":
 #运行sumo
    traci.start(sumoCmd)
    # traci.gui.setSchema('View #0','cus')  #改变GUI为真实车辆

    traci_control(simulation_time)
    
    output_lane_speed()
    output_lane_OOC()
    print(qq_table)
    qq_table.to_excel(r'F:\software two\sumo-1.8.0/file1/img/'+'qqtable.xlsx',index=False)

    # ax= qq_table[['r']].plot(fontsize =30)
    # plt.title('qq_table ',fontsize = 30)
    # fig = ax.get_figure()
    # plt.xlabel('time',fontsize = 30)
    # plt.ylabel(' ',fontsize = 30)
    # plt.show()
    # fig.savefig(r'F:\software two\sumo-1.8.0/file1/img/'   + 'qqtable.png')
