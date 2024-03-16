#!/bin/bash

SOURCE_DIR=${1:-"lab_uno"}
RM_LIST=${2:-"2remove"}
TARGET_DIR=${3:-"bakap"}

if [[ ! -d $TARGET_DIR ]]; then
    mkdir -p "$TARGET_DIR"
fi

if [[ ! -f $RM_LIST ]]; then
    echo "Plik $RM_LIST nie istnieje."
    exit 1
fi
if [[ ! -d $SOURCE_DIR ]]; then
    echo "Folder $SOURCE_DIR nie istnieje."
    exit 1
fi

while IFS= read -r line || [[ -n "$line" ]]; do
    if [[ -f "$SOURCE_DIR/$line" ]]; then
        rm -rf "$SOURCE_DIR/$line" 
    fi
done < "$RM_LIST"

ITEM_COUNTER=$(find "$SOURCE_DIR" -maxdepth 1 -type f | wc -l)
if [[ $ITEM_COUNTER -ge 2 ]]; then
    echo "Zostały co najmniej dwa pliki"
    if [[ $ITEM_COUNTER -gt 4 ]]; then
    	echo "Zostało więcej niż 4 pliki"
    else
    	echo "Ale nie więcej niż 4"
    fi
elif [[ $ITEM_COUNTER -eq 1 ]]; then
    echo "W katalogu jest jeden plik"
else
    echo "Terrain ahead, pull up"
fi

current_date=$(date +"%Y-%m-%d")
zip_filename="bakap_$current_date.zip"
zip -r "$zip_filename" "$TARGET_DIR"
