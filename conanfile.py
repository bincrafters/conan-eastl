#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools
import os


class EastlConan(ConanFile):
    name = "EASTL"
    version = "3.06.00"
    url = "https://github.com/bincrafters/conan-eastl"
    description = "EASTL stands for Electronic Arts Standard Template Library. It is an extensive and robust implementation that has an emphasis on high performance."

    # Indicates License type of the packaged library
    license = "BSD-3-Clause"

    # Packages the license for the conanfile.py
    exports = ["LICENSE.md"]

    # Remove following lines if the target lib does not use cmake.
    exports_sources = ["CMakeLists.txt"]
    generators = "cmake"

    # Options may need to change depending on the packaged library.
    settings = "os", "arch", "compiler", "build_type"
    options = {"shared": [False]}
    default_options = "shared=False"

    # Custom attributes for Bincrafters recipe conventions
    source_subfolder = "source_subfolder"
    build_subfolder = "build_subfolder"

    def source(self):
        source_url = "https://github.com/electronicarts/EASTL"
        tools.get("{0}/archive/{1}.tar.gz".format(source_url, self.version))
        extracted_dir = self.name + "-" + self.version

        #Rename to "source_subfolder" is a convention to simplify later steps
        os.rename(extracted_dir, self.source_subfolder)


    def build(self):
        cmake = CMake(self)
        cmake.configure(build_folder=self.build_subfolder)
        cmake.build()
        cmake.install()

    def package(self):
        # If the CMakeLists.txt has a proper install method, the steps below may be redundant
        # If so, you can replace all the steps below with the word "pass"
        #include_folder = os.path.join(self.source_subfolder, "include")
        #self.copy(pattern="LICENSE")
        #self.copy(pattern="*", dst="include", src=include_folder)
        #self.copy(pattern="*.dll", dst="bin", keep_path=False)
        #self.copy(pattern="*.lib", dst="lib", keep_path=False)
        #self.copy(pattern="*.a", dst="lib", keep_path=False)
        #self.copy(pattern="*.so*", dst="lib", keep_path=False)
        #self.copy(pattern="*.dylib", dst="lib", keep_path=False)
        pass


    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
