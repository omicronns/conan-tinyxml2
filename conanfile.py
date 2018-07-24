from conans import ConanFile, CMake, tools
import os


class TinyxmlConan(ConanFile):
    name = "tinyxml2"
    version = "0.1.0"
    license = "MIT"
    url = "https://github.com/omicronns/conan-tinyxml2"
    settings = "os", "compiler", "build_type", "arch"
    options = {
        "version": ["6.2.0"],
    }
    default_options = (
        "version=" + options["version"][-1],
    )
    generators = "cmake"

    def source(self):
        self.run("git clone --branch {} --single-branch https://github.com/leethomason/tinyxml2 sources".format(self.options.version))

    def build(self):
        cmake = CMake(self)
        source_dir = os.path.join(self.build_folder, "sources")
        cmake.configure(source_dir=source_dir)
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include/tinyxml2", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so*", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a*", dst="lib", keep_path=False)
        self.copy("*.lib*", dst="lib", keep_path=False)
        self.copy("*.pdb", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["tinyxml2"]
