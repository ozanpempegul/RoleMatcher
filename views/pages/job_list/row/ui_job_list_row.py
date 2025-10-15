# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'job_list_rowjNneJv.ui'
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
    QLabel, QSizePolicy, QToolButton, QWidget)

class Ui_Frame(object):
    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.resize(976, 85)
        Frame.setStyleSheet(u"QFrame {\n"
"    font-family: \"Segoe UI\";\n"
"    font-size: 12pt;\n"
"}")
        self.horizontalLayout = QHBoxLayout(Frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_id = QLabel(Frame)
        self.label_id.setObjectName(u"label_id")
        self.label_id.setMinimumSize(QSize(40, 0))
        self.label_id.setMaximumSize(QSize(40, 16777215))
        self.label_id.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label_id, 0, Qt.AlignmentFlag.AlignLeft)

        self.label_site = QLabel(Frame)
        self.label_site.setObjectName(u"label_site")
        self.label_site.setMinimumSize(QSize(75, 0))
        self.label_site.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label_site, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_title = QLabel(Frame)
        self.label_title.setObjectName(u"label_title")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_title.sizePolicy().hasHeightForWidth())
        self.label_title.setSizePolicy(sizePolicy)
        self.label_title.setMinimumSize(QSize(200, 0))
        self.label_title.setMaximumSize(QSize(200, 16777215))
        self.label_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label_title, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_company_name = QLabel(Frame)
        self.label_company_name.setObjectName(u"label_company_name")
        self.label_company_name.setMinimumSize(QSize(150, 0))
        self.label_company_name.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label_company_name, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_location = QLabel(Frame)
        self.label_location.setObjectName(u"label_location")
        self.label_location.setMinimumSize(QSize(120, 0))
        self.label_location.setMaximumSize(QSize(120, 16777215))
        self.label_location.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label_location, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_job_type = QLabel(Frame)
        self.label_job_type.setObjectName(u"label_job_type")
        self.label_job_type.setMinimumSize(QSize(75, 0))
        self.label_job_type.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label_job_type, 0, Qt.AlignmentFlag.AlignHCenter)

        self.checkBox_is_remote = QCheckBox(Frame)
        self.checkBox_is_remote.setObjectName(u"checkBox_is_remote")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.checkBox_is_remote.sizePolicy().hasHeightForWidth())
        self.checkBox_is_remote.setSizePolicy(sizePolicy1)
        self.checkBox_is_remote.setMinimumSize(QSize(75, 20))
        self.checkBox_is_remote.setMaximumSize(QSize(75, 20))
        self.checkBox_is_remote.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.horizontalLayout.addWidget(self.checkBox_is_remote, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_job_level = QLabel(Frame)
        self.label_job_level.setObjectName(u"label_job_level")
        self.label_job_level.setMinimumSize(QSize(120, 0))
        self.label_job_level.setMaximumSize(QSize(120, 16777215))
        self.label_job_level.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label_job_level, 0, Qt.AlignmentFlag.AlignHCenter)

        self.line = QFrame(Frame)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"background-color: rgb(170, 255, 255);")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.toolButton_open_link = QToolButton(Frame)
        self.toolButton_open_link.setObjectName(u"toolButton_open_link")
        self.toolButton_open_link.setStyleSheet(u"background-color: rgb(170, 170, 255);")

        self.horizontalLayout.addWidget(self.toolButton_open_link)

        self.toolButton_remove = QToolButton(Frame)
        self.toolButton_remove.setObjectName(u"toolButton_remove")
        self.toolButton_remove.setStyleSheet(u"background-color: rgb(170, 170, 255);\n"
"background-color: rgb(159, 47, 27);")

        self.horizontalLayout.addWidget(self.toolButton_remove)


        self.retranslateUi(Frame)

        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Frame", None))
        self.label_id.setText(QCoreApplication.translate("Frame", u"id", None))
        self.label_site.setText(QCoreApplication.translate("Frame", u"LINKEDIN", None))
        self.label_title.setText(QCoreApplication.translate("Frame", u"title", None))
        self.label_company_name.setText(QCoreApplication.translate("Frame", u"company name", None))
        self.label_location.setText(QCoreApplication.translate("Frame", u"location", None))
        self.label_job_type.setText(QCoreApplication.translate("Frame", u"fulltime", None))
        self.checkBox_is_remote.setText("")
        self.label_job_level.setText(QCoreApplication.translate("Frame", u"mid-senior level", None))
#if QT_CONFIG(tooltip)
        self.toolButton_open_link.setToolTip(QCoreApplication.translate("Frame", u"Open Link", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_open_link.setText("")
#if QT_CONFIG(tooltip)
        self.toolButton_remove.setToolTip(QCoreApplication.translate("Frame", u"Remove", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_remove.setText("")
    # retranslateUi

