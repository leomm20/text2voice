from cx_Freeze import setup, Executable


setup(
    name="guifoo",
    version="0.1",
    author='Leonardo Maggiotti',
    description="Text 2 Voice",
    executables=[Executable("texto_a_voz_gtts.py")],
)
