[app]
title = Zenith Messenger
package.name = zenith
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy==2.3.0,requests,urllib3,certifi

orientation = portrait
osx.python_version = 3
osx.kivy_version = 1.9.1
fullscreen = 0

android.archs = arm64-v8a
android.allow_backup = True
android.api = 31
android.minapi = 21
android.sdk = 31
android.ndk_api = 21
android.permissions = INTERNET

[buildozer]
log_level = 2
warn_on_root = 1
