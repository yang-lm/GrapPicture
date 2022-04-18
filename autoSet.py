'''
Description: 
Author: xiaoming
Date: 2022-01-21 10:41:55
'''
import os
# 启动程序的路径
# dir = r'C:\iKanban\iKanban.exe'
gdir = os.getcwd() + '\iKanban\iKanban.exe'

#上传文件的路径
gurl = r'http://****.com/public//efficiency/Kanban/uploadImg'

guser = ""
gpassword = ""

#代码图片存放的目录
gpicture = "./picture/"

#代码中日志存放位置
glog = "./log/"

gaction=[
        {
            "productionAction":"NB\r\n生产效率\r\n看板",
            "chartAction":{"title":"P1", "auto_id":"rbtP1", "control_type":"RadioButton"},
            "pictureName" : "NBP1.png"
        },
        {
            "productionAction":"NB\r\n生产效率\r\n看板",
            "chartAction":{"title":"WarRoom","auto_id":"rbtWarRoom", "control_type":"RadioButton"},
            "pictureName" : "NBWarRoom.png"
        },
        {
            "productionAction":'DT\r\n生产效率\r\n看板',
            "chartAction":{"title":"WarRoom", "auto_id":"rbtWarRoom", "control_type":"RadioButton"},
            "pictureName" : "DTWarRoom.png",
            "overtime":3
        },
        {
            "productionAction":'DT\r\n生产效率\r\n看板',
            "chartAction":{"title":"P_WarRoom", "auto_id":"rtbP_WarRoom", "control_type":"RadioButton"},
            "pictureName" : "DTP_WarRoom.png",
            "overtime":3,
        },
        {
            "productionAction":"NB\r\n生产效率\r\n看板",
            "chartAction":{"title":"WarRoom","auto_id":"rbtWarRoom", "control_type":"RadioButton"},
            "pictureName" : "NBWarRoom.png"
        },
        {
            "productionAction":'title="SVR\r\n生产效率\r\n看板',
            "chartAction":{"title":"WarRoom", "auto_id":"rbtWarRoom", "control_type":"RadioButton"},
            "pictureName" : "SVRWarRoom.png"
        },
        {
            "productionAction":'title="SVR\r\n生产效率\r\n看板',
            "chartAction":{"title":"P_WarRoom", "auto_id":"rbtP_WarRoom", "control_type":"RadioButton"},
            "pictureName" : "SVRP_WarRoom.png"
        },
        {
            "productionAction":'OPT\r\n生产效率\r\n看板',
            "chartAction":{"title":"L1", "auto_id":"rbtL1", "control_type":"RadioButton"},
            "pictureName" : "OPTL1.png"
        },
        {
            "productionAction":'OPT\r\n生产效率\r\n看板',
            "chartAction":{"title":"L2", "auto_id":"rbtL2", "control_type":"RadioButton"},
            "pictureName" : "OPTL2.png"
        },
    ]


