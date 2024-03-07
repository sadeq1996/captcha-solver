from setuptools import setup, Extension

# Define the extension module
extension_mod = Extension(
    name="CAPTCHA_OCR",
    sources=["CAPTCHA_OCR.py"],
)

# Define the setup configuration
setup(
    name="CAPTCHA_OCR",
    version="1.0",
    description="Your Python module",
    ext_modules=[extension_mod]
)
