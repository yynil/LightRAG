import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from lightrag.prompt_chinese import PROMPTS

hint_prompt = PROMPTS["entity_extraction"]

print(hint_prompt)

context_base = dict(
        tuple_delimiter=PROMPTS["DEFAULT_TUPLE_DELIMITER"],
        record_delimiter=PROMPTS["DEFAULT_RECORD_DELIMITER"],
        completion_delimiter=PROMPTS["DEFAULT_COMPLETION_DELIMITER"],
        entity_types=','.join(PROMPTS["DEFAULT_ENTITY_TYPES"]),
        output_language='中文',
    )
continue_prompt = PROMPTS["entiti_continue_extraction"]
if_loop_prompt = PROMPTS["entiti_if_loop_extraction"]
print(context_base)
print(continue_prompt)
print(if_loop_prompt)

input_text = """
贷款市场报价利率（Loan Prime Rate, LPR）是由具有代表性的报价行，根据本行对最优质客户的贷款利率，以公开市场操作利率（主要指中期借贷便利利率）加点形成的方式报价，由中国人民银行授权全国银行间同业拆借中心计算并公布的基础性的贷款参考利率，各金融机构应主要参考LPR进行贷款定价。 现行的LPR包括1年期和5年期以上两个品种 [1]。LPR市场化程度较高，能够充分反映信贷市场资金供求情况，使用LPR进行贷款定价可以促进形成市场化的贷款利率，提高市场利率向信贷利率的传导效率。
2020年8月12日，中国工商银行、中国建设银行、中国农业银行、中国银行和中国邮政储蓄银行五家国有大行同时发布公告，于8月25日起对批量转换范围内的个人住房贷款，按照相关规则统一调整为LPR（贷款市场报价利率）定价方式。 [2]
最新贷款市场报价利率（LPR）：2024年10月21日，1年期LPR为3.10%，5年期以上LPR为3.60%，均较此前下降0.25个百分点。
"""

print(hint_prompt.format(**context_base, input_text=input_text))
print(context_base)
