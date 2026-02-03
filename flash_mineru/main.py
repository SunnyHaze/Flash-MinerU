from flash_mineru.ray_utils import (
    RayModule,
    Dispatch,
)

# 这个也可以不要，逻辑都封装在下面，你看怎么舒服怎么来
class MinerUPipeline():
    def __init__(self):
        pass
    def run(self, data: list[str]):
        print("Running MinerU Pipeline on data:", data)
        return "Pipeline Result"

class MineruEngine():
    def __init__(self):
        # 配置具体的pipeline, 下载模型，传参啥的，统一暴露接口并提供默认接口
        pass

    def run(self, path_of_pdfs: list[str]):
        print("MineruEngine is running... for ", path_of_pdfs)
        return "Flash-MinerU Engine is running!"