import info


class subinfo(info.infoclass):
    def setTargets(self):
        self.versionInfo.setDefaultValues()

    def setDependencies(self):
        self.runtimeDependencies["virtual/base"] = "default"
        self.buildDependencies["dev-util/png2ico"] = "default"
        # needed for many kf5's
        if OsUtils.isWin():
            self.buildDependencies["dev-util/winflexbison"] = "default"
        else:
            self.buildDependencies["autotools/flex"] = "default"
            self.buildDependencies["autotools/bison"] = "default"
        self.buildDependencies["libs/qt5/qttools"] = "default"

        if CraftCore.settings.getboolean("CMake", "KDE_L10N_AUTO_TRANSLATIONS", False):
            self.buildDependencies["dev-util/ruby"] = "default"


from Package.CMakePackageBase import *


class Package(CMakePackageBase):
    def __init__(self):
        CMakePackageBase.__init__(self)
