# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from spack.pkg.k4.key4hep_stack import Ilcsoftpackage


class Marlin(CMakePackage, Ilcsoftpackage):
    """Linear Collider framework"""

    homepage = "https://github.com/iLCSoft/marlin"
    git = "https://github.com/iLCSoft/marlin.git"
    url = "https://github.com/iLCSoft/marlin/archive/v01-05.tar.gz"

    maintainers("vvolkl")

    version("master", branch="master")

    version(
        "1.19.5",
        sha256="d0ad571fa7f47badf874bd577f644686ad85175c622a7d9797501bdfa5ea93f6",
    )
    version(
        "1.19.4",
        sha256="1cefd23065a8e554ddaf38961457f67497bc8a3eb940bb037b4ca60443e0a0d2",
    )
    version(
        "1.19.3",
        sha256="b581e4e80b67979e3dae9b2c926848e3de005f30e6193ee6b3b6e746e8ae6b6b",
    )
    version(
        "1.19.2",
        sha256="13e51a1d46540df55596853612c13314860f8299e4caf356e2070780ecddc7c2",
    )
    version(
        "1.19.1",
        sha256="9737c21a6273d9939952a4fb2bae23fe9739a3381b1e2c98ede6d0124ae92fdf",
    )
    version(
        "1.19",
        sha256="e3a109da04efb6f0ce904aba864fe8ce4dcfaaa6f910a68374ca499efc4a14dd",
    )
    version(
        "1.18",
        sha256="e556302fb6cc48b999a011122479dd51c9e99f6a256771e4a5a154040c7fa2dc",
    )
    version(
        "1.17.1",
        sha256="b928c6072bbf8db5fdb3b9716227b8724dfc90182967212cd9f2f51ceb760dd0",
    )
    version(
        "1.17",
        sha256="076acc3a91b7e2e253f338395a8e56bf00498e6aa1a118d3e7bde84f1065d3d6",
    )

    variant("gui", default=False, description="builds with qt gui")
    variant("lccd", default=False, description="builds with lccd")
    variant("clhep", default=True, description="builds with clhep")
    variant("aida", default=True, description="builds with aida")
    variant("doc", default=False, description="build doxygen documentation")

    depends_on("cxx", type="build")

    depends_on("ilcutil")
    depends_on("gear")
    depends_on("lcio")
    depends_on("lcio@2.19:", when="@1.19:")
    depends_on("doxygen", when="+doc")
    depends_on("qt@:4.99.99", when="+gui")
    depends_on("lccd", when="+lccd")
    depends_on("clhep", when="+clhep")
    depends_on("raida", when="+aida")

    def cmake_args(self):
        args = []
        args.append(self.define_from_variant("INSTALL_DOC", "doc"))
        args.append(self.define_from_variant("MARLIN_GUI", "gui"))
        args.append(self.define_from_variant("MARLIN_LCCD", "lccd"))
        args.append(self.define_from_variant("MARLIN_CLHEP", "clhep"))
        args.append(self.define_from_variant("MARLIN_AIDA", "aida"))
        args.append(
            f"-DCMAKE_CXX_STANDARD={self.spec['lcio'].variants['cxxstd'].value}"
        )
        if "aida" in self.spec:
            args.append("-DAIDA_DIR=%s" % self.spec["aida"].prefix)
        return args
