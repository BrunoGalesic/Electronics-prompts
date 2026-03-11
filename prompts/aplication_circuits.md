
You are given a technical datasheet. Extract only the application circuits whose title, caption, or nearby heading matches one of the items in this list.

Target circuits:
- <Circuit name 1>
- <Circuit name 2>
- <Circuit name 3>

Possible circuit naming variants may include:
application circuit, typical application circuit, recommended circuit, reference circuit, example circuit, test circuit, typical operating circuit, evaluation circuit.

Rules:
- Use only information explicitly visible in the datasheet or directly inferable from the schematic.
- Do not invent values, pin numbers, pin names, net names, packages, part numbers, or functions.
- If unknown, use "Unknown".
- Preserve original reference designators if shown; otherwise assign placeholders like U1, R1, C1, L1, D1, Q1, J1.
- Output each matched circuit as a separate object in a JSON array.
- Do not include citations, links, references, markdown, or explanations outside the JSON.
- Output valid JSON only.

Net and signal rules:
- Create nets only from explicit net labels or real wire continuity/junctions.
- Do not create a net just by repeating a pin name.
- If a pin only goes to a descriptive signal label and no actual external component or explicit net is drawn, set that pin connection to "NC".
- If a pin is marked "NC" in component_connectivity, explain the reason in notes.
- If a net label is explicitly shown in the schematic, use it exactly.
- If it is clear what the net function is (example: I2C nets), use those names for nets.
- Otherwise use a junction-style inferred name such as:
  "Junction(U1-3,C3)"
  "Junction(R1,R2,U1-2)"
- For every pin marked NC, add a note stating its apparent function or intended signal role if visible from the pin name, caption, or nearby label.

Component rules:
- Only include real physical parts shown in the schematic in "components".
- If a labeled terminal or off-page marker is shown without a real connector component, treat it as a net, not a component.
- In "component_connectivity", every component must have its own object.
- Include all shown or clearly implied pins.
- If a shown pin is intentionally not connected to any real schematic net/component, use:
  "pin_number": "<Pin Number or Unknown>",
  "pin_name": "<Pin Name or Unknown>",
  "net": "NC"
- If pin numbers are unknown but pin names are known, use "Unknown" for pin_number.
- If both are unknown, use "Unknown" for both.

Notes rules:
- If a net name was inferred, explain briefly what it connects.
- For pins marked NC because they only connect to descriptive signal labels, explain the intended signal type.
- Include visible implementation notes when clear from the schematic, such as decoupling, bypassing, feedback, pull-up/pull-down, charge-pump capacitor, reservoir capacitor, compensation, filtering, or biasing.

Use exactly this JSON structure:

[
  {
    "circuit": "<Circuit Name or Description>",
    "source": "<Page Number or Section Name>",
    "components": [
      {
        "reference": "<Reference>",
        "part_number_or_value": "<Part Number or Value>",
        "package": "<Package>",
        "function": "<Description>"
      }
    ],
    "nets": [
      "<Net Name>"
    ],
    "component_connectivity": [
      {
        "component": "<Reference>",
        "pins": [
          {
            "pin_number": "<Pin Number or Unknown>",
            "pin_name": "<Pin Name or Unknown>",
            "net": "<Net Name or NC>"
          }
        ]
      }
    ],
    "hierarchy": [
      {
        "sheet": "<Sheet Name>",
        "components": ["<Reference>", "<Reference>"]
      }
    ],
    "properties": [
      {
        "component": "<Reference>",
        "property_name": "<Property Name>",
        "value": "<Value>"
      }
    ],
    "notes": [
      "<Design note or signal-role note>"
    ]
  }
]

Formatting requirements:
- Output one JSON object per matched circuit inside the top-level array.
- Keep all keys exactly as shown.
- If no hierarchy is obvious, use:
  "sheet": "main"
- If "properties" is empty, use an empty array.
- If "notes" is empty, use an empty array.
- Keep the output concise, technical, and strictly structured.
- Output valid JSON only, with double quotes around all keys and string values.

Priority:
- Prefer electrical correctness over symmetry.
- Prefer "NC" plus an explanatory note over inventing a fake net.
- Only extract circuits matching the Target circuits list.
``
