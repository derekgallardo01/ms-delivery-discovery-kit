# FAQ

## When should I use this versus skipping straight to a build?

Skip discovery only when the engagement is truly trivial (under 4 hours,
single connector, no compliance angle, no handover expected). For
anything else — even a "quick" Power Automate flow — running the
discovery prevents the "oh, also..." amendment cycle that eats margin.

## How much should I charge for discovery itself?

USD 500–1,200 (UK: £400–£900, AU: AUD 800–1,500) depending on engagement
size, credited against the fixed price if you proceed. The framing
matters: it's a paid scoping call, not a free consultation. Clients who
won't pay for discovery are clients who will haggle the build down too.

## Why are out-of-scope items more important than in-scope items?

Because the in-scope is what got the client to call you. The out-of-
scope is what protects you from the request 6 weeks in that "we also
need..." Without an explicit list of "no", every new ask becomes a
debate.

## How do I phrase "acceptance criteria" so they're actually testable?

The pattern is "<observable thing>: <observable measurement>". Examples:
- "The flow runs on schedule, writes correct rows, passes test data."
- "3 consecutive days pass with zero duplicates."
- "Eval set passes 100% in production."

If you can't write the test, the acceptance criterion isn't observable
yet — refine it.

## What if the client won't sign a SOW?

That's a "no" wrapped in indecision. Counter with: "I'm happy to do a
one-hour paid scoping call to walk through the SOW together — that
usually resolves the unknowns." If still no after that, walk away. The
worst outcome is starting work without a signed SOW.

## Do I need a separate contract on top of this SOW?

Yes — pair the SOW with your master services agreement (or Upwork's
contract structure). The SOW captures scope + commercials; the MSA
captures jurisdiction, IP, liability cap, indemnities, termination.
Different documents, different lifecycles.

## How do I extend the questionnaire per industry?

Add a section. Useful additions per industry:
- **Healthcare**: data subject rights, HIPAA / DPA / NHS DSPT.
- **Financial services**: FCA / APRA / SOX-style control evidence.
- **Government**: FedRAMP / IRAP / IL5 boundary.

Run `python validate.py` on the bare template after — it should still
emit placeholders for any field you expect the user to fill.

## Why is "Derek G." in the SOW template hard-coded?

Because the kit is published on my GitHub. If you're not Derek and you
want to use the kit, fork it and replace the name. Or use it as a
prompt — re-type the SOW with your own header. The kit's value is the
*structure*, not the bytes.

## How do I add a new worked example?

Drop your engagement's discovery + SOW into `examples/` under a non-
real client name. Run `python validate.py` — it should pass clean. Add
the file paths to `tests/test_validate.py` so the new example is
regression-tested.
