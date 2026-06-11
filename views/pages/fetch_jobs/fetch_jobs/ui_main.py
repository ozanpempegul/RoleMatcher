# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainDICeeT.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QPushButton,
    QSizePolicy, QStackedWidget, QToolButton, QVBoxLayout,
    QWidget)

class Ui_Frame(object):
    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.resize(376, 518)
        self.verticalLayout = QVBoxLayout(Frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 20, 0, 0)
        self.frame = QFrame(Frame)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_by_search = QPushButton(self.frame)
        self.pushButton_by_search.setObjectName(u"pushButton_by_search")

        self.horizontalLayout_2.addWidget(self.pushButton_by_search)

        self.pushButton_by_link = QPushButton(self.frame)
        self.pushButton_by_link.setObjectName(u"pushButton_by_link")

        self.horizontalLayout_2.addWidget(self.pushButton_by_link)


        self.verticalLayout.addWidget(self.frame)

        self.stackedWidget_pages = QStackedWidget(Frame)
        self.stackedWidget_pages.setObjectName(u"stackedWidget_pages")

        self.verticalLayout.addWidget(self.stackedWidget_pages)

        self.frame_2 = QFrame(Frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 0))
        self.frame_2.setMaximumSize(QSize(16777215, 30))
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.toolButton_fetch = QToolButton(self.frame_2)
        self.toolButton_fetch.setObjectName(u"toolButton_fetch")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_fetch.sizePolicy().hasHeightForWidth())
        self.toolButton_fetch.setSizePolicy(sizePolicy)
        self.toolButton_fetch.setMinimumSize(QSize(100, 0))

        self.horizontalLayout.addWidget(self.toolButton_fetch, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout.addWidget(self.frame_2)


        self.retranslateUi(Frame)

        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Frame", None))
        self.pushButton_by_search.setText(QCoreApplication.translate("Frame", u"By Search", None))
        self.pushButton_by_link.setText(QCoreApplication.translate("Frame", u"By Link", None))
        self.toolButton_fetch.setText(QCoreApplication.translate("Frame", u"Fetch", None))
    # retranslateUi

