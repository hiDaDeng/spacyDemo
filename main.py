import spacy_streamlit
import streamlit as st

st.markdown("""
*Spacy库是Python的自然语言处理库，可以做句法依存、词向量解析、模式识别等，功能十分强大，现如今已支持中文。感兴趣的同学可以去[spacy](https://spacy.io/api)官方文档了解一二。但一般我们经管人文专业没必要死磕spacy，能学会jieba、pandas、scikit-learn等包就能应付基本文本分析需求。*
""")


models = ["zh_core_web_lg", "en_core_web_lg"]
default_text = "Sundar Pichai is the CEO of Google."
spacy_streamlit.visualize(models, default_text)




def setting_tutorials():

    st.header('Spacy配置步骤')
    st.markdown('''
    1. 下载[**en_core_web_lg**](https://github.com/explosion/spacy-models/releases/download/en_core_web_lg-3.0.0/en_core_web_lg-3.0.0-py3-none-any.whl)和[**zh_core_web_lg**](https://github.com/explosion/spacy-models/releases/download/zh_core_web_lg-3.0.0/zh_core_web_lg-3.0.0-py3-none-any.whl)的whl文件，下载后放置于桌面。下载本案例代码压缩包至于桌面
    
    2. 打开命令行(Win即为cmd； Mac即为terminal)， 执行**cd desktop**命令，将命令行切换至桌面路径。
    
    3. 在命令行中依次执行下列安装配置命令
    ''', unsafe_allow_html=True)

    st.code('pip3 install en_core_web_lg-3.0.0/en_core_web_lg-3.0.0-py3-none-any.whl')
    st.code('pip3 install zh_core_web_lg-3.0.0/zh_core_web_lg-3.0.0-py3-none-any.whl')
    st.code('pip3 install -r requirements.txt')

    st.markdown('''4. 启动本地spacy网站，在命令行执行''')

    st.code('streamlit run main.py')


setting_tutorials()



st.markdown("""
# 谢谢支持
- [**腾讯课堂: Python网络爬虫与文本分析**](https://ke.qq.com/course/482241?tuin=163164df)
- [**B站:大邓和他的python**](https://space.bilibili.com/122592901/channel/detail?cid=66008)
- [**github: DaDeng**](https://github.com/thunderhit)
- **公众号：大邓和他的python**

""")

st.image('大邓和他的Python.png')













