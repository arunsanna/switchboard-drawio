# The diagram agent's kit

Copied with every draw.io release Switchboard installs (to `<SWITCHBOARD_HOME>/drawio/current/agent/`),
for the Claude Code agent that drafts and edits Canvas diagrams.

- `search-index.json`, `xml-reference.md`, `style-reference.md`: from JGraph's draw.io AI kit,
  [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) at `e227b9ad530ac22d2a00066c7e6ac3b9583dba74`
  (`shape-search/search-index.json`, `shared/xml-reference.md`, `shared/style-reference.md`),
  Apache-2.0. The index lists 10,000+ draw.io shapes with their style strings.
- `find_shape.py`: Switchboard's search over that index (whole words or word starts; current AWS
  shapes first). `python3 find_shape.py internet gateway`.
