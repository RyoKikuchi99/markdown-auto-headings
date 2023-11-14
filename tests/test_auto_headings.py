import unittest
from src.generate_auto_headings import generate_auto_headings


class TestAutoHeadings(unittest.TestCase):

    def test_auto_headings_start_at_1(self):

        input_text = (
            "# Introduction\n"
            "## Section 1\n"
            "### Subsection 1.1\n"
            "## Section 2\n"
            "### Subsection 2.1\n"
            "### Subsection 2.2\n"
        )

        expected_output = (
            "# [A-1] Introduction\n"
            "## [A-1-1] Section 1\n"
            "### [A-1-1-1] Subsection 1.1\n"
            "## [A-1-2] Section 2\n"
            "### [A-1-2-1] Subsection 2.1\n"
            "### [A-1-2-2] Subsection 2.2\n"
        )

        result = generate_auto_headings(input_text, 'A', '-', 1)
        self.assertEqual(result, expected_output)

    def test_auto_headings_start_at_2(self):

        input_text = (
            "# Introduction\n"
            "## Section 1\n"
            "### Subsection 1.1\n"
            "## Section 2\n"
            "### Subsection 2.1\n"
            "### Subsection 2.2\n"
        )

        expected_output = (
            "# Introduction\n"
            "## [A-1] Section 1\n"
            "### [A-1-1] Subsection 1.1\n"
            "## [A-2] Section 2\n"
            "### [A-2-1] Subsection 2.1\n"
            "### [A-2-2] Subsection 2.2\n"
        )

        result = generate_auto_headings(input_text, 'A', '-', 2)
        self.assertEqual(result, expected_output)

    def test_auto_headings_start_at_3(self):

        input_text = (
            "# Introduction\n"
            "## Section 1\n"
            "### Subsection 1.1\n"
            "## Section 2\n"
            "### Subsection 2.1\n"
            "### Subsection 2.2\n"
            "#### Subsubsection 2.2.1"
        )

        expected_output = (
            "# Introduction\n"
            "## Section 1\n"
            "### [A-1] Subsection 1.1\n"
            "## Section 2\n"
            "### [A-2] Subsection 2.1\n"
            "### [A-3] Subsection 2.2\n"
            "#### [A-3-1] Subsubsection 2.2.1"
        )

        result = generate_auto_headings(input_text, 'A', '-', 3)
        self.assertEqual(result, expected_output)


if __name__ == '__main__':
    unittest.main()
