# ArchCode

# 1. How to run it

## 1) prepare python virtual environment

```bash
conda create -n ArchCode python=3.10
conda activate ArchCode
```

## 2) import third party packages

```bash
git clone https://github.com/ldilab/expand_langchain.git third_party/expand_langchain
pip install -e expand_langchain
```

## 3) save API keys
1. In root directory, make `api_keys.json` file.
2. save API keys in the file in JSON dictionary format.

- Example
  ```json
  {
    "OPENAI_API_KEY": "sk-xxx"
  }
  ```

## 4) run python script

### i. generation

```bash
python run.py generator \
    --config_path=configs/llama3_8b-vanilla-fr.yaml \
    - run \
    - merge_json \
    - exit
```

### ii. evaluation
```bash
python run.py evaluator \
    --path=results/llama3_8b-archcode-fr/results_merged_1.json \
    --gt_key=passed \
    --filter_keys=[gen_tc_passed] \
    --filter_weights=[1] \
    - run \
    --k=[1,2,5,10] \
    --n=10
```

# 2. Configs
<!-- todo: add explanation about configs -->
