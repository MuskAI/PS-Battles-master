# 说明
作者之前给的脚本下载不行，然后自己写了一个简单的爬虫，一个文件是生成txt url的 download是开始下载的

# PS-Battles
Repository of the [PS-Battles dataset, an image collection for image manipulation detection](https://arxiv.org/abs/1804.04866).

# Download instructions

## Ubuntu
On ubuntu, simply run the provided ```download.sh``` script. It will download all images from the provided .tsv-files and verify them with the provided sha256sum.

## MacOS
On Mac, there is no ```sha256sum``` command.
 We recommend either running the following command first: ```function sha256sum() { shasum -a 256 "$@" ; } && export -f sha256sum```
 OR you can either change the command in the ```download.sh``` script to ```shasum -a 256```
 OR you can disable checksum-verification in the provided script.

## Windows
We do not provide a download script for windows, you can use your preferred scripting language and download tool to download images using the links in the provided .tsv-files.

# Bibtex
```
@article{heller2018psBattles,
  author        = {Silvan Heller and Luca Rossetto and Heiko Schuldt},
  title         = {{The PS-Battles Dataset -- an Image Collection for Image Manipulation Detection}},
  journal       = {CoRR},
  volume        = {abs/1804.04866},
  year          = {2018},
  url           = {http://arxiv.org/abs/1804.04866},
  archivePrefix = {arXiv},
  eprint        = {1804.04866}
}
```
