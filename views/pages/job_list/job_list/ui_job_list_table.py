# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'job_list_tableGFpUGR.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Frame(object):
    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.resize(518, 300)
        self.verticalLayout = QVBoxLayout(Frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_job_list_table = QFrame(Frame)
        self.frame_job_list_table.setObjectName(u"frame_job_list_table")
        self.frame_job_list_table.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_job_list_table.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_job_list_table)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_job_list_header = QFrame(self.frame_job_list_table)
        self.frame_job_list_header.setObjectName(u"frame_job_list_header")
        self.frame_job_list_header.setMinimumSize(QSize(0, 40))
        self.frame_job_list_header.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_job_list_header.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_2.addWidget(self.frame_job_list_header)


        self.verticalLayout.addWidget(self.frame_job_list_table)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(Frame)

        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Frame", None))
    # retranslateUi

