# Integrating LLMs and Model-Driven Engineering for Automated GUI Re-generation

[![Python](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12-blue?logo=python&logoColor=gold)](https://pypi.org/project/besser/)
[![PyPI - License](https://img.shields.io/pypi/l/besser)](https://opensource.org/license/MIT)

This repository contains the implementation of the approach proposed in the paper **"Integrating LLMs and Model-Driven Engineering for Automated GUI Re-generation"** (Atefeh Nirumand, Jordi Cabot — Luxembourg Institute of Science and Technology & University of Luxembourg). The approach provides an end-to-end, platform-independent pipeline for GUI extraction, enhancement, and re-generation: it lifts existing HTML/CSS implementations into platform-independent B-UML models using LLM-assisted prompting, optionally refines those models through HCI-guided enhancement and human-in-the-loop designer interaction, and re-generates executable web applications via deterministic model-to-code transformation — all implemented on top of the [BESSER](https://github.com/BESSER-PEARL/BESSER) low-code platform.

---

## Overview

The pipeline takes HTML/CSS web pages as input, lifts them to platform-independent B-UML models, optionally enhances them using HCI principles and human feedback, and re-generates executable web applications through deterministic model-to-code transformation.

The approach consists of **two core phases** and **two optional refinement phases**:

| Phase | Type | Description |
|-------|------|-------------|
| 1. LLM-based Code-to-Model Extraction | **Core** | Derives a Structural (data) model and an IFML-like GUI model from HTML/CSS source files using LLM-assisted prompting |
| 2. LLM-based Model Enhancement (HCI) | *Optional* | Refines the extracted IFML-like GUI model according to HCI principles (Usefulness, Usability, Findability, Desirability) and exports an SVG visual representation |
| 3. Human-in-the-Loop Interaction | *Optional* | Allows designers to inspect, edit, and refine the SVG representation in tools such as Figma before final code generation |
| 4. Deterministic Model-to-Code Generation | **Core** | Consumes the validated B-UML models and produces executable applications (Django or React) with integrated CRUD logic and styling |

The pipeline supports both single-page and multi-page applications, automatically binding inter-page navigation relationships into a unified GUI model.

---

## Repository Structure

```
BESSER-SourceCode-to-GUI/
├── besser/
│   ├── BUML/
│   │   └── notations/
│   │       ├── sourceCode_to_structural/   # HTML/CSS → Structural model
│   │       └── sourceCode_to_buml/         # HTML/CSS → IFML-like GUI model + SVG + HCI
│   └── generators/                         # Structural + GUI model → Django/React app
└── Evaluation/                             # Full replication package (RQ1–RQ8)
```

---

## Installation

The implementation requires Python 3.10+ and is built on top of the BESSER platform.

```bash
git clone https://github.com/BESSER-PEARL/BESSER-SourceCode-to-GUI.git
cd BESSER-SourceCode-to-GUI
python setup_environment.py
```

An OpenAI API key is required (GPT-5.2 was used as the primary backbone in the paper).

---

## Usage (example)

### Full Pipeline: HTML/CSS → B-UML GUI Model → SVG

```python
from besser.BUML.notations.sourceCode_to_buml.sourceCode_to_buml import source_code_to_buml

source_code_to_buml(
    api_key="<your-openai-api-key>",
    input_folder="path/to/html/folder",       # folder with .html / .htm files
    output_folder="path/to/output",            # default: ./output
    # Optional — for multi-page applications:
    navigation_image_path="path/to/nav_diagram.png",
    pages_order_file_path="path/to/pages_order.txt",
    additional_info_path="path/to/app_description.txt",
    # Optional — for styling-aware extraction:
    styling_file_path="path/to/css/folder",
)
```

The function automatically detects whether the input folder contains one or multiple HTML files and dispatches to the appropriate single-page or multi-page pipeline.

### Structural Model Extraction Only

```python
from besser.BUML.notations.sourceCode_to_structural.sourceCode_to_structural import source_code_to_structural

source_code_to_structural(
    api_key="<your-openai-api-key>",
    input_folder="path/to/html/folder",
    output_folder="path/to/output",
    additional_info_path="path/to/app_description.txt",  # optional
)
```

### Output Structure

```
output/
├── plantuml/
│   └── generated_plantuml.puml      # Intermediate PlantUML class diagram
├── buml/
│   └── model.py                     # B-UML Structural (DomainModel)
├── gui_model/
│   └── generated_gui_model.py       # B-UML IFML-like GUI model
└── hci_enhanced/
    └── enhanced_svg/                # HCI-enhanced SVG representations
```

---

## Implementation Details

### Phase 1 — LLM-based Code-to-Model Extraction

Located in `besser/BUML/notations/sourceCode_to_structural/` and `besser/BUML/notations/sourceCode_to_buml/`.

**Structural model extraction** uses a two-step pipeline:
1. A direct prompt instructs the LLM to generate a PlantUML class diagram from the HTML/CSS input.
2. A self-improvement prompt refines the diagram for syntactic correctness, removes duplicates, and enforces type consistency.
The final PlantUML is converted to a B-UML `DomainModel` via the existing BESSER `plantuml_to_buml` converter.

**IFML-like GUI model extraction** uses:
1. *Direct prompting* — the LLM generates an initial GUI model (screens, buttons, forms, data lists, layout, styling) from the source code, guided by the GUI metamodel image and few-shot HTML-to-Python examples.
2. *Self-improvement prompting* — iterative refinement comparing the generated model against the source code and the Structural model to resolve inconsistencies and align attributes.
3. *Property binding* — a dedicated pass replaces string literals with actual `Property` objects from the Structural model.
4. When a CSS file is provided, additional styling passes integrate layout, color, and size attributes.

For multi-page applications, the pipeline additionally performs: shared structural model generation, per-page GUI model generation with cross-page context, whole-application unification into a single `Module`, and navigation binding (resolving `targetScreen` references for all `Navigate` buttons).

### Phase 2 — LLM-based HCI Enhancement

The IFML-like GUI model is first converted to SVG using a deterministic Jinja-template-based generator. An LLM-based enhancement pipeline then applies four HCI principles sequentially to the SVG:

| Principle | Focus |
|-----------|-------|
| Usefulness | Remove redundant elements, improve task relevance, grid-based alignment |
| Usability | Readability, contrast, navigation flow, accessible UI structures |
| Findability | Visual hierarchy, navigation cues, scanability, whitespace |
| Desirability | Color harmony, typography, shadows, visual polish |

### Phase 3 — Human-in-the-Loop

The generated SVG can be imported into Figma for visual inspection and manual refinement. The updated SVG is exported (with bounding boxes and preserved IDs) and converted back to an updated B-UML GUI model before code generation.

### Phase 4 — Deterministic Model-to-Code Generation

Located in `besser/generators/django/`. The generator transforms the Structural and IFML-like GUI models into a fully functional Django web application, including ORM models, CRUD views, URL routing, and styled HTML templates. A React generator is also available for front-end-only generation from the same models.

---

## IFML-like GUI Metamodel

The metamodel (in `besser/BUML/notations/sourceCode_to_buml/llm_assistant/gui_metamodel_spec/`) provides a platform-independent abstract representation of GUIs organized around four dimensions:

- **Application Structure** — `GUIModel`, `Module`, `Screen`
- **Visual Elements** — `ViewContainer`, `ViewComponent`, `Button`, `InputField`, `Form`, `DataList`, `Image`, `Menu`, `MenuItem`
- **Data Source Layer** — `DataSource`, `CollectionDataSource`, `DataSourceElement`, `FileDataSource`
- **Layout and Styling** — `Layout`, `Size`, `Position`, `Color`, aggregated through a `Styling` object

---

## Evaluation

The full replication package is in the [`Evaluation/`](./Evaluation/) directory, including:

- **200 HTML/CSS case studies** from WebSight and CodePen with their generated Structural and IFML-like GUI models
- **Backbone comparison results** for GPT-4o-mini, Gemini 2.5 Flash, and Llama 4 Scout
- **Ablation study results** for each prompt component (task description, few-shot examples, metamodel reference)
- **Stability results** across three independent runs per case
- **HCI preference study** data (34 participants, 10 cases)
- **Fidelity evaluation** for 20 generated web applications (element coverage + visual similarity)
- **Navigation fidelity** results for 3 multi-page applications

See [`Evaluation/README.md`](./Evaluation/README.md) for detailed results and tables.

---

## Acknowledgements

This research is supported by the Luxembourg National Research Fund (FNR) through the PEARL program under grant agreement 16544475.

---

## License

This project is licensed under the [MIT](https://mit-license.org/) license.
