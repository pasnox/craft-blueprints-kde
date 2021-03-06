import info


class subinfo(info.infoclass):
    def setTargets(self):
        self.versionInfo.setDefaultValues()

    def setDependencies(self):
        self.buildDependencies["virtual/base"] = "default"
        self.buildDependencies["frameworks/extra-cmake-modules"] = "default"
        self.runtimeDependencies["frameworks/tier1/kconfig"] = "default"
        self.runtimeDependencies["frameworks/tier1/ki18n"] = "default"
        self.runtimeDependencies["frameworks/tier1/kwidgetsaddons"] = "default"
        self.runtimeDependencies["frameworks/tier2/kpackage"] = "default"
        self.runtimeDependencies["frameworks/tier3/knewstuff"] = "default"
        self.runtimeDependencies["frameworks/tier3/kiconthemes"] = "default"
        self.runtimeDependencies["frameworks/tier3/kio"] = "default"
        self.runtimeDependencies["frameworks/tier3/knotifications"] = "default"


from Package.CMakePackageBase import *


class Package(CMakePackageBase):
    def __init__(self):
        CMakePackageBase.__init__(self)
