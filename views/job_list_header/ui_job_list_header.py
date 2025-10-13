# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'job_list_headertHEOwZ.ui'
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
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Frame(object):
    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.resize(993, 87)
        Frame.setStyleSheet(u"QFrame {\n"
"    font-family: \"Segoe UI\";\n"
"    font-size: 14pt;\n"
"}")
        self.verticalLayout = QVBoxLayout(Frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Frame)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QSize(200, 0))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_id = QLabel(self.frame)
        self.label_id.setObjectName(u"label_id")
        self.label_id.setMaximumSize(QSize(40, 16777215))
        self.label_id.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_id, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_site = QLabel(self.frame)
        self.label_site.setObjectName(u"label_site")
        self.label_site.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_site, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_title = QLabel(self.frame)
        self.label_title.setObjectName(u"label_title")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_title.sizePolicy().hasHeightForWidth())
        self.label_title.setSizePolicy(sizePolicy1)
        self.label_title.setMinimumSize(QSize(150, 0))
        self.label_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_title, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_company_name = QLabel(self.frame)
        self.label_company_name.setObjectName(u"label_company_name")
        self.label_company_name.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_company_name, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_location = QLabel(self.frame)
        self.label_location.setObjectName(u"label_location")
        self.label_location.setMinimumSize(QSize(120, 0))
        self.label_location.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_location, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_job_type = QLabel(self.frame)
        self.label_job_type.setObjectName(u"label_job_type")
        self.label_job_type.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_job_type, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)

        self.horizontalLayout_2.addWidget(self.label, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_job_level = QLabel(self.frame)
        self.label_job_level.setObjectName(u"label_job_level")
        self.label_job_level.setMinimumSize(QSize(100, 0))
        self.label_job_level.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_job_level, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_description = QLabel(self.frame)
        self.label_description.setObjectName(u"label_description")
        self.label_description.setMinimumSize(QSize(200, 0))
        self.label_description.setMaximumSize(QSize(200, 16777215))
        self.label_description.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_description, 0, Qt.AlignmentFlag.AlignHCenter)

        self.frame_line_placeholder = QFrame(self.frame)
        self.frame_line_placeholder.setObjectName(u"frame_line_placeholder")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_line_placeholder.sizePolicy().hasHeightForWidth())
        self.frame_line_placeholder.setSizePolicy(sizePolicy3)
        self.frame_line_placeholder.setMinimumSize(QSize(3, 0))
        self.frame_line_placeholder.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_line_placeholder.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_2.addWidget(self.frame_line_placeholder)

        self.frame_button_placeholder = QFrame(self.frame)
        self.frame_button_placeholder.setObjectName(u"frame_button_placeholder")
        sizePolicy2.setHeightForWidth(self.frame_button_placeholder.sizePolicy().hasHeightForWidth())
        self.frame_button_placeholder.setSizePolicy(sizePolicy2)
        self.frame_button_placeholder.setMinimumSize(QSize(23, 23))
        self.frame_button_placeholder.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_button_placeholder.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_2.addWidget(self.frame_button_placeholder)


        self.verticalLayout.addWidget(self.frame)

        self.line = QFrame(Frame)
        self.line.setObjectName(u"line")
        self.line.setMinimumSize(QSize(0, 3))
        self.line.setStyleSheet(u"background-color: rgb(85, 255, 255);")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)


        self.retranslateUi(Frame)

        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Frame", None))
        self.label_id.setText(QCoreApplication.translate("Frame", u"id", None))
        self.label_site.setText(QCoreApplication.translate("Frame", u"site", None))
        self.label_title.setText(QCoreApplication.translate("Frame", u"title", None))
        self.label_company_name.setText(QCoreApplication.translate("Frame", u"company name", None))
        self.label_location.setText(QCoreApplication.translate("Frame", u"location", None))
        self.label_job_type.setText(QCoreApplication.translate("Frame", u"job type", None))
        self.label.setText(QCoreApplication.translate("Frame", u"Remote", None))
        self.label_job_level.setText(QCoreApplication.translate("Frame", u"job level", None))
        self.label_description.setText(QCoreApplication.translate("Frame", u"description", None))
    # retranslateUi

