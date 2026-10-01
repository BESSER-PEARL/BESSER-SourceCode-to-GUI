<div align="center">
  <img src="./docs/source/_static/besser_logo_light.png" alt="BESSER platform" width="500"/>
</div>

[![Python](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12-blue?logo=python&logoColor=gold)](https://pypi.org/project/besser/)
[![PyPI version](https://img.shields.io/pypi/v/besser?logo=pypi&logoColor=white)](https://pypi.org/project/besser/)
[![PyPI - Downloads](https://static.pepy.tech/badge/besser)](https://pypi.org/project/besser/)
[![Documentation Status](https://readthedocs.org/projects/besser/badge/?version=latest)](https://besser.readthedocs.io/en/latest/)
[![PyPI - License](https://img.shields.io/pypi/l/besser)](https://opensource.org/license/MIT)
[![LinkedIn](https://img.shields.io/badge/-LinkedIn-blue?logo=Linkedin&logoColor=white)](https://www.linkedin.com/company/besser-pearl)
[![GitHub Repo stars](https://img.shields.io/github/stars/besser-pearl/besser?style=social)](https://star-history.com/#besser-pearl/besser)

BESSER is a [low-modeling](https://modeling-languages.com/welcome-to-the-low-modeling-revolution/) [low-code](https://lowcode-book.com/) open-source platform. BESSER (Building bEtter Smart Software fastER) is funded thanks to an [FNR Pearl grant](https://modeling-languages.com/a-smart-low-code-platform-for-smart-software-in-luxembourg-goodbye-barcelona/) led by the [Luxembourg Institute of Science and Technology](https://www.list.lu/) with the participation of the [Snt/University of Luxembourg](https://www.uni.lu/snt-en/) and open to all your contributions!

The BESSER low-code platform is built on top of [B-UML](https://besser.readthedocs.io/en/latest/buml_language.html) our Python-based personal interpretation of a "Universal Modeling Language" (yes, heavily inspired and a simplified version of the better known UML, the Unified Modeling Language).
With B-UML you can specify your software application and then use any of the [code-generators available](https://besser.readthedocs.io/en/latest/generators.html) to translate your model into executable code suitable for various applications, such as Django web apps or database structures compatible with SQLAlchemy.

This repository contains the backend foundation for the ecosystem: the
metamodel, code generators, notations, utilities, and services that drive the web modeling editor and the Python SDK. The editor's frontend is maintained in the companion [BESSER_WME_standalone](https://github.com/BESSER-PEARL/BESSER_WME_standalone) repository and is included here only as a submodule for local deployments.

**Check out the [BESSER Web Modeling Editor online](https://editor.besser-pearl.org/)**
![BESSER Web Modeling Editor Demo](./docs/source/img/besser_new.gif)

**Check out the official [documentation](https://besser.readthedocs.io/en/latest/)**

## Basic Installation

BESSER works with Python 3.10+. We recommend creating a virtual environment (e.g. [venv](https://docs.python.org/3/tutorial/venv.html), [conda](https://docs.conda.io/en/latest/)).

The latest stable version of BESSER is available in the Python Package Index (PyPi) and can be installed using

    $ pip install besser

BESSER can be used with any of the popular IDEs for Python development such as [VScode](https://code.visualstudio.com/), [PyCharm](https://www.jetbrains.com/pycharm/), [Sublime Text](https://www.sublimetext.com/), etc.

## Running BESSER Locally

If you are interested in developing new code generators or designing BESSER extensions, you can download and modify the full codebase, including tests and examples.

### Step 1: Clone the repository

    $ git clone https://github.com/BESSER-PEARL/BESSER.git
    $ cd BESSER

### Step 2: Create a virtual environment

Run the setup script to create a virtual environment (if not already created), install the requirements, and configure the ``PYTHONPATH``. This ensures compatibility with IDEs (like VSCode) that may not automatically set the ``PYTHONPATH`` for recognizing *besser* as an importable module.

    $ python setup_environment.py

**Note:** Each time you start your IDE, run the `setup_environment.py` script to ensure the environment is properly configured.

### Step 3: Run an example

To verify the setup, you can run a basic example.

    $ cd tests/BUML/metamodel/structural/library
    $ python library.py

## Examples
If you want to try examples, check out the [BESSER-examples](https://github.com/BESSER-PEARL/BESSER-examples) repository!

## Contributing

We encourage contributions from the community and any comment is welcome!

If you are interested in contributing to this project, please read the [CONTRIBUTING.md](CONTRIBUTING.md) file.
You can also explore our step-by-step [Contributor Guide](https://besser.readthedocs.io/en/latest/contributor_guide.html) and the dedicated [AI Assistant Guide](https://besser.readthedocs.io/en/latest/ai_assistant_guide.html) to understand the workflows and expectations before opening a pull request.

## GUI Re-generation: Source Code to B-UML

This repository includes an extension to BESSER for **automated GUI re-generation** from HTML/CSS source code, as described in:

> **Integrating LLMs and Model-Driven Engineering for Automated GUI Re-generation**  
> Atefeh Nirumand, Jordi Cabot — Luxembourg Institute of Science and Technology (LIST)

The approach takes HTML/CSS web pages as input and automatically produces platform-independent B-UML models (Structural + IFML-like GUI), optionally enhances them using HCI principles, and re-generates executable web applications via deterministic model-to-code generation.

### Overview

The pipeline consists of two core phases and two optional refinement phases:

1. **LLM-based Code-to-Model Extraction** *(Core)* — Derives a Structural (data) model and an IFML-like GUI model from HTML/CSS source files using LLM-assisted prompting.
2. **LLM-based Model Enhancement guided by HCI Principles** *(Optional)* — Refines the extracted IFML-like GUI model according to established HCI principles (Usefulness, Usability, Findability, Desirability) and exports an SVG-based visual representation.
3. **Human-in-the-Loop Interaction** *(Optional)* — Allows designers to inspect, edit, and refine the SVG representation in tools such as Figma before final code generation.
4. **Deterministic Model-to-Code Generation** *(Core)* — Consumes the Structural and IFML-like GUI models and produces executable applications (Django or React) with integrated CRUD logic and styling.

The pipeline handles both single-page and multi-page applications, automatically binding inter-page navigation relationships into the unified GUI model.

### Key Results (evaluated on 200 real-world web pages)

| Metric | Result |
|--------|--------|
| GUI extraction precision | 99% |
| GUI extraction recall | 94% |
| GUI extraction F-measure | 97% |
| End-to-end fidelity score | 0.860 |
| Multi-page navigation fidelity | 100% (P/R/F1) |
| HCI enhancement user preference | 74.7% (blind study, 34 participants) |

### Relevant Source Code

The implementation is located under `besser/BUML/notations/`:

- **`sourceCode_to_structural/`** — Extracts the Structural (data) model from HTML/CSS source code. Uses an LLM to generate a PlantUML class diagram, then refines and converts it to a B-UML `DomainModel`.
  - Entry point: `sourceCode_to_structural.py` → `source_code_to_structural(api_key, input_folder, output_folder, additional_info_path)`
  - Supports single-page (`one_page.py`) and multi-page (`multiple_pages.py`) workflows.

- **`sourceCode_to_buml/`** — Extracts the IFML-like GUI model from HTML/CSS source code. Uses direct prompting + self-improvement prompting to generate a Python-serialized B-UML GUI model, then generates an SVG representation and optionally applies HCI-based enhancements.
  - Entry point: `sourceCode_to_buml.py` → `source_code_to_buml(api_key, input_folder, ...)`
  - Supports single-page (`one_page.py`) and multi-page (`multiple_pages.py`) workflows.
  - Optional CSS styling file and navigation image inputs for improved fidelity.

### Usage

```python
from besser.BUML.notations.sourceCode_to_buml.sourceCode_to_buml import source_code_to_buml

source_code_to_buml(
    api_key="<your-openai-api-key>",
    input_folder="path/to/html/folder",
    # Optional inputs for multi-page applications:
    navigation_image_path="path/to/navigation_diagram.png",
    pages_order_file_path="path/to/pages_order.txt",
    additional_info_path="path/to/additional_info.txt",
    styling_file_path="path/to/css/folder",
    output_folder="path/to/output",
)
```

For Structural model extraction only:

```python
from besser.BUML.notations.sourceCode_to_structural.sourceCode_to_structural import source_code_to_structural

source_code_to_structural(
    api_key="<your-openai-api-key>",
    input_folder="path/to/html/folder",
    output_folder="path/to/output",
    additional_info_path="path/to/additional_info.txt",  # optional
)
```

The functions automatically detect whether the input folder contains one or multiple HTML files and dispatch to the appropriate single-page or multi-page pipeline.

### Output Structure

```
output/
├── plantuml/
│   └── generated_plantuml.puml    # Intermediate PlantUML structural model
├── buml/
│   └── model.py                   # B-UML Structural (DomainModel) representation
├── gui_model/
│   └── generated_gui_model.py     # B-UML IFML-like GUI model
└── hci_enhanced/
    └── enhanced_svg/              # HCI-enhanced SVG representations
```

### Evaluation Data

The full replication package — datasets, generated artifacts, and evaluation results for all eight research questions — is available in the [`Evaluation/`](./Evaluation/) directory.

---

## How to cite BESSER

This repository has the CITATION.cff file, which activates the "Cite this repository" button in the About section (right side of the repository). The citation is in APA and BibTex format.

## Code of Conduct

At BESSER, our commitment is centered on establishing and maintaining development environments that are welcoming, inclusive, safe and free from all forms of harassment. All participants are expected to voluntarily respect and support our [Code of Conduct](CODE_OF_CONDUCT.md).

## Governance

The development of this project follows the governance rules described in the [GOVERNANCE.md](GOVERNANCE.md) document.

## Contact
You can reach us at: [info@besser-pearl.org](mailto:info@besser-pearl-org)

Website: https://besser-pearl.org

## License

This project is licensed under the [MIT](https://mit-license.org/) license.
