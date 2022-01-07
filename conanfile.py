from conans import ConanFile
from conans import tools
from conan.tools.cmake import CMakeToolchain, CMake
from conan.tools.layout import cmake_layout


class PlutovgConan(ConanFile):
    name = "plutovg"
    version = "0.1.0"
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
        tools.get("https://github.com/tschabo/plutovg/archive/refs/tags/v0.1.0.tar.gz", md5='eea1ae4ae376241ed422210a39c57ff2', sha1='29da1df82175af272be2c24a4f845482508762b8', sha256='c55082d88b69e0d647df2f3dcfe2ed3ec8cea9178e8257b87db7434197d5f9e7')

    def layout(self):
        cmake_layout(self)

    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure(build_script_folder="plutovg-0.1.0")
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["plutovg"]
