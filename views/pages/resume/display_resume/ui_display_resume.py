# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'display_resumeDHGqQE.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QScrollArea,
    QSizePolicy, QSpacerItem, QToolButton, QVBoxLayout,
    QWidget)

class Ui_Frame(object):
    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.resize(569, 430)
        self.verticalLayout = QVBoxLayout(Frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea = QScrollArea(Frame)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollContent = QWidget()
        self.scrollContent.setObjectName(u"scrollContent")
        self.scrollContent.setGeometry(QRect(0, 0, 549, 410))
        self.contentLayout = QVBoxLayout(self.scrollContent)
        self.contentLayout.setObjectName(u"contentLayout")
        self.groupMeta = QGroupBox(self.scrollContent)
        self.groupMeta.setObjectName(u"groupMeta")
        self.metaLayout = QVBoxLayout(self.groupMeta)
        self.metaLayout.setObjectName(u"metaLayout")

        self.contentLayout.addWidget(self.groupMeta)

        self.groupProfile = QGroupBox(self.scrollContent)
        self.groupProfile.setObjectName(u"groupProfile")
        self.profileLayout = QVBoxLayout(self.groupProfile)
        self.profileLayout.setObjectName(u"profileLayout")

        self.contentLayout.addWidget(self.groupProfile)

        self.groupSkills = QGroupBox(self.scrollContent)
        self.groupSkills.setObjectName(u"groupSkills")
        self.skillsLayout = QVBoxLayout(self.groupSkills)
        self.skillsLayout.setObjectName(u"skillsLayout")

        self.contentLayout.addWidget(self.groupSkills)

        self.groupEducation = QGroupBox(self.scrollContent)
        self.groupEducation.setObjectName(u"groupEducation")
        self.educationLayout = QVBoxLayout(self.groupEducation)
        self.educationLayout.setObjectName(u"educationLayout")

        self.contentLayout.addWidget(self.groupEducation)

        self.groupExperience = QGroupBox(self.scrollContent)
        self.groupExperience.setObjectName(u"groupExperience")
        self.experienceLayout = QVBoxLayout(self.groupExperience)
        self.experienceLayout.setObjectName(u"experienceLayout")

        self.contentLayout.addWidget(self.groupExperience)

        self.groupProjects = QGroupBox(self.scrollContent)
        self.groupProjects.setObjectName(u"groupProjects")
        self.projectsLayout = QVBoxLayout(self.groupProjects)
        self.projectsLayout.setObjectName(u"projectsLayout")

        self.contentLayout.addWidget(self.groupProjects)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.contentLayout.addItem(self.verticalSpacer)

        self.toolButton_remove_cv = QToolButton(self.scrollContent)
        self.toolButton_remove_cv.setObjectName(u"toolButton_remove_cv")
        self.toolButton_remove_cv.setMinimumSize(QSize(75, 35))
        self.toolButton_remove_cv.setStyleSheet(u"background-color: rgb(207, 19, 19);\n"
"color: rgb(255, 255, 255);")

        self.contentLayout.addWidget(self.toolButton_remove_cv)

        self.scrollArea.setWidget(self.scrollContent)

        self.verticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(Frame)

        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Frame", None))
        self.groupMeta.setTitle(QCoreApplication.translate("Frame", u"Meta", None))
        self.groupProfile.setTitle(QCoreApplication.translate("Frame", u"Profile", None))
        self.groupSkills.setTitle(QCoreApplication.translate("Frame", u"Skills", None))
        self.groupEducation.setTitle(QCoreApplication.translate("Frame", u"Education", None))
        self.groupExperience.setTitle(QCoreApplication.translate("Frame", u"Experience", None))
        self.groupProjects.setTitle(QCoreApplication.translate("Frame", u"Projects", None))
        self.toolButton_remove_cv.setText(QCoreApplication.translate("Frame", u"Remove", None))
    # retranslateUi

