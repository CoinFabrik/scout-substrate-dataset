# Scout Substrate Dataset: Audited Substrate Projects

![https://img.shields.io/badge/license-MIT-green](https://img.shields.io/badge/license-MIT-green)

<p align="center">
  <img src="./assets/scout-in-the-dark-cave-0.png" alt="Scout Entering the Cave of Audits" width="300" center />
</p>

Welcome to the **Scout Substrate Dataset**, a collection of thoroughly analyzed audited Substrate pallets, runtime, and node code. This repository serves as a knowledge base for Substrate developers, auditors, and security researchers aiming to identify common Substrate vulnerabilities and improve the security of their projects.

Our goal is to provide a reference point for the community, compiling key security issues found in Substrate projects, facilitating better security practices, and serving as a resource for improving vulnerability detection tools like [Scout](https://www.coinfabrik.com/products/scout/)

## Dataset Breakdown

We have structured the `Scout Substrate Dataset` into the following folders:

- **`/audited-projects/`**:
  - Contains directories for each audited project, labeled by `[audited-project-id]-[project-name]`.
  - Each directory contains:
    - **`[project-audit].pdf`**: The original audit report in PDF format.
    - **`findings-[audited-project-id]-[project-name].json`**: JSON file containing the project-specific findings.

### Generate Dataset

To generate the dataset, run `make dataset`. It will generate the **`/dataset/`** directory with the following files:

- **`findings.json`**: A comprehensive list of all findings across the audited projects.
- **`findings-linear.json`**: The `findings.json` file further processed to be imported into Hugging Face.

### Accessing Audited Project Code

For access to the complete codebase associated with this dataset, including tagged archives for each audit finding and remediation, visit the [Scout Substrate Dataset Code](https://github.com/CoinFabrik/scout-substrate-dataset-code) repository. Download bundles by tag or commit hash, enabling a full historical view of each project version.

## Audited Projects

This dataset currently contains the following audited Substrate projects:

| Audited Project ID | Project Name              | Auditor                |
| ------------------ | ------------------------- | ---------------------- |
| 1                  | Parallel                  | Trail of Bits          |
| 2                  | Parallel                  | Slow Mist              |
| 3                  | Ava Protocol              | Slow Mist              |
| 4                  | Pendulum                  | Hacken                 |
| 5                  | Nodle                     | Halborn                |
| 6                  | Reef Chain                | Halborn                |
| 7                  | Manta Network             | Veridise               |
| 8                  | Manta Network             | Halborn                |
| 9                  | Manta Network             | Veridise               |
| 10                 | Astar                     | Security Research Labs |
| 11                 | Astar                     | Zellic                 |
| 12                 | Bifrost                   | Oak Security           |
| 13                 | HydraDX                   | Security Research Labs |
| 14                 | LAOS                      | CoinFabrik             |
| 15                 | Acala                     | Code4Arena             |
| 16                 | PolkadotRunetimeTemplates | Security Research Labs |
| 17                 | Acala                     | Trail of Bits          |
| 18                 | Astar                     | Quantstamp             |
| 19                 | Astar                     | Quantstamp             |
| 20                 | PolkadotRuntimeTemplates  | Security Research Labs |

## Substrate Issue Classes

As we analyzed various audit reports and their respective findings, we observed a range of issue classes applied by auditing companies, each recorded under the field `vulnerability_class_audit` in the dataset. Despite some variation in classification, certain categories tend to recur.

To provide a common classification across the reviewed audits, we provide a `vulnerability_class_scout` field for each finding. Below, we list several issue classes that we find applicable to **Substrate pallets**, **runtime**, and **node code**, and that we applied for this field.

- **Dependency**: Issues related to using vulnerable or outdated dependencies in the project. These vulnerabilities could introduce potential risks due to unmaintained or insecure libraries.  
  _Example Projects with Findings in this Class: [1-Parallel], [2-Parallel], [5-Nodle]_

- **Arithmetic**: Arithmetic-related vulnerabilities, such as unchecked arithmetic operations, saturating calculations, and overflows. These issues can result in unexpected behaviors or crashes due to incorrect handling of mathematical operations.  
  _Example Projects with Findings in this Class: [3-AvaProtocol], [6-ReefChain], [7-MantaNetwork]_

- **Weight Management**: Incorrect or missing weight calculations, including static versus dynamic weight handling, or failure to account for changes in workload. This can lead to DoS vulnerabilities as resource costs are underestimated.  
  _Example Projects with Findings in this Class: [7-MantaNetwork], [10-Astar], [4-Pendulum]_

- **Error Handling and Validation**: Inadequate error handling and validation, such as improper use of `DispatchError`, missing error checks, and insufficient input validation. These issues can cause unexpected program flows and unauthorized access.  
  _Example Projects with Findings in this Class: [5-Nodle], [4-Pendulum], [1-Parallel]_

- **Denial of Service (DoS) and Spamming**: Vulnerabilities that could lead to potential denial of service or spamming, often tied to extrinsic calls or weights.  
  _Example Projects with Findings in this Class: [4-Pendulum], [10-Astar]_

- **Business Logic**: Issues in project-specific rules or logic, leading to exploitable or unintended behaviors.  
  _Example Projects with Findings in this Class: [7-MantaNetwork], [5-Nodle]_

- **Code Quality**: Issues impacting readability, maintainability, or structure, increasing risk of errors.  
  _Example Projects with Findings in this Class: [7-MantaNetwork], [5-Nodle]_

- **TBD**: Findings or issues with pending classification.

We understand that this classification depends largely on expert criteria and that a finding could potentially be assigned to multiple classes simultaneously. We plan to further refine this classification as we add more audited projects to the dataset.

## About CoinFabrik

We - [CoinFabrik](https://www.coinfabrik.com/) - are a research and development company specialized in Web3, with a strong background in cybersecurity. Founded in 2014, we have worked on over 500 blockchain-related projects, EVM-based and also for Solana, Algorand, and Polkadot. Beyond development, we offer security audits through a dedicated in-house team of senior cybersecurity professionals, currently working on code in Substrate, Solidity, Clarity, Rust, and TEAL.

Our team has an academic background in computer science and mathematics, with work experience focused on cybersecurity and software development, including academic publications, patents turned into products, and conference presentations. Furthermore, we have an ongoing collaboration on knowledge transfer and open-source projects with the University of Buenos Aires.

As proud members, and with the support of the [Polkadot Assurance Legion (PAL)](https://github.com/polkadot-assurance-legion/pal-docs), we are pleased to contribute this audited code dataset to the Substrate community, aiming to enhance vulnerability detection and promote security best practices within the Polkadot ecosystem.

## License

The Scout Substrate Dataset is licensed and distributed under the MIT license. [Contact us](https://www.coinfabrik.com/) if you're looking for an exception to the terms.
