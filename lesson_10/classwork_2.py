"""
Создать тест в отдельном файле и проверить несколько телефонных номеров.
"""

import classwork_1

assert classwork_1.main('999999999') == 'no'
assert classwork_1.main('+375 (29) 999-99-99') == 'yes'
assert classwork_1.main('29 999-99-99') == 'no'
