from conan import ConanFile
from conan.tools.cmake import cmake_layout

class Sub(ConanFile):
    name = "sub"
    version = "0.1"
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeToolchain", "CMakeDeps"

    def requirements(self):
        self.requires("freetype/2.13.2")
        self.requires("harfbuzz/8.3.0")

    def layout(self):
        cmake_layout(self)
