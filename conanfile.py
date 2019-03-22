#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools
import os


class EastlConan(ConanFile):
    name = "eastl"
    version = "3.13.04"
    description = "EASTL stands for Electronic Arts Standard Template Library. It is an extensive and robust implementation that has an emphasis on high performance."
    topics = ("conan", "eastl", "stl", "high-performance")
    url = "https://github.com/bincrafters/conan-eastl"
    homepage = "https://github.com/electronicarts/EASTL"
    author = "Bincrafters <bincrafters@gmail.com>"
    license = "BSD 3-Clause"
    exports = ["LICENSE.md"]
    exports_sources = ["CMakeLists.txt"]
    generators = "cmake"

    settings = "os", "arch", "compiler", "build_type"
    options = {"shared": [False, True]}
    default_options = {'shared': 'False'}

    _source_subfolder = "source_subfolder"

    def source(self):
        sha256 = "1f6279fb4347cbe2c28a7d4f62401db9347686b8e940b02ac8bb67b080f0324f"
        tools.get("{0}/archive/{1}.tar.gz".format(self.homepage, self.version), sha256=sha256)
        extracted_dir = self.name.upper() + "-" + self.version
        os.rename(extracted_dir, self._source_subfolder)


    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.install()
        self.copy(pattern="LICENSE", dst="licenses")

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
        if self.settings.compiler in ("clang", "gcc"):
            self.cpp_info.libs += ["pthread"]
