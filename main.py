radical_dict = {'书': '个, 些, 本', '猫': '个, 些, 只', '熊猫': '个, 些, 只', '画家': '个, 些, 位', '语言学家': '个, 些, 位',
                '医院': '个, 些, 座', '词典': '个, 些, 本', '爸爸': '个, 些, 口', '妈妈': '个, 些, 口', '弟弟': '个, 些, 口',
                '哥哥': '个, 些, 口', '爷爷': '个, 些, 口', '奶奶': '个, 些, 口', '姐姐': '个, 些, 口', '妹妹': '个, 些, 口',
                '老爷': '个, 些, 口', '爱人': '个, 些, 口', '外婆': '个, 些, 口', '电脑': '个, 些, 台', '手机': '个, 些, 台',
                '兰花': '个, 些, 朵', '花': '个, 些, 朵', '大学': '个, 些, 座', '学校': '个, 些, 座', '照片': '个, 些, 张',
                '毛衣': '个, 些, 件', 'T恤': '个, 些, 件', '大衣': '个, 些, 件', '裙子': '个, 些, 条, 件', '河': '个, 些, 条, 座',
                '房子': '个, 些, 座', '地图': '个, 些, 张', '江': '个, 些, 条, 座', '杯子': '个, 些', '咖啡': '个, 些, 杯', '茶': '个, 些, 杯'}

a = input('Введите своё имя:')
print('Добро пожаловать, ', a, '!')
print('Пожалуйста, введите какое-нибудь существительное, '
      'и наш сервис покажет, какие счётные слова можно использовать с ним.')
print('Если слова нет в словаре, сервис сообщит об этом.')
input_noun = input()
if input_noun in radical_dict.keys():
    b = radical_dict.get(input_noun)
    print('Для слова', input_noun, 'можно использовать следующие счётные слова: ', b, '.')
else:
    print('Этого слова нет в словаре!')
print('Спасибо, что воспользовались нашим сервисом! Мы постоянно пополняем наш словарь, '
      'ждём Вас снова!')
