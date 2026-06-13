# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowDmEWrW.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QMainWindow,
    QSizePolicy, QSpacerItem, QStackedWidget, QStatusBar,
    QToolButton, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1236, 505)
        MainWindow.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 20)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 40))
        self.frame.setMaximumSize(QSize(16777215, 40))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.toolButton_show_fetch_jobs_page = QToolButton(self.frame)
        self.toolButton_show_fetch_jobs_page.setObjectName(u"toolButton_show_fetch_jobs_page")
        self.toolButton_show_fetch_jobs_page.setStyleSheet(u"font: 11pt \"Segoe UI\";")

        self.horizontalLayout.addWidget(self.toolButton_show_fetch_jobs_page)

        self.toolButton_show_retrieved_jobs_page = QToolButton(self.frame)
        self.toolButton_show_retrieved_jobs_page.setObjectName(u"toolButton_show_retrieved_jobs_page")
        self.toolButton_show_retrieved_jobs_page.setStyleSheet(u"font: 11pt \"Segoe UI\";")

        self.horizontalLayout.addWidget(self.toolButton_show_retrieved_jobs_page)

        self.toolButton_show_resume_page = QToolButton(self.frame)
        self.toolButton_show_resume_page.setObjectName(u"toolButton_show_resume_page")
        self.toolButton_show_resume_page.setStyleSheet(u"font: 11pt \"Segoe UI\";")

        self.horizontalLayout.addWidget(self.toolButton_show_resume_page)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addWidget(self.frame)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_fetch_jobs = QWidget()
        self.page_fetch_jobs.setObjectName(u"page_fetch_jobs")
        self.stackedWidget.addWidget(self.page_fetch_jobs)
        self.page_retrieved_jobs = QWidget()
        self.page_retrieved_jobs.setObjectName(u"page_retrieved_jobs")
        self.stackedWidget.addWidget(self.page_retrieved_jobs)
        self.page_resume = QWidget()
        self.page_resume.setObjectName(u"page_resume")
        self.stackedWidget.addWidget(self.page_resume)

        self.verticalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.toolButton_show_fetch_jobs_page.setText(QCoreApplication.translate("MainWindow", u"Fetch Jobs", None))
        self.toolButton_show_retrieved_jobs_page.setText(QCoreApplication.translate("MainWindow", u"Retrieved Jobs", None))
        self.toolButton_show_resume_page.setText(QCoreApplication.translate("MainWindow", u"Resume", None))
    # retranslateUi

