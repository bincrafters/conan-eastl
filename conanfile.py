#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools
import os


class EastlConan(ConanFile):
    name = "eastl"
    version = "3.07.00"
    url = "https://github.com/bincrafters/conan-eastl"
    description = "EASTL stands for Electronic Arts Standard Template Library. It is an extensive and robust implementation that has an emphasis on high performance."
    license = "BSD 3-Clause"
    exports = ["LICENSE.md"]
    exports_sources = ["CMakeLists.txt"]
    generators = "cmake"
    settings = "os", "arch", "compiler", "build_type"
    options = {"shared": [False, True]}
    default_options = "shared=False"
    source_subfolder = "source_subfolder"

    def source(self):
        source_url = "https://github.com/electronicarts/EASTL"
        tools.get("{0}/archive/{1}.tar.gz".format(source_url, self.version))
        extracted_dir = self.name.upper() + "-" + self.version
        os.rename(extracted_dir, self.source_subfolder)


    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        cmake.install()

    def package(self):
        self.copy(pattern="LICENSE", dst="licenses")
        # The rest of the library is copied by cmake.install()

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
