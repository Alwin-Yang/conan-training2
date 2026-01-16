from conan import ConanFile
from conan.tools.cmake import cmake_layout

class FormatterRecipe(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeToolchain", "CMakeDeps"

    options = {"with_std_format": [True, False]}
    default_options = {"with_std_format": False}

    def requirements(self):
        if not self.options.with_std_format:
            self.requires("fmt/11.2.0")
    
    def layout(self):
        cmake_layout(self)



