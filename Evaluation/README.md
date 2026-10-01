# Evaluation

This directory contains the replication package for the empirical evaluation reported in:

> **Integrating LLMs and Model-Driven Engineering for Automated GUI Re-generation**
> Atefeh Nirumand, Jordi Cabot — Luxembourg Institute of Science and Technology (LIST)

The evaluation covers eight research questions organized across four parts: extraction pipeline quality (RQ1–RQ3), LLM robustness (RQ4–RQ5), HCI enhancement effectiveness (RQ6), and end-to-end generation quality (RQ7–RQ8).

---

## Dataset

The evaluation uses **200 real-world HTML/CSS web pages** from two sources:

- **WebSight** (`source_to_buml_extraction_results/Websight_Case Studies/`): 100 pages drawn from the [HuggingFaceM4/WebSight](https://huggingface.co/datasets/HuggingFaceM4/WebSight) dataset.
- **CodePen** (`source_to_buml_extraction_results/CodePen_Case Studies/`): 100 pages manually curated from [CodePen](https://codepen.io) across ten application categories:

| # | Category |
|---|----------|
| 1 | Social Media |
| 2 | Search Engines |
| 3 | Registration |
| 4 | Inventory |
| 5 | Educational |
| 6 | E-Commerce |
| 7 | Dashboard |
| 8 | CRUD Applications |
| 9 | Contact Manager |
| 10 | Authentication |

For RQ4, RQ5, and RQ7, a representative subset of **20 CodePen cases** (cases 02 and 05 from each category) was selected.
For RQ6, **10 cases** were selected from the 20 above (one per category, choosing the case with lower UI element overlap).
For RQ8, **3 multi-page applications** were selected.

All experiments used **GPT-5.2** as the primary backbone, except for the backbone agnosticism comparison (RQ4).

---

## Directory Structure

```
Evaluation/
├── source_to_buml_extraction_results/   # RQ1–RQ3: extraction accuracy on 200 pages
│   ├── CodePen_Case Studies/
│   └── Websight_Case Studies/
├── backbone_comparison_results/          # RQ4: backbone agnosticism (20 cases × 4 models)
│   └── case_NN/
│       ├── gpt-4o-mini/
│       ├── gemini-25-flash/
│       ├── llama-4-scout/
│       └── gpt-5.2/
├── ablation_results/                     # RQ4: ablation study (prompt component contribution)
│   ├── full/
│   ├── no_C1/
│   ├── no_C2/
│   ├── no_C3/
│   ├── ablation_results.csv
│   └── ablation_summary.csv
├── stability_results/                    # RQ5: extraction stability across 3 runs
│   ├── case_NN/
│   ├── per_run_results.csv
│   ├── summary.csv
│   └── overall_summary.txt
├── HCI-enhancement effectivenes_results/ # RQ6: user preference study results
├── fidelity_of_generated_applications/   # RQ7: end-to-end fidelity (20 cases)
│   ├── generated_apps/
│   │   └── case_NN/
│   │       ├── evaluation_report.json
│   │       └── evaluation_results.csv
│   └── app_evaluation_results.csv
└── multi_page_navigation_fidelity_results/ # RQ8: navigation fidelity (3 multi-page apps)
```

---


## Experimental Setup

- **Machine**: Windows 11 Enterprise, Intel Core i7-1280P @ 1.80 GHz, 32 GB RAM
- **Primary LLM**: GPT-5.2
- **Backbone comparison**: GPT-4o-mini, Gemini 2.5 Flash, Llama 4 Scout
- **Target code generation framework**: Django (proof of concept); React also used for RQ7/RQ8
