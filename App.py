name: Build Anime Official APK

on:
  workflow_dispatch:
  push:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Build APK with Buildozer
        uses: ArtemSBulgakov/buildozer-action@v1
        with:
          workdir: .
          buildozer_version: stable
          command: buildozer android debug

      - name: Upload APK
        uses: actions/upload-artifact@v4
        with:
          name: Anime-Official-APK
          path: bin/*.apk
