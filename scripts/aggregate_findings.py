import json
import os
from pathlib import Path
from typing import List, Optional

def aggregate_findings(input_dir: Path, output_file: Path, descending: bool = False, files_to_aggregate: Optional[List[Path]] = None, fields_to_exclude: Optional[List[str]] = None):
    findings_data = []
    
    # Use the provided list of files or search for JSON files in the input directory
    if files_to_aggregate is None:
        files_to_aggregate = [Path(root) / file for root, _, files in os.walk(input_dir) for file in files if file.endswith('.json')]
    
    # Traverse the list of files to aggregate
    for file_path in files_to_aggregate:
        if file_path.is_file():  # Ensure it's a file
            with file_path.open('r') as f:
                data = json.load(f)
                if 'audited_project_id' not in data:
                    raise ValueError(f"Missing 'audited_project_id' in file {file_path}")
                
                # Remove specified fields from the top level if needed
                if fields_to_exclude:
                    for field in fields_to_exclude:
                        data.pop(field, None)
                
                # Remove specified fields from each entry in the "findings" list
                if "findings" in data and fields_to_exclude:
                    for finding in data["findings"]:
                        for field in fields_to_exclude:
                            finding.pop(field, None)
                
                findings_data.append(data)
    
    # Sort findings by 'audited_project_id' based on the 'descending' parameter
    findings_data.sort(key=lambda x: x['audited_project_id'], reverse=descending)
    
    # Write aggregated findings to output file
    with output_file.open('w') as f:
        json.dump(findings_data, f, indent=4)

if __name__ == "__main__":
    # Define input and output paths relative to this script's location
    base_dir = Path(__file__).resolve().parent.parent  # Move up from 'utils' to root
    input_directory = base_dir / "audited-projects"
    full_output_path = base_dir / "dataset" / "findings.json"        # Output for full version
    mini_output_path = base_dir / "dataset" / "findings_mini.json"    # Output for mini version
    
    # Optionally, pass a list of specific files to aggregate
    specific_files = None  # Replace with list of Paths if needed
    
    # Run aggregation for full findings.json without exclusions
    aggregate_findings(input_directory, full_output_path, files_to_aggregate=specific_files)
    print(f"Full aggregated findings saved to {full_output_path}")
    
    # Run aggregation for findings_mini.json excluding the "description" field
    fields_to_exclude = ["description"]
    aggregate_findings(input_directory, mini_output_path, files_to_aggregate=specific_files, fields_to_exclude=fields_to_exclude)
    print(f"Mini aggregated findings saved to {mini_output_path}")
