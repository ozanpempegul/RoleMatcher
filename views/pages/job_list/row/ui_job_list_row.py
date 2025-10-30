# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'job_list_rowQConts.ui'
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
        Frame.resize(788, 85)
        Frame.setStyleSheet(u"QFrame {\n"
"    font-family: \"Segoe UI\";\n"
"    font-size: 12pt;\n"
"}")
        self.horizontalLayout = QHBoxLayout(Frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_id = QLabel(Frame)
        self.label_id.setObjectName(u"label_id")
        self.label_id.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label_id)

        self.label_title = QLabel(Frame)
        self.label_title.setObjectName(u"label_title")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_title.sizePolicy().hasHeightForWidth())
        self.label_title.setSizePolicy(sizePolicy)
        self.label_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label_title)

        self.label_company_name = QLabel(Frame)
        self.label_company_name.setObjectName(u"label_company_name")
        self.label_company_name.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label_company_name)

        self.label_location = QLabel(Frame)
        self.label_location.setObjectName(u"label_location")
        self.label_location.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label_location)

        self.label_job_type = QLabel(Frame)
        self.label_job_type.setObjectName(u"label_job_type")
        self.label_job_type.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label_job_type)

        self.checkBox_is_remote = QCheckBox(Frame)
        self.checkBox_is_remote.setObjectName(u"checkBox_is_remote")
        self.checkBox_is_remote.setEnabled(False)
        sizePolicy.setHeightForWidth(self.checkBox_is_remote.sizePolicy().hasHeightForWidth())
        self.checkBox_is_remote.setSizePolicy(sizePolicy)
        self.checkBox_is_remote.setMinimumSize(QSize(20, 0))
        self.checkBox_is_remote.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.horizontalLayout.addWidget(self.checkBox_is_remote)

        self.label_match_score = QLabel(Frame)
        self.label_match_score.setObjectName(u"label_match_score")
        sizePolicy.setHeightForWidth(self.label_match_score.sizePolicy().hasHeightForWidth())
        self.label_match_score.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.label_match_score)

        self.line = QFrame(Frame)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"background-color: rgb(170, 255, 255);")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.toolButton_generate_cover_letter = QToolButton(Frame)
        self.toolButton_generate_cover_letter.setObjectName(u"toolButton_generate_cover_letter")
        self.toolButton_generate_cover_letter.setStyleSheet(u"background-color: rgb(255, 0, 255);")

        self.horizontalLayout.addWidget(self.toolButton_generate_cover_letter)

        self.toolButton_generate_tailored_resume = QToolButton(Frame)
        self.toolButton_generate_tailored_resume.setObjectName(u"toolButton_generate_tailored_resume")
        self.toolButton_generate_tailored_resume.setStyleSheet(u"background-color: rgb(85, 170, 0);")

        self.horizontalLayout.addWidget(self.toolButton_generate_tailored_resume)

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
        self.label_title.setText(QCoreApplication.translate("Frame", u"title", None))
        self.label_company_name.setText(QCoreApplication.translate("Frame", u"company name", None))
        self.label_location.setText(QCoreApplication.translate("Frame", u"location", None))
        self.label_job_type.setText(QCoreApplication.translate("Frame", u"fulltime", None))
        self.checkBox_is_remote.setText("")
        self.label_match_score.setText(QCoreApplication.translate("Frame", u"Score", None))
#if QT_CONFIG(tooltip)
        self.toolButton_generate_cover_letter.setToolTip(QCoreApplication.translate("Frame", u"generate cover letter", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_generate_cover_letter.setText("")
#if QT_CONFIG(tooltip)
        self.toolButton_generate_tailored_resume.setToolTip(QCoreApplication.translate("Frame", u"tailor resume", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_generate_tailored_resume.setText("")
#if QT_CONFIG(tooltip)
        self.toolButton_open_link.setToolTip(QCoreApplication.translate("Frame", u"Open Link", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_open_link.setText("")
#if QT_CONFIG(tooltip)
        self.toolButton_remove.setToolTip(QCoreApplication.translate("Frame", u"Remove", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_remove.setText("")
    # retranslateUi

