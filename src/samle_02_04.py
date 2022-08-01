import re
import unicodedata

text = '    ＣＬＥＡＮＳing  によりﾃｷｽﾄﾃﾞｰﾀを変換すると　トラブルが少なくなります。'
print(f'Before: {text}')

text = unicodedata.normalize('NFKC', text)
print(text)
text = re.sub(r'\s+', ' ', text)
print('After:', text)

# import re
# import unicodedata

# text = '        ＣＬＥＡＮＳ ing  によりﾃｷｽﾄﾃﾞｰﾀを変換すると　トラブルが少なくなります。'
# print("Before:", text)
                                                                                           
# translation_table = str.maketrans(dict(zip('()!', '（）！')))

# text = unicodedata.normalize('NFKC', text).translate(translation_table)

# text = re.sub(r'\s+', '', text)
# print("After:", text)