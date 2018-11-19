#!/bin/bash

function usage {
  echo "$0 [manifest-url] [zp-model]";
  exit;
}

if [ $# != 2 ]
then
  usage
fi

MANIFEST_URL=$1
MODEL=$2

XML_MANIFEST=$(curl --silent $MANIFEST_URL) 
PATH=$(echo $MANIFEST_URL | sed -r 's@(.*)/.*@\1@g')

echo $PATH
VERSION=$(echo $XML_MANIFEST | /usr/bin/xmllint --xpath "string(update_manifest/update_list/image[@model=$MODEL])" -)

UBOOT_PATH=$PATH${VERSION/^//}-1-$MODEL.upd # Bootloader
SYSTEM_PATH=$PATH${VERSION/^//}-2-$MODEL.upd

echo "UBoot: $UBOOT_PATH"
echo "System: $SYSTEM_PATH"
