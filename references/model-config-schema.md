\
# Interactive Explorer Model Configuration

The JSON configuration drives `templates/paper_network_explorer.html`. The build helper embeds the JSON into a standalone HTML file.

## Top-level fields

| Field | Required | Meaning |
|---|---|---|
| `title` | yes | Paper/model title shown above the graph |
| `subtitle` | no | Short task/architecture summary |
| `sourceNote` | no | Evidence scope and caveats |
| `modules` | yes | Array of graph nodes |
| `edges` | yes | Array of directed connections |

## Module fields

| Field | Required | Meaning |
|---|---|---|
| `id` | yes | Unique stable machine ID, e.g. `encoder_1` |
| `title` | yes | Display name |
| `x`, `y` | yes | Numeric top-left position on SVG canvas |
| `code` | recommended | Stable human ID, e.g. `M1` |
| `type` | recommended | `input`, `feature`, `router`, `fusion`, `prediction`, `loss`, or a suitable custom type |
| `w`, `h` | recommended | Node width/height |
| `short` | no | Short label |
| `summary` | recommended | Role in the architecture |
| `inputs` | recommended | Array of `{name, shape, meaning}` |
| `outputs` | recommended | Array of `{name, shape, meaning}` |
| `steps` | recommended | Ordered list of concrete operations |
| `sourceFiles` | recommended | Source file/function locations, or explicit “unverified” status |
| `upstream` | recommended | Array of upstream module IDs |
| `downstream` | recommended | Array of downstream module IDs |
| `status` | required for evidence quality | `source-verified`, `paper-described`, `inferred`, or `unverified` |
| `caveats` | no | Unverified details, version notes, or caveats |

Shapes must be strings such as `[B,T,D]`, `[B,S,256]`, `scalar`, `list[str]`, or `not verified`. Do not invent dimensions.

## Edge fields

Each edge has:
- `from`: source module ID;
- `to`: destination module ID;
- `label`: variable/data being passed, ideally including shape if concise;
- `type`: `data` for normal data flow or `training` for training-only/loss/gradient paths.

Every `from` and `to` must refer to an existing module. An edge should correspond to a real or clearly labeled paper-described connection.

## Minimal example

```json
{
  "title": "Example model",
  "subtitle": "A small illustrative pipeline",
  "sourceNote": "Illustrative example, not source-verified.",
  "modules": [
    {
      "id": "input",
      "code": "M1",
      "title": "Input",
      "type": "input",
      "x": 40,
      "y": 120,
      "w": 160,
      "h": 90,
      "summary": "Receives the input.",
      "inputs": [],
      "outputs": [{"name": "x", "shape": "not verified", "meaning": "Input data"}],
      "steps": ["Load the input."],
      "sourceFiles": ["unverified"],
      "upstream": [],
      "downstream": ["model"],
      "status": "unverified",
      "caveats": ["Replace this example with evidence from the current project."]
    },
    {
      "id": "model",
      "code": "M2",
      "title": "Model",
      "type": "feature",
      "x": 300,
      "y": 120,
      "w": 180,
      "h": 100,
      "summary": "Processes the input.",
      "inputs": [{"name": "x", "shape": "not verified", "meaning": "From M1"}],
      "outputs": [{"name": "y", "shape": "not verified", "meaning": "Model output"}],
      "steps": ["Apply the verified computation here."],
      "sourceFiles": ["unverified"],
      "upstream": ["input"],
      "downstream": [],
      "status": "unverified",
      "caveats": []
    }
  ],
  "edges": [
    {"from": "input", "to": "model", "label": "x → y", "type": "data"}
  ]
}
```
