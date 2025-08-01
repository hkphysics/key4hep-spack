from spack.package import *
from spack.pkg.k4.key4hep_stack import Key4hepPackage


class Fccsw(CMakePackage, Key4hepPackage):
    """Software framework of the FCC project"""

    homepage = "https://github.com/HEP-FCC/FCCSW/"
    url = "https://github.com/HEP-FCC/FCCSW/archive/v0.16.tar.gz"
    git = "https://github.com/HEP-FCC/FCCSW.git"

    maintainers("vvolkl")

    version("master", branch="master")

    version(
        "1.0pre11",
        sha256="79a1b424069544a4be0084ced91506084a09265c3e171bb3f409b7362e1f6677",
    )
    version(
        "1.0pre10",
        sha256="7d7cd655a557b272e816b399c068fa5e6ee1c72491bb7e0dffa552557b949cbf",
    )

    version("1.0pre09", tag="v1.0pre09")
    version("1.0pre08", tag="v1.0pre08")
    version("1.0pre07", tag="v1.0pre07")
    version("1.0pre06", tag="v1.0pre06")
    version("1.0pre05", tag="v1.0pre05")

    depends_on("cxx", type="build")

    depends_on("gaudi")
    depends_on("k4fwcore")
    depends_on("k4gen")
    depends_on("k4simdelphes")
    depends_on("fccdetectors")
    depends_on("k4simgeant4")
    depends_on("k4reccalorimeter")
    depends_on("k4geo")
    depends_on("fccanalyses")
    depends_on("root")

    def cmake_args(self):
        args = []
        args.append(
            f"-DCMAKE_CXX_STANDARD={self.spec['root'].variants['cxxstd'].value}"
        )
        return args

    def setup_dependent_build_environment(self, env, dependent_spec):
        env.set("FCCSW", self.prefix.share.FCCSW)
        env.prepend_path("PYTHONPATH", self.prefix.python)

    def setup_run_environment(self, env):
        env.set("FCCSW", self.prefix.share.FCCSW)
        env.prepend_path("PYTHONPATH", self.prefix.python)

    def setup_build_environment(self, env):
        self.setup_run_environment(env)
