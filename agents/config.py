from autogen import AssistantAgent, UserProxyAgent, config_list_from_json

# Load LLM configuration (use OpenAI's free tier or local LLM)
config_list = config_list_from_json(env_or_file="OAI_CONFIG_LIST.json")