import argparse
import sys
import subprocess
import json
import hashlib
import pathlib

def argparser():
    p = argparse.ArgumentParser(description='Upload code referenced in the dataset issues')
    p.add_argument(
        '-r', 
        '--remote', 
        default="https://github.com/CoinFabrik/scout-substrate-dataset-code.git", 
        help='Git repository where the relevant commits will be pushed to (default:%(default)s)'
    )
    p.add_argument(
        '-w', 
        '--workdir',
        help='Directory where the original git repositories will be cloned (default: new temp dir)',
        required=True
    )
    p.add_argument('json', nargs="+", help="JSON files to be processed")
    return p

def main(argv):
    args = argparser().parse_args(argv[1:])
    process_jsons(
        jsons=args.json, 
        remote=args.remote, 
        workdir=args.workdir
    )

def process_jsons(*,jsons, remote, workdir):
    for fname in jsons:
        with open(fname, "r") as f:
            data = json.load(f)
            project_id = data['audited_project_id']
            for index, e in enumerate(data['findings']):
                repository = e['repository']
                audited_commit = e['audited_commit']
                reported_remediated_commit = e['reported_remediated_commit']
                process_finding(
                    workdir=workdir,
                    remote=remote,
                    project_id=project_id,
                    index=index,
                    repository=repository,
                    audited_commit=audited_commit,
                    reported_remediated_commit=reported_remediated_commit
                )

def process_finding(
    *, 
    remote, 
    workdir, 
    project_id, 
    index, 
    repository, 
    audited_commit, 
    reported_remediated_commit
):
    print(f"Processing {project_id=} {index=}")
    base_workdir = pathlib.Path(workdir)
    target_dir = hashlib.sha256(repository.encode('utf-8')).hexdigest()

    subprocess.run(
        ('git', 'clone', repository, target_dir),
        cwd=base_workdir
    )

    local_workdir = base_workdir / target_dir

    tag_and_push(workdir=local_workdir, commit=audited_commit, tag=f"audited-{project_id}-{index}", remote=remote)

    if reported_remediated_commit is not None:
        tag_and_push(workdir=local_workdir, commit=reported_remediated_commit, tag=f"remediated-{project_id}-{index}", remote=remote)


def tag_and_push(*, workdir, commit, tag, remote):
    subprocess.run(
        ('git', 'checkout', commit),
        check=True,
        cwd=workdir   
    )

    subprocess.run(
        ('git', 'tag', '-d', tag),
        cwd=workdir
    )

    subprocess.run(
        ('git', 'tag', tag),
        check=True,
        cwd=workdir 
    )

    subprocess.run(
        ('git', 'push', remote, 'tag', tag, '--force'),
        check=True,
        cwd=workdir
    )



if __name__ == '__main__':
    main(sys.argv)