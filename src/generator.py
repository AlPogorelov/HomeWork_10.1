

def filter_by_currency(transaction, currency='UDS'):
    result = iter([x for x in transaction if x["operationAmount"]["currency"]['code']== currency])
    return result


def transaction_descriptions(transactions):
    trans_description = (x["description"] for x in transactions )
    return trans_description


def card_number_generator(start, enter):
    for i in range(start, enter):
        vid_account =10000000000000000
        x_ = [(str(vid_account+i)[1:]) for i in range(start, enter+1)]
        card_number = map(lambda i: ' '.join([(i[z:z+4]) for z in range(0, len(i),4)]), x_)
        return card_number
