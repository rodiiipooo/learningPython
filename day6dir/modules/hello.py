import messages as msg
msg.hello()
msg.bye()

from messages import hello,bye
hello()
bye()

from messages import *
# not recommended for somthing in a large program with multiple modules