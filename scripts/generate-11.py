import json
import pathlib as pl

def findings():
    return (
        {
            "title": "Weight calculation",
            "repository": "https://github.com/AstarNetwork/Astar",
            "audited_commit": "fc14b13401e1fb5e7391715fc76a308204173802",
            "reported_remediated_commit": None,
            "location": None,
            "reported_impact": "Low",
            "reported_likelihood": "Low",
            "cwe_classification": None,
            "vulnerability_class_audit": "Coding Mistakes",
            "description": "All the assets pallet functions exposed by the chain extension are weighted with a constant amount. \
The weight of some operations is charged using the same quantity that the assets pallet benchmarks \
have computed. However, other operations only charge the weight of one runtime database read \
operation — T::DbWeight::get().reads(1_u64).\n\
Two functions, MetadataSymbol and MetadataName, operate on a variable amount of data, but they \
also only account for one runtime database read operation.",
            "description_summary": "Constant weight for functions, ignores variable data in MetadataSymbol & MetadataName."
        }
    ,)

def audit_dict():
    return {
        "audited_project_id": 11,
        "project_name": "Astar",
        "auditor": "Zellic",
        "audit_link": "https://github.com/polkadot-assurance-legion/pal-docs/blob/main/audits/24h1/astar-zellic-2401.pdf",
        "findings": findings()
    }

with open(pl.Path(__file__).parent / ".." / "audited-projects" / "11-Astar" / "findings-11-Astar.json", "w") as f:
    json.dump(audit_dict(), f, indent=2)