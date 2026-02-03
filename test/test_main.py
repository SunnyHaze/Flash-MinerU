from flash_mineru import MineruEngine

engine = MineruEngine()
data = ["sample1.pdf", "sample2.pdf"]
result = engine.run(data)  # 也不一定真返回具体值，也可以入参传入输出路径，然后直接写出到具体路径。看怎么方便怎么来