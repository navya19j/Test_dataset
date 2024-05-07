from datasets import Dataset, Features
from datasets import Image as ImageFeature
from datasets import Value

def gen_examples(dataset):
    def fn():
        for sample in dataset:
            yield {
                "original_prompt": sample["original_prompt"],
                "input_image": {"path": str(sample["input_image"])},
                "edit_prompt": sample["edit_prompt"],
                "edited_prompt": sample["edited_prompt"],
                "edited_image": {"path": str(sample["edited_image"])},
            }

    return fn