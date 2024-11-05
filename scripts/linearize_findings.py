from pathlib import Path
import json

def stringize_loc_lines_item(item):
    if isinstance(item, dict):
        return f"{item['from']}-{item['to']}"
    else:
        return str(item)

def stringize_loc_item(item):
    rv = item["file_path"]

    if item["lines"] is None:
        return rv
    
    rv += ":"
    rv += ",".join(map(stringize_loc_lines_item, item["lines"]))

    return rv

def stringize_location(loc):
    if loc is None:
        return None
    
    return "\n".join(map(stringize_loc_item, loc))
    


def audit_entries(e):
    common_fields = {k:v for k,v in e.items() if k != 'findings'}
    for i, f in enumerate(e['findings']):
        yield dict(
            issue_index = i,
            location = stringize_location(f['location']),
            **{k:v for k,v in f.items() if k != 'location'},
            **common_fields,
        )

def linearize_findings(input_path, output_path):
    with open(input_path, "r") as f:
        data_in = json.load(f)

    data_out = []
    for e in data_in:
        for ee in audit_entries(e):
            data_out.append(ee)

    with open(output_path, "w") as f:
        json.dump(data_out, f, indent=2)

if __name__ == "__main__":
    # Define input and output paths relative to this script's location
    base_dir = Path(__file__).resolve().parent.parent  # Move up from 'utils' to root
    input_directory = base_dir / "audited-projects"
    input_path = base_dir / "dataset" / "findings.json" 
    output_path = base_dir / "dataset" / "findings-linear.json" 
       
    # Run aggregation for full findings.json without exclusions
    linearize_findings(input_path, output_path)
    print(f"Linearized findings saved to {output_path}")