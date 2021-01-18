def account_check(username, password, accounts_list):
    is_valid = False
    for key, value in accounts_list.items():

        if value[0] == username and value[1] == password:
            is_valid = True

    if is_valid:
        return True
    else:
        return False