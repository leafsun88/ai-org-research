---
company: "Anysphere"
research_key: CURSOR
type: official
source: "cursor.com"
title: "changelog"
url: https://cursor.com/changelog
date: unknown
fetched_at: 2026-04-20T17:57:33
credibility: S2-S4
evidence: E2-E3
chars: 20054
---

# changelog

**Source**: https://cursor.com/changelog
**Channel**: official

---

Changelog

Apr 15, 2026 · Changelog

Cursor can now respond by creating interactive canvases.

These visualizations can include dashboards and custom interfaces built using first-party components like tables, boxes, diagrams, and charts, as well as existing Cursor components like diffs and to-do lists.

In the Agents Window, canvases are durable artifacts that live in the side panel alongside the terminal, browser, and source control.

Try it out in Cursor 3.1 in the Agents Window or the editor. Read more in our announcement.

3.1 Apr 13, 2026 · Changelog

This release introduces improvements to our Agents Window interface as part of Cursor 3.

#Tiled layout

Split your current view into panes to run and manage several agents in parallel. The tiled layout makes it easier to multi-task and compare outputs across agents without jumping between tabs.

Expand panes to focus on a conversation, drag agents into tiles, and use keybindings for quick navigation and organization. Your setup also persists across sessions.

#Upgraded voice input

Dictation through voice input is more reliable and accurate. It records your full voice clip and transcribes it with batch STT for higher-quality speech-to-text.

You can press and hold Ctrl+M to speak, and we've added controls to the UI while recording, such as a waveform, timer, and buttons for cancelling and confirming.

#Branch selection in empty state

Previously, starting an agent from the empty state usually defaulted to your current branch. Now you can search and select a branch first, then launch a cloud agent directly against that branch.

This cuts down on additional steps to switch branches and reduces accidental runs on the wrong branch.

#Diff to file navigation

Jump from the diff straight to the exact line in the file. Once there, you have the full power of the editor, make changes manually, use Tab, go to definition, and more.

#Filters for searching files

Use include/exclude filters in "Search in Files" for scoping code search to specific file sets.

Agents Window Improvements↓↑

Prompt buttons now stay in place while voice input is processing.

Plan tabs now get the same document behaviors as files: support for reliable loading, dirty tracking, reload on plan changes, and the ability to save, copy, and export markdown.

New agent sessions now start in your preferred project target by default.

File tab names are now resolved within the current agent's visible tabs instead of trying to be globally unique across all other agents' tabs.

Cmd-K now shows fewer, more relevant agent results, capped to the recent matching set (i.e., items that match your query and are from a recent subset).

On macOS, text is now rendered with anti-aliasing, producing sharper character edges.

Design Mode now lets you navigate the element tree (up, down, and sideways) with keyboard support to pick the UI element before commenting.

The Agents Window now avoids expensive updates and fetches unless they're truly needed.

Closing tabs is now less likely to glitch the file tree, and recovery is faster.

Limited local diff fetches to reduce CPU/network spikes and lag in SCM views.

File tree now responds to changes more reliably and is less likely to flicker, stale, or miss updates.

Extension events (e.g., file change, diagnostics update) are now scoped to each workspace, reducing cross-project interference.

Hitting enter to send a follow-up in a long chat used to hang for over a second and now feels instant.

Large edits stream more smoothly now after cutting dropped frames by ~87%.

Agents Window Bug Fixes↓↑

Fixed a bug where scrolling through long conversations used to stutter. Now it's smooth, even in large threads.

Fixed a bug where an agent conversation full of diffs or code blocks would flash and freeze.

Apr 8, 2026 · Changelog

This release introduces updates to Bugbot including the ability to self-improve in real time, MCP support, improvements to Bugbot Autofix, and the highest resolution rate to date.

#Bugbot Learned Rules

Bugbot can now learn from feedback on pull requests and turn those signals into learned rules that improve future reviews.

It looks at reactions and replies to Bugbot comments and comments from human reviewers to create candidate rules. Bugbot automatically promotes the ones that accumulate signal and disables the ones that stop being useful.

Read more about learned rules in our announcement or manage learning in the Bugbot dashboard.

#Bugbot MCP Support

Give Bugbot access to MCP servers for additional context during code reviews. On Teams and Enterprise plans, you can add tools to Bugbot in the Bugbot dashboard.

Bugbot Improvements (6)↓↑

Bugbot's resolution rate is now 78%.

Added a "Fix All" action to apply multiple Bugbot fixes in one operation.

