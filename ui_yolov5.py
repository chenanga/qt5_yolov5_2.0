#!/usr/bin/env python                                
# -*- coding:utf-8 -*-                           
# @author   : ChenAng                                    
# @file     : ui_yolov5.py
# @Time     : 2021/8/27 10:13

import time
import os
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import *
import cv2
import sys
from PyQt5.QtWidgets import *
# from detect_qt5 import main_detect,my_lodelmodel
from detect_qt5 import v5detect

'''摄像头和视频实时检测界面'''
class Ui_MainWindow(QWidget):
    def __init__(self, parent=None):
        super(Ui_MainWindow, self).__init__(parent)

        # self.face_recong = face.Recognition()
        self.timer_camera1 = QtCore.QTimer()
        self.timer_camera2 = QtCore.QTimer()
        self.timer_camera3 = QtCore.QTimer()
        self.timer_camera4 = QtCore.QTimer()
        self.cap = cv2.VideoCapture()

        self.CAM_NUM = 0

        # self.slot_init()
        self.__flag_work = 0
        self.x = 0
        self.count = 0
        self.setWindowTitle("yolov5检测")
        self.setWindowIcon(QIcon(os.getcwd() + '\\data\\source_image\\Detective.ico'))
        # self.resize(300, 150)  # 宽×高
        window_pale = QtGui.QPalette()
        window_pale.setBrush(self.backgroundRole(), QtGui.QBrush(
            QtGui.QPixmap(os.getcwd() + '\\data\\source_image\\backgroud.jpg')))
        self.setPalette(window_pale)
        self.setFixedSize(1600, 900)
        # self.my_model = my_lodelmodel()
        self.myv5 = v5detect()
        self.button_open_camera = QPushButton(self)
        self.button_open_camera.setText(u'打开摄像头')
        self.button_open_camera.setStyleSheet(''' 
                                     QPushButton
                                     {text-align : center;
                                     background-color : white;
                                     font: bold;
                                     border-color: gray;
                                     border-width: 2px;
                                     border-radius: 10px;
                                     padding: 6px;
                                     height : 14px;
                                     border-style: outset;
                                     font : 14px;}
                                     QPushButton:pressed
                                     {text-align : center;
                                     background-color : light gray;
                                     font: bold;
                                     border-color: gray;
                                     border-width: 2px;
                                     border-radius: 10px;
                                     padding: 6px;
                                     height : 14px;
                                     border-style: outset;
                                     font : 14px;}
                                     ''')
        self.button_open_camera.move(10, 40)
        self.button_open_camera.clicked.connect(self.button_open_camera_click)
        #self.button_open_camera.clicked.connect(self.button_open_camera_click1)
        # btn.clicked.connect(self.openimage)

        self.btn1 = QPushButton(self)
        self.btn1.setText("检测摄像头")
        self.btn1.setStyleSheet(''' 
                                             QPushButton
                                             {text-align : center;
                                             background-color : white;
                                             font: bold;
                                             border-color: gray;
                                             border-width: 2px;
                                             border-radius: 10px;
                                             padding: 6px;
                                             height : 14px;
                                             border-style: outset;
                                             font : 14px;}
                                             QPushButton:pressed
                                             {text-align : center;
                                             background-color : light gray;
                                             font: bold;
                                             border-color: gray;
                                             border-width: 2px;
                                             border-radius: 10px;
                                             padding: 6px;
                                             height : 14px;
                                             border-style: outset;
                                             font : 14px;}
                                             ''')
        self.btn1.move(10, 80)
        self.btn1.clicked.connect(self.button_open_camera_click1)
        # print("QPushButton构建")



        self.open_video = QPushButton(self)
        self.open_video.setText("打开视频")
        self.open_video.setStyleSheet(''' 
                                             QPushButton
                                             {text-align : center;
                                             background-color : white;
                                             font: bold;
                                             border-color: gray;
                                             border-width: 2px;
                                             border-radius: 10px;
                                             padding: 6px;
                                             height : 14px;
                                             border-style: outset;
                                             font : 14px;}
                                             QPushButton:pressed
                                             {text-align : center;
                                             background-color : light gray;
                                             font: bold;
                                             border-color: gray;
                                             border-width: 2px;
                                             border-radius: 10px;
                                             padding: 6px;
                                             height : 14px;
                                             border-style: outset;
                                             font : 14px;}
                                             ''')
        self.open_video.move(10, 160)
        self.open_video.clicked.connect(self.open_video_button)
        print("QPushButton构建")

        self.btn1 = QPushButton(self)
        self.btn1.setText("检测视频文件")
        self.btn1.setStyleSheet(''' 
                                             QPushButton
                                             {text-align : center;
                                             background-color : white;
                                             font: bold;
                                             border-color: gray;
                                             border-width: 2px;
                                             border-radius: 10px;
                                             padding: 6px;
                                             height : 14px;
                                             border-style: outset;
                                             font : 14px;}
                                             QPushButton:pressed
                                             {text-align : center;
                                             background-color : light gray;
                                             font: bold;
                                             border-color: gray;
                                             border-width: 2px;
                                             border-radius: 10px;
                                             padding: 6px;
                                             height : 14px;
                                             border-style: outset;
                                             font : 14px;}
                                             ''')
        self.btn1.move(10, 200)
        self.btn1.clicked.connect(self.detect_video)
        print("QPushButton构建")

        # btn1.clicked.connect(self.detect())
        # btn1.clicked.connect(self.button1_test)


        #btn1.clicked.connect(self.detect())
        # btn1.clicked.connect(self.button1_test)

        btn2 = QPushButton(self)
        btn2.setText("返回上一界面")
        btn2.setStyleSheet(''' 
                                             QPushButton
                                             {text-align : center;
                                             background-color : white;
                                             font: bold;
                                             border-color: gray;
                                             border-width: 2px;
                                             border-radius: 10px;
                                             padding: 6px;
                                             height : 14px;
                                             border-style: outset;
                                             font : 14px;}
                                             QPushButton:pressed
                                             {text-align : center;
                                             background-color : light gray;
                                             font: bold;
                                             border-color: gray;
                                             border-width: 2px;
                                             border-radius: 10px;
                                             padding: 6px;
                                             height : 14px;
                                             border-style: outset;
                                             font : 14px;}
                                             ''')
        btn2.move(10, 240)
        btn2.clicked.connect(self.back_lastui)


        # 信息显示
        self.label_show_camera = QLabel(self)
        self.label_move = QLabel()
        self.label_move.setFixedSize(100, 100)
        # self.label_move.setText(" 11  待检测图片")
        self.label_show_camera.setFixedSize(700, 500)
        self.label_show_camera.setAutoFillBackground(True)
        self.label_show_camera.move(110,80)
        self.label_show_camera.setStyleSheet("QLabel{background:#F5F5DC;}"
                                  "QLabel{color:rgb(300,300,300,120);font-size:10px;font-weight:bold;font-family:宋体;}"
                                  )
        self.label_show_camera1 = QLabel(self)
        self.label_show_camera1.setFixedSize(700, 500)
        self.label_show_camera1.setAutoFillBackground(True)
        self.label_show_camera1.move(850, 80)
        self.label_show_camera1.setStyleSheet("QLabel{background:#F5F5DC;}"
                                             "QLabel{color:rgb(300,300,300,120);font-size:10px;font-weight:bold;font-family:宋体;}"
                                             )

        self.timer_camera1.timeout.connect(self.show_camera)
        self.timer_camera2.timeout.connect(self.show_camera1)
        # self.timer_camera3.timeout.connect(self.show_camera2)
        self.timer_camera4.timeout.connect(self.show_camera2)
        self.timer_camera4.timeout.connect(self.show_camera3)
        self.clicked = False

        # self.setWindowTitle(u'摄像头')
        self.frame_s=3
        '''
        # 设置背景图片
        palette1 = QPalette()
        palette1.setBrush(self.backgroundRole(), QBrush(QPixmap('background.jpg')))
        self.setPalette(palette1)
        '''






    def back_lastui(self):
        self.timer_camera1.stop()
        self.cap.release()
        self.label_show_camera.clear()
        self.timer_camera2.stop()

        self.label_show_camera1.clear()
        cam_t.close()
        ui_p.show()

    '''摄像头'''
    def button_open_camera_click(self):
        if self.timer_camera1.isActive() == False:
            flag = self.cap.open(self.CAM_NUM)
            if flag == False:
                msg = QtWidgets.QMessageBox.warning(self, u"Warning", u"请检测相机与电脑是否连接正确",
                                                    buttons=QtWidgets.QMessageBox.Ok,
                                                    defaultButton=QtWidgets.QMessageBox.Ok)

            else:
                self.timer_camera1.start(30)

                self.button_open_camera.setText(u'关闭摄像头')
        else:
            self.timer_camera1.stop()
            self.cap.release()
            self.label_show_camera.clear()
            self.timer_camera2.stop()

            self.label_show_camera1.clear()
            self.button_open_camera.setText(u'打开摄像头')


    def show_camera(self):  #摄像头左边
        flag, self.image = self.cap.read()

        dir_path=os.getcwd()
        camera_source =dir_path+ "\\data\\test\\2.jpg"
        cv2.imwrite(camera_source, self.image)


        width = self.image.shape[1]
        height = self.image.shape[0]

        # 设置新的图片分辨率框架
        width_new = 700
        height_new = 500

        # 判断图片的长宽比率
        if width / height >= width_new / height_new:

            show = cv2.resize(self.image, (width_new, int(height * width_new / width)))
        else:

            show = cv2.resize(self.image, (int(width * height_new / height), height_new))

        show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)


        showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0],3 * show.shape[1], QtGui.QImage.Format_RGB888)


        self.label_show_camera.setPixmap(QtGui.QPixmap.fromImage(showImage))

    def button_open_camera_click1(self):
        if self.timer_camera2.isActive() == False:
            flag = self.cap.open(self.CAM_NUM)
            if flag == False:
                msg = QtWidgets.QMessageBox.warning(self, u"Warning", u"请检测相机与电脑是否连接正确",
                                                    buttons=QtWidgets.QMessageBox.Ok,
                                                    defaultButton=QtWidgets.QMessageBox.Ok)

            else:
                self.timer_camera2.start(30)
                self.button_open_camera.setText(u'关闭摄像头')
        else:
            self.timer_camera2.stop()
            self.cap.release()
            self.label_show_camera1.clear()
            self.button_open_camera.setText(u'打开摄像头')

    def show_camera1(self):
        flag, self.image = self.cap.read()


        # dir_path = os.getcwd()
        # camera_source = dir_path + "\\data\\test\\2.jpg"
        #
        # cv2.imwrite(camera_source, self.image)

        # im0, label = main_detect(self.my_model, camera_source)
        label, im0 = self.myv5.detect(self.image)

        if label=='debug':
            print("labelkong")

        width = im0.shape[1]
        height = im0.shape[0]

        # 设置新的图片分辨率框架
        width_new = 700
        height_new = 500

        # 判断图片的长宽比率
        if width / height >= width_new / height_new:

            show = cv2.resize(im0, (width_new, int(height * width_new / width)))
        else:

            show = cv2.resize(im0, (int(width * height_new / height), height_new))
        im0 = cv2.cvtColor(show, cv2.COLOR_RGB2BGR)
        # print("debug2")

        showImage = QtGui.QImage(im0, im0.shape[1], im0.shape[0], 3 * im0.shape[1], QtGui.QImage.Format_RGB888)

        self.label_show_camera1.setPixmap(QtGui.QPixmap.fromImage(showImage))


    '''视频检测'''
    def open_video_button(self):


        if self.timer_camera4.isActive() == False:

            imgName, imgType = QFileDialog.getOpenFileName(self, "打开视频", "", "*.mp4;;*.AVI;;*.rmvb;;All Files(*)")

            self.cap_video = cv2.VideoCapture(imgName)

            flag = self.cap_video.isOpened()

            if flag == False:
                msg = QtWidgets.QMessageBox.warning(self, u"Warning", u"请检测相机与电脑是否连接正确",
                                                    buttons=QtWidgets.QMessageBox.Ok,
                                                    defaultButton=QtWidgets.QMessageBox.Ok)
       
            else:

                # self.timer_camera3.start(10)
                self.show_camera2()
                self.open_video.setText(u'关闭视频')
        else:
            # self.timer_camera3.stop()
            self.cap_video.release()
            self.label_show_camera.clear()
            self.timer_camera4.stop()
            self.frame_s=3
            self.label_show_camera1.clear()
            self.open_video.setText(u'打开视频')


    def detect_video(self):

        if self.timer_camera4.isActive() == False:
            flag = self.cap_video.isOpened()
            if flag == False:
                msg = QtWidgets.QMessageBox.warning(self, u"Warning", u"请检测相机与电脑是否连接正确",
                                                    buttons=QtWidgets.QMessageBox.Ok,
                                                    defaultButton=QtWidgets.QMessageBox.Ok)

            else:
                self.timer_camera4.start(30)

        else:
            self.timer_camera4.stop()
            self.cap_video.release()
            self.label_show_camera1.clear()




    def show_camera2(self):     #显示视频的左边

                  #抽帧
        length = int(self.cap_video.get(cv2.CAP_PROP_FRAME_COUNT))   #抽帧
        print(self.frame_s,length) #抽帧
        flag, self.image1 = self.cap_video.read()   #image1是视频的
        if flag == True:


            width=self.image1.shape[1]
            height=self.image1.shape[0]

            # 设置新的图片分辨率框架
            width_new = 700
            height_new = 500

            # 判断图片的长宽比率
            if width / height >= width_new / height_new:

                show = cv2.resize(self.image1, (width_new, int(height * width_new / width)))
            else:

                show = cv2.resize(self.image1, (int(width * height_new / height), height_new))


            show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)


            showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0],3 * show.shape[1], QtGui.QImage.Format_RGB888)


            self.label_show_camera.setPixmap(QtGui.QPixmap.fromImage(showImage))
        else:
            self.cap_video.release()
            self.label_show_camera.clear()
            self.timer_camera4.stop()

            self.label_show_camera1.clear()
            self.open_video.setText(u'打开视频')

    def show_camera3(self):

        flag, self.image1 = self.cap_video.read()
        self.frame_s += 1
        if flag==True:
            # if self.frame_s % 3 == 0:   #抽帧
                # face = self.face_detect.align(self.image)
                # if face:
                #     pass

            # dir_path = os.getcwd()
            # camera_source = dir_path + "\\data\\test\\video.jpg"
            #
            # cv2.imwrite(camera_source, self.image1)
            # print("im01")
            # im0, label = main_detect(self.my_model, camera_source)
            label, im0  = self.myv5.detect(self.image1)
            # print("imo",im0)
            # print(label)
            if label=='debug':
                print("labelkong")
            # print("debug")

            # im0, label = slef.detect()
            # print("debug1")
            width = im0.shape[1]
            height = im0.shape[0]

            # 设置新的图片分辨率框架
            width_new = 700
            height_new = 500

            # 判断图片的长宽比率
            if width / height >= width_new / height_new:

                show = cv2.resize(im0, (width_new, int(height * width_new / width)))
            else:

                show = cv2.resize(im0, (int(width * height_new / height), height_new))

            im0 = cv2.cvtColor(show, cv2.COLOR_RGB2BGR)
            # print("debug2")

            showImage = QtGui.QImage(im0, im0.shape[1], im0.shape[0], 3 * im0.shape[1], QtGui.QImage.Format_RGB888)

            self.label_show_camera1.setPixmap(QtGui.QPixmap.fromImage(showImage))

