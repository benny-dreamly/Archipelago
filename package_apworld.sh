#!/bin/bash

VERSION="2.0.0"

# Ensure the versioned release directory exists
mkdir -p "releases/${VERSION}"

# Define exclude patterns
EXCLUDES=(
  ".DS_Store"
  "__pycache__/*"
  "__MACOSX/*"
  "s4ap_0.1.11b_Messages.txt"
  "items-testing-please-ignore-me.json"
)

# Change to the worlds directory and zip sims4 folder
(
  cd worlds || exit
  zip -r "../releases/${VERSION}/sims4.apworld" "sims4" -x "${EXCLUDES[@]}"
)