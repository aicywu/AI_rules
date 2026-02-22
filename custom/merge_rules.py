import yaml
import requests

# 上游规则 URL
upstream_urls = [
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/refs/heads/master/rule/Clash/OpenAI/OpenAI_No_Resolve.yaml",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/refs/heads/master/rule/Clash/Gemini/Gemini_No_Resolve.yaml",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/refs/heads/master/rule/Clash/BardAI/BardAI_No_Resolve.yaml",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/refs/heads/master/rule/Clash/Anthropic/Anthropic_No_Resolve.yaml",
  
]

# 自定义规则 URL
custom_urls = [
    "https://raw.githubusercontent.com/aicywu/AI_rules/refs/heads/main/custom/extra.yaml"
]

merged = {}

# 下载并聚合上游规则
for url in upstream_urls:
    r = requests.get(url)
    data = yaml.safe_load(r.text)
    for rule in data.get('payload', []):
        merged[rule] = True  # 去重

# 下载并聚合自定义规则
for url in custom_urls:
    r = requests.get(url)
    data = yaml.safe_load(r.text)
    for rule in data.get('payload', []):
        merged[rule] = True

# 输出最终聚合文件
with open('build/ai_merged.yaml', 'w') as out:
    out.write("payload:\n")
    for rule in merged.keys():
        out.write(f"  - {rule}\n")
