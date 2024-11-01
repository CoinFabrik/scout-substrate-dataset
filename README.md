# Scout Substrate Dataset: Audited Substrate Projects

![https://img.shields.io/badge/license-MIT-green](https://img.shields.io/badge/license-MIT-green)

<p align="center">
  <img src="./assets/scout-in-the-dark-cave-0.png" alt="Scout Entering the Cave of Audits" width="300" center />
</p>

Welcome to the **Scout Substrate Dataset**, a collection of thoroughly analyzed audited Substrate pallets, runtime, and node code. This repository serves as a knowledge base for Substrate developers, auditors, and security researchers aiming to identify common Substrate vulnerabilities and improve the security of their projects.

Our goal is to provide a reference point for the community, compiling key security issues found in Substrate projects, facilitating better security practices, and serving as a resource for improving vulnerability detection tools like [Scout](https://www.coinfabrik.com/products/scout/)

### Dataset Breakdown

We have structured the `Scout Substrate Dataset` into the following folders:

- **`/dataset/`**:
  - **`findings.json`**: A comprehensive list of all findings across the audited projects.
- **`/audited-projects/`**:
  - Contains directories for each audited project, labeled by `[audited-project-id]-[project-name]`.
  - Each directory contains:
    - **`[project-audit].pdf`**: The original audit report in PDF format.
    - **`findings-[audited-project-id]-[project-name].json`**: JSON file containing the project-specific findings.

For information on accessing the full codebase, including audited and remediated code for each project, refer to the [Accessing Audited Project Code](#accessing-audited-project-code) section below.

## Audited Projects

This dataset currently contains the following audited Substrate projects:

| Audited Project ID | Project Name  | Auditor                |
| ------------------ | ------------- | ---------------------- |
| 1                  | Parallel      | Trail of Bits          |
| 2                  | Parallel      | SlowMist               |
| 3                  | Ava Protocol  | Slow Mist              |
| 5                  | Nodle         | Halborn                |
| 6                  | Reef Chain    | Halborn                |
| 7                  | Manta Network | Veridise               |
| 8                  | Manta Network | Halborn                |
| 9                  | Manta Network | Veridise               |
| 10                 | Astar         | Security Research Labs |
| 11                 | Astar         | Zellic                 |

More projects will be added as new audits are analyzed.

## Accessing Audited Project Code

For access to the complete codebase associated with this dataset, including tagged archives for each audit finding and remediation, visit the [Scout Substrate Dataset Code](https://github.com/CoinFabrik/scout-substrate-dataset-code) repository. Download bundles by tag or commit hash, enabling a full historical view of each project version.

## About CoinFabrik

We - [CoinFabrik](https://www.coinfabrik.com/) - are a research and development company specialized in Web3, with a strong background in cybersecurity. Founded in 2014, we have worked on over 500 blockchain-related projects, EVM-based and also for Solana, Algorand, and Polkadot. Beyond development, we offer security audits through a dedicated in-house team of senior cybersecurity professionals, currently working on code in Substrate, Solidity, Clarity, Rust, and TEAL.

Our team has an academic background in computer science and mathematics, with work experience focused on cybersecurity and software development, including academic publications, patents turned into products, and conference presentations. Furthermore, we have an ongoing collaboration on knowledge transfer and open-source projects with the University of Buenos Aires.

## License

Scout is licensed and distributed under a MIT license. [Contact us](https://www.coinfabrik.com/) if you're looking for an exception to the terms.
