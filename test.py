from dotenv import dotenv_values

config = dotenv_values("credentials.env")
print(config)


print(type(config['DB_PASS']))