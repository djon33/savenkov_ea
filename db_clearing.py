def clear_users(cursor, user_name):
    sql = f"""
        delete from mantis_user_mantis
        where 1 = 1
            and username = '{user_name}'
    """
    cursor.execute(sql)


def clear_all_data(cursor, user_name):
    clear_users(cursor, user_name)
