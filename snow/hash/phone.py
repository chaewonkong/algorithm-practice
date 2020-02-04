
# def is_prefix(a, b):
#     if len(a) > len(b):
#         a, b = b, a
#     for i in range(len(a)):
#         if a[i] != b[i]:
#             return False
#     return True


def solution(phone_book):
    phone_book = sorted(phone_book)

    for n1, n2 in zip(phone_book, phone_book[1:]):
        if n2.startswith(n1):
            return False
    return True
