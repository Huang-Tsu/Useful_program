#!/bin/bash

if [ $# -ne 3 ]; then
  echo "Usage: ./script.sh <src_dir> <dst_dir> <file_type>"
  exit 1
fi

# The source directory
src_dir=$1

# The destination directory
dst_dir=$2

# The target file type
file_type=$3

# Create the destination directory if it doesn't exist
if [ ! -d "$dst_dir" ]; then
  mkdir -p "$dst_dir"
fi

# Find all files of the target file type in the source directory and its sub-directories
find "$src_dir" -type f -name "*.$file_type" | while read file; do
  # Copy each file of the target file type to the destination directory
  cp "$file" "$dst_dir"
done
