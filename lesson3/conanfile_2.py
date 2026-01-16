from conan import ConanFile
from conan.tools.cmake import cmake_layout, CMakeToolchain, CMakeDeps

class FormatterRecipe(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeToolchain", "CMakeDeps"

    options = {"with_std_format": [True, False]}
    default_options = {"with_std_format": False}

    def generate(self):
        tc = CMakeToolchain(self)
        tc.cache_variables["USE_STD_FORMAT"] = self.options.with_std_format
        tc.generate()

        cd = CMakeDeps(self)
        cd.generate()

    def requirements(self):
        if not self.options.with_std_format:
            self.requires("fmt/11.2.0")
    
    def layout(self):
        cmake_layout(self)



