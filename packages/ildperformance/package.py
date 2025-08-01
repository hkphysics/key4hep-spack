# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from spack.pkg.k4.key4hep_stack import Ilcsoftpackage


class Ildperformance(CMakePackage, Ilcsoftpackage):
    """Assembly of various Marlin processor for reconstruction."""

    url = "https://github.com/iLCSoft/ILDPerformance/archive/v01-08.tar.gz"
    homepage = "https://github.com/iLCSoft/ILDPerformance"
    git = "https://github.com/iLCSoft/ILDPerformance.git"

    maintainers("vvolkl")

    version("master", branch="master")
    version(
        "1.12.1",
        sha256="b392e1a32dcc8eb325a5f27e15172aca3d43468241e11ee65f70d692d2cb136a",
    )
    version(
        "1.12",
        sha256="d606cc5d71dfb3b2a753000dc665187b2b9d937906d1611a789e7a19cd4edd2e",
    )
    version(
        "1.11",
        sha256="8445e68fd1a20d76f15d615dcc3a9044d1829d91e3b7cedac3eafdf098c957ee",
    )
    version(
        "1.10",
        sha256="5dc9b20af8018d2268df02d05a7245ca8087365a404fd9c3a110484235f7d383",
    )
    version(
        "1.9", sha256="3a8187036eee39b35e4a58d874fa906182a7b83e1d143811ec7d721ea405f3dc"
    )
    version(
        "1.8", sha256="bcf19d3a6f425fa5eea228676d07558635881a0329c4d66ffda4230dfe9617c1"
    )

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("ilcutil")
    depends_on("marlin")
    depends_on("marlinutil")
    depends_on("generalbrokenlines")
    depends_on("aidatt")
    depends_on("marlintrk")
    depends_on("gsl")
    depends_on("root")
    depends_on("dd4hep")

    def setup_run_environment(self, env):
        env.prepend_path("MARLIN_DLL", self.prefix.lib + "/libILDPerformance.so")

    def cmake_args(self):
        # C++ Standard
        return [f"-DCMAKE_CXX_STANDARD={self.spec['root'].variants['cxxstd'].value}"]
