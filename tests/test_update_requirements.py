from pathlib import Path
from ppam.utils import write_requirements

def test_write_requirements(tmp_path):
    p = tmp_path / "requirements.txt"
    write_requirements(p, ["b==1.0", "a==2.0", "a==2.0"])
    content = p.read_text()

    assert "a==2.0" in content
    assert "b==1.0" in content

    # requirements should be sorted and deduplicated
    lines = content.strip().split("\n")
    assert lines == ["a==2.0", "b==1.0"]
