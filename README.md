# old_kedro_proj

## Issue

Runtime parameter behaves differently with --env flag used, with OmegaConfigLoader set in src/old_kedro_proj/settings.py.

Tested environment: Python 3.9.12 + Kedro 0.18.14

Result as follows:

- kedro run
  - `{'aaa': {'bbb': {'aba': '2023-11-01', 'abb': '2023-11-01', 'abc': 14}}, 'xyz': {'asdf': 123123}}`
- kedro run --params="aaa.bbb.abb=2023-11-11"
  - `{'aaa': {'bbb': {'aba': '2023-11-01', 'abb': '2023-11-01', 'abc': 14}}, 'xyz': {'asdf': 123123}}`
- kedro run --env add
  - `{'aaa': {'bbb': {'aba': '2023-11-01', 'abb': '2023-11-01', 'abc': 14}}, 'xyz': {'asdf': 123123}, 'def': {'gg': 123}}`
- kedro run --env add --params="def.ghi=12345"
  - `{'aaa': {'bbb': {'aba': '2023-11-01', 'abb': '2023-11-01', 'abc': 14}}, 'xyz': {'asdf': 123123}, 'def': {'gg': 123, 'ghi': 12345}}`
- kedro run --env add --params="aaa.bbb.abb=2023-11-11"
  - `{'aaa': {'bbb': {'abb': '2023-11-11'}}, 'xyz': {'asdf': 123123}, 'def': {'gg': 123}}`
  - 
Result if not using OmegaConfigLoader (by disabling the OmegaConfigLoader lines in settings.py):

- kedro run
  - `{'aaa': {'bbb': {'aba': '2023-11-01', 'abb': '2023-11-01', 'abc': 14}}, 'xyz': {'asdf': 123123}}`
- kedro run --params="aaa.bbb.abb=2023-11-11"
  - `{'aaa': {'bbb': {'aba': '2023-11-01', 'abb': '2023-11-01', 'abc': 14}}, 'xyz': {'asdf': 123123}}`
- kedro run --env add
  - `{'aaa': {'bbb': {'aba': '2023-11-01', 'abb': '2023-11-01', 'abc': 14}}, 'xyz': {'asdf': 123123}, 'def': {'gg': 123}}`
- kedro run --env add --params="def.ghi=12345"
  - `{'aaa': {'bbb': {'aba': '2023-11-01', 'abb': '2023-11-01', 'abc': 14}}, 'xyz': {'asdf': 123123}, 'def': {'gg': 123, 'ghi': 12345}}`
- kedro run --env add --params="aaa.bbb.abb=2023-11-11"
  - `{'aaa': {'bbb': {'aba': '2023-11-01', 'abb': '2023-11-11', 'abc': 14}}, 'xyz': {'asdf': 123123}, 'def': {'gg': 123}}`