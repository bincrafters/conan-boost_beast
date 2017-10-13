from conans import ConanFile, tools, os


class BoostBeastConan(ConanFile):
    name = "Boost.Beast"
    version = "20171013"
    commit_id = "f09b2d3e1c9d383e5d0f57b1bf889568cf27c39f"
    url = "https://github.com/bincrafters/conan-boost-beast"
    description = "Boost.beast provides HTTP and WebSocket built on Boost.Asio in C++11"
    license = "www.boost.org/users/license.html"
    lib_short_names = ["beast"]
    requires =  "Boost.Asio/1.65.1@bincrafters/stable", \
        "Boost.Intrusive/1.65.1@bincrafters/stable"
    
    def source(self):
        source_url = "https://github.com/boostorg/beast"
        self.run("git clone --depth=1 --branch=master {0}.git".format(source_url))
        with tools.chdir("./beast"):
            self.run("git checkout {0}".format(self.commit_id))
            
    def package(self):
        for lib_short_name in self.lib_short_names:
            include_dir = os.path.join(lib_short_name, "include")
            self.copy(pattern="*", dst="include", src=include_dir)		

    def package_id(self):
        self.info.header_only()
