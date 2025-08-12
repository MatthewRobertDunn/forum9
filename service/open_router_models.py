
# The general models of the collection
GeneralModels = [
    "qwen/qwen3-235b-a22b:free",
    "deepseek/deepseek-r1-0528:free",
    "meta-llama/llama-3.1-405b-instruct:free",
    "meta-llama/llama-3.3-70b-instruct:free",
    "qwen/qwen3-4b:free",
    "qwen/qwen3-coder:free",
    "qwen/qwen-2.5-72b-instruct:free",
    "deepseek/deepseek-chat-v3-0324:free",
    "deepseek/deepseek-r1-distill-llama-70b:free",
    "google/gemma-3-27b-it:free",
    "tngtech/deepseek-r1t2-chimera:free",
    "cognitivecomputations/dolphin3.0-r1-mistral-24b:free",
    "mistralai/mistral-small-3.2-24b-instruct:free",
]

# The fastest models of the collection, good for dumb characters, formatting.
FastModels = [
    "meta-llama/llama-3.3-70b-instruct:free",  # 111.5tps
    "openai/gpt-oss-20b:free",  # 212.1 tps
    "qwen/qwen3-4b:free",  # 146.2tps
    "qwen/qwen-2.5-72b-instruct:free",  # 100tps
    "meta-llama/llama-3.2-3b-instruct:free",  # 164.2
    "mistralai/mistral-small-3.2-24b-instruct:free",
]

# Represents the strongest reasoning models, usually slower, gets more token allocation
StrongModels = [
    "qwen/qwen3-235b-a22b:free",
    "deepseek/deepseek-chat-v3-0324:free",
    "qwen/qwen3-coder:free",
    "deepseek/deepseek-r1-0528:free",
    "tngtech/deepseek-r1t2-chimera:free",
    "meta-llama/llama-3.1-405b-instruct:free",
]
