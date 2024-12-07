from conan import ConanFile

class CHXRecipe(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "PremakeDeps"

    def requirements(self):
        # Server dependencies
        self.requires("boost/1.86.0")           # General utils
        self.requires("spdlog/1.15.0")          # Logging
        self.requires("fmt/11.0.2")             # Formatting
        self.requires("cpp-httplib/0.18.2")     # HTTP Server
        self.requires("reflect-cpp/0.16.0")     # Struct Serialization
        self.requires("inja/3.4.0")             # HTML Template lib

        # Explicit versions
        self.requires("openssl/3.3.2")          # HTTPS encryption

    def configure(self):
        self.options["cpp-httplib"].with_zlib = True
        self.options["cpp-httplib"].with_openssl = True
        self.options["reflect-cpp"].with_yaml = True
