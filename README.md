# Codex Plugins

A repository marketplace for Codex plugins.

## Available plugins

| Plugin | Purpose |
| --- | --- |
| [Workflow](plugins/workflow/README.md) | Discovery, planning, implementation, and independent review of plans and code. Codex port of the Claude workflow team, with three companion agents. |

From this repository's root, install the workflow:

```sh
codex plugin marketplace add .
codex plugin add workflow@codex-plugins
```

Start a new Codex session after installation and use `$workflow:brainstorm`
or `$workflow:orchestrate`. See the
[plugin guide](plugins/workflow/README.md#companion-agents) for optional native
agent setup; the orchestrator can also use the bundled definitions with generic
subagents.

The former `workflow-loop` plugin is retired. See the [migration notes](plugins/workflow/README.md#replacing-workflow-loop) for existing installations.

## Structure

```text
.agents/
  plugins/
    marketplace.json          # Marketplace identity and ordered plugin catalog
plugins/                      # One directory per plugin
```

Each plugin you add uses this layout:

```text
plugins/my-plugin/
  .codex-plugin/
    plugin.json               # Plugin identity and metadata
  skills/                     # Optional reusable instructions
    my-skill/
      SKILL.md
  scripts/                    # Optional supporting scripts
  assets/                     # Optional icons and other resources
  .mcp.json                   # Optional MCP server configuration
  .app.json                   # Optional app connections
```

Only create optional components when your plugin uses them. There is no root plugin manifest: this repository is a catalog of plugins, each with its own manifest.

## Register the marketplace

From this repository's root, run:

```sh
codex plugin marketplace add .
codex plugin marketplace list
```

Registration makes the catalog available to Codex. Install Workflow with
`codex plugin add workflow@codex-plugins`.

After publishing this repository to a Git host, users can register its HTTPS Git URL instead of a local path. GitHub repositories also support `owner/repo` and an optional `--ref` argument.

## Add a plugin

1. Create `plugins/my-plugin/.codex-plugin/plugin.json`, using your own plugin name and metadata:

   ```json
   {
     "name": "my-plugin",
     "version": "0.1.0",
     "description": "Reusable workflows for my projects.",
     "author": {
       "name": "astrosteveo"
     },
     "skills": "./skills/",
     "interface": {
       "displayName": "My Plugin",
       "shortDescription": "Reusable project workflows",
       "longDescription": "A collection of reusable skills for working on my projects.",
       "developerName": "astrosteveo",
       "category": "Productivity",
       "capabilities": [],
       "defaultPrompt": ["Help me use my project workflows."]
     }
   }
   ```

2. Add your instructions in `plugins/my-plugin/skills/my-skill/SKILL.md`. Each skill needs YAML frontmatter with `name` and `description`, followed by its instructions. Describe when the skill should be used. Remove the manifest's `skills` field if your plugin has no skills.

3. Append an entry to the `plugins` array in `.agents/plugins/marketplace.json`:

   ```json
   {
     "name": "my-plugin",
     "source": {
       "source": "local",
       "path": "./plugins/my-plugin"
     },
     "policy": {
       "installation": "AVAILABLE",
       "authentication": "ON_INSTALL"
     },
     "category": "Productivity"
   }
   ```

   The source path is relative to the **repository root**, not the directory containing `marketplace.json`. Keep the entry name, plugin directory name, and manifest name identical. Catalog array order controls display order.

4. Register the marketplace if needed, then install the plugin:

   ```sh
   codex plugin add my-plugin@codex-plugins
   ```

   Start a new Codex session to use its skills and tools. You can also browse configured marketplaces with `/plugins` in the Codex CLI.

## Metadata conventions

- Keep the marketplace's `name` stable; installation commands use it. Change `interface.displayName` to customize its visible title.
- Use lowercase hyphenated plugin names and semantic versions such as `0.1.0`.
- Keep component and asset paths relative to the plugin root, starting with `./`.
- Include `mcpServers` or `apps` in a plugin manifest only when the referenced configuration exists.
- Add real author, repository, license, and asset metadata when available.

## References

- [Official OpenAI plugin packaging and marketplace guidance](https://developers.openai.com/plugins/build/plugins)
- [Using plugins in Codex](https://learn.chatgpt.com/docs/plugins)
- Installed CLI reference: `codex plugin --help` and `codex plugin marketplace --help`.
