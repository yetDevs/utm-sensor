from cx_Freeze import setup, Executable

setup(
    name = "UTM Sensor",
    options = {"build_exe": {"packages":["numpy"], "include_files":["assets/"]}},
    version = "0.1",
    description = "UTM Sensor script",
    executables = [Executable("utm-sensor.py")],
)