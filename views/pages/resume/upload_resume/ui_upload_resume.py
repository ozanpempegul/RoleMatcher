# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'upload_resumeYSGMlT.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QSizePolicy,
    QVBoxLayout, QWidget)

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
        self.frame_drop_area.setStyleSheet(u"QFrame {\n"
"    border: 2px dashed gray;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QFrame:hover {\n"
"    border: 2px dashed blue;\n"
"}")
        self.frame_drop_area.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_drop_area.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_drop_area)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(9, 9, 9, 9)
        self.label_2 = QLabel(self.frame_drop_area)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 13pt \"Segoe UI\";\n"
"color: rgb(160, 160, 160);\n"
"border: none")

        self.verticalLayout_3.addWidget(self.label_2)

        self.label = QLabel(self.frame_drop_area)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"color: rgb(190, 190, 190);\n"
"border: none")

        self.verticalLayout_3.addWidget(self.label, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout.addWidget(self.frame_drop_area, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.retranslateUi(Frame)

        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Frame", None))
        self.label_2.setText(QCoreApplication.translate("Frame", u"Click to upload or drag and drop", None))
        self.label.setText(QCoreApplication.translate("Frame", u".DOCX", None))
    # retranslateUi