Redesigned Bugbot settings, and split personal and team settings into clearer sections.

Bugbot Autofix only runs when findings are substantial enough to warrant a fix.

Bugbot Autofix now uses only relevant rules, reducing noise in prompting.

Improved reliability of Bugbot Autofix CI checks on PRs.

Simplified Bugbot check progress messages in GitHub PRs.

Bugbot Bug Fixes (2)↓↑

Fixed a bug where stale privacy mode state from inactive teams could incorrectly block Bugbot Autofix.

Fixed infra issues that caused longer than expected Bugbot run times.

3.0 Apr 2, 2026 · Changelog

Cursor 3 is now available.

#Agents Window

The new Cursor interface allows you to run many agents in parallel across repos and environments: locally, in worktrees, in the cloud, and on remote SSH.

It's simpler, more powerful, and centered around agents, while keeping the depth of a development environment.

To try the Agents Window, upgrade Cursor and type Cmd+Shift+P -> Agents Window.

You can switch back to the IDE anytime, or have both open simultaneously.

Read more in our announcement.

#Design Mode

In the Agents Window, you can use Design Mode to annotate and target UI elements directly in the browser.

This allows you to give more precise feedback and iterate faster by pointing the agent to exactly the part of the interface you're referring to.

Keyboard shortcuts include:

⌘ + Shift + D to toggle to Design Mode

Shift + drag to select an area

⌘ + L to add element to chat

⌥ + click to add element to input

#Agent Tabs in the Editor

Agent Tabs allow you to view multiple chats at once, side-by-side or in a grid.

Editor (4)↓↑

Added a new command /worktree that creates a separate git worktree so changes happen in isolation.

Added a new command /best-of-n that runs the same task in parallel across multiple models, each in its own isolated worktree, then compares outcomes.

Deprecated the previous worktree and best-of-n selection from the Editor.

Removed cloud agents from the Editor.

Plugins & MCP (2)↓↑

MCP Apps now support structured content, enabling richer tool outputs.

Third-party plugin imports now default to off for Enterprises when unset, while preserving explicit Admin overrides.

Enterprise & Teams (3)↓↑

Added the directory group name so audit logs are human-readable without looking up IDs.

Added a team-level Admin setting for cloud agents that restricts creating, editing, and deleting team secrets to Admins.

Added an Enterprise Admin control for disabling "Made with Cursor" code attribution for the entire team. Per-user settings still exist via Cursor Settings > Agent > Attribution.

Other Improvements (10)↓↑

Large-file diff rendering is now much faster, smoother, and less memory-heavy.

Agents are now better at monitoring long-running jobs.

Added an Await tool that lets agents wait for background shell commands and subagents to complete, or wait for specific output such as "Ready" or "Error".

Reduced the browser automation tool surface and tightened the subagent to use browser tools only, helping it stay more focused on the task. Also improved the browser instructions to reduce error loops, and added screenshot-based coordinate clicking as a fallback when DOM interactions are unreliable.

Plans are now included in shared chats alongside the transcript.

Added caching to improve Explorer subagents startup time.

Past chat transcripts are now surfaced directly in at-mention search results.

Added a "scroll to bottom" button in the agent panel that appears when content overflows.

Tab bar can now span the full available width in maximized chat layouts.

Consolidated the Early Access release track behind Nightly.

Bug Fixes (8)↓↑

Fixed text area behavior for Network Access Controls so pressing Enter can reliably add a newline at the end of the input.

Fixed hooks loading so multi-root workspaces read project hook files from all workspace folders instead of only the first one.

Fixed a markdown parsing bug where parenthesized HTTP(S) links could be misread as citations.

Fixed todo card visibility to prevent them from disappearing after all todos complete.

Fixed Agent queued prompts that were not resuming automatically after editing operations.

Fixed picker behavior for models that are disabled but selectable by removing misleading "not allowed" styling and auto-enabling a model when the user selects it.

Fixed a bug where expanding/collapsing thinking blocks didn't work while streaming was still in progress.

Fixed a bug where Shift+Enter line breaks weren't treated as multiline content, so the prompt input field could stay in an incorrect state.

Mar 25, 2026 · Changelog

Cursor now supports self-hosted cloud agents that keep your code and tool execution entirely in your own network.

Your codebase, build outputs, and secrets all stay on internal machines running in your infrastructure, while the agent handles tool calls locally.

