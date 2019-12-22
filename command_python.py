def foo(arg1, arg2): # наша команда
    print('FOO',(arg1, arg2))

def bar(cmd, arg2):
    # Приемник команды. Ничего не знает о функции foo...
    print ('BAR %s' % arg2)
    cmd(arg2 * 2) # ...но вызывает её
from functools import partial
bar(partial(foo, 1), 2)
bar(lambda x: foo(x, 5), 100)
