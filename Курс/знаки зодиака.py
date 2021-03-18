elif month == ('апрель' and 21 <= day <= 30) or ('май' and day <= 21):
  zodiac = 'Телец'

elif month == ('май' and 22 <= day <= 31) or ('июнь' and day <= 21):
  zodiac = 'Близнецы'

elif month == ('июнь' and 22 <= day <= 30) or ('июль' and day <= 22):
  zodiac = 'Рак'

elif month == ('июль' and 23 <= day <= 31) or ('август' and day <= 21):
  zodiac = 'Лев'

elif month == 'август' and 22 <= day <= 30 or 'сентябрь' and day <= 23:
  zodiac = 'Дева'

elif month == 'сентябрь' and 24 <= day <= 31 or 'октябрь' and day <= 23:
  zodiac = 'Весы'

elif month == 'октябрь' and 24 <= day <= 30 or 'ноябрь' and day <= 22:
  zodiac = 'Скорпион'

elif month == 'ноябрь' and 23 <= day <= 31 or 'декабрь' and day <= 22:
  zodiac = 'Стрелец'

elif month == 'декабрь' and 23 <= day <= 30 or 'январь' and day <= 20:
  zodiac = 'Козерог'

elif month == 'январь' and 21 <= day <= 31 or 'февраль' and day <= 19:
  zodiac = 'Водолей'

elif month == ('февраль' and 20 <= day <= 31) or ('март' and day <= 20):
  zodiac = 'Рыбы'