Self-hosted cloud agents offer the same capabilities as Cursor-hosted cloud agents, including isolated VMs, full development environments, multi-model harnesses, plugins, and more.

Try it out today by enabling self-hosted cloud agents in your Cursor Dashboard. Read more in our announcement.

Changelog

Apr 15, 2026 · Changelog

Cursor can now respond by creating interactive canvases.

These visualizations can include dashboards and custom interfaces built using first-party components like tables, boxes, diagrams, and charts, as well as existing Cursor components like diffs and to-do lists.

In the Agents Window, canvases are durable artifacts that live in the side panel alongside the terminal, browser, and source control.

Try it out in Cursor 3.1 in the Agents Window or the editor. Read more in our announcement.

3.1 Apr 13, 2026 · Changelog

This release introduces improvements to our Agents Window interface as part of Cursor 3.

#Tiled layout

Split your current view into panes to run and manage several agents in parallel. The tiled layout makes it easier to multi-task and compare outputs across agents without jumping between tabs.

Expand panes to focus on a conversation, drag agents into tiles, and use keybindings for quick navigation and organization. Your setup also persists across sessions.

#Upgraded voice input

Dictation through voice input is more reliable and accurate. It records your full voice clip and transcribes it with batch STT for higher-quality speech-to-text.

You can press and hold Ctrl+M to speak, and we've added controls to the UI while recording, such as a waveform, timer, and buttons for cancelling and confirming.

#Branch selection in empty state

Previously, starting an agent from the empty state usually defaulted to your current branch. Now you can search and select a branch first, then launch a cloud agent directly against that branch.

This cuts down on additional steps to switch branches and reduces accidental runs on the wrong branch.

#Diff to file navigation

Jump from the diff straight to the exact line in the file. Once there, you have the full power of the editor, make changes manually, use Tab, go to definition, and more.

#Filters for searching files

Use include/exclude filters in "Search in Files" for scoping code search to specific file sets.

Agents Window Improvements↓↑

Prompt buttons now stay in place while voice input is processing.

Plan tabs now get the same document behaviors as files: support for reliable loading, dirty tracking, reload on plan changes, and the ability to save, copy, and export markdown.

New agent sessions now start in your preferred project target by default.

File tab names are now resolved within the current agent's visible tabs instead of trying to be globally unique across all other agents' tabs.

Cmd-K now shows fewer, more relevant agent results, capped to the recent matching set (i.e., items that match your query and are from a recent subset).

On macOS, text is now rendered with anti-aliasing, producing sharper character edges.

Design Mode now lets you navigate the element tree (up, down, and sideways) with keyboard support to pick the UI element before commenting.

The Agents Window now avoids expensive updates and fetches unless they're truly needed.

Closing tabs is now less likely to glitch the file tree, and recovery is faster.

Limited local diff fetches to reduce CPU/network spikes and lag in SCM views.

File tree now responds to changes more reliably and is less likely to flicker, stale, or miss updates.

Extension events (e.g., file change, diagnostics update) are now scoped to each workspace, reducing cross-project interference.

Hitting enter to send a follow-up in a long chat used to hang for over a second and now feels instant.

Large edits stream more smoothly now after cutting dropped frames by ~87%.

Agents Window Bug Fixes↓↑

Fixed a bug where scrolling through long conversations used to stutter. Now it's smooth, even in large threads.

Fixed a bug where an agent conversation full of diffs or code blocks would flash and freeze.

Apr 8, 2026 · Changelog

This release introduces updates to Bugbot including the ability to self-improve in real time, MCP support, improvements to Bugbot Autofix, and the highest resolution rate to date.

#Bugbot Learned Rules

Bugbot can now learn from feedback on pull requests and turn those signals into learned rules that improve future reviews.

It looks at reactions and replies to Bugbot comments and comments from human reviewers to create candidate rules. Bugbot automatically promotes the ones that accumulate signal and disables the ones that stop being useful.

Read more about learned rules in our announcement or manage learning in the Bugbot dashboard.

#Bugbot MCP Support

Give Bugbot access to MCP servers for additional context during code reviews. On Teams and Enterprise plans, you can add tools to Bugbot in the Bugbot dashboard.

Bugbot Improvements (6)↓↑

Bugbot's resolution rate is now 78%.

Added a "Fix All" action to apply multiple Bugbot fixes in one operation.

Redesigned Bugbot settings, and split personal and team settings into clearer sections.

Bugbot Autofix only runs when findings are substantial enough to warrant a fix.