'''单张图片检测'''
class picture(QWidget):

    def __init__(self):
        super(picture, self).__init__()

        self.str_name = '0'


        self.myv5 = v5detect()

        # self.my_model=my_lodelmodel()
        self.resize(1600, 900)
        self.setWindowIcon(QIcon(os.getcwd() + '\\data\\source_image\\Detective.ico'))
        self.setWindowTitle("yolov5目标检测平台")



        window_pale = QtGui.QPalette()
        window_pale.setBrush(self.backgroundRole(), QtGui.QBrush(
            QtGui.QPixmap(os.getcwd() + '\\data\\source_image\\backgroud.jpg')))
        self.setPalette(window_pale)


        camera_or_video_save_path = 'data\\test'
        if not os.path.exists(camera_or_video_save_path):
            os.makedirs(camera_or_video_save_path)

        self.label1 = QLabel(self)
        self.label1.setText("   待检测图片")
        self.label1.setFixedSize(700, 500)
        self.label1.move(110, 80)

        self.label1.setStyleSheet("QLabel{background:#7A6969;}"
                                  "QLabel{color:rgb(300,300,300,120);font-size:20px;font-weight:bold;font-family:宋体;}"
                                  )
        self.label2 = QLabel(self)
        self.label2.setText("   检测结果")
        self.label2.setFixedSize(700, 500)
        self.label2.move(850, 80)

        self.label2.setStyleSheet("QLabel{background:#7A6969;}"
                                  "QLabel{color:rgb(300,300,300,120);font-size:20px;font-weight:bold;font-family:宋体;}"
                                  )

        self.label3 = QLabel(self)
        self.label3.setText("")
        self.label3.move(1200, 620)
        self.label3.setStyleSheet("font-size:20px;")
        self.label3.adjustSize()



        btn = QPushButton(self)
        btn.setText("打开图片")
        btn.setStyleSheet(''' 
                                                     QPushButton
                                                     {text-align : center;
                                                     background-color : white;
                                                     font: bold;
                                                     border-color: gray;
                                                     border-width: 2px;
                                                     border-radius: 10px;
                                                     padding: 6px;
                                                     height : 14px;
                                                     border-style: outset;
                                                     font : 14px;}
                                                     QPushButton:pressed
                                                     {text-align : center;
                                                     background-color : light gray;
                                                     font: bold;
                                                     border-color: gray;
                                                     border-width: 2px;
                                                     border-radius: 10px;
                                                     padding: 6px;
                                                     height : 14px;
                                                     border-style: outset;
                                                     font : 14px;}
                                                     ''')
        btn.move(10, 30)
        btn.clicked.connect(self.openimage)

        btn1 = QPushButton(self)
        btn1.setText("检测图片")
        btn1.setStyleSheet(''' 
                                                     QPushButton
                                                     {text-align : center;
                                                     background-color : white;
                                                     font: bold;
                                                     border-color: gray;
                                                     border-width: 2px;
                                                     border-radius: 10px;
                                                     padding: 6px;
                                                     height : 14px;
                                                     border-style: outset;
                                                     font : 14px;}
                                                     QPushButton:pressed
                                                     {text-align : center;
                                                     background-color : light gray;
                                                     font: bold;
                                                     border-color: gray;
                                                     border-width: 2px;
                                                     border-radius: 10px;
                                                     padding: 6px;
                                                     height : 14px;
                                                     border-style: outset;
                                                     font : 14px;}
                                                     ''')
        btn1.move(10, 80)
        # print("QPushButton构建")
        btn1.clicked.connect(self.button1_test)




        btn3 = QPushButton(self)
        btn3.setText("视频和摄像头检测")
        btn3.setStyleSheet(''' 
                                                     QPushButton
                                                     {text-align : center;
                                                     background-color : white;
                                                     font: bold;
                                                     border-color: gray;
                                                     border-width: 2px;
                                                     border-radius: 10px;
                                                     padding: 6px;
                                                     height : 14px;
                                                     border-style: outset;
                                                     font : 14px;}
                                                     QPushButton:pressed
                                                     {text-align : center;
                                                     background-color : light gray;
                                                     font: bold;
                                                     border-color: gray;
                                                     border-width: 2px;
                                                     border-radius: 10px;
                                                     padding: 6px;
                                                     height : 14px;
                                                     border-style: outset;
                                                     font : 14px;}
                                                     ''')
        btn3.move(10, 160)
        btn3.clicked.connect(self.camera_find)

        self.imgname1='0'


    def camera_find(self):
        ui_p.close()
        cam_t.show()


    def openimage(self):

        imgName, imgType = QFileDialog.getOpenFileName(self, "打开图片", "", "*.jpg;;*.png;;All Files(*)")

        if imgName!='':
            self.imgname1=imgName
            # print("imgName",imgName,type(imgName))
            self.im0=cv2.imread(imgName)

            width = self.im0.shape[1]
            height = self.im0.shape[0]

            # 设置新的图片分辨率框架
            width_new = 700
            height_new = 500

            # 判断图片的长宽比率
            if width / height >= width_new / height_new:

                show = cv2.resize(self.im0, (width_new, int(height * width_new / width)))
            else:

                show = cv2.resize(self.im0, (int(width * height_new / height), height_new))

            im0 = cv2.cvtColor(show, cv2.COLOR_RGB2BGR)
            showImage = QtGui.QImage(im0, im0.shape[1], im0.shape[0], 3 * im0.shape[1], QtGui.QImage.Format_RGB888)
            self.label1.setPixmap(QtGui.QPixmap.fromImage(showImage))

            # jpg = QtGui.QPixmap(imgName).scaled(self.label1.width(), self.label1.height())
            # self.label1.setPixmap(jpg)


    def button1_test(self):



        if self.imgname1!='0':
            QApplication.processEvents()
            label, im0 = self.myv5.detect(self.im0)

            QApplication.processEvents()

            width = im0.shape[1]
            height = im0.shape[0]

            # 设置新的图片分辨率框架
            width_new = 700
            height_new = 500

            # 判断图片的长宽比率
            if width / height >= width_new / height_new:

                show = cv2.resize(im0, (width_new, int(height * width_new / width)))
            else:

                show = cv2.resize(im0, (int(width * height_new / height), height_new))
            im0 = cv2.cvtColor(show, cv2.COLOR_RGB2BGR)
            image_name = QtGui.QImage(im0, im0.shape[1], im0.shape[0], 3 * im0.shape[1], QtGui.QImage.Format_RGB888)
            # label=label.split(' ')[0]    #label 59 0.96   分割字符串  取前一个
            self.label2.setPixmap(QtGui.QPixmap.fromImage(image_name))
            # jpg = QtGui.QPixmap(image_name).scaled(self.label1.width(), self.label1.height())
            # self.label2.setPixmap(jpg)
        else:
            QMessageBox.information(self, '错误', '请先选择一个图片文件', QMessageBox.Yes, QMessageBox.Yes)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    splash = QSplashScreen(QPixmap(".\\data\\source_image\\logo.png"))
    # 设置画面中的文字的字体
    splash.setFont(QFont('Microsoft YaHei UI', 12))
    # 显示画面
    splash.show()
    # 显示信息
    splash.showMessage("程序初始化中... 0%", QtCore.Qt.AlignLeft | QtCore.Qt.AlignBottom, QtCore.Qt.black)
    time.sleep(0.3)


    splash.showMessage("正在加载模型配置文件...60%", QtCore.Qt.AlignLeft | QtCore.Qt.AlignBottom, QtCore.Qt.black)
    cam_t=Ui_MainWindow()
    splash.showMessage("正在加载模型配置文件...100%", QtCore.Qt.AlignLeft | QtCore.Qt.AlignBottom, QtCore.Qt.black)


    ui_p = picture()
    ui_p.show()
    splash.close()


    sys.exit(app.exec_())
