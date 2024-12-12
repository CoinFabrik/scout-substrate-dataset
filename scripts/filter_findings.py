import json
from pathlib import Path

def filter_findings(input_path: Path, output_path: Path):
    with input_path.open("r") as f:
        data_in = json.load(f)

    data_out = []
    for finding in data_in:
        location = finding.get("location")
        
        # Condition 1: If location is None, skip unless location is specifically "Cargo.toml"
        # However, if location is None, it can't be "Cargo.toml". So skip if None.
        if location is None:
            continue

        # Condition 2: If location includes "Cargo.toml", keep the finding even if no line info is specified
        if "Cargo.toml" in location:
            data_out.append(finding)
            continue

        # Condition 3: Otherwise, keep only if lines are specified.
        # Lines are considered specified if there's a colon (':') in the location string,
        # typically indicating filename:line or filename:start-end format.
        if ":" in location:
            data_out.append(finding)

    with output_path.open("w") as f:
        json.dump(data_out, f, indent=2)


if __name__ == "__main__":
    # Paths based on the instructions
    base_dir = Path(__file__).resolve().parent.parent
    input_file = base_dir / "dataset" / "findings-linear.json"
    output_file = base_dir / "dataset" / "findings-linear-filtered.json"
    
    filter_findings(input_file, output_file)
    print(f"Filtered findings saved to {output_file}")
