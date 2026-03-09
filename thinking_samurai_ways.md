# Thinking Samurai Ways

A practice log for developing clear, concise problem-solving through coding warmups.

## Core Principles

1. **Cut once** - Understand the problem fully before writing code
2. **No wasted motion** - Every line serves a purpose
3. **See the whole** - Grasp the structure before diving into details
4. **Simplicity** - The clearest solution is often the best

### How to use these problems to train the right habit
For each one:
1. Restate the problem in your own words.
2. Ask 2–3 clarifying questions before touching code.
3. Identify the core operation (grouping, deduping, parsing, windowing).
4. Sketch the shape of the solution in plain English.
5. Write code incrementally, testing with tiny examples.
6. Narrate your thinking as if the founder is sitting next to you.

This is exactly the mental discipline that prevents "rushing into solutions" and builds the calm, structured reasoning founders look for.

## Analytic Tips

### Why this is a senior-level habit

This is exactly how experienced engineers think:
- They don't start with the outer loop.
- They don't start with syntax.
- They start by naming the conceptual units.
- Then they build the small pieces → Then the final structure emerges naturally.

You just walked through that progression.

## Practice Log

<!-- Add entries as you practice -->
A strong walkthrough sounds calm, structured, and grounded in invariants rather than code mechanics. 
The goal is to make the founder think, “This person sees the real problem, decomposes it cleanly, and builds the solution from first principles.” 
What follows is a way to narrate your thinking that matches exactly how you naturally reasoned through the SKU problem.

## Framing the problem clearly: 
Start by anchoring the real question:
“We’re given a list of time intervals, and we want to collapse any that overlap. Before coding, I want to define what ‘overlap’ means and what assumptions the algorithm needs.”
This signals that you’re not rushing into implementation.

## Defining the invariants
You already did this beautifully in your notes. Say it out loud:
“Each interval is a tuple (start, end) with start ≤ end.”
“Two intervals overlap if the next interval’s start is less than or equal to the current interval’s end.”
“If they overlap, the merged interval must cover the entire span, so the new end is the max of both ends.”
“This only works if the intervals are sorted by start time.”
This shows you understand the structure of the problem, not just the mechanics.

## Explaining the decomposition
Now describe the pieces you decided to isolate:
“I’ll separate the logic into two small helpers: one that checks overlap, and one that merges two intervals. That keeps the invariants in one place and makes the outer loop much easier to reason about.”

## Describing the outer loop using ZIP
Now you explain your ZIP choice in a way that sounds intentional:
“Once the intervals are sorted, I can walk them pairwise using zip(intervals, intervals[1:]). That gives me the current interval and the next interval at each step. I maintain a running curr_tuple that represents the interval I’m building. If the next interval overlaps with it, I merge them. If not, I append the finished interval to the result and start a new one.”
This shows clarity and control.

## Showing the final structure
You don’t need to recite code. Just describe the flow:
Sort the intervals.
Initialize curr_tuple to the first interval.
For each (curr, next) pair:
    If they overlap → merge into curr_tuple.
    If not → append curr_tuple and reset it to next.
After the loop, append the final curr_tuple.
This is clean, predictable, and invariant‑driven.

## Why this narration sounds senior 
It demonstrates: Problem framing — you start with definitions, not code.
Invariant clarity — you articulate the mathematical rule for overlap.
Decomposition — helpers for overlap and merging.
State management — a running interval that grows as needed.
Data‑flow reasoning — ZIP expresses the pairwise structure cleanly.
Confidence — you’re not guessing; the solution emerges from the invariants.
This is exactly the tone founders listen for.

## Recursive Function Structures: Why the base case goes first
the structure of that recursive function is one of the most important “clicks” in learning recursion: the base case comes first, and the recursive call is the final action. It feels unfamiliar at first, but once you see why it works, it becomes the most natural way to express a recursive scan.
Recursion is fundamentally a decision tree: 
Are we done?  
If not, do one step and recurse. 
Putting the base case first makes the function read like a mathematical definition:

If no more "search_char" exists → return the last one we saw.
Otherwise → update state and recurse.
This mirrors how you’d define something like “the last occurrence of X in a sequence” on paper.

Why the recursive call is the last line
Ending with the recursive call gives you two benefits:
The function’s return value is exactly the return value of the recursive call.

You don’t need extra variables or bookkeeping after the recursion.
This pattern is called tail recursion (even though Python doesn’t optimize it). It’s the cleanest way to express “keep going until the base case.”

## Recursive pattern is always:
def recurse(pointer, state):
    if pointer is past the end:
        return state
    update state if needed
    return recurse(pointer + 1, state)

## The deeper pattern you’ve now internalized
Grouping by N keys → N nested dicts → list at the bottom
For example:

1 key → {date: [values]}

2 keys → {date: {user: [values]}}

3 keys → {date: {user: {hour: [values]}}}

4 keys → {date: {user: {hour: {event_type: [values]}}}}

This is the same fold pattern, just extended deeper.

And the algorithm is always the same:

Extract all grouping keys.

Walk down the nested dicts, creating levels as needed.

Append the value at the bottom.
Once you see this, grouping becomes a mechanical operation.

## You can now narrate grouping problems at a senior level:
“The output shape dictates the accumulator.”
“Each grouping dimension becomes a dict level.”
“The deepest level is always a list that grows.”
“The fold is: ensure outer key exists → ensure inner key exists → append.”
This is the exact kind of calm, structural reasoning founders and senior engineers listen for.****


## The deeper pattern you’re starting to see
## You’ve now internalized a key invariant:

If the output is “one item per key,” the accumulator should be a dict keyed by that field.

This generalizes to:
“latest update per product”
“first occurrence per value”
“max version per ID”
“group by key”
“dedupe while preserving order”
“merge records by ID”

## Python strings have a small set of “core” methods that show up everywhere:
.strip() ; .split() ; .join() ; .startswith() ; .endswith(); .replace()
.find() ; .lower(), .upper()