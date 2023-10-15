def show_messages(messages):
    """传入一个列表，然后打印列表中的每一条消息"""
    for message in messages:
        print(message)


def send_messages(messages, sent_messages):
    """传入一个列表，将列表中的每一条消息都打印并传入另一条列表中"""
    while messages:
        message = messages.pop()
        print(message)
        sent_messages.append(message)

messages = ['hello', 'hi', 'how r u']
sent_messages = []
show_messages(messages)

#使用切片表示法传入列表副本
send_messages(messages[:], sent_messages)
print(messages, sent_messages)