from platform import version
from conans import ConanFile
from conans import tools
from conan.tools.cmake import CMakeToolchain, CMake
from conan.tools.layout import cmake_layout


class PlutovgConan(ConanFile):
    name = "plutovg"
    license = "MIT"
    author = "tschabo"
    url = ""
    description = "PlutoVG is a standalone 2D vector graphics library in C."
    topics = ("vector graphics", "2d", "bitmap")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC
    
    def source(self):
        tools.get(**self.conan_data["sources"][self.version], strip_root=True)

    def layout(self):
        cmake_layout(self)

    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["plutovg"]
