# Exercise format — match the existing course exercises

Based on Module 01 exercises (e.g. `Functions/exercise/02_Function_Definition.ipynb`).
The originals put everything in one markdown cell with code in fenced blocks. For modules
02–05 keep the same look and section structure, but make the code **runnable cells** so the
solution can be executed and the asserts actually check something.

## Structure
1. Markdown: `# <N>) <Topic> — Exercises`
2. Markdown: `**Goals:** <comma-separated skills practised>` and, if useful, one line on the data.
3. Code: imports + the data every task uses (small DataFrame or `data/` file, relative path).
4. `### Warm-ups` (2–3 tasks), `### Core` (3–5 tasks), `### Challenge` (1–2 tasks).
5. Each task:
   - Markdown: `**<n>. <Short bold title>**` + 1–3 sentences saying what to build and why it
     matters in energy terms. State the expected units.
   - Code: a function stub (signature + docstring) whose body is the solution block.
   - Code: 1–3 `assert` lines that check the answer — numbers with a tolerance
     (`abs(x - expected) < 1e-6` or `math.isclose`), shapes, column names, signs.
   - For interpretation questions: a markdown cell with the answer in an HTML-comment block.

## Solution markers (the build script reads these)
```python
def merit_order_price(plants: pd.DataFrame, demand_MW: float) -> float:
    """Return the clearing price (EUR/MWh) for one hour."""
    ### BEGIN SOLUTION
    order = plants.sort_values("marginal_cost")
    cum = order["p_max"].cumsum()
    return float(order.loc[cum >= demand_MW, "marginal_cost"].iloc[0])
    ### END SOLUTION
```
becomes, for students:
```python
def merit_order_price(plants: pd.DataFrame, demand_MW: float) -> float:
    """Return the clearing price (EUR/MWh) for one hour."""
    ...  # YOUR CODE HERE
```
Markdown answers: `<!-- BEGIN SOLUTION -->` … `<!-- END SOLUTION -->` → *Your answer here.*
A whole cell only for the answer key (e.g. a plot of the solution): tag it `solution-only`.

## Good asserts
- Test the *answer*, not that something exists: `assert abs(cost - 24_000) < 1e-6`, not `assert cost`.
- Each stub must make at least one assert fail when left as `...` — the build script checks this.
- Prefer values you can derive by hand for warm-ups (students can verify on paper).
- For LP tasks, check the objective, a key dispatch value, and a dual/price — not every number.
- Put a short message in asserts that guide students: `assert x == y, "Did you sort by marginal cost?"`
