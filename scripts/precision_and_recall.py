import json
import csv
from pathlib import Path

def parse_location(location: str):
    """
    Parse the location field to extract a list of entries.
    Each entry will be a tuple (crate, file, line) suitable for CSV output.
    
    Rules:
    - If Cargo.toml is found in a segment, return one entry with file="Cargo.toml" and no line.
    - Otherwise, try to extract lines.
    - If no lines are found for that file (and it's not Cargo.toml), discard that file.
    - If multiple lines or line ranges are specified, return multiple entries (one per line extracted).
    
    Returns:
      A list of tuples: [(crate, file, line), ...]
      If no valid entries, return an empty list.
    """
    results = []
    # Split the location by space to handle multiple files potentially separated by space
    segments = location.split()

    for segment in segments:
        # Handle Cargo.toml files
        if "Cargo.toml" in segment:
            # Just Cargo.toml, no lines
            results.append(("", "Cargo.toml", ""))
            continue

        # Attempt to split by colon to identify file and line parts
        # Note that some segments may have multiple colon-separated lines, like file:line-info
        parts = segment.split(":")
        path_part = parts[0].strip()

        if len(parts) > 1:
            line_part = ":".join(parts[1:]).strip()
        else:
            line_part = ""

        # Determine crate and file from path_part
        src_index = path_part.find("src/")
        if src_index != -1:
            crate = path_part[:src_index].rstrip("/").strip()
            file = path_part[src_index:].strip()
        else:
            # If no "src/" found, split by last slash
            if "/" in path_part:
                last_slash = path_part.rfind("/")
                crate = path_part[:last_slash].strip()
                file = path_part[last_slash+1:].strip()
            else:
                crate = ""
                file = path_part.strip()

        # Process line_part
        # It can contain multiple lines or line ranges separated by commas.
        # For line ranges: we only take the first line of the range.
        # If empty or no lines found, discard this file unless it was Cargo.toml (already handled above).

        if line_part:
            lines = []
            line_specs = line_part.split(",")
            for spec in line_specs:
                spec = spec.strip()
                if "-" in spec:
                    # range
                    start_line = spec.split("-")[0].strip()
                    if start_line.isdigit():
                        lines.append(start_line)
                else:
                    # single line
                    if spec.isdigit():
                        lines.append(spec)

            # Only add entries if we found valid lines
            for ln in lines:
                results.append((crate, file, ln))
        else:
            # No line_part means no lines - discard this file
            # (Only Cargo.toml files can have no lines and still be included)
            pass

    return results


if __name__ == "__main__":
    base_dir = Path(__file__).resolve().parent.parent
    input_file = base_dir / "dataset" / "findings-linear-filtered.json"
    output_file = base_dir / "dataset" / "findings-precision-and-recall.csv"

    with input_file.open("r") as f:
        data_in = json.load(f)

    # CSV columns: scout commit, detector, project, repository, commit, crate, file, line, truth
    # We leave scout commit, detector, truth empty as instructed.
    # commit is the remediated commit if available, otherwise audited_commit.
    # project from project_name
    # repository from repository
    # crate, file, line from location parsing

    with output_file.open("w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["scout commit","detector","project","repository","commit","crate","file","line","truth"])

        for finding in data_in:
            project = finding.get("project_name","")
            repository = finding.get("repository","")
            if repository and not repository.endswith(".git"):
                repository += ".git"
            # commit: use reported_remediated_commit if not null else audited_commit
            commit = finding.get("reported_remediated_commit")
            if not commit:
                commit = finding.get("audited_commit","")

            location = finding.get("location","")
            entries = parse_location(location)

            # If no entries (no lines and no Cargo.toml), produce no output for that finding
            # If we do need at least one entry per finding (if no lines?), handle that here:
            if not entries:
                # If we must produce something even if no lines and no Cargo.toml, uncomment next line:
                # writer.writerow(["","",project,repository,commit,"","","",""])
                # But as per instructions, if no valid lines or Cargo.toml, don't output.
                continue
            else:
                for (crate, file, ln) in entries:
                    writer.writerow(["","",project,repository,commit,crate,file,ln,""])

    print(f"CSV saved to {output_file}")