Bugbot Autofix now uses only relevant rules, reducing noise in prompting.

Improved reliability of Bugbot Autofix CI checks on PRs.

Simplified Bugbot check progress messages in GitHub PRs.

Bugbot Bug Fixes (2)↓↑

Fixed a bug where stale privacy mode state from inactive teams could incorrectly block Bugbot Autofix.

Fixed infra issues that caused longer than expected Bugbot run times.

3.0 Apr 2, 2026 · Changelog

Cursor 3 is now available.

#Agents Window

The new Cursor interface allows you to run many agents in parallel across repos and environments: locally, in worktrees, in the cloud, and on remote SSH.

It's simpler, more powerful, and centered around agents, while keeping the depth of a development environment.

To try the Agents Window, upgrade Cursor and type Cmd+Shift+P -> Agents Window.

You can switch back to the IDE anytime, or have both open simultaneously.

Read more in our announcement.

#Design Mode

In the Agents Window, you can use Design Mode to annotate and target UI elements directly in the browser.

This allows you to give more precise feedback and iterate faster by pointing the agent to exactly the part of the interface you're referring to.

Keyboard shortcuts include:

⌘ + Shift + D to toggle to Design Mode

Shift + drag to select an area

⌘ + L to add element to chat

⌥ + click to add element to input

#Agent Tabs in the Editor

Agent Tabs allow you to view multiple chats at once, side-by-side or in a grid.

Editor (4)↓↑

Added a new command /worktree that creates a separate git worktree so changes happen in isolation.

Added a new command /best-of-n that runs the same task in parallel across multiple models, each in its own isolated worktree, then compares outcomes.

Deprecated the previous worktree and best-of-n selection from the Editor.

Removed cloud agents from the Editor.

Plugins & MCP (2)↓↑

MCP Apps now support structured content, enabling richer tool outputs.

Third-party plugin imports now default to off for Enterprises when unset, while preserving explicit Admin overrides.

Enterprise & Teams (3)↓↑

Added the directory group name so audit logs are human-readable without looking up IDs.

Added a team-level Admin setting for cloud agents that restricts creating, editing, and deleting team secrets to Admins.

Added an Enterprise Admin control for disabling "Made with Cursor" code attribution for the entire team. Per-user settings still exist via Cursor Settings > Agent > Attribution.

Other Improvements (10)↓↑

Large-file diff rendering is now much faster, smoother, and less memory-heavy.

Agents are now better at monitoring long-running jobs.

Added an Await tool that lets agents wait for background shell commands and subagents to complete, or wait for specific output such as "Ready" or "Error".

Reduced the browser automation tool surface and tightened the subagent to use browser tools only, helping it stay more focused on the task. Also improved the browser instructions to reduce error loops, and added screenshot-based coordinate clicking as a fallback when DOM interactions are unreliable.

Plans are now included in shared chats alongside the transcript.

Added caching to improve Explorer subagents startup time.

Past chat transcripts are now surfaced directly in at-mention search results.

Added a "scroll to bottom" button in the agent panel that appears when content overflows.

Tab bar can now span the full available width in maximized chat layouts.

Consolidated the Early Access release track behind Nightly.

Bug Fixes (8)↓↑

Fixed text area behavior for Network Access Controls so pressing Enter can reliably add a newline at the end of the input.

Fixed hooks loading so multi-root workspaces read project hook files from all workspace folders instead of only the first one.

Fixed a markdown parsing bug where parenthesized HTTP(S) links could be misread as citations.

Fixed todo card visibility to prevent them from disappearing after all todos complete.

Fixed Agent queued prompts that were not resuming automatically after editing operations.

Fixed picker behavior for models that are disabled but selectable by removing misleading "not allowed" styling and auto-enabling a model when the user selects it.

Fixed a bug where expanding/collapsing thinking blocks didn't work while streaming was still in progress.

Fixed a bug where Shift+Enter line breaks weren't treated as multiline content, so the prompt input field could stay in an incorrect state.

Mar 25, 2026 · Changelog

Cursor now supports self-hosted cloud agents that keep your code and tool execution entirely in your own network.

Your codebase, build outputs, and secrets all stay on internal machines running in your infrastructure, while the agent handles tool calls locally.

Self-hosted cloud agents offer the same capabilities as Cursor-hosted cloud agents, including isolated VMs, full development environments, multi-model harnesses, plugins, and more.

Try it out today by enabling self-hosted cloud agents in your Cursor Dashboard. Read more in our announcement.
