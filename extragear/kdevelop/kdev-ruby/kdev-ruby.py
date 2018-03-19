import info


class subinfo(info.infoclass):
    def setTargets(self):
        self.svnTargets['master'] = 'git://anongit.kde.org/kdev-ruby'
        self.defaultTarget = 'master'

    def setDependencies(self):
        self.description = "ruby support for kdevelop"
        self.runtimeDependencies["virtual/base"] = "default"
        if OsUtils.isWin():
            self.buildDependencies["dev-util/winflexbison"] = "default"
        else:
            self.buildDependencies["autotools/flex"] = "default"
            self.buildDependencies["autotools/bison"] = "default"
        self.runtimeDependencies["extragear/kdevelop/kdevelop"] = "default"


from Package.CMakePackageBase import *


class Package(CMakePackageBase):
    def __init__(self):
        CMakePackageBase.__init__(self)
