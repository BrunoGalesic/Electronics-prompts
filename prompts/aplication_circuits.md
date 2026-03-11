You are given a technical datasheet. Your task is to identify and interpret the application circuits shown in the datasheet and convert them into the JSON structure defined below.

A typical application circuit may also appear under names such as application circuit, recommended circuit, reference circuit, example circuit, test circuit, or typical operating circuit.

Your goal is to produce a clear, human-readable, and reconstructable JSON representation of each circuit.

General requirements:
- Only use information that is explicitly visible in the datasheet or can be directly inferred from the circuit drawing.
- Do not invent component values, pin numbers, pin names, package names, part numbers, net names, or functions unless they are visible or clearly inferable.
- If information is not available, use "Unknown".
- Preserve original reference designators if they are shown in the schematic.
- If reference designators are not shown, assign reasonable placeholders such as U1, R1, C1, L1, D1, Q1, etc.
- Output each circuit separately as an object in a JSON array.
- For each extracted circuit, include:
  - "circuit"
  - "source" (if available)
- Do not include any explanations outside the JSON output.
- Output valid JSON only.

Interpretation rules:
- A net may be identified either by an explicit net label or by graphical continuity of wires and junction dots.
- If a net is not explicitly labeled in the original schematic, infer the node from continuous wiring and junctions.
- If the function of the inferred net is clear, assign a descriptive net name such as "FB", "VOUT", "SENSE", "BIAS", "ENABLE", etc.
- If the function of the inferred net is not clear, assign a generated name such as "N001", "N002", "N003", etc.
- If the schematic shows only a labeled terminal, off-page connection, or node marker, and not a real connector component, treat it as a net and do not invent a component.
- Only include real physical parts shown in the schematic in the "components" array.
- For non-polarized two-terminal components such as resistors, terminal numbering may be assigned arbitrarily if not shown, provided the output remains electrically correct and internally consistent.
- In "component_connectivity", every listed component must have its own object.
- Within each component object, include all pins that are shown or clearly implied by the circuit.
- If a pin is intentionally not connected, use "NC" as the net value for that pin.
- Do not create a separate no-connect section.
- If pin names or numbers are not visible on the schematic in the datasheet, look for them in other parts of the datasheet.
- If a component has unknown pin numbers but known pin names, use:
  "pin_number": "Unknown", "pin_name": "<Pin Name>"
- If both pin number and pin name are unknown, use:
  "pin_number": "Unknown", "pin_name": "Unknown"

Notes requirements:
- If any net name was inferred rather than explicitly shown in the schematic, include an explanation in the "notes" array.
- For each inferred net, briefly explain what the node represents and which component pins or circuit elements are connected by it.
- Also include any clearly visible implementation notes from the schematic, such as decoupling purpose, feedback function, compensation role, or biasing purpose, when they are evident from the diagram.

Use exactly this JSON structure:

[
  {
    "circuit": "<Circuit Name or Description>",
    "source": "<Page Number or Section Name>",
    "components": [
      {
        "reference": "<Reference>",
        "part": "<Part Number or Value>",
        "package": "<Package>",
        "function": "<Description>"
      }
    ],
    "nets": [
      "<Net Name>"
    ],
    "component_connectivity": [
      {
        "component": "<Component>",
        "pins": [
          {
            "pin_number": "<Pin Number>",
            "pin_name": "<Pin Name>",
            "net": "<Net Name or NC>"
          }
        ]
      }
    ],
    "hierarchy": [
      {
        "sheet": "<Sheet Name>",
        "components": ["<Component>", "<Component>"]
      }
    ],
    "properties": [
      {
        "component": "<Component>",
        "property_name": "<Property Name>",
        "value": "<Value>"
      }
    ],
    "notes": [
      "<Design note or implementation guideline>"
    ]
  }
]

Formatting rules:
- Output a JSON array.
- Each circuit must be represented as one object in the array.
- Use one component object per component in "components".
- Use one net name per entry in "nets".
- In "component_connectivity", group all pins belonging to the same component inside one object.
- If no hierarchy is obvious, use:
  "hierarchy": [
    {
      "sheet": "main",
      "components": ["<all components>"]
    }
  ]
- If no optional properties are available, use an empty array: "properties": []
- If no notes are needed, use an empty array: "notes": []
- If no source is available, use "source": "Unknown"
- Keep the output concise, technical, and strictly structured.
- Return valid JSON only, with no prose before or after it.

Now analyze the provided datasheet and return all typical application circuits using only the required JSON structure.
