
You are generating a hierarchical electronic circuit system in JSON using reusable blocks.

Output requirements:
- Output only valid JSON
- Do not output markdown
- Do not output comments
- Use the canonical circuit JSON format exactly
- Set "design_type" to "system"
- Use block instances instead of redefining the internal components of the blocks
- Populate:
  - schema_version
  - design_id
  - design_type
  - name
  - description
  - category
  - tags
  - ports
  - nets
  - instances
  - interconnect
- Leave these as empty arrays unless explicitly needed:
  - components
  - connectivity
  - hierarchy
  - constraints
  - properties
  - notes
- Every top-level system connection must be declared in "ports"
- Every net used in "interconnect" must be declared in "nets"
- Each instance must reference a valid block_id from the provided block library
- Use parameter_overrides when instance values differ from block defaults
- Do not flatten block internals unless explicitly requested

Available blocks:
<PASTE BLOCK JSONS OR BLOCK SUMMARIES HERE>

Task:
Create a system using these reusable blocks: <DESCRIBE SYSTEM HERE>

Connection requirements:
<DESCRIBE INSTANCE-TO-INSTANCE CONNECTIONS HERE>
