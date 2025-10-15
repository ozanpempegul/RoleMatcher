# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'configwtiivk.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QSizePolicy, QSpinBox,
    QVBoxLayout, QWidget)

class Ui_Frame(object):
    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.resize(339, 444)
        self.verticalLayout = QVBoxLayout(Frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_site_names = QFrame(Frame)
        self.frame_site_names.setObjectName(u"frame_site_names")
        self.frame_site_names.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_site_names.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_site_names)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_site_names)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(150, 0))

        self.horizontalLayout.addWidget(self.label)

        self.frame = QFrame(self.frame_site_names)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.checkBox_linkedin = QCheckBox(self.frame)
        self.checkBox_linkedin.setObjectName(u"checkBox_linkedin")

        self.verticalLayout_2.addWidget(self.checkBox_linkedin)

        self.checkBox_indeed = QCheckBox(self.frame)
        self.checkBox_indeed.setObjectName(u"checkBox_indeed")

        self.verticalLayout_2.addWidget(self.checkBox_indeed)


        self.horizontalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.frame_site_names)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.checkBox_google = QCheckBox(self.frame_2)
        self.checkBox_google.setObjectName(u"checkBox_google")

        self.verticalLayout_3.addWidget(self.checkBox_google)


        self.horizontalLayout.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.frame_site_names)

        self.frame_search_term = QFrame(Frame)
        self.frame_search_term.setObjectName(u"frame_search_term")
        self.frame_search_term.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_search_term.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_search_term)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_search_term)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lineEdit_search_term = QLineEdit(self.frame_search_term)
        self.lineEdit_search_term.setObjectName(u"lineEdit_search_term")

        self.horizontalLayout_2.addWidget(self.lineEdit_search_term)


        self.verticalLayout.addWidget(self.frame_search_term)

        self.frame_location = QFrame(Frame)
        self.frame_location.setObjectName(u"frame_location")
        self.frame_location.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_location.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_location)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_location)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_3.addWidget(self.label_3)

        self.lineEdit_location = QLineEdit(self.frame_location)
        self.lineEdit_location.setObjectName(u"lineEdit_location")

        self.horizontalLayout_3.addWidget(self.lineEdit_location)


        self.verticalLayout.addWidget(self.frame_location)

        self.frame_results_wanted = QFrame(Frame)
        self.frame_results_wanted.setObjectName(u"frame_results_wanted")
        self.frame_results_wanted.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_results_wanted.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_results_wanted)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame_results_wanted)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_4.addWidget(self.label_4)

        self.spinBox_fetch_count = QSpinBox(self.frame_results_wanted)
        self.spinBox_fetch_count.setObjectName(u"spinBox_fetch_count")

        self.horizontalLayout_4.addWidget(self.spinBox_fetch_count)


        self.verticalLayout.addWidget(self.frame_results_wanted)

        self.frame_hours_old = QFrame(Frame)
        self.frame_hours_old.setObjectName(u"frame_hours_old")
        self.frame_hours_old.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_hours_old.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_hours_old)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_hours_old)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_5.addWidget(self.label_5)

        self.spinBox_hours_old = QSpinBox(self.frame_hours_old)
        self.spinBox_hours_old.setObjectName(u"spinBox_hours_old")

        self.horizontalLayout_5.addWidget(self.spinBox_hours_old)


        self.verticalLayout.addWidget(self.frame_hours_old)

        self.frame_is_fetch_description = QFrame(Frame)
        self.frame_is_fetch_description.setObjectName(u"frame_is_fetch_description")
        self.frame_is_fetch_description.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_is_fetch_description.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_is_fetch_description)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.frame_is_fetch_description)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_6.addWidget(self.label_6)

        self.checkBox_fetch_description = QCheckBox(self.frame_is_fetch_description)
        self.checkBox_fetch_description.setObjectName(u"checkBox_fetch_description")
        self.checkBox_fetch_description.setMinimumSize(QSize(20, 20))

        self.horizontalLayout_6.addWidget(self.checkBox_fetch_description, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout.addWidget(self.frame_is_fetch_description)


        self.retranslateUi(Frame)

        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Frame", None))
        self.label.setText(QCoreApplication.translate("Frame", u"Sites", None))
        self.checkBox_linkedin.setText(QCoreApplication.translate("Frame", u"Linkedin", None))
        self.checkBox_indeed.setText(QCoreApplication.translate("Frame", u"Indeed", None))
        self.checkBox_google.setText(QCoreApplication.translate("Frame", u"Google", None))
        self.label_2.setText(QCoreApplication.translate("Frame", u"Search Term: ", None))
        self.label_3.setText(QCoreApplication.translate("Frame", u"Location: ", None))
        self.label_4.setText(QCoreApplication.translate("Frame", u"Fetch Count: ", None))
        self.label_5.setText(QCoreApplication.translate("Frame", u"Hours old: ", None))
        self.label_6.setText(QCoreApplication.translate("Frame", u"Fetch Description: ", None))
        self.checkBox_fetch_description.setText("")
    # retranslateUi

