import info


class subinfo(info.infoclass):
    def setTargets(self):
        self.versionInfo.setDefaultValues()

        self.description = "KTuberling"

    def setDependencies(self):
        self.runtimeDependencies["virtual/base"] = "default"
        self.buildDependencies["frameworks/extra-cmake-modules"] = "default"
        self.runtimeDependencies["libs/qt5/qtbase"] = "default"
        self.runtimeDependencies["frameworks/tier2/kcompletion"] = "default"
        self.runtimeDependencies["frameworks/tier1/kconfig"] = "default"
        self.runtimeDependencies["frameworks/tier1/kcoreaddons"] = "default"
        self.runtimeDependencies["frameworks/tier1/ki18n"] = "default"
        self.runtimeDependencies["frameworks/tier1/kdbusaddons"] = "default"
        self.runtimeDependencies["frameworks/tier2/kcrash"] = "default"
        self.runtimeDependencies["frameworks/tier3/kxmlgui"] = "default"
        self.runtimeDependencies["frameworks/tier1/kwidgetsaddons"] = "default"
        self.runtimeDependencies["frameworks/tier4/kdelibs4support"] = "default"
        self.runtimeDependencies["kde/kdegames/libkdegames"] = "default"
        self.runtimeDependencies["qt-libs/phonon"] = "default"


from Package.CMakePackageBase import *


class Package(CMakePackageBase):
    def __init__(self):
        CMakePackageBase.__init__(self)
