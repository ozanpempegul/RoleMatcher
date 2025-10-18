# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowSvknZW.ui'
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
        MainWindow.resize(825, 502)
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

        self.toolButton_show_upload_resume_page = QToolButton(self.frame)
        self.toolButton_show_upload_resume_page.setObjectName(u"toolButton_show_upload_resume_page")
        self.toolButton_show_upload_resume_page.setStyleSheet(u"font: 11pt \"Segoe UI\";")

        self.horizontalLayout.addWidget(self.toolButton_show_upload_resume_page)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.toolButton_settings = QToolButton(self.frame)
        self.toolButton_settings.setObjectName(u"toolButton_settings")
        self.toolButton_settings.setStyleSheet(u"background-color: rgb(85, 170, 255);")

        self.horizontalLayout.addWidget(self.toolButton_settings)

        self.toolButton_minimize = QToolButton(self.frame)
        self.toolButton_minimize.setObjectName(u"toolButton_minimize")
        self.toolButton_minimize.setStyleSheet(u"background-color: rgb(244, 244, 122);")

        self.horizontalLayout.addWidget(self.toolButton_minimize)

        self.toolButton_maximize = QToolButton(self.frame)
        self.toolButton_maximize.setObjectName(u"toolButton_maximize")
        self.toolButton_maximize.setStyleSheet(u"background-color: rgb(85, 170, 0);")

        self.horizontalLayout.addWidget(self.toolButton_maximize, 0, Qt.AlignmentFlag.AlignRight)

        self.toolButton_exit = QToolButton(self.frame)
        self.toolButton_exit.setObjectName(u"toolButton_exit")
        self.toolButton_exit.setStyleSheet(u"background-color: rgb(188, 0, 0);")

        self.horizontalLayout.addWidget(self.toolButton_exit, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout.addWidget(self.frame)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_fetch_jobs = QWidget()
        self.page_fetch_jobs.setObjectName(u"page_fetch_jobs")
        self.stackedWidget.addWidget(self.page_fetch_jobs)
        self.page_retrieved_jobs = QWidget()
        self.page_retrieved_jobs.setObjectName(u"page_retrieved_jobs")
        self.stackedWidget.addWidget(self.page_retrieved_jobs)
        self.page_upload_resume = QWidget()
        self.page_upload_resume.setObjectName(u"page_upload_resume")
        self.stackedWidget.addWidget(self.page_upload_resume)

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
        self.toolButton_show_upload_resume_page.setText(QCoreApplication.translate("MainWindow", u"Upload Resume", None))
#if QT_CONFIG(tooltip)
        self.toolButton_settings.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_settings.setText("")
#if QT_CONFIG(tooltip)
        self.toolButton_minimize.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_minimize.setText("")
#if QT_CONFIG(tooltip)
        self.toolButton_maximize.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_maximize.setText("")
#if QT_CONFIG(tooltip)
        self.toolButton_exit.setToolTip(QCoreApplication.translate("MainWindow", u"Exit", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_exit.setText("")
    # retranslateUi

