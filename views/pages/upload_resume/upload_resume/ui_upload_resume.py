# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'upload_resumeyoGfdG.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QSizePolicy, QToolButton, QVBoxLayout, QWidget)

class Ui_Frame(object):
    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.resize(400, 300)
        self.verticalLayout = QVBoxLayout(Frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_drop_area = QFrame(Frame)
        self.frame_drop_area.setObjectName(u"frame_drop_area")
        self.frame_drop_area.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.frame_drop_area.setAcceptDrops(True)
        self.frame_drop_area.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_drop_area.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_drop_area)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame_drop_area)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 16pt \"Segoe UI\";\n"
"color: rgb(160, 160, 160);")

        self.horizontalLayout.addWidget(self.label, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.verticalLayout.addWidget(self.frame_drop_area)

        self.toolButton_upload_cv = QToolButton(Frame)
        self.toolButton_upload_cv.setObjectName(u"toolButton_upload_cv")
        self.toolButton_upload_cv.setMinimumSize(QSize(100, 30))
        self.toolButton_upload_cv.setStyleSheet(u"font: 11pt \"Segoe UI\";")

        self.verticalLayout.addWidget(self.toolButton_upload_cv, 0, Qt.AlignmentFlag.AlignRight)


        self.retranslateUi(Frame)

        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Frame", None))
        self.label.setText(QCoreApplication.translate("Frame", u"Drop your CV here\n"
" or Choose a file", None))
        self.toolButton_upload_cv.setText(QCoreApplication.translate("Frame", u"Upload CV", None))
    # retranslateUi

