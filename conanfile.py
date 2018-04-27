from conans import ConanFile, CMake

class StatsWriterStatsd(ConanFile):
  settings = "os", "compiler", "build_type", "arch"
  requires = "boost/1.66.0@conan/stable", "gtest/1.8.0@bincrafters/stable" # comma separated list of requirements
  generators = "cmake"

  def config(self):
    if self.settings.os == "Linux":
      self.options["boost*"].fPIC = True
      self.options["boost*"].shared = False
      self.options["gtest*"].shared = True
