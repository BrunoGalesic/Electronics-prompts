
You are generating a reusable electronic circuit block in JSON.

Output requirements:
- Output only valid JSON
- Do not output markdown
- Do not output comments
- Use the canonical circuit JSON format exactly
- Set "design_type" to "block"
- Populate:
  - schema_version
  - design_id
  - design_type
  - name
  - description
  - category
  - tags
  - ports
  - parameters
  - components
  - nets
  - connectivity
- Leave these as empty arrays unless explicitly needed:
  - instances
  - interconnect
  - hierarchy
  - constraints
  - properties
  - notes
- Every externally visible connection must be declared in "ports"
- Every net used in connectivity must be declared in "nets"
- Every primitive component connection must be declared in "connectivity"
- Use "net": null and "no_connect": true for intentionally unconnected pins
- Do not use "NC" as a fake net
- Parameterize values that are expected to vary between designs
- Use structured value_spec objects for fields like value, package, and part_number
- Use stable reference designators like R1, C1, L1, U1, J1, Q1, D1

Task:
Create a reusable block for: <DESCRIBE BLOCK HERE>
