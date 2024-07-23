# ArchCode

# 1. How to run it

## 1) prepare python virtual environment

```bash
conda create -n ArchCode python=3.10
conda activate ArchCode
pip install -r requirements.txt
```

## 2) run third party packages

### i. install `expand_langchain`

```bash
git submodule update --init --recursive
pip install -e third_party/expand_langchain
```

### ii. run `CodeExecContainer`

At a new terminal, run the following command and keep it running.

```bash
source third_party/CodeExecContainer/run.sh
```

### iii. run Ollama (for local llm generation)

refer to [Ollama](https://github.com/ollama/ollama) for more information.

```bash
docker run -d \
  -v ollama:/root/.ollama \
  -p 11434:11434 \
  --name ollama \
  ollama/ollama
docker exec -d ollama ollama pull ollama/llama3:8b-instruct-fp16
```

## 4) save API keys

1. In root directory, copy `api_keys_example.json` to `api_keys.json`.
2. set your API keys in the file.

## 4) run python script

refer to [Python Fire](https://google.github.io/python-fire/guide/) for arguments setting.

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
