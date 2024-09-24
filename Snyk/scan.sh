#!/bin/bash

# Create a directory for the scan results
results_dir="scan_results"
mkdir -p $results_dir

# Get a list of active Docker images
images=$(docker images --format "{{.Repository}}:{{.Tag}}" | grep -v "<none>:<none>")

# Scan each image and save the result to a separate file
for image in $images
do
    # Create a valid filename by replacing ":" with "_" and "/" with "_"
    filename=$(echo "$image" | tr ':/' '__')
    
    # Define the output file path
    output_file="$results_dir/${filename}.md"
    
    # Ensure the directory exists
    mkdir -p "$(dirname "$output_file")"
    
    # Scan the image and save the result
    echo "Scanning $image..."
    echo "**Scanning $image**" > $output_file
    echo '```' >> $output_file
    snyk container test $image >> $output_file
    echo '```' >> $output_file
done
