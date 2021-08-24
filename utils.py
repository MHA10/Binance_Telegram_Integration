async def parse_message(msg):
    """
    parse the message send from telegram
    extracts buy/sell, symbol and percentage
    :return:
    """
    # msg_dict = {}
    # msg_list = msg.split("-")
    # msg_dict["buy_or_sell"] = msg_list[0]
    # msg_dict["symbol"] = msg_list[1]
    # msg_dict["percentage"] = msg_list[2]

    order_details = msg.split(' ')

    msg_dic = {
        'side': order_details[0],
        'symbol': order_details[1],
        'token': order_details[2],
        'percentage': order_details[3],
    }

    return msg_dic
    # return msg_dict
