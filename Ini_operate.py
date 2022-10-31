from configobj import ConfigObj
import os
import datetime
import sys

class ini_operate:
    file_path = os.path.dirname(os.path.abspath(sys.argv[0])) + '\conf.ini'
    #命令集合（字典）
    order_dist = dict()
    def __init__(self):
        self.config = ConfigObj()
        #检查配置文件是否存在
        if(os.path.exists(self.file_path)):
            self.config = ConfigObj(self.file_path)
            self.order_dist = self.config.dict()
            self.config.write()
            return
        else:
            self.config.filename = self.file_path
            self.config['create_time'] = datetime.datetime.now()
            self.config.write()

    def save_region(self , c:list , r:list ,img_size_c , img_size_r):
        print(1)
        self.config = ConfigObj(self.file_path)
        self.config['image_width_c'] = img_size_c[0]
        self.config['image_height_c'] = img_size_c[1]
        self.config['image_width_r'] = img_size_r[0]
        self.config['image_height_r'] = img_size_r[1]
        for i in range(0 , len(c)):
            str1 = 'c' + '_' + str(i)
            self.config[str1] = c[i]
        for t in range(0, len(r)):
            str2 = 'r' + '_' + str(t)
            self.config[str2] = r[t]
        self.config.write()

    def get_region(self):
        self.config = ConfigObj(self.file_path)
        self.order_dist = self.config.dict()
        keys = list(self.order_dist.keys())
        size_c = [self.order_dist['image_width_c'] , self.config['image_height_c']]
        size_r = [self.order_dist['image_width_r'] , self.config['image_height_r']]
        c = list()
        r = list()
        for i in keys:
            if i[:2] == 'c_':
                c.append(self.order_dist[i])
            if i[:2] == 'r_':
                r.append(self.order_dist[i])
        return c , r ,size_c , size_r
