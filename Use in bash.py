import jieba
from collections import Counter
import re

def segment_and_count(text, use_hmm=True):
    """
    分词并统计词频
    
    参数:
        text: 输入文本
        use_hmm: 是否使用HMM模型识别新词
    
    返回:
        按词频降序排列的词语列表，格式为[(词, 频次), ...]
    """
    # 使用jieba进行分词
    words = jieba.lcut(text, HMM=use_hmm)
    
    # 过滤掉空白字符和标点符号
    filtered_words = []
    for word in words:
        word = word.strip()
        if word and not re.match(r'^\W+$', word):  # 排除纯标点符号
            filtered_words.append(word)
    
    # 统计词频
    word_counts = Counter(filtered_words)
    
    # 按词频降序排列
    sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    
    return sorted_words

def main():
    # 输入大段文本
    print("请输入要分词的文本（输入空行结束）：")
    lines = []
    while True:
        line = input()
        if not line:
            break
        lines.append(line)
    
    text = '\n'.join(lines)
    
    if not text:
        print("未输入任何文本！")
        return
    
    # 分词并统计词频
    word_freq = segment_and_count(text)
    
    # 输出结果
    print("\n分词结果（按词频降序排列）：")
    print("{:<10}{:<10}".format("词语", "频次"))
    print("-" * 20)
    for word, freq in word_freq:
        print("{:<10}{:<10}".format(word, freq))

if __name__ == "__main__":
    # 加载jieba的词典（可选，可以提高分词准确性）
    # jieba.load_userdict("userdict.txt")
    
    main()
