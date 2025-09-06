#!/bin/bash

read -rp "file path: " source


destination="$source/new_assets"
mkdir -p "$destination"

prefix=""
read -rp "add prefix (y/n): " ans
if [[ "$ans" == "y" || "$ans" == "Y" ]]; then
    read -rp "prefix: " prefix
fi

postfix=""
read -rp "add postfix (y/n): " ans
if [[ "$ans" == "y" || "$ans" == "Y" ]]; then
    read -rp "postfix: " postfix
fi


for file in "$source"/*; do
    if [[ -f "$file" ]]; then
        filename=$(basename "$file")
        name="${filename%.*}"
        ext="${filename##*.}"


        new_name=$(echo "$name" | tr '[:upper:]' '[:lower:]' | tr ' ' '_')


        new_name="$prefix$new_name$postfix.$ext"


        cp "$file" "$destination/$new_name"
        echo "Copied: $filename -> $new_name"
    fi
done
