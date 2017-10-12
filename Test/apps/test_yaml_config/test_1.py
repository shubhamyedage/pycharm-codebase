import yaml

# with open("config.yml", 'r') as yamlfile:
#     cnfig = yaml.load(yamlfile)
#
# for sec in cnfig:
#     print(sec)
#
# print(cnfig.get("root"))
#
# print(type(cnfig.get("my name")))

# with open("tree_str.yaml", "r") as yamlfile:
#     cfg = yaml.load(yamlfile)
#
# print(cfg.get("Earnings per share").get("children").get("div").get("dividend"))

with open("report_config.yaml") as yamlfile:
    cfg = yaml.load(yamlfile)
    print(cfg)