import unittest
import yaml
from check import validate_skill


class MetadataTests(unittest.TestCase):
    def test_multiline_description(self):
        self.assertEqual(validate_skill("---\nname: memento\ndescription: >\n  Resume safely.\n---\n")['description'].strip(), 'Resume safely.')

    def test_invalid_metadata(self):
        cases = [
            "name: memento\ndescription: broken: yaml",
            "name: memento\ndescription: 12",
            "name: bad--name\ndescription: valid",
            "name: memento",
            "- not a mapping",
        ]
        for case in cases:
            with self.subTest(case=case), self.assertRaises((ValueError, yaml.YAMLError)):
                validate_skill(f"---\n{case}\n---\n")


if __name__ == '__main__':
    unittest.main()
