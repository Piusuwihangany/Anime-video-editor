
[app]

title = Anime Official
package.name = animeofficial
package.domain = org.animeofficial

source.dir = .
source.include_exts = py,kv,png,jpg,jpeg,atlas,json,txt

version = 1.0

requirements = python3,kivy

orientation = portrait
fullscreen = 0

[buildozer]

log_level = 2
warn_on_root = 1

[app]

android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a

p4a.bootstrap = sdl2
