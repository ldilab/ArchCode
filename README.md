# ArchCode

# 1. How to run it

## 1) prepare python virtual environment

```bash

```

## 2) save API keys

<!-- todo: make wandb account configuration -->

1. In root directory, make `api_keys.json` file.
2. save API keys in the file in JSON dictionary format.

- Example
  ```json
  {
    "OPENAI_API_KEY": "sk-xxx"
  }
  ```

## 3) run python script

### i. generation

<!-- todo: add example -->

```bash
...
```

### ii. filter

#### How to run

- Prerequisites

  - For all problems and all generated test cases, indivisually test results files must be prepared in advance. For example, The results file is like "./split_eval_results_for_filtering/he/he_code_contract_test_by_general_result.json""

- Command

  ```sh
  $ python ./run.py filter --benchmark {he, cc} -K {1, 2, 5} [--gt_eval_file_path <GT Result Path>] [--code_types ["contract", "requirement", ...]] [--gen_tc_eval_results {...}]run

  # Example
  $ python ./run.py filter --benchmark he --K 1 --gen_tc_eval_results "{'general': {'code_type': 'contract', 'weight': 1, 'results_file_path':
  './split_eval_results_for_filtering/he/he_code_contract_test_by_general_result.json'}}" run
  Processing ./split_eval_results_for_filtering/he/he_code_contract_test_by_general_result.json
  Naive: 15.91
  Unbiased Filtering Result: 18.37
  Bins: [132, 66, 152, 132, 1158]
  Mixed with Ratio:
  general: 1
  Weighted Filtering Result: 18.37
  Bins: [132, 66, 152, 132, 1158]
  ```

### iii. evaluation

```bash
...
```

# 2. Configs

## 1) target

- target.dataset_type
  - huggingface dataset name
  - `openai_humaneval` or `deepmind/code_contests`
- target.dataset_split
  - huggingface dataset split name

## 2) example

each key is reasoning chain name.

- dataset_type:
  - huggingface dataset name
  - `openai_humaneval` or `deepmind/code_contests`
- path
  - path to the dataset

## 3) chain.kwargs

- graph
  - reasoning chain graph
- chain_kwargs
  - kwargs for reasoning chain class

## 4) eval

- name
  - evaluation name
- pred_key
  - key of predicted code in the output file
- ref_key
  - key of reference testcases in the output file
- dataset_type
  - huggingface dataset name
  - `openai_humaneval` or `deepmind/code_contests`
- k
  - list of pass@k values
- timeout
  - timeout for each test case
- early_stop
  - whether to stop when the model fails to pass one test case among the test cases
- ignore_assertion_errors
  - whether to ignore assertion errors when executing the code
