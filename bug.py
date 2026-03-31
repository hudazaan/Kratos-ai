# def connect():
#     db_pass = "root1235" # AI should catch this hardcoded pass
#     return db_pass


import os

def delete_database():
    # This is a massive security risk and a logical bug
    password = "admin_password_123" 
    os.system("rm -rf /") # DO NOT RUN THIS FOR REAL, JUST FOR THE BOT
    return password