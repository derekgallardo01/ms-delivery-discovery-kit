import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)

import validate  # noqa: E402


def _abs(rel):
    return os.path.join(ROOT, rel)


def test_examples_have_no_unfilled_placeholders():
    for name in ("examples/discovery-greenfield-logistics.md",
                 "examples/sow-greenfield-logistics.md",
                 "examples/discovery-whitford-legal.md",
                 "examples/sow-whitford-legal.md"):
        issues = validate.lint(_abs(name))
        assert issues == [], f"{name} still has placeholders: {issues[:3]}"


def test_blank_sow_template_still_looks_like_a_template():
    # The bare template SHOULD have placeholders — that's what makes it a template.
    issues = validate.lint(_abs("sow-template.md"))
    assert len(issues) >= 5
